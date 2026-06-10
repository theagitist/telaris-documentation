# Adicionar mídia

O corpo de um buraco de minhoca é a descrição; sua **mídia** é tudo o que é visual ou sonoro e que a visitante encontra junto do corpo: uma imagem, um trecho de filme, uma gravação sonora, um documento PDF, um player embutido de outro site. Este capítulo percorre cada tipo, na ordem em que o modal os apresenta.

Um buraco de minhoca carrega no máximo **um visual primário** por vez. Image, Video, e PDF são três abas no modal que compartilham um único slot subjacente; escolher uma e salvar limpa as outras. O quarto tipo de mídia, **áudio**, é independente do visual primário: um buraco de minhoca com uma imagem *e* uma trilha de áudio toca o áudio enquanto a imagem permanece na tela.

A própria seção de mídia tem duas abas de nível superior: **Clássico** e **Hotglue**. Tudo o que foi descrito acima (imagem, video, PDF, áudio, código de incorporação) fica sob **Clássico**, a opção padrão. **Hotglue** é outra maneira de construir a mídia de um buraco de minhoca: em vez de uma única imagem ou um único video, você compõe uma página livre, posicionando texto e imagens onde quiser sobre uma tela aberta. As duas são alternativas; a aba que estiver aberta ao salvar é o que as visitantes veem. Hotglue é tratada no fim deste capítulo.

## A aba Image

A aba padrão, e a escolha de mídia mais comum. Use para fotografias, ilustrações, escaneamentos, diagramas, qualquer coisa parada.

![Aba Image no modal New Wormhole: campo de URL e seletor de arquivo, além do interruptor Use-as-wormhole-icon](assets/images/editor-manual-pt/05-new-wormhole-modal.png)

Duas formas de anexar uma imagem:

- **Image URL**: cole o endereço de uma imagem hospedada em outro lugar na web. Use quando a casa da imagem é algo estável (um arquivo de museu, o site de uma comunidade, um CDN sob seu controle). A URL precisa apontar para a imagem em si, não para uma página que contém a imagem.
- **Seletor de arquivo**: escolha **Choose File** e envie uma imagem do seu computador. Telaris mantém o arquivo enviado na sua instância e o serve de volta para as visitantes.

De qualquer forma, a imagem vira o visual primário da visitante quando ela abre o buraco de minhoca.

**Use as wormhole icon** é um interruptor abaixo dos campos de imagem. Quando ligado, a imagem substitui o ícone padrão do nó 3D do tema: as visitantes veem a imagem *como* o buraco de minhoca na cena 3D, e não só dentro do cartão de informações. Útil quando a imagem é a identidade do buraco de minhoca (um retrato, uma capa, um logotipo). Quando desligado, a cena 3D mostra o ícone padrão do tema e a imagem só aparece dentro do cartão aberto.

**Image attribution** é um pequeno campo de texto livre que viaja com a imagem. Use para crédito da fotógrafa, arquivo de origem, nota de licença, qualquer coisa que seria anexada à imagem se ela aparecesse em um livro impresso. As visitantes veem ao lado da imagem no cartão de informações.

## A aba Video

Use para trechos de filme, entrevistas gravadas, animações, qualquer coisa em movimento. Telaris suporta apenas MP4 neste momento; outros formatos (WebM, MOV, AVI) precisam ser transcodificados antes ou hospedados em um serviço de vídeo e embutidos (veja Embed code abaixo).

![Aba Video no modal New Wormhole: URL de vídeo / seletor de arquivo para um MP4](assets/images/editor-manual-pt/07-media-video-tab.png)

Os mesmos dois caminhos da imagem: cole uma URL para um MP4 hospedado em outro lugar, ou envie um arquivo. Uma vez salvo o buraco de minhoca, o cartão de informações da visitante mostra um player de vídeo com controles padrão (play, pause, busca, volume, tela cheia).

**O tamanho importa.** Arquivos de vídeo costumam ser muito maiores que imagens; o limite de upload de uma instância pode te parar bem antes de esgotar sua paciência. Se o upload falha, pergunte à sua operadora sobre o limite, ou hospede o vídeo externamente e use o campo de URL.

Se seu vídeo vive em um serviço de streaming (Vimeo, YouTube, archive.org), o campo Embed code abaixo é a ferramenta certa, não a aba Video.

## A aba PDF

Para documentos: artigos, guias de campo, fotocópias, relatórios, partituras, manuscritos.

![Aba PDF no modal New Wormhole: URL de PDF / seletor de arquivo](assets/images/editor-manual-pt/08-media-pdf-tab.png)

Mesmos dois caminhos. Uma vez salvo, o cartão de informações da visitante embute um leitor de PDF na própria página: ela pode rolar o documento, buscar, copiar texto, e baixá-lo (as funções padrão do visualizador de PDF).

Uploads de PDF têm um limite de tamanho definido pela sua operadora (comumente 25 MB). Se o arquivo for maior, divida, hospede externamente e ligue pelo campo de URL, ou peça à sua operadora para elevar o limite.

## Áudio

O campo Audio aparece abaixo das abas de visual primário. É independente da escolha de imagem / vídeo / PDF; um buraco de minhoca pode ter qualquer combinação de áudio e um visual primário.

- **Audio URL / File**: cole uma URL para um arquivo de áudio ou faça upload de um. MP3 é a escolha mais segura; muitos navegadores também suportam OGG e WAV.

Quando o áudio está anexado, dois interruptores controlam a reprodução:

- **Autoplay**: quando ligado, o áudio começa assim que a visitante abre o cartão de informações. Quando desligado, a visitante vê um botão de play e inicia o áudio. O autoplay costuma ser certo para trilhas curtas, ambientes, ou atmosféricas; desligado é certo para fala, música, qualquer coisa que pede atenção.
- **Loop**: quando ligado, o áudio reinicia do começo cada vez que termina. Use para loops ambientais, drones, paisagens sonoras; desligue para qualquer áudio com arco narrativo.

O áudio toca em segundo plano no cartão de informações; a visitante pode pausar ou navegar a qualquer momento usando os controles padrão de áudio.

## Embed code

O quarto caminho de mídia, para conteúdo hospedado em outro serviço que já fornece um trecho de embed: um iframe do Vimeo, um player do Spotify, uma faixa do SoundCloud, um visualizador do archive.org, uma cena 3D do SketchFab.

Encontre o campo **Embed code** (abaixo das abas de visual primário) e cole o trecho exatamente como o serviço o entrega. Telaris não transforma nem higieniza código de embed; o que você cola é o que as visitantes recebem. Teste o buraco de minhoca depois abrindo-o em modo visitante; se o embed estiver quebrado, o campo é o lugar para arrumar.

Embed code e o visual primário não são mutuamente exclusivos (o embed aparece separadamente no cartão de informações), mas para clareza costuma fazer sentido escolher um ou outro.

## O ícone personalizado

Abaixo dos campos de mídia, aparece um campo **Icon URL / File**. Ele define a aparência do buraco de minhoca na cena 3D, *separadamente* do visual primário. Use quando:

- Você quer um ícone 3D personalizado (um pequeno gráfico que representa o buraco de minhoca na escala da cena), distinto da imagem maior que as visitantes veem dentro do cartão.
- O interruptor Use-as-wormhole-icon na aba Image não basta porque você tem uma imagem *e* quer que o ícone da cena seja outra coisa.

A maioria das editoras não precisa disso; os ícones padrão do tema cobrem a maior parte dos casos. Quando precisar, forneça uma pequena imagem quadrada (PNG ou SVG) e Telaris usa na cena 3D.

## Armazenamento e o que viaja com um buraco de minhoca

A mídia enviada por upload é armazenada na sua instância. Os uploads de cada buraco de minhoca vivem sob uma pasta identificada pelo id do buraco; restaurar um snapshot traz os uploads junto, apagar um buraco de minhoca remove seus uploads.

A mídia ligada por URL permanece no host original; se o host remove o arquivo, a mídia do buraco de minhoca fica escura. Editoras com referências externas valiosas devem considerar enviar o arquivo por upload em vez de só ligar, para que o arquivo sobreviva ao host original.

## Compor uma página com Hotglue

Às vezes uma única imagem ou um único video não bastam. Você quer uma pequena composição: um título, um parágrafo, duas fotografias lado a lado, uma legenda embaixo, um link para fora. **Hotglue** é o modo de mídia para isso. Em vez de preencher um espaço fixo, você compõe uma página livre onde cada elemento pode ser posicionado, dimensionado e organizado à mão, e essa página se torna a mídia do buraco de minhoca.

No modal de editar buraco de minhoca, abra a seção **Mídia** e escolha a aba **Hotglue**, depois escolha **Editar conteúdo hotglue**. Abre-se um editor quase em tela cheia sobre a página. É uma tela aberta: não há linhas nem colunas às quais se ajustar. Você adiciona um bloco de texto ou uma imagem e depois o arrasta para onde quiser, redimensiona e sobrepõe um elemento ao outro.

![O modal de editar buraco de minhoca com a aba de mídia Hotglue ativa: uma breve linha de ajuda e o botão Editar conteúdo hotglue](assets/images/editor-manual-pt/14-media-hotglue-tab.png)

Os movimentos básicos:

- **Adicionar texto.** Dê um duplo clique em uma área vazia da tela para criar um bloco de texto e digite. Clique fora dele para terminar. Arraste o bloco para reposicioná-lo; arraste a borda para redimensioná-lo.
- **Adicionar uma imagem.** Arraste um arquivo de imagem do seu computador para a tela, ou use a barra de ferramentas para escolher uma. A imagem é guardada com a página. Arraste-a e redimensione-a como qualquer outro elemento.
- **Organizar com liberdade.** Os elementos podem ficar em qualquer lugar e se sobrepor. Não há grade; a disposição que você construir é a que as visitantes veem.
- **A página é salva enquanto você trabalha.** Não há um botão de salvar à parte dentro da tela; suas mudanças são mantidas conforme você as faz. Quando terminar, feche o editor.

De volta ao modal do buraco de minhoca, deixe a aba **Hotglue** selecionada e salve o buraco de minhoca. A partir daí, abrir esse buraco de minhoca mostra sua página composta no lugar da imagem ou do video clássicos. As visitantes veem a página exatamente como você a organizou; elas não podem editá-la.

Algumas coisas a ter em mente:

- **Você só edita páginas em galáxias nas quais tem um assento.** A edição com Hotglue segue a mesma regra de acesso do resto do buraco de minhoca: você pode compor páginas nas suas próprias galáxias, e não em galáxias às quais não recebeu acesso.
- **Uma página de Hotglue é uma única superfície composta.** Diferente do resto do Telaris, ela não se traduz sozinha conforme o idioma de quem visita; o texto que você coloca é o texto que todo mundo vê. Se o seu público é multilíngue, escreva a página tendo isso em conta.
- **A disposição livre é o modo de mídia mais expressivo e o menos tolerante.** O posicionamento absoluto aparece exatamente como você o fixou, o que também significa que ele não se reajusta para telas pequenas nem para tecnologia assistiva como o texto comum se reajusta. Use-a onde a composição importa; apoie-se nas abas clássicas Image ou PDF para documentos simples.
- **Clássico e Hotglue são alternativas, não uma pilha.** Um buraco de minhoca mostra um ou outro, conforme qual aba estiver aberta ao salvar. Voltar para Clássico não apaga a página de Hotglue; apenas deixa de mostrá-la, então você pode voltar a ela mais tarde reselecionando a aba Hotglue.

## Coisas que vale a pena saber

- **Trocar de aba de visual primário limpa o campo em que você estava.** Um aviso de segurança antes de salvar te alerta. Se mudar de ideia, volte para a aba anterior antes de salvar.
- **Áudio em loop pode soar abrupto na primeira visita.** Se você publica um loop, escute a fronteira (o instante em que o loop reinicia); a costura é o que as visitantes vão notar.
- **Uma imagem em alta resolução é mais útil do que em baixa.** Telaris reduz a escala das imagens para a cena 3D automaticamente; enviar em qualidade plena dá um cartão de informações mais nítido, e evita reuploads diante de mudanças de formato no futuro.
- **O texto de um PDF é pesquisável no leitor embutido**, mas só se o PDF tiver uma camada de texto. Documentos escaneados sem OCR são imagens chapadas dentro de uma embalagem de PDF; a caixa de busca não acha nada.
- **Arquivos de vídeo não chegam em pedaços por streaming**: quando uma visitante abre o buraco de minhoca, o arquivo inteiro baixa. Mantenha vídeos curtos e bem comprimidos.
- **Embeds externos podem quebrar com o tempo.** Serviços mudam seu formato de embed, descontinuam players, ou removem conteúdo. Um buraco de minhoca que depende de um embed tem meia-vida mais curta do que um cuja mídia vive na sua instância.
