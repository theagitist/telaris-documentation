# Trabalho multigaláxia

Às vezes uma ideia vive em mais de uma galáxia: um tema de pesquisa que abarca duas coleções; uma exposição com várias salas; uma série de edições relacionadas. Telaris é construído para que o buraco de minhoca permaneça na sua galáxia de origem e a *combinação* seja um arranjo de visualização, não um arranjo estrutural. Este capítulo percorre as três formas de compor galáxias, e quando cada uma é a escolha certa.

## Os três caminhos de composição

Telaris oferece três formas de pôr várias galáxias em uma única vista:

1. **Tags de galáxia** (capítulo 4): duas galáxias que compartilham uma tag formam uma *união de galáxias*. As visitantes chegam à união por `/tag/<tag-slug>` e veem os buracos de minhoca de cada galáxia marcada juntos, com cada um mantendo o estilo visual da sua galáxia de origem.
2. **Agrupamento por prefixo entre colchetes**: galáxias cujos nomes começam com o mesmo prefixo `[colchete]` se unem automaticamente em `/[colchete]`. Um fallback natural às tags de galáxia; o prefixo é também o sinal visual para editoras navegando o seletor.
3. **Listas explícitas de galáxias**: passar uma lista separada por vírgulas na URL `?galaxies=slug1,slug2` produz uma união pontual. Útil para compartilhar uma combinação curada sem alterar as galáxias subjacentes.

A escolha entre os três depende de **quão duradoura a combinação é**:

- *Duradoura*: tags de galáxia. A conexão é editorial e persiste entre sessões.
- *Convencional*: prefixo entre colchetes. Útil quando as galáxias são irmãs por convenção de nome, e não apenas por tag.
- *Pontual*: lista explícita. Útil para um e-mail ou link que conduz uma leitora por uma combinação específica uma vez.

## Compartilhar buracos de minhoca sem duplicar

O primeiro instinto em muitos sistemas de arquivo é copiar um buraco de minhoca para uma segunda galáxia quando uma ideia pertence aos dois lugares. Telaris é construído contra esse instinto: copiar cria dois buracos de minhoca a manter, dois lugares a atualizar quando a fonte muda, dois lugares de onde retirar quando a comunidade de origem retira o consentimento.

O caminho pretendido é: deixar o buraco de minhoca na sua única galáxia de origem e deixar **palavras-chave compartilhadas** conectá-lo a outros. Visitantes que seguem *intertidal* na galáxia A alcançam os buracos de minhoca marcados *intertidal* na galáxia B; o conteúdo do buraco de minhoca vive em um lugar; a conexão é computada a partir da palavra-chave.

Quando isso não basta, as opções da editora são, em ordem do mais ao menos invasivo:

1. **Adicionar uma tag de galáxia** às duas galáxias que compartilham o tema. As visitantes que seguem a tag veem a união.
2. **Colocar um portal** (capítulo 9) de uma galáxia à outra. O portal é um buraco de minhoca, mas é pequeno e deliberado; não duplica nenhum conteúdo.
3. **Duplicar o buraco de minhoca** (menu de ações do capítulo 5). Somente quando o conteúdo do buraco de minhoca genuinamente precisa viver em dois lugares (por exemplo, uma galáxia está sendo semeada com material de outra, com a decisão editorial de transplantar em vez de ligar). A duplicata é independente a partir daí; as duas cópias precisam ser mantidas.

Os dois primeiros caminhos são quase sempre preferíveis ao terceiro.

## A experiência de visitante de uma união

Uma visitante que chega a uma união por tag de galáxia (por exemplo, `/tag/coast`) vê:

- Uma cena composta pelos buracos de minhoca de cada galáxia que carrega a tag.
- **Temas de origem por buraco de minhoca**: cada buraco de minhoca renderiza com o tema da sua galáxia de origem, não com um tema unificado. Isso é intencional; a visitante vê a união como o *encontro de galáxias*, não como um achatamento delas.
- Uma faixa ou seletor de galáxias no topo mostrando as galáxias constituintes, com a opção de entrar em uma específica.
- Os mesmos recursos Discovery de qualquer galáxia (keyword chips, related wormholes, etc.), agora bebendo da união.

A URL da visitante permanece em `/tag/<tag>` enquanto ela está na união; clicar em um buraco de minhoca abre seu cartão de informações sem sair da união.

## Quando adicionar uma tag de galáxia

Uma tag é editorial. As duas perguntas a fazer:

- **A relação entre estas galáxias é duradoura?** Uma tag persiste; se a relação é pontual, uma URL explícita é mais limpa.
- **A relação é simétrica?** Uma tag é simétrica (cada galáxia que carrega a tag é igualmente membro). Se a relação é direcional (a galáxia A é a introdução à galáxia B), um portal é mais honesto.

Exemplos que justificam uma tag:
- Uma série de coleções de pesquisa relacionadas.
- Uma exposição com várias salas.
- Um agrupamento regional (galáxias que descrevem conteúdo de uma única paisagem, geografia, ou comunidade).

Exemplos que não:
- "Galáxias antigas que quero reunir para um link único" (use `?galaxies=...`).
- "Galáxias que compartilham algumas palavras-chave" (use as palavras-chave diretamente).

## Quando usar agrupamento por prefixo entre colchetes

Telaris reconhece nomes de galáxia que começam com o mesmo `[colchete]` como uma família. Uma galáxia chamada `[demo] Coastal plants` e outra chamada `[demo] Tide pools` compartilham o prefixo `[demo]`; as visitantes que seguem `/[demo]` veem as duas em união.

O prefixo entre colchetes é mais útil quando:

- Você tem várias editoras trabalhando em galáxias relacionadas, e o prefixo sinaliza a elas que as galáxias são irmãs.
- As galáxias formam uma família que você também quer visível como família no seletor da editora (o seletor agrupa galáxias pelo prefixo).
- Você quer o comportamento de união sem compor explicitamente uma tag em cada galáxia.

O prefixo entre colchetes e uma tag de galáxia explícita não são mutuamente exclusivos; ambos se aplicam se ambos estão presentes.

## Quando usar uma lista explícita de galáxias

Às vezes você quer uma união pontual para um momento específico: um e-mail a uma curadora mostrando uma combinação particular; um link de ensino que conduz uma turma por três galáxias lado a lado; uma exposição temporária que não justifica uma tag duradoura.

A forma da URL é `?galaxies=slug1,slug2,slug3` anexada ao endereço da sua instância. O resultado é idêntico ao de uma união por tag, mas a combinação existe somente como a URL em si.

Essa é a ferramenta certa para curadoria pontual. Também serve como uma checagem rápida: se uma combinação específica de galáxias se lê bem como URL explícita, você tem uma candidata a uma tag permanente.

## Multigaláxia entre instâncias

E quanto a galáxias que vivem em **outras** instâncias de Telaris? Isso é domínio da operadora: conteúdo entre instâncias chega à sua superfície de edição via federação ou via importações por bridge que a operadora configura. Do assento da editora, galáxias federadas e bridged se comportam como galáxias locais (uma galáxia é uma galáxia é uma galáxia), mas a editora não compõe uniões entre instâncias; só a operadora pode configurar a federação que as torna possíveis.

## Coisas que vale a pena saber

- **Um buraco de minhoca pertence a exatamente uma galáxia por vez.** Multigaláxia é um conceito de *visualização*, não estrutural. A galáxia de origem do buraco de minhoca é sua única fonte da verdade.
- **A visitante em uma vista de união não distingue à primeira vista qual galáxia originou um dado buraco de minhoca** além do tema visual do ícone. O cartão de informações mostra a galáxia de origem no rodapé; o tema do ícone é o indicador rápido.
- **Uma galáxia em uma união não perde sua individualidade.** As visitantes podem entrar em uma galáxia específica a partir da vista de união; a união é uma camada de visualização, não uma fusão.
- **Palavras-chave são globais por texto** (capítulo 7). As palavras-chave de um buraco de minhoca na galáxia A são as mesmas palavras-chave que as mesmas palavras em um buraco de minhoca na galáxia B. Uma vista de união consolida a faixa de chips de palavras-chave em todas as galáxias constituintes; clicar em uma palavra-chave na união filtra a união.
- **A tela de palavras-chave continua por galáxia** (capítulo 8). Não existe uma "tela de união"; cada galáxia mantém seu próprio arranjo de palavras-chave. As palavras-chave em si são compartilhadas (renomear ou fundir vale em todo lugar), mas o layout dos chips e as relações desenhadas se restringem a cada galáxia.
