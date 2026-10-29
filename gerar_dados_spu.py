#!/usr/bin/env python3
"""Gera a base auditável do protótipo a partir do relatório HTML do SIORG.

O SIORG prevalece para códigos e cargos. RI SPUv2 prevalece para denominação
e hierarquia quando há divergência documentada; a retificação de 05/08/2026
é aplicada à Divisão de Vendas e fica explicitada nos metadados.
"""

from __future__ import annotations

import json
from pathlib import Path
import re

from bs4 import BeautifulSoup


PASTA = Path(__file__).resolve().parent
ENTRADA = PASTA / "relatorio-dinamico-estrutura-viva.html"
SAIDA = PASTA / "dados-estrutura-spu.js"

NOMES_REGIMENTO = {
    "618532": "Coordenação-Geral de Gestão e Monitoramento de Programas",
    "311826": "Serviço de Documentação",
    "312359": "Divisão de Infraestrutura em Áreas Terrestres",
    "618651": "Coordenação de Infraestrutura Tecnológica",
    "106029": "Coordenação de Sistemas",
    "312563": "Divisão de Sustentação e Evolução de Sistemas",
    "618633": "Coordenação de Governança de Tecnologia da Informação e Comunicação",
    "618671": "Divisão de Gestão de Serviços de Tecnologia da Informação e Comunicação",
    "618712": "Divisão de Captação de Recursos Externos",
    "618631": "Divisão de Infraestrutura em Águas Públicas",
    "312406": "Divisão de Vendas",  # retificação posterior ao RI SPUv2
    "108673": "Coordenação do Escritório de Processos",
    "108670": "Coordenação de Orçamento e Finanças",
    "312371": "Divisão de Praias e Orlas",
    "618591": "Coordenação de Procedimentos Pós-Demarcatórios",
    "618672": "Divisão de Sistemas Geoespaciais e Geotecnologias",
    "78266": "Gabinete",
    "108963": "Coordenação da Superintendência do Patrimônio da União em Goiás",
}

PAIS_REGIMENTO = {
    "618631": "312323",  # Coordenação de Infraestrutura (DEDES)
    "312406": "293066",  # Coordenação-Geral de Gestão Econômica de Ativos
    "312573": "618651",  # Coordenação de Infraestrutura Tecnológica
    "312568": "618632",  # Coordenação de Governança de Dados
}

TITULARES = {
    "Secretário", "Chefe de Gabinete", "Diretor", "Coordenador-Geral",
    "Coordenador", "Chefe", "Superintendente",
}


def limpo(valor: str) -> str:
    return re.sub(r"\s+", " ", valor.replace("\xa0", " ")).strip()


def tipo_unidade(nome: str, codigo: str) -> str:
    if codigo == "1986":
        return "SPU"
    prefixos = (
        ("Gabinete", "GAB"),
        ("Superintendência", "SUP"),
        ("Diretoria", "DIR"),
        ("Coordenação-Geral", "CG"),
        ("Coordenação", "CO"),
        ("Divisão", "DIV"),
        ("Serviço", "SV"),
        ("Seção", "SEC"),
        ("Setor", "SET"),
        ("Conselho", "COL"),
    )
    return next((tipo for prefixo, tipo in prefixos if nome.startswith(prefixo)), "OUT")


def main() -> None:
    soup = BeautifulSoup(ENTRADA.read_text(encoding="utf-8"), "html.parser")
    cabecalhos = [limpo(th.get_text(" ", strip=True)) for th in soup.select("thead th")]
    linhas = []
    for tr in soup.select("tbody tr"):
        celulas = [limpo(td.get_text(" ", strip=True)) for td in tr.find_all("td", recursive=False)]
        if len(celulas) != len(cabecalhos):
            raise ValueError(f"Linha com {len(celulas)} células; esperadas {len(cabecalhos)}")
        linhas.append(dict(zip(cabecalhos, celulas)))

    unidades = []
    por_codigo = {}
    for linha in linhas:
        codigo = linha["Código Unidade"]
        unidade = por_codigo.get(codigo)
        if unidade is None:
            unidade = {
                "id": codigo,
                "siorg": codigo,
                "sigla": linha["Sigla Unidade"],
                "nomeSiorg": linha["Denominação Unidade"],
                "nome": NOMES_REGIMENTO.get(codigo, linha["Denominação Unidade"]),
                "tipo": "",
                "nivelSiorg": int(linha["Nível Hierárquico"]),
                "categoriaUnidade": linha["Categoria Unidade"],
                "competenciaSiorg": linha["Competência"],
                "paiSiorg": None,
                "pai": None,
                "cargos": [],
                "fonteNome": "RI SPUv2 + retificação de 05/08/2026" if codigo in NOMES_REGIMENTO else "SIORG",
                "fontePai": "RI SPUv2" if codigo in PAIS_REGIMENTO else "SIORG",
            }
            unidade["tipo"] = tipo_unidade(unidade["nome"], codigo)
            unidades.append(unidade)
            por_codigo[codigo] = unidade

        if linha["Tipo do Cargo"]:
            categoria = linha["Categoria"] or "1"
            nivel = (linha["Nível"] or "").zfill(2)
            unidade["cargos"].append({
                "id": f"{codigo}:{len(unidade['cargos']) + 1}",
                "codigo": f"{linha['Tipo do Cargo']} {categoria}.{nivel}",
                "titulo": linha["Denominação"],
                "quantidade": int(linha["Quantidade"] or 0),
                "principal": linha["Denominação"] in TITULARES,
                "fonte": "SIORG",
            })

    pilha = {}
    for unidade in unidades:
        nivel = unidade["nivelSiorg"]
        if nivel > 1:
            pai = pilha.get(nivel - 1)
            if pai is None:
                raise ValueError(f"Não foi possível inferir o pai de {unidade['id']} — {unidade['nome']}")
            unidade["paiSiorg"] = pai["id"]
            unidade["pai"] = pai["id"]
        pilha[nivel] = unidade
        pilha = {n: u for n, u in pilha.items() if n <= nivel}

    for codigo, pai in PAIS_REGIMENTO.items():
        por_codigo[codigo]["pai"] = pai

    # O colegiado não integra o art. 2º nem a árvore de unidades administrativas.
    unidades_administrativas = [u for u in unidades if u["tipo"] != "COL"]

    for unidade in unidades_administrativas:
        principais = [c for c in unidade["cargos"] if c["principal"]]
        if len(principais) != 1:
            raise ValueError(
                f"{unidade['id']} — {unidade['nome']}: esperava um cargo titular, encontrei {len(principais)}"
            )

    meta = {
        "versaoBase": 2,
        "geradoEm": "2026-08-18",
        "fonteCargos": "relatorio-dinamico-estrutura-viva.html — exportação SIORG",
        "fonteEstrutura": "RI SPUv2.docx",
        "retificacao": "4__Despacho_Retificacao_Divisao_de_Vendas.docx",
        "unidadesAdministrativas": len(unidades_administrativas),
        "cargosFuncoes": sum(sum(c["quantidade"] for c in u["cargos"]) for u in unidades_administrativas),
        "colegiadoForaDaArvore": {"id": "221732", "nome": "Conselho Estratégico"},
    }

    conteudo = (
        "/* Arquivo gerado por gerar_dados_spu.py. Não editar manualmente. */\n"
        f"window.META_BASE_SPU = {json.dumps(meta, ensure_ascii=False, indent=2)};\n"
        f"window.BASE_SPU = {json.dumps(unidades_administrativas, ensure_ascii=False, indent=2)};\n"
    )
    SAIDA.write_text(conteudo, encoding="utf-8")
    print(f"Geradas {len(unidades_administrativas)} unidades e {meta['cargosFuncoes']} cargos/funções em {SAIDA.name}.")


if __name__ == "__main__":
    main()
