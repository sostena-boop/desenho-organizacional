# Desenho Organizacional

Ferramenta para elaborar e comparar propostas de estrutura organizacional, simular cargos e pontos, registrar notas e iniciar o esqueleto de um regimento interno.

## Estado atual

Esta primeira versão publicada preserva o funcionamento do protótipo validado. Os dados de trabalho ainda são guardados no navegador. A estrutura de persistência autenticada já foi criada no projeto Supabase `spuprocessos` e será conectada à interface na etapa seguinte.

As tabelas usam o prefixo `desenho_` para permanecerem separadas das demais ferramentas do mesmo projeto. Todas têm RLS; os dados de trabalho pertencem ao usuário autenticado, e somente uma publicação sanitizada pode ser consultada sem login.

## Executar localmente

Sirva esta pasta por HTTP e abra `index.html`. Por exemplo:

```bash
python3 -m http.server 8767
```

Depois acesse `http://127.0.0.1:8767/`.

## Fontes de referência

- Estrutura organizacional: fotografia local derivada do SIORG e do regimento interno vigente.
- Cargos, remunerações e pontos: tabela incorporada ao protótipo, cuja vigência deve ser conferida antes do uso em processo oficial.

## Segurança e privacidade

Não publique arquivos JSON de backup: eles podem conter propostas, notas e históricos de trabalho.
