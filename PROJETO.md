# Desenho Organizacional

## Objetivo

Ferramenta privada para elaborar projetos de alteração da estrutura da SPU. Cada projeto parte de uma fotografia congelada da estrutura vigente, permite trabalhar cenários alternativos e transforma alterações em demonstrativo de cargos e pontos. Notas e versões precisam permanecer rastreáveis.

O produto também terá duas ferramentas privadas relacionadas, mas independentes:

- simulador rápido de cargos e pontos, para cálculos avulsos;
- módulo de Regimento Interno, que pode ser iniciado a partir de uma estrutura aprovada ou de forma independente.

A consulta pública será uma página própria, somente leitura, gerada a partir de uma versão expressamente publicada.

## Estado atual

Protótipo publicado no GitHub Pages e conectado ao projeto Supabase `spuprocessos`. A ferramenta funciona sem login com cópia local; depois da autenticação, o projeto corrente também é sincronizado e pode receber versões recuperáveis.

O protótipo contém:

- página privada inicial com as três entradas e o projeto recente;
- título automático pela data de abertura, subtítulo opcional, prazo, processo SEI e estado;
- cenário inicial “Cenário A” e base SIORG congelada;
- painel permanente com total da estrutura, pontos liberados, consumidos, saldo, meta e silhueta;
- estrutura em árvore, organizada por Secretaria, cada Diretoria, unidades diretamente subordinadas e, por último, o grupo de Superintendências;
- controles “Abrir tudo” e “Recolher tudo” para expansão integral da árvore;
- seleção da unidade na árvore e edição em painel separado, com comparação da situação atual;
- criação de unidade iniciada pela escolha do cargo ou função que a chefia;
- criação de unidade limitada a CCE/FCE 1.xx e outros cargos vinculados limitados a CCE 2/3 e FCE 2/3/4;
- extinção de ramo sem remanejamento silencioso das subordinadas;
- abas de Cargos e pontos, Quadro comparativo e Notas e histórico;
- notas livres gerais e notas ligadas a cada unidade, com visão consolidada por unidade e acesso direto à árvore;
- cards do quadro comparativo que também funcionam como filtros;
- botões de passagem do desenho para o regimento e do regimento para o desenho;
- prévia local da consulta pública, com tabelas lado a lado da estrutura atual e da proposta, destaques por cor e cargos/pontos agregados;
- backup JSON recolhido como recurso temporário do protótipo, a ser retirado quando houver persistência publicada;
- acesso por e-mail/senha ou link/código para contas já cadastradas no Supabase;
- salvamento remoto automático com cópia local de segurança;
- versões manuais e restauração na aba de Notas e histórico;
- simulador rápido carregado de `simulador-de-cargos-original.html`;
- protótipo mais recente de Regimento Interno carregado de `../../Produção de Textos Normativos/Regimento Interno/modulo_DECIP_regimento_interno_3.html`.

Base atual: **291 unidades administrativas e 302 cargos/funções**, em `dados-estrutura-spu.js`. A base é regenerável por `gerar_dados_spu.py`.

## Decisões vigentes

As decisões detalhadas estão em `REQUISITOS.md`. Em síntese:

- projeto é cada processo de alteração da estrutura, pequeno ou grande;
- não há nome, objetivo resumido nem responsável digitados; a abertura é identificada pela data;
- um projeto pode ter cenários A, B etc. e um cenário principal;
- estrutura de referência e tabela de pontos ficam congeladas por projeto;
- a unidade é criada a partir do cargo ou função que a chefia;
- a ferramenta controla posições, não pessoas ocupantes;
- remuneração não polui a árvore; aparece no simulador e nas áreas de cálculo;
- notas não alteram a estrutura automaticamente;
- estrutura e regimento são módulos separados, com vínculo opcional;
- a versão pública não expõe histórico, dados internos, remuneração, código SIORG nem cargo de chefia;
- observação só aparece publicamente quando marcada expressamente para divulgação;
- protótipo local precede qualquer alteração no GitHub ou no Supabase.

## Verificação de 29/10/2026

Verificado em navegador por servidor local:

- carregamento da página privada inicial;
- abertura do projeto e da árvore com 291 unidades;
- seleção da Secretaria e painel atual × proposta;
- diálogo de criação iniciada pelo cargo;
- simulador rápido integrado;
- Regimento Interno v3 integrado sem duplicação do arquivo;
- prévia pública com comparação, agrupamentos e tabela agregada de pontos;
- metas de manutenção, redução e aumento autorizado;
- busca por nome ou sigla com abertura automática dos resultados;
- abertura e recolhimento integral da árvore e Superintendências confirmadas como último bloco;
- filtros do quadro comparativo;
- notas gerais e por unidade;
- listas separadas de códigos que criam unidade e códigos de assessoria/técnicos, incluindo FCE 4.xx;
- os dois sentidos do vínculo entre desenho e regimento;
- comparação pública lado a lado com exclusões em vermelho, alterações em amarelo e criações em verde;
- prévia pública sem pontos, com comparativo de quantidades de cargos e variações positivas em verde e negativas em vermelho;
- filtros por unidades alteradas, remanejadas, criadas e excluídas no quadro interno e na prévia;
- consolidação de todas as notas por unidade, com navegação direta para a unidade;
- JavaScript inline validado sintaticamente;
- resposta HTTP 200 do protótipo.

## Próximos passos

Publicação inicial concluída:

- repositório: `https://github.com/sostena-boop/desenho-organizacional`;
- GitHub Pages: `https://sostena-boop.github.io/desenho-organizacional/`.

1. Cadastrar a conta pessoal que editará a ferramenta no Auth do projeto `spuprocessos` e validar o primeiro login ponta a ponta.
2. Completar o gerenciamento de vários projetos/cenários e a escolha do cenário principal.
3. Implementar a publicação sanitizada da consulta em página separada e somente leitura.
4. Projetar a geração de DOCX para o projeto e para o esqueleto do regimento.
5. Revisar as fontes e a vigência da tabela de cargos/pontos com SIORG e ato normativo.

## Fontes e arquivos relacionados

- `REQUISITOS.md` — especificação consolidada das rodadas de decisão.
- `dados-estrutura-spu.js` — fotografia local da estrutura e dos cargos.
- `relatorio-dinamico-estrutura-viva.html` — exportação de referência do SIORG.
- `simulador-de-cargos-original.html` — simulador avulso incorporado como módulo privado.
- `../../Produção de Textos Normativos/Regimento Interno/modulo_DECIP_regimento_interno_3.html` — referência funcional mais recente do módulo de regimento.
- SIORG Cidadão — organograma e cargos comissionados, fontes externas que precisarão ser consultadas e datadas quando a base for atualizada.

## Riscos e pendências de dados

- A vigência da tabela de remuneração e pontos precisa ser documentada antes de uso oficial.
- A base local é uma fotografia e não deve ser tratada como sincronizada automaticamente com o SIORG.
- Categorias CCE 2/3 e FCE 2/3/4 precisam permanecer aderentes ao ato vigente.
- A consulta pública ainda é uma prévia dentro da ferramenta; falta gerar uma publicação sanitizada em página separada.
- O Auth do projeto está com novos cadastros desativados. O e-mail pessoal informado ainda precisa ser cadastrado ou convidado antes do primeiro teste autenticado.
- O fluxo atual abre o projeto mais recentemente atualizado do usuário; a tela de escolha entre vários projetos e cenários ainda não foi implementada.
