# Desenho Organizacional — Requisitos e decisões

## Finalidade deste documento

Concentrar as regras funcionais, decisões e questões em aberto da ferramenta **Desenho Organizacional**. Este arquivo antecede alterações relevantes no protótipo e serve para evitar sucessivas reescritas do mesmo código.

## Forma de trabalho

- Primeiro discutir e registrar requisitos e regras.
- Agrupar decisões por bloco funcional.
- Só alterar o protótipo local quando o bloco estiver suficientemente definido.
- Validar visualmente o protótipo antes de qualquer integração externa.
- Não alterar GitHub ou Supabase sem autorização expressa após a validação do protótipo.
- Não transformar proposta, hipótese ou fala de reunião em decisão confirmada.

## Nome e finalidade

**Nome de trabalho:** Desenho Organizacional.

**Finalidade:** apoiar a elaboração, análise e documentação de propostas de alteração da estrutura organizacional, incluindo unidades, subordinações, cargos e funções, pontos, histórico de discussão, comparação com a estrutura de referência e preparação de um esqueleto de regimento interno.

## Fontes de referência

- Organograma vigente do SIORG.
- Tabela de remuneração e CCE unitário do SIORG.
- Regimento interno vigente.
- Proposta de regimento interno em tramitação, quando aplicável.
- Documentos de correspondência, retificação e demais fontes expressamente identificadas.

Cada carga ou extração deverá registrar fonte, endereço, data de consulta e versão ou vigência conhecida.

## Arquitetura funcional preliminar

### Área de trabalho autenticada

1. Projetos e cenários.
2. Estrutura organizacional.
3. Cargos e pontos.
4. Comparação entre estrutura de referência e proposta.
5. Reuniões e histórico.
6. Regimento interno.
7. Publicação de uma versão para consulta.

Além dos projetos, a área autenticada terá um **simulador rápido de cargos e pontos**, destinado a cálculos avulsos que não alteram uma estrutura nem exigem a criação de projeto.

### Página pública de consulta

- Sem login e sem edição.
- Exibe apenas uma versão expressamente publicada.
- Apresenta a proposta e a comparação com a estrutura de referência.
- Não exibe rascunhos, anotações de reunião, justificativas internas ou pendências não autorizadas.

## Estrutura e comparação

A ferramenta deverá distinguir, no mínimo:

- unidade mantida;
- unidade renomeada;
- unidade remanejada;
- unidade criada;
- unidade extinta;
- unidade resultante de fusão;
- unidade resultante de desmembramento.

A comparação deverá contemplar denominação, sigla, natureza, subordinação, cargos e funções, pontos e situação da unidade.

## Reuniões e histórico

A ferramenta deverá permitir registrar falas, propostas, decisões, pendências e responsáveis sem confundir essas categorias. O histórico deverá permanecer associado ao projeto e, quando indicado, a uma unidade ou alteração específica.

## Regimento interno

O trabalho de estrutura e o trabalho de regimento serão módulos separados, ainda que possam ser relacionados.

- Em regra, a proposta de estrutura será elaborada e aprovada antes do início do regimento correspondente.
- Também será possível iniciar um trabalho de regimento sem uma proposta estrutural anterior.
- Quando houver uma estrutura aprovada, ela poderá alimentar o esqueleto do regimento.
- O módulo de regimento poderá ter permissões próprias, inclusive edição restrita às áreas responsáveis por determinados artigos ou unidades.
- A ferramenta local `modulo_DECIP_regimento_interno_3.html` será tratada como referência funcional para esse módulo, pois já permite visualização integral do regimento e edição restrita à área da DECIP, incluindo propostas de denominação e vinculação.

Cada unidade proposta deverá registrar sua relação com uma ou mais unidades da estrutura anterior.

- Unidade mantida: oferece o artigo anterior como referência.
- Unidade renomeada: atualiza o caput e oferece as competências anteriores para reaproveitamento.
- Unidade remanejada: oferece o texto anterior e sinaliza a necessidade de revisar sua compatibilidade com a nova subordinação.
- Unidade nova: gera esqueleto de artigo com competências a definir.
- Fusão: apresenta os artigos das unidades de origem para consolidação.
- Desmembramento: apresenta o artigo de origem para distribuição das competências.
- Extinção: não gera artigo na proposta, mas permanece no histórico e no comparativo.

O reaproveitamento de competências nunca será automático. O usuário deverá confirmar se deseja reaproveitar sem alteração, reaproveitar e editar, começar em branco ou usar outra unidade como fonte.

### Saídas previstas

- Versão de trabalho em DOCX, com textos de referência destacados, fontes e pendências.
- Minuta limpa em DOCX, somente com o texto proposto.

## Persistência e publicação

- O protótipo local continuará sendo a primeira superfície de validação.
- A persistência futura poderá utilizar o projeto Supabase existente `spuprocessos`, em área isolada para Desenho Organizacional.
- A publicação futura poderá utilizar a conta pessoal GitHub `sostena-boop`.
- Nenhuma dessas integrações será implementada antes da validação expressa do protótipo.

## Decisões — rodada 1

### Projeto e cenários

- Cada projeto corresponde a um processo específico de alteração da estrutura organizacional.
- Um projeto pode tratar de uma mudança pequena, como a alteração de um ou dois cargos, ou de uma reestruturação mais ampla.
- Esses processos podem ocorrer em ciclos anuais, de aproximadamente um ano e meio ou em outra periodicidade determinada pela necessidade administrativa.
- Cada projeto parte da estrutura completa de referência e pode conter cenários alternativos, como “Cenário A” e “Cenário B”.
- Os cenários poderão ser copiados, comparados e posteriormente escolhidos como proposta principal do projeto.

### Estrutura de referência

- A estrutura vigente será congelada como uma fotografia no momento de criação do projeto.
- Uma alteração posterior no SIORG não modificará silenciosamente projetos em andamento.
- A ferramenta poderá avisar sobre uma base mais recente e oferecer uma comparação, preservando a referência original do projeto.

### Registro durante reuniões

- A captura deverá priorizar rapidez e baixa fricção.
- Toda entrada poderá começar como uma nota livre.
- Durante ou depois da reunião, a nota poderá ser classificada como proposta, decisão, pendência ou encaminhamento.
- A nota poderá ser associada a uma unidade ou alteração específica.

### Consulta pública

- A página pública exibirá, por padrão, somente a versão publicada mais recente.
- Versões anteriores permanecerão preservadas internamente.
- Uma versão anterior somente continuará disponível publicamente mediante decisão expressa.

## Decisões — rodada 2

### Estados do projeto

- Em elaboração.
- Em discussão.
- Em aprovação.
- Concluído.
- Cancelado.

“Publicado” será estado de uma versão, e não do projeto.

### Cenário principal

- Somente um cenário poderá ser marcado como proposta principal do projeto por vez.
- Os demais cenários permanecerão guardados como alternativas.
- A escolha ou troca do cenário principal será registrada no histórico.

### Histórico automático

- Toda alteração registrará usuário, data, situação anterior e situação nova.
- Alterações realizadas durante uma reunião aberta serão automaticamente vinculadas a ela.
- Não será exigida justificativa para cada operação elementar.
- Antes da publicação, deverá existir uma justificativa geral da alteração ou da versão.

### Meta de pontos

O projeto poderá adotar uma das seguintes metas:

- neutralidade, com saldo zero;
- redução de determinada quantidade de pontos;
- acréscimo autorizado de determinada quantidade de pontos;
- saldo livre, apenas para simulação.

A meta não bloqueará a edição. A ferramenta mostrará a diferença entre resultado e meta e emitirá alerta antes da publicação quando a meta não tiver sido atingida.

## Decisões — rodada 3

### Identificação e dados do projeto

- O projeto não terá nome nem objetivo resumido preenchidos pelo usuário.
- Sua identificação visível será gerada automaticamente a partir da data de abertura, no padrão “Alteração organizacional aberta em DD/MM/AAAA”.
- A data de abertura será registrada automaticamente na criação.
- O responsável não será solicitado como campo, pois será o próprio usuário que criou o projeto.
- O projeto terá campo de prazo ou data de vencimento para a resposta demandada.
- O projeto terá campo para o número do processo SEI.
- O projeto terá campo de observações gerais.
- Se houver mais de um projeto aberto na mesma data, o sistema manterá um identificador interno adicional para distingui-los sem exigir um nome do usuário.
- O prazo poderá ficar em branco quando a demanda ainda não tiver data definida.
- Quando informado, o prazo será destacado com indicadores de situação, como “em dia”, “próximo do vencimento” e “vencido”.

### Criação e comparação de cenários

- Um cenário inicial, idêntico à estrutura de referência congelada, será criado automaticamente com o projeto.
- Um novo cenário poderá partir da estrutura de referência ou ser criado como cópia de outro cenário.
- Será possível comparar dois cenários entre si.
- Na consulta pública, a comparação principal será entre a estrutura de referência e o cenário principal.

### Arquivamento e exclusão

- Projetos e cenários que já possuam histórico não serão excluídos pela interface; serão arquivados.
- Somente um cenário vazio, criado por engano e ainda sem alterações, poderá ser eliminado.

### Página inicial

A página inicial será organizada em tabela e mostrará, no mínimo:

- data de abertura e identificação automática do projeto;
- prazo e situação do prazo;
- número do processo SEI;
- estado do projeto;
- última atualização;
- cenário principal;
- meta e resultado em pontos;
- alertas relevantes.

A página terá busca e filtros por estado, prazo e período.

## Decisões — rodada 4

### Árvore de referência e árvore proposta

- A árvore proposta será a superfície principal de edição.
- A estrutura de referência será imutável.
- Ao selecionar uma unidade, a interface mostrará a situação atual e a proposta para aquela unidade.
- A estrutura vigente completa poderá ser aberta para consulta.
- Alterações serão destacadas por cores e rótulos de situação.

### Extinção e remanejamento com subunidades

- Nenhuma subunidade será eliminada silenciosamente.
- Ao extinguir uma unidade com subordinadas, o usuário deverá escolher entre extinguir toda a ramificação ou remanejar as subunidades antes da extinção da unidade superior.
- Ao remanejar uma unidade, sua ramificação acompanhará o movimento.
- Para mover somente a unidade superior, será necessário definir previamente o destino das subordinadas.

### Unidades novas

- Unidades novas receberão identificador temporário automático, como `NOV-001`.
- Enquanto não houver código oficial, serão apresentadas com o rótulo “Sem código SIORG”.
- O código SIORG oficial poderá ser informado posteriormente sem perda do histórico da unidade.

### Movimentos externos de pontos

- Haverá área própria para recebimento, cessão ou permuta de pontos ou cargos sem unidade correspondente.
- Esses movimentos afetarão o saldo disponível do projeto.
- Os movimentos externos permanecerão separados do total de cargos efetivamente vinculados à estrutura proposta.

## Decisões e ajustes — rodada 5

### Simulador rápido

- Haverá uma aba ou entrada privada para o simulador rápido de cargos e pontos.
- O simulador será independente dos projetos e da edição da estrutura.
- Seu objetivo será permitir cálculos avulsos, como verificar quantos cargos de determinado nível podem ser obtidos com certa quantidade de pontos.
- O simulador não aparecerá na página pública de consulta.
- O simulador existente será revisado em etapa própria.

### Cargo que dá origem à unidade

- Na modelagem adotada, uma unidade administrativa será criada a partir da escolha do cargo ou função que a chefia.
- A interface não usará como rótulo principal a expressão técnica “cargo titular”.
- A criação de uma unidade administrativa sem o respectivo cargo de chefia não fará parte do fluxo normal.
- Quando o cargo for selecionado, a ferramenta poderá sugerir a natureza ou o nível da unidade correspondente, sujeito à confirmação do usuário.

### Apresentação dos valores

- Remuneração e detalhamento de pontos não serão exibidos permanentemente na árvore da estrutura.
- Durante a seleção ou alteração de um cargo, a interface poderá mostrar o impacto em pontos de forma contextual.
- Tabelas e valores detalhados ficarão na área de cargos e pontos e no simulador rápido.

### Pessoas ocupantes

- A ferramenta controlará posições organizacionais, e não pessoas ocupantes.

### Versão da tabela de pontos

- O projeto guardará a versão da tabela utilizada, com fonte e data de consulta.
- Uma atualização da tabela não modificará silenciosamente os cálculos anteriores.
- A ferramenta poderá oferecer comparação e recálculo expresso com uma nova versão.

### Validações aceitas

Impedirão a publicação:

- subordinação circular;
- unidade ativa subordinada a unidade extinta;
- código SIORG duplicado;
- código de cargo inexistente na tabela selecionada;
- posição sem quantidade válida;
- ausência de cenário principal.

Gerarão alerta, sem bloqueio:

- sigla ausente ou repetida;
- unidade nova ainda sem código SIORG;
- meta de pontos não atingida;
- existência de tabela de pontos mais recente;
- campos regimentais ainda não preenchidos, quando o módulo de regimento estiver em uso.

“Unidade sem cargo de chefia” deixa de ser tratada como simples alerta, porque a criação da unidade administrativa partirá obrigatoriamente da escolha desse cargo.

## Decisões — rodada 6

### Página privada inicial

A página privada inicial terá três entradas principais:

- Desenho Organizacional;
- Simulador rápido;
- Regimento Interno.

Abaixo das entradas serão apresentados os trabalhos recentes.

### Simulador rápido

- Será temporário por padrão, como um cálculo de “papel de pão”.
- Permitirá limpar, copiar e exportar o cálculo.
- Não exigirá criação de projeto nem produzirá histórico automaticamente.
- A possibilidade de salvar um cálculo poderá ser acrescentada posteriormente, caso se mostre necessária.

### Outros cargos vinculados

- Cargos que não dão origem a unidade própria, como assessorias e gerências de projeto, serão chamados de “outros cargos vinculados”.
- Serão apresentados em seção recolhível da unidade, sem poluir a árvore principal.
- Entrarão normalmente no total de pontos da estrutura.

### Relação opcional entre estrutura e regimento

- Uma estrutura aprovada poderá originar um projeto de regimento.
- Um projeto de regimento poderá ser iniciado de forma independente.
- Um regimento iniciado primeiro poderá ser vinculado posteriormente a um projeto de estrutura.
- O módulo de regimento poderá conceder permissões restritas por artigos, unidades ou áreas responsáveis.

## Decisões — rodada 7

### Abertura da reunião

- A reunião receberá identificação automática no padrão “Reunião de DD/MM/AAAA, HH:MM”.
- Participantes e pauta serão opcionais.
- A reunião pertencerá ao projeto, e não obrigatoriamente a um único cenário.

### Captura de anotações

- A interface terá um campo amplo e simples para anotação rápida.
- Cada registro receberá horário automaticamente.
- Toda entrada começará como nota livre.
- A nota poderá ser classificada durante ou depois da reunião como proposta, decisão, pendência ou encaminhamento.
- Quando aplicável, a nota poderá ser associada a um cenário e a uma unidade específica.

### Aplicação de propostas

- Uma proposta registrada em reunião não alterará automaticamente a estrutura.
- A ação “Aplicar ao cenário” mostrará previamente o impacto sobre a unidade e os pontos.
- A alteração efetiva permanecerá vinculada à proposta que lhe deu origem.

### Encerramento da reunião

Ao finalizar a reunião, a ferramenta apresentará resumo contendo:

- decisões;
- propostas aplicadas;
- propostas não aplicadas;
- pendências;
- encaminhamentos;
- responsáveis;
- prazos.

## Decisões — rodada 8

### Linha do tempo

- Haverá uma linha do tempo única para reuniões, alterações estruturais, troca do cenário principal, mudanças de meta, versões e publicações.
- Alterações elementares realizadas na mesma sessão serão agrupadas para evitar excesso de eventos visíveis.

### Marcos de versão

Uma versão imutável será criada automaticamente:

- ao encerrar uma reunião;
- ao escolher ou trocar o cenário principal;
- antes de recalcular um cenário com nova tabela de pontos;
- ao publicar uma proposta.

Também haverá a ação “Criar marco agora”.

### Recuperação

- Uma versão anterior nunca substituirá silenciosamente o cenário atual.
- A ação “Retomar a partir desta versão” criará um novo cenário.
- Todo o histórico posterior à versão retomada permanecerá preservado.

### Filtros do histórico

- período;
- cenário;
- tipo de evento;
- reunião;
- unidade;
- usuário;
- busca textual.

### Saídas do histórico

- resumo de reunião em DOCX;
- relatório consolidado do projeto em DOCX;
- histórico filtrado em Excel ou CSV;
- cópia completa de segurança em JSON.

## Decisões — rodada 9

### Cabeçalho e resumo público

A consulta pública apresentará:

- identificação automática do projeto;
- versão publicada;
- data de publicação;
- data da estrutura de referência;
- justificativa geral aprovada para divulgação;
- total de unidades atual e proposto;
- total de cargos atual e proposto;
- pontos atuais, propostos e diferença;
- meta do projeto;
- quantidades de unidades mantidas, criadas, extintas, renomeadas e remanejadas.

### Organização da árvore pública

A estrutura será apresentada sempre em árvore, com níveis hierárquicos, organizada por grandes unidades expansíveis:

- Secretaria, contendo Gabinete, Coordenações-Gerais e demais unidades diretamente subordinadas;
- uma seção expansível para cada Diretoria, contendo toda a sua árvore;
- uma seção própria de Superintendências, que abrirá o conjunto das Superintendências.

### Visualizações

- Proposta: organograma ou árvore da estrutura proposta.
- Comparação: estrutura atual e proposta, com diferenças destacadas.
- Cargos e pontos: quadro consolidado por código e quantidade.

### Dados da unidade na consulta pública

O detalhe público da unidade mostrará somente:

- denominação;
- sigla;
- subordinação.

Não serão exibidos no detalhe público:

- código SIORG;
- cargo que chefia a unidade;
- demais dados técnicos internos.

O quadro consolidado de cargos e pontos poderá mostrar códigos, quantidades e pontos, sem remuneração individual.

### Dados internos e observações

- Prazo, participantes, notas de reunião, usuários, pendências internas, processo SEI e observações gerais permanecerão ocultos por padrão.
- Uma observação somente poderá aparecer na consulta pública mediante escolha expressa de divulgação.
- A interface deverá perguntar claramente se determinada observação será divulgada.

### Saídas públicas

- impressão ou PDF da proposta;
- quadro comparativo em Excel ou CSV;
- relatório limpo em DOCX.

A consulta pública não fornecerá o JSON completo nem acesso ao histórico interno.

## Decisões — rodada 10

### Topo permanente do projeto

Permanecerão visíveis:

- identificação do projeto e prazo;
- seletor de cenário;
- estado do cenário;
- total de pontos da estrutura atual e da proposta;
- meta e diferença para a meta;
- situação da gravação.

### Navegação do projeto de estrutura

O projeto terá as abas:

- Estrutura;
- Cargos e pontos;
- Comparação;
- Reuniões e histórico.

O Regimento Interno continuará como módulo separado.

### Aba Estrutura

- À esquerda ficará a árvore expansível, organizada em Secretaria, Diretorias e Superintendências.
- À direita ficarão os detalhes da unidade selecionada, com situação atual e proposta.
- Campos de edição somente serão mostrados após a seleção de uma unidade.

### Aba Cargos e pontos

- quadro consolidado;
- movimentos externos;
- simulação do impacto das mudanças;
- remunerações e valores detalhados, sem poluir a árvore.

### Reunião em andamento

- Um botão permanente abrirá painel lateral de anotações sem retirar o usuário da unidade ou aba atual.
- Quando houver unidade selecionada, uma nova nota poderá ser automaticamente associada a ela.

### Comparação, pré-visualização e publicação

- A comparação terá aba própria.
- “Pré-visualizar consulta” será uma ação separada.
- “Publicar versão” será outra ação, sujeita às validações definidas.
- No protótipo local, a publicação será apenas simulada e não enviará dados ao GitHub ou ao Supabase.

## Próximo marco

Preparar uma primeira revisão consolidada do protótipo local com a nova identidade, navegação e organização funcional, preservando a base e os cálculos existentes. Nenhuma integração externa será realizada neste marco.

## Decisões — rodada 11

### Simplificação da estrutura

- A busca utilizará somente denominação e sigla da unidade; o código SIORG não será pesquisado nem mencionado no campo.
- A árvore começará totalmente recolhida.
- A pesquisa abrirá automaticamente apenas os caminhos necessários para mostrar os resultados.
- O botão “Abrir resultados” será retirado; permanecerão “Limpar busca” e “Recolher tudo”.
- Textos explicativos extensos e a faixa técnica sobre carga/reconciliação da base serão retirados do fluxo principal.

### Meta de pontos

A proposta poderá trabalhar com:

- manutenção do total atual;
- redução de uma quantidade informada de pontos;
- aumento autorizado até uma quantidade informada;
- ausência de meta.

O painel superior mostrará o realizado, o restante ou eventual excesso em relação à meta.

### Regras dos códigos de cargos e funções

- CCE e FCE 1.xx criam ou chefiam unidade organizacional.
- CCE 2.xx e 3.xx não criam unidade e poderão ser adicionados como cargos vinculados.
- FCE 2.xx, 3.xx e 4.xx não criam unidade e poderão ser adicionados como funções vinculadas.
- A criação de unidade oferecerá somente códigos 1.xx.
- A inclusão de outro cargo ou função vinculada oferecerá somente CCE 2/3 e FCE 2/3/4.
- Todo cargo ou função deverá estar vinculado a uma unidade; os ajustes avulsos serão retirados.
- A tabela de referência incorporará FCE 4.01 a FCE 4.13, conforme consulta ao SIORG Cidadão em 29/10/2026.

### Identificação e estado

- O título será automático: “Proposta de Desenho Organizacional — DD/MM/AAAA”.
- Haverá subtítulo opcional em uma frase.
- Os estados serão somente “Em elaboração” e “Concluída”.

### Comparação

Os cards de unidades mantidas, alteradas, criadas e extintas também funcionarão como filtros da tabela. Clicar novamente no card ativo removerá o filtro.

### Notas e histórico

- O conceito de reunião e suas classificações serão retirados.
- Haverá notas livres gerais da proposta e notas livres vinculadas a cada unidade.
- O histórico automático das alterações estruturais permanecerá separado das notas.

### Passagem entre desenho e regimento

- O desenho terá a ação “Criar regimento deste desenho”.
- O regimento terá a ação “Criar desenho a partir deste regimento”.
- Do desenho para o regimento serão transferidos, em versão futura, denominação, sigla, subordinação e o esqueleto de artigos.
- Do regimento para o desenho serão identificadas criação, extinção, renomeação e mudança de subordinação.
- Unidades novas vindas do regimento exigirão a escolha de CCE/FCE 1.xx.
- Nenhuma alteração será aplicada silenciosamente; haverá conferência antes da incorporação.

## Decisões — rodada 12

### Consulta pública comparativa

- A consulta apresentará dois quadros lado a lado: “Como está hoje” e “Estrutura proposta”.
- Na estrutura atual, unidades excluídas serão destacadas em vermelho e unidades alteradas em amarelo.
- Na estrutura proposta, unidades alteradas serão destacadas em amarelo e unidades criadas em verde.
- Cada quadro mostrará denominação, sigla, subordinação e situação, mantendo a hierarquia visual por recuo.
- Uma legenda explicará as cores.
- Em telas menores, os quadros serão empilhados.

### Backup JSON

- O JSON não fará parte da experiência normal quando o sistema tiver persistência publicada.
- Enquanto o protótipo depender do armazenamento do navegador, ficará recolhido em “Backup do protótipo”.
- Essa área permitirá baixar e restaurar o JSON e será retirada após a implantação da gravação no sistema.

### Visão consolidada das notas

- A aba “Notas e histórico” mostrará todas as notas vinculadas a unidades, agrupadas por unidade.
- Será apresentado o total de notas e de unidades com notas.
- Cada grupo terá uma ação “Abrir unidade”, que levará diretamente ao ponto correspondente da árvore.
- As notas gerais, as notas por unidade e o histórico automático permanecerão separados.

## Decisões — rodada 13

### Expansão e ordem da árvore

- A barra da árvore terá as ações “Abrir tudo” e “Recolher tudo” lado a lado.
- “Abrir tudo” expandirá todos os grandes blocos e todas as unidades; “Recolher tudo” manterá o comportamento de fechar toda a árvore.
- O grupo de Superintendências será sempre o último bloco da árvore.
- Unidades diretamente subordinadas à Secretaria, exceto o Gabinete e as Diretorias, aparecerão depois das Diretorias e imediatamente antes das Superintendências.

## Decisões — rodada 14

### Prévia sem pontos e filtros por mudança

- A prévia de consulta não mostrará saldo, totais nem tabela de pontos.
- A prévia mostrará o total de cargos atual e proposto, além da diferença por código.
- Aumentos de quantidade serão destacados em verde e reduções em vermelho.
- Os cards de unidades alteradas, remanejadas, criadas e excluídas funcionarão como filtros.
- Os mesmos quatro filtros serão usados no quadro comparativo interno e na prévia de consulta.
- Clicar novamente no card ativo retirará o filtro.

