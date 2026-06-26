# Adicionando conteúdo

Este capítulo cobre cada tipo de objeto que você pode colocar numa página, e as ferramentas que cada um oferece depois de estar na tela. Você adiciona a maioria deles pelo **menu NEW** (clique uma vez no fundo vazio). As ferramentas próprias de cada objeto aparecem como pequenos ícones ao redor dele quando você o seleciona.

## Imagens

**Para adicionar uma imagem,** use a ferramenta de envio no menu NEW, ou simplesmente arraste um ficheiro de imagem do seu computador e solte-o em qualquer lugar da página. O Hotglue aceita JPEG, PNG, GIF e WebP. Se você soltar uma imagem muito grande, o Hotglue a reduz automaticamente para um tamanho razoável para a página (os GIFs animados ficam no tamanho original).

Quando uma imagem está selecionada, suas ferramentas permitem que você:

- **Ative ou desative a repetição da imagem**, para que a imagem se repita preenchendo a sua caixa como um padrão.
- **Reponha o tamanho da imagem** de volta às suas dimensões naturais. Mantenha <kbd>shift</kbd> ou <kbd>ctrl</kbd> ao fazer isso para preservar a proporção.
- **Ajuste a seleção da imagem** arrastando, para mostrar apenas parte da imagem.
- **Transfira ficheiro original**.
- **Edite esta imagem no editor de desenho** (veja *Desenhos* abaixo).

## Texto

**Para adicionar texto,** escolha "adicionar um novo objeto de texto" no menu NEW. Uma caixa de texto aparece. Clique numa caixa de texto selecionada para editar suas palavras na hora; pressione <kbd>esc</kbd> para parar de editar.

As ferramentas de uma caixa de texto permitem moldá-la em detalhe:

- **Cor de fundo** da caixa, ou **tornar o fundo transparente**.
- **Tamanho da fonte**: arraste a ferramenta para alterá-lo, clique para redefinir.
- **Cor da fonte**.
- **Tipo de letra**: clique para alternar entre as fontes disponíveis.
- **Estilo da fonte**: alterne entre normal, negrito e itálico.
- **Altura de linha**, **espaçamento entre letras** e **espaçamento entre palavras**.
- **Alinhamento do texto**: à esquerda, centralizado, à direita, depois justificado.
- **Espaçamento interno** dentro da caixa.

As caixas de texto também entendem algumas macros que se preenchem automaticamente, como `$BASEURL$` e `$PAGE$`. Digite-as numa caixa de texto e elas são substituídas quando a página é exibida.

## Vídeo da web

**Para incorporar um vídeo,** escolha "incorporar um vídeo do youtube, vimeo ou peertube" no menu NEW e cole o endereço do vídeo quando solicitado. O Hotglue reconhece links do YouTube, Vimeo e PeerTube (incluindo vídeos do PeerTube em qualquer host federado) e cria o player incorporado correto para cada um.

Quando o objeto de vídeo está selecionado, suas ferramentas permitem que você:

- **Alterne a reprodução automática** do vídeo (a alteração entra em vigor depois que a página publicada é recarregada).
- **Alterne a repetição** do vídeo (também após um recarregamento).

No modo de edição, uma pequena faixa "arraste aqui" fica sobre o player para que você possa mover o objeto sem que o vídeo capture os seus cliques.

## Desenhos

O Hotglue inclui um editor de imagens completo dentro da página (miniPaint) para criar ou retocar uma imagem sem sair da tela. Há dois caminhos:

- No menu NEW, escolha **desenhar uma nova imagem** para começar numa tela em branco.
- Com uma imagem selecionada, escolha **editar esta imagem no editor de desenho** para abrir essa imagem para alterações.

O editor de desenho se abre numa janela com as ferramentas usuais de pintura. Quando você terminar, clique em **colocar na página** para soltar o resultado de volta na sua página Hotglue (isso achata as suas camadas numa única imagem), ou em **cancelar** para descartá-lo. Se você estava editando uma imagem existente, a nova versão toma o seu lugar.

## Som (o soundboard)

O **soundboard** transforma uma página em algo que você pode tocar. É uma configuração por página que você ativa no menu PAGE: "alternar o modo soundboard". Quando está ligado, a página publicada trata os seus blocos de vídeo como gatilhos, e tocar num bloco inicia o seu clipe.

O que faz dele um soundboard, e não apenas vários vídeos, é a mixagem de áudio:

- **Clipes de vídeo hospedados por você próprio** que você enviou tocam através de um único mecanismo de áudio compartilhado, então vários clipes podem soar ao mesmo tempo e se sobrepor. Isso funciona tanto em telefones quanto em desktop.
- **Vídeos incorporados** (YouTube, PeerTube, Vimeo) tocam através dos seus próprios controles de player embutidos. Vários podem tocar em paralelo; isso é confiável no desktop e mais limitado nos telefones.

A alteração entra em vigor depois que a página publicada é recarregada. O modo soundboard fica desligado a menos que você o ligue, então uma página comum com vídeos se comporta normalmente.

## Ferramentas de objeto (qualquer objeto)

Além das ferramentas por tipo acima, todo objeto compartilha um conjunto comum:

- **Clonar objeto**.
- **Alterar a transparência** arrastando.
- **Tornar o objeto numa ligação**: aponte-o para um endereço web, outra página ou uma âncora, com a opção de abrir numa nova aba.
- **Obter o nome deste objeto**, para que você possa criar um link para ele a partir de outro lugar.
- **Fazer este objeto aparecer em todas as páginas** (útil para um logotipo ou um rodapé).
- **Travar** o objeto para que não possa ser movido ou redimensionado por acidente; clique de novo para destravar.
- **Inverter** o objeto.
- **Excluir** o objeto.

> [!note] Sem código personalizado
> A versão Telaris do Hotglue deixa de fora, de propósito, os módulos que permitiriam colar HTML ou scripts arbitrários. Tudo o que você adiciona é um dos tipos de conteúdo acima. Isso é uma escolha de segurança, não um descuido.
