# Buracos de minhoca

Um buraco de minhoca é a menor unidade de conteúdo em Telaris. Tudo o que uma editora publica é, no fim, um buraco de minhoca: uma passagem de texto, uma fotografia, uma gravação de áudio, um trecho de filme, um PDF, uma citação, um pensamento solto. Este capítulo percorre criar um, editar um, os campos que o moldam, e as escolhas que o formulário convida você a fazer.

## Criar um novo buraco de minhoca

Na tela inicial da editora, selecione a galáxia em que está trabalhando e escolha **Novo buraco de minhoca**. Um modal abre:

![Modal Adicionar buraco de minhoca: formulário vazio com Nome, Galáxia destino, Tipo de buraco de minhoca, Palavras-chave, Descrição, URL, e abas de mídia visíveis](assets/images/editor-manual-pt/05-new-wormhole-modal.png)

O formulário tem quatro regiões amplas, na ordem em que aparecem ao rolar o modal para baixo:

1. **Identidade** no topo: Nome, Galáxia destino, Tipo de buraco de minhoca, Palavras-chave.
2. **Interruptores de comportamento**: Acentuar buraco de minhoca, Mostrar palavras-chave.
3. **Corpo**: Descrição, URL.
4. **Mídia**: imagem, vídeo, áudio, PDF, e o ícone personalizado.

Salve com o botão no rodapé do modal; o novo buraco de minhoca aparece na lista imediatamente. Cancele ou clique fora do modal para descartar.

## Campos de identidade

### Nome

Obrigatório. O rótulo que a visitante lê na cena 3D, em qualquer lista, e na URL quando compartilha. Escolha um nome que se leia bem sozinho; vai ser citado fora de contexto mais do que você imagina.

Nomes dentro de uma galáxia precisam ser únicos; o modal avisa se um nome já está em uso antes de salvar. Entre galáxias, dois buracos de minhoca podem compartilhar o nome sem conflito.

### Galáxia destino

Obrigatório, mas em geral pré-preenchido. O menu suspenso mostra cada galáxia que você pode editar. Se você começou a partir de uma galáxia específica na tela inicial da editora, ela vem selecionada por padrão; se você começou em *Todas as minhas galáxias*, escolhe aqui.

Trocar a galáxia neste menu **move** o buraco de minhoca para aquela galáxia. As palavras-chave vão junto, mas as *posições* das palavras-chave na tela da galáxia de destino podem precisar de retoque.

### Tipo de buraco de minhoca

Um menu suspenso com dois valores:

- **Objeto** é o padrão e a escolha certa para quase todo buraco de minhoca. Um Objeto carrega conteúdo (descrição, mídia).
- **Portal** transforma o buraco de minhoca em uma porta para outra galáxia. Selecionar Portal revela um segundo menu suspenso para a galáxia de destino. O capítulo 9 cobre portais.

### Palavras-chave

Um campo de chips. Digite uma palavra-chave e aperte **Enter** (ou vírgula) para adicioná-la; clique no **×** de um chip para removê-lo. Sugestões aparecem conforme você digita, vindas de:

- Palavras-chave já usadas em **esta** galáxia.
- Palavras-chave usadas em galáxias que compartilham o prefixo `[colchete]` da galáxia atual.

Escolha palavras-chave com o caminho da visitante em mente: cada palavra-chave que você anexa é uma porta entre este buraco de minhoca e qualquer outro que carregue a mesma palavra. Quanto menos palavras-chave você atribui, mais deliberada cada conexão; quanto mais, mais densa a teia. O capítulo 7 cobre estratégia de palavras-chave.

## Interruptores de comportamento

### Acentuar buraco de minhoca

Desligado por padrão. Quando ligado, este buraco de minhoca aparece maior e mais proeminente na cena 3D. Use com parcimônia: se você acentua tudo, nada está acentuado. O sinal de acentuação é também o marcador que o recurso de percurso automático pode usar para escolher suas paradas (capítulo 11).

### Mostrar palavras-chave

Desligado por padrão. Quando ligado, a visitante vê as palavras-chave deste buraco de minhoca escritas ao seu lado na cena 3D, antes de abri-lo. Útil para buracos de minhoca cujo papel na galáxia se entende melhor pelas tags (um documento de referência; uma pista de navegação; uma definição).

## Corpo

### Descrição

O texto que a visitante lê quando abre o buraco de minhoca. Não há limite de extensão; uma linha curta ou um ensaio longo, ambos cabem. O campo aceita formatação markdown básica: parágrafos (uma linha em branco), `**negrito**`, `*itálico*`, `[link](https://...)`, listas, e `código` em linha. Cabeçalhos e mídia embutida não são renderizados dentro da descrição; se precisar de uma quebra semelhante a um título, deixe uma linha em branco e comece um novo parágrafo.

Escreva descrições na sua própria voz. Telaris não edita o que você escreve; a plataforma enquadra o conteúdo, o conteúdo é seu.

### URL

Opcional. Se você preenche, o buraco de minhoca vira um link clicável: quando a visitante abre o cartão de informações, um botão *Abrir link* aparece e a leva para a URL em uma nova aba.

Use para referências de origem (um artigo, uma página de livro, um arquivo sonoro, o site de uma comunidade). Deixe em branco quando o buraco de minhoca for autossuficiente.

## Mídia

Um buraco de minhoca pode carregar um **visual primário** mais uma trilha de **áudio** opcional e um **ícone personalizado** opcional. O visual primário é o que as visitantes veem no topo do cartão de informações quando abrem o buraco de minhoca; o áudio toca ao fundo; o ícone personalizado muda como o buraco de minhoca aparece na cena 3D.

O modal organiza o visual primário como um conjunto de abas: **Imagem**, **Vídeo (MP4)**, **PDF**. Escolher uma e salvar limpa as outras; apenas um visual primário por vez. O capítulo 6 cobre cada aba em detalhe.

O campo de áudio é independente do visual primário; um buraco de minhoca com uma imagem e um arquivo de áudio toca o áudio enquanto a imagem está visível. Código de embed (por exemplo, um iframe de Spotify ou Vimeo) é suportado como alternativa a imagem / vídeo / PDF quando o visual está hospedado externamente.

## Editar um buraco de minhoca existente

Para editar um buraco de minhoca, clique em qualquer ponto da sua linha na lista, ou abra o menu de ações da linha e escolha **Editar**:

![Modal Editar buraco de minhoca para Beach Strawberry: nome preenchido, chips de palavras-chave, descrição, abas de mídia](assets/images/editor-manual-pt/06-edit-wormhole-modal.png)

O modal é o mesmo do formulário de criação, com os valores existentes preenchidos. O id do buraco de minhoca aparece no canto superior direito (aqui, `#279`); editoras raramente precisam consultar ids, mas o número é útil ao reportar um problema à sua operadora.

Salvar persiste a alteração imediatamente. As visitantes que estão vendo a galáxia recebem a sua atualização no próximo carregamento da página.

## Duplicar, visualizar, apagar

O menu de ações em cada linha de buraco de minhoca oferece estas operações:

- **Ver** abre uma prévia somente leitura do cartão de informações como a visitante o veria. Use sempre que quiser checar uma mudança antes de tratar o trabalho como pronto.
- **Editar** abre o modal acima.
- **Duplicar** cria uma cópia do buraco de minhoca, com o mesmo conteúdo, na mesma galáxia, chamada "Original Name (Copy)". O novo buraco de minhoca recebe uma posição fresca na cena 3D; o resto vem junto. Útil quando você quer um quase-duplicado como ponto de partida.
- **Criar modelo** salva a forma do buraco de minhoca como um modelo reutilizável a partir do qual você pode estampar novos buracos de minhoca depois. A seção Modelos, abaixo, cobre isso por inteiro.
- **Excluir** remove o buraco de minhoca. Um modal de confirmação aparece primeiro; deleções são permanentes (a sua operadora às vezes consegue restaurar de um snapshot, mas a resposta deve ser: não apague a menos que esteja decidida).

Duplicar e Criar modelo respondem a duas necessidades diferentes: Duplicar te dá mais um buraco de minhoca agora mesmo, nesta galáxia; Criar modelo te dá um molde que você pode reutilizar entre galáxias e entre sessões.

## Ordenar a lista de buracos de minhoca

Clique em qualquer cabeçalho de coluna na lista de buracos de minhoca para ordenar por aquela coluna; clique de novo para inverter a ordem. Ordene por nome para achar um buraco de minhoca em ordem alfabética, ou pela coluna de última modificação para trazer o trabalho mais recente ao topo. A ordenação é apenas uma conveniência de visualização; não muda nada nos buracos de minhoca em si nem como eles aparecem para as visitantes.

## Modelos

Um modelo é um ponto de partida reutilizável para novos buracos de minhoca. Se você se pega criando um buraco de minhoca atrás do outro com a mesma forma (o mesmo tipo, o mesmo punhado de palavras-chave, o mesmo tom de descrição, o mesmo tipo de mídia embutida), pode capturar essa forma uma vez e estampar novos buracos de minhoca a partir dela, em vez de preencher os mesmos campos à mão toda vez.

Os modelos são **privados de você**. Os modelos que você cria são só seus; outra pessoa editora na mesma instância não os vê, e você não vê os dela. (Quem administra pode ver todos os modelos, do mesmo jeito que pode ver todas as galáxias.)

### Criar um modelo a partir de um buraco de minhoca

Você não constrói um modelo a partir de um formulário em branco. Você o constrói a partir de um buraco de minhoca de que já gosta. Abra o menu de ações da linha do buraco de minhoca e escolha **Criar modelo**:

![Um menu de ações de linha de buraco de minhoca aberto, mostrando Ver, Editar, Duplicar, Criar modelo e Excluir](assets/images/editor-manual-pt/15-create-template-action.png)

Telaris captura uma cópia da estrutura e do conteúdo daquele buraco de minhoca: o tipo, as palavras-chave, a descrição, a URL, os interruptores de comportamento e as configurações de mídia. Se o buraco de minhoca carrega conteúdo Hotglue, o modelo copia também esse conteúdo, de modo que um buraco de minhoca criado a partir do modelo abre sobre a sua própria cópia privada da mesma página em formato livre. O buraco de minhoca original fica intacto; o modelo é uma coisa separada e autônoma a partir do momento em que é feito. Editar ou apagar o buraco de minhoca depois não altera o modelo, e vice-versa.

O novo modelo assume o nome do buraco de minhoca. Você pode renomeá-lo depois pela aba Modelos.

### Basear um novo buraco de minhoca em um modelo

Ao lado de **Novo buraco de minhoca** na tela inicial da editora há um pequeno menu suspenso. Seu padrão é **Sem modelo**, que te dá o formulário em branco de sempre. Escolha um modelo no menu suspenso, e o próximo buraco de minhoca que você criar abre com os campos daquele modelo já preenchidos:

![A barra de ferramentas da tela inicial da editora: o botão Novo buraco de minhoca ao lado de um menu suspenso com Sem modelo, acompanhado de uma lista de modelos salvos](assets/images/editor-manual-pt/16-template-selector.png)

O modal que se abre é o modal Novo buraco de minhoca de sempre, pré-preenchido. Tudo continua editável: mude o nome (você quase sempre vai querer, já que o nome do modelo é só um espaço reservado), ajuste as palavras-chave, reescreva a descrição. Nada fica travado. O modelo só decide onde o formulário começa, não onde ele termina. Se o modelo incluía conteúdo Hotglue, o novo buraco de minhoca recebe a sua própria cópia privada desse conteúdo, que você depois edita de forma independente.

Escolher um modelo é uma escolha por criação. O menu suspenso não fica "armado"; depois que você cria um buraco de minhoca a partir de um modelo, ele volta para **Sem modelo**, de modo que o próximo buraco de minhoca fica em branco a menos que você escolha um modelo de novo.

### Gerenciar seus modelos

A tela inicial da editora tem três abas no alto: **Buracos de minhoca**, **Modelos** e **Conteúdo hotglue**. A aba Modelos lista todos os modelos que você possui:

![A aba Modelos: uma tabela de modelos com colunas Nome e Hotglue, uma caixa de busca, e ações Renomear e Excluir por linha](assets/images/editor-manual-pt/17-templates-tab.png)

A lista tem duas colunas: o **Nome** do modelo e uma coluna **Hotglue** que marca os modelos que carregam conteúdo Hotglue. Uma caixa de busca filtra a lista por nome. Clique em um cabeçalho de coluna para ordenar.

As ações de cada modelo são:

- **Renomear** muda o nome do modelo. Isso é puramente um rótulo para seu próprio uso; não toca em nenhum buraco de minhoca já criado a partir do modelo.
- **Excluir** remove o modelo. Os buracos de minhoca que você já criou a partir dele não são afetados; agora são buracos de minhoca comuns, sem nenhum vínculo vivo de volta ao modelo. Excluir um modelo não pode ser desfeito.

Nesta primeira versão, renomear e excluir são as únicas edições. Para mudar o que um modelo contém, crie um modelo novo a partir de um buraco de minhoca que tenha a forma que você quer, e apague o antigo.

## Coisas que vale a pena saber

- **Salve antes de trocar de galáxia no menu suspenso** se estiver no meio de uma edição; trocar pode fechar o modal sem salvar.
- **A posição na cena 3D é automática.** Cada buraco de minhoca recebe uma posição atribuída pelo sistema no momento da criação. Você não precisa escolher onde o buraco de minhoca fica no espaço; o layout é gerado. Para sortear uma nova posição para um buraco de minhoca, duplique-o e apague o original (o duplicado recebe uma nova posição).
- **Palavras-chave casam sem diferenciar maiúsculas.** "Native" e "native" são a mesma palavra-chave; o chip usa a forma em que a palavra apareceu pela primeira vez na galáxia.
- **Um buraco de minhoca sem descrição é permitido, mas silencioso.** As visitantes que o abrem só veem o nome. Use esse padrão quando o papel do buraco de minhoca é puramente visual (um cartão-postal só de imagem) ou quando funciona como pista de navegação.
- **Os chips de palavras-chave de um buraco de minhoca são coloridos de forma determinística** pelo texto da palavra. A mesma palavra-chave recebe sempre o mesmo pastel em toda galáxia da sua instância; é intencional, para que visitantes reconheçam *native* pela cor tanto quanto pela grafia.
- **Buracos de minhoca importados são somente leitura.** Se sua instância importa conteúdo de uma fonte externa (um arquivo irmão, uma comunidade upstream), esses buracos de minhoca aparecem na sua lista de edição mas não podem ser editados; o modal de edição abre em estado de visualização. A mudança tem que acontecer na fonte.
