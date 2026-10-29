# Diário — Ferramenta de Transição de Governo

## 2026-10-07 — Card do total de pontos da estrutura
- Feito: acrescentado ao painel permanente um quarto card, "Total da estrutura", em primeiro lugar na faixa: valor grande com o total da estrutura proposta, recalculado a cada alteração, e abaixo, em letra miúda, o total da situação atual como referência fixa, com a diferença entre os dois. Antes o painel só mostrava movimento — liberados, consumidos e saldo —, nunca o tamanho absoluto da estrutura.
- Decidido: os ajustes avulsos ficam fora da conta. Por definição são cargos sem unidade na estrutura, e somá-los faria o card dizer uma coisa diferente do que o rótulo promete. O total da situação atual não se move quando a proposta muda — é referência, não resultado.
- Verificado no navegador: estrutura atual da SPU em 378,15 pontos; extinguindo a Divisão Virtual de Avaliação e elevando o Secretário de FCE 1.15 para CCE 1.17, a proposta vai a 381,82 com diferença de +3,67. A diferença bate exatamente com o que o demonstrativo de movimentos apura (consumidos menos liberados), e o total da situação atual não se mexeu.
- Publicado: versão 2 do artefato, em https://claude.ai/artifact/A7WTuctjGw9i2XNCw5JWJL.


## 2026-10-07 — Publicação como artefato
- Feito: publicada uma versão da ferramenta como artefato em https://claude.ai/artifact/A7WTuctjGw9i2XNCw5JWJL, com a base `dados-estrutura-spu.js` publicada ao lado da página. Adaptações exigidas pela moldura do artefato, que bloqueia três coisas que a versão local usa: as caixas do navegador (`confirm`/`alert`) viraram uma caixa de diálogo própria, em português e com a ação destrutiva em vermelho e o foco inicial em "Cancelar"; os downloads viraram entrega por cópia, numa caixa que mostra o conteúdo e o nome de arquivo sugerido, com botão de copiar e seleção como alternativa; o BOM do CSV saiu, porque o conteúdo agora passa pela área de transferência e o BOM apareceria como caractere solto na primeira célula.
- Corrigido de passagem: a limpeza de acentos do nome de arquivo dependia de caracteres combinantes crus no fonte e quebrava quando a página era servida sem declaração de codificação; passou a usar escapes `\u0300-\u036f`. A árvore de unidades ganhou rolagem horizontal própria, para não empurrar a página inteira em tela estreita, e as grades de campos passam a empilhar abaixo de 900px.
- Verificado no navegador: 291 unidades carregadas, caixa de confirmação extinguindo a Divisão Virtual de Avaliação e liberando 0,83 ponto, caixa de saída do quadro comparativo com nome e conteúdo corretos, e nenhum erro de console depois da correção de codificação.
- Observação: o artefato é privado. Para alguém da equipe abrir, é preciso compartilhar pelo menu da própria página.
- Mantido: a versão local `ferramenta-transicao.html` continua intacta, com download de arquivo, que funciona fora da moldura. As duas precisam ser atualizadas juntas quando a ferramenta mudar.


## 2026-08-18 — Abertura da pasta, resgate das duas ferramentas e protótipo integrado
- Feito: pasta criada; baixada a cópia fiel do simulador publicado em `sostena-boop/simulador-de-cargos`; lido o módulo de regimento interno da DECIP colocado por Juarez na pasta; mapeado o que cada um faz e onde se encaixam; construído e testado em navegador o `ferramenta-transicao.html`, arquivo único e offline, com quatro abas (Estrutura, Cargos e pontos, Regimento, Quadro comparativo), painel permanente de pontos e silhueta, guarda automática no navegador e quatro saídas (cenário `.json`, demonstrativo `.csv`, minuta de competências `.txt`, quadro comparativo `.txt`).
- Decidido: a unidade organizacional é o objeto comum às duas ferramentas, e os pontos passam a ser consequência do que se faz com a estrutura, em vez de digitados à parte — é o que impede a minuta do decreto e a do regimento de divergirem; os dois momentos jurídicos (decreto fixa quantidade e nível; regimento fixa denominação e competências) ficam explícitos, com interruptor que libera as competências de Diretoria quando a transição também altera o decreto; a silhueta passa a ser recontada a cada mudança em vez de declarada fixa no cabeçalho; a tabela manual do simulador antigo sobrevive como "ajustes avulsos", para cargos sem unidade correspondente no regimento.
- Ficou pendente: os níveis de cargo da estrutura atual são sugestão por nível hierárquico e precisam ser substituídos pelos valores do Anexo II do decreto — nenhuma das ferramentas de origem trazia o cargo de cada unidade, e sem isso o saldo não vale como peça de processo; confirmar a vigência da tabela CCE/FCE; confirmar se a DIFIS se subordina mesmo à Diretoria e não à CGFIS, como está na fonte; decidir se a transição roda por diretoria ou pela SPU inteira numa árvore só; decidir se a ferramenta deve chegar a gerar minuta de decreto e texto articulado do regimento.

## 2026-08-18 — Carga da SPU inteira, cargos reais do SIORG e árvore em acordeões
- Feito: analisada a exportação `relatorio-dinamico-estrutura-viva.html`; identificadas 292 unidades, das quais 291 administrativas e um colegiado, e 302 cargos/funções; cotejado o art. 2º do `RI SPUv2.docx`; aplicada a retificação posterior da Divisão de Vendas; criado `gerar_dados_spu.py` e gerada a base auditável `dados-estrutura-spu.js`.
- Decidido: o SIORG prevalece para código e cargo; o RI SPUv2 prevalece para denominação e quatro vinculações documentadas; a retificação de 05/08 entra como camada explícita; o Conselho Estratégico fica fora da árvore administrativa; unidade e posição passam a ser objetos distintos.
- Interface: criados quatro macroacordeões — Secretaria, Gabinete, Diretorias e Superintendências —, com acordeão próprio para cada Diretoria e Superintendência, busca por nome/sigla/SIORG/cargo e edição de cargo titular e posições adicionais. Secretário-Adjunto, Assessores e Gerente de Projeto ficam diretamente na Secretaria; o Gabinete mantém somente o Chefe de Gabinete e suas subunidades.
- Verificado em navegador: 291 unidades na aba Regimento, 6 Diretorias, 27 Superintendências, 5 posições na Secretaria, 1 cargo no Gabinete, abertura da subárvore do Gabinete com três unidades, busca por DECIP, saldo inicial zero, inclusão/remoção de posição adicional e ausência de erros no console. Cálculos conferidos: FCE 1.15 → CCE 1.15 consome 2,32; CCE 2.13 → FCE 2.13 libera 1,65; restaurações voltam a zero.
- Pendente: confirmar o ato vigente da tabela de pontos e a equivalência de categorias 2/3; reconciliar integralmente as competências do RI SPUv2; confirmar a identidade histórica 618711/638171; validar com a área o Conselho Estratégico fora da árvore e a precedência da retificação Divisão de Vendas.

## 2026-08-18 — Escopo concentrado em estrutura e cargos
- Decidido por Juarez: a minuta de regimento e a edição de competências não são necessárias nesta etapa. A interface passa de quatro para três abas — Estrutura, Cargos e pontos e Quadro comparativo — e a exportação de minuta de regimento deixa de ser oferecida.
- Ajustado: a unidade raiz da SPU explicita o campo "Denominação da Secretaria"; o cargo titular do Secretário aparece primeiro entre as posições vinculadas e pode ser trocado entre FCE e CCE. A diferença de pontos é calculada e a alteração aparece no quadro comparativo.
- Preservado: o SIORG, o RI SPUv2 e os documentos de correspondência continuam sendo as fontes da árvore reconciliada. A retirada da minuta é uma decisão de escopo atual, não descarte dessas fontes nem impedimento de retomada futura.
- Verificado: o JavaScript inline passou na validação sintática; a interface contém somente as três abas previstas e não referencia mais os controles da minuta; a base mantém 291 unidades e identifica o Secretário como titular FCE 1.17. Pela tabela embutida, sua troca para CCE 1.17 consome 3,20 pontos. A abertura automatizada do arquivo local no navegador interno foi bloqueada pela política de URL do navegador, portanto esta alteração específica ficou sem nova inspeção visual automatizada.

## 2026-10-29 — Primeiro protótipo consolidado de Desenho Organizacional

- Decidido com Juarez: a antiga Ferramenta de Transição de Governo passa a ser tratada como **Desenho Organizacional**; cada projeto corresponde a um processo de alteração e é identificado pela data de abertura, sem nome, objetivo ou responsável digitados. Prazo, processo SEI, estado e observações pertencem ao projeto.
- Especificado: cenários alternativos; referência SIORG e tabela de pontos congeladas; reunião e histórico; consulta pública separada; simulador rápido privado; Regimento Interno independente, mas vinculável; regras de criação, remanejamento e extinção; visibilidade pública; exportações e arquitetura futura. O registro completo está em `REQUISITOS.md`.
- Implementado localmente em `ferramenta-transicao.html`: página inicial privada com três módulos; metadados do projeto; quarta aba para reuniões e histórico; painel de anotação durante reunião; estrutura em duas colunas; unidade criada a partir do cargo; linguagem “cargo que chefia a unidade” e “outros cargos vinculados”; extinção de ramo sem remanejamento silencioso; prévia pública com comparação, árvore e pontos agregados.
- Integrado sem copiar: `simulador-de-cargos-original.html` e `../../Produção de Textos Normativos/Regimento Interno/modulo_DECIP_regimento_interno_3.html` são carregados como módulos independentes.
- Verificado em navegador: página inicial; projeto; árvore com 291 unidades; seleção e comparação de unidade; diálogo de criação; simulador; Regimento v3; consulta pública; abertura de reunião, registro de proposta e marco de encerramento. O JavaScript passou na validação sintática e a página respondeu HTTP 200.
- Mantido fora desta etapa: gerenciamento completo de vários cenários, cenário principal, metas de pontos, validações de publicação, DOCX e colaboração multiusuário.
- Preservada a regra: nenhuma alteração foi feita no GitHub ou no Supabase. A próxima decisão depende da avaliação do protótipo local por Juarez.

## 2026-10-29 — Revisão após comentários no navegador

- Simplificado: retirada a busca por código SIORG, o botão “Abrir resultados”, os textos explicativos extensos, a faixa técnica da base, os ajustes avulsos e a estrutura de reuniões/classificações.
- Alterado: a árvore começa recolhida; a busca por nome ou sigla abre automaticamente somente os resultados; permaneceram “Limpar busca” e “Recolher tudo”.
- Acrescentado: meta de manutenção, redução ou aumento autorizado, com acompanhamento no painel superior; título automático “Proposta de Desenho Organizacional — DD/MM/AAAA”; subtítulo opcional; estados apenas “Em elaboração” e “Concluída”.
- Cargos: criação de unidade limitada a CCE/FCE 1.xx; outros cargos vinculados limitados a CCE 2/3 e FCE 2/3/4. Incorporadas à referência as faixas completas consultadas no SIORG Cidadão em 29/10/2026, inclusive FCE 4.01 a FCE 4.13.
- Notas: criadas notas gerais da proposta e notas próprias de cada unidade, separadas do histórico automático.
- Comparação: os cards de mantidas, alteradas, criadas e extintas passaram a filtrar a tabela e permitem retirar o filtro com novo clique.
- Regimento: incluídos os caminhos “Criar regimento deste desenho” e “Criar desenho a partir deste regimento”, com tela de conferência e registro do vínculo; a transferência integral dos artigos permanece como etapa posterior.
- Verificado no navegador: sintaxe JavaScript; árvore inicialmente recolhida; busca automática por DECIP; meta de redução; filtros comparativos; inclusão e remoção de nota; criação de unidade somente com códigos 1.xx; novo cargo vinculado somente com CCE 2/3 e FCE 2/3/4; tabela com 114 códigos; ausência das tabelas de ajustes avulsos; confirmação dos dois sentidos do vínculo entre módulos.
- Mantido: protótipo exclusivamente local, sem alteração no GitHub ou no Supabase.

## 2026-10-29 — Comparação pública e consolidação das notas

- Reformulada a prévia pública: dois quadros lado a lado mostram a estrutura atual e a proposta, com hierarquia, denominação, sigla, subordinação e situação. Exclusões aparecem em vermelho, alterações em amarelo e criações em verde; em telas menores os quadros se empilham.
- Rebaixado o JSON a “Backup do protótipo”, dentro de controle recolhível. O texto informa que o recurso será retirado quando o sistema publicado tiver persistência própria.
- Ampliada a aba Notas e histórico: todas as notas vinculadas a unidades são agrupadas por unidade; o resumo informa número de notas e unidades; “Abrir unidade” seleciona a unidade correspondente e abre seu caminho na árvore.
- Verificado no navegador: 291 linhas em cada quadro no cenário sem mudanças; cenário alterado com três linhas vermelhas e uma verde; alteração temporária destacada em amarelo nos dois quadros; nota temporária listada no consolidado, retorno correto à Secretaria e remoção sem resíduo.
- Mantido: nenhuma publicação ou alteração em GitHub/Supabase.

## 2026-10-29 — Expansão e ordem da árvore

- Incluído “Abrir tudo” ao lado de “Recolher tudo”. O primeiro expande todos os blocos e todas as unidades; o segundo fecha integralmente a árvore.
- Reordenados os grandes blocos: Secretaria e Gabinete, Diretorias, demais unidades diretamente subordinadas à Secretaria e, por último, Superintendências.
- Ajustada a navegação das notas para abrir o novo bloco correto quando a unidade for diretamente subordinada à Secretaria.
- Verificado no navegador: 304 elementos expansíveis abertos e depois nenhum aberto; Superintendências confirmadas como o último bloco, inclusive com unidade nova diretamente subordinada à Secretaria.
- Mantido: nenhuma publicação ou alteração em GitHub/Supabase.

## 2026-10-29 — Revisão final antes da publicação

- Retirados da prévia o saldo e a tabela de pontos.
- Criado comparativo de cargos por código, com quantidades atual e proposta e diferença; aumento aparece em verde e redução em vermelho.
- Substituídos os cards por quatro tipos de mudança: alteradas, remanejadas, criadas e excluídas. Todos filtram o quadro comparativo interno e a comparação pública.
- Verificado no navegador: ausência de pontos na prévia; presença do comparativo de cargos; filtro de unidade criada na prévia; filtro de unidade remanejada no quadro interno.
- Autorização posterior de Juarez para iniciar a preparação da publicação no GitHub e da persistência no Supabase, condicionada à conferência das contas e dos acessos.

## 2026-10-29 — Preparação de GitHub e Supabase

- Confirmado pelo conector: conta pessoal do GitHub `sostena-boop`, distinta de `SPU-ProjetoseProcessos`; o login do terminal estava vencido e foi iniciado novo fluxo oficial de autorização.
- Confirmado pelo conector: organização Supabase pessoal com os projetos `spuprocessos` e `indexador`; adotado `spuprocessos` conforme decisão anterior.
- Criadas no Supabase as tabelas `desenho_projetos`, `desenho_cenarios`, `desenho_revisoes` e `desenho_publicacoes`, todas com RLS. Dados privados usam propriedade por `auth.uid()`; consulta sem login alcança apenas publicações sanitizadas e ativas.
- Executados os consultores de segurança e desempenho. Não surgiu alerta de RLS nas novas tabelas; foram criados os índices indicados para as novas chaves estrangeiras.
- Preparados `index.html`, `README.md`, `.gitignore`, migrações versionadas e cópia local do módulo de Regimento Interno para que a versão publicada não dependa de caminhos externos ao repositório.
