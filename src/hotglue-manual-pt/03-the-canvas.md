# A tela

Este capítulo é o coração do manual: como a superfície de edição funciona depois que você a abre.

## Modo de edição

Uma página Hotglue tem dois estados: a visão publicada que quem visita vê, e o **modo de edição**, onde você pode alterar as coisas. Você entra no modo de edição pelos botões descritos em *Entrando*. No modo de edição a página ganha os seus menus e cada objeto passa a ser arrastável.

![Uma página Hotglue aberta na tela de edição: uma faixa de título, um subtítulo e duas colunas de texto, cada uma um objeto separado que você pode mover](assets/images/hotglue-manual-pt/03-canvas.png)

## Os dois menus

Quase tudo o que você faz começa em um de dois menus, e qual deles aparece depende de como você clica no fundo vazio da página:

- **Clique uma vez no fundo** para abrir o **menu NEW**: as ferramentas para adicionar coisas à página (enviar um ficheiro, adicionar texto, incorporar um vídeo, desenhar uma imagem). O atalho de teclado é <kbd>alt</kbd> + <kbd>o</kbd>.

  ![O menu NEW aberto na tela: pequenos ícones para adicionar um desenho, texto, um ficheiro enviado, uma imagem e um vídeo](assets/images/hotglue-manual-pt/04-new-menu.png)

- **Clique duas vezes no fundo** para abrir o **menu PAGE**: as ferramentas que afetam a página inteira (cor e imagem de fundo, a grade). O atalho de teclado é <kbd>alt</kbd> + <kbd>p</kbd>.

  ![O menu PAGE aberto na tela: uma grade de ferramentas de página inteira, incluindo título, URL da página, página inicial, cor e imagem de fundo, e a grade](assets/images/hotglue-manual-pt/05-page-menu.png)

Quando você **seleciona um objeto** (clicando nele), aparece um terceiro conjunto de ferramentas: o **menu de contexto** do próprio objeto, um leque de pequenos ícones ao redor dele. Os ícones diferem por tipo de objeto (uma imagem tem ferramentas diferentes das de uma caixa de texto), e são cobertos por tipo em *Adicionando conteúdo*.

## Posicionando, selecionando e movendo

**Adicionar um objeto** o coloca onde você clicou (no caso dos itens de menu) ou onde você o soltou (no caso do arrastar e soltar). Depois você pode movê-lo para qualquer lugar.

**Selecionando:**

- Clique num objeto para selecioná-lo.
- Mantenha <kbd>shift</kbd> e clique para adicionar mais objetos à seleção (ou remover um).
- Clique no fundo vazio para desmarcar tudo.
- <kbd>ctrl</kbd> + <kbd>A</kbd> seleciona todos os objetos, <kbd>ctrl</kbd> + <kbd>D</kbd> não seleciona nenhum, <kbd>ctrl</kbd> + <kbd>I</kbd> inverte a seleção, e <kbd>tab</kbd> percorre os objetos um a um.

**Movendo:**

- Arraste um objeto selecionado com o mouse.
- Mantenha <kbd>shift</kbd> enquanto arrasta para travar o movimento em um eixo (puramente horizontal ou puramente vertical).
- Mantenha <kbd>ctrl</kbd> enquanto arrasta para ignorar a grade de encaixe e posicionar o objeto livremente.
- As teclas de seta deslocam uma seleção um pixel por vez; <kbd>shift</kbd> + uma tecla de seta a move por um passo da grade.

**Redimensionando:** arraste a alça de redimensionamento no canto de um objeto selecionado. Uma pequena leitura mostra a largura, a altura e a posição ao vivo enquanto você arrasta. Mantenha <kbd>ctrl</kbd> para redimensionar livre da grade.

**Excluindo:** pressione <kbd>delete</kbd> com um objeto selecionado, ou use o próprio ícone de exclusão do objeto.

## Camadas e ordem de empilhamento

Quando objetos se sobrepõem, você controla qual fica na frente:

- Arraste o ícone de primeiro plano/fundo do objeto para a esquerda ou para a direita para movê-lo um passo para frente ou para trás de cada vez.
- <kbd>shift</kbd> + <kbd>page up</kbd> traz a seleção para a frente de tudo; <kbd>shift</kbd> + <kbd>page down</kbd> a envia para o fundo de tudo.

## A grade e o encaixe

Por padrão, os objetos se encaixam numa grade invisível enquanto você os move e redimensiona, o que mantém o layout arrumado. No menu PAGE você pode mostrar ou ocultar a grade, e pode alterar o seu espaçamento arrastando a ferramenta de grade (a leitura mostra o tamanho como NxN). Para posicionar um único objeto fora da grade sem alterar a grade em si, mantenha <kbd>ctrl</kbd> enquanto o arrasta ou redimensiona.

## O fundo

No menu PAGE você pode:

- **Alterar a cor de fundo** com uma roda de cores (ou clicar na roda com shift pressionado para digitar um valor exato).
- **Enviar uma imagem de fundo** para a página.
- Alternar se a imagem de fundo fica **fixa** enquanto a página rola, ou se rola junto com ela.
- Ajustar qual parte da imagem de fundo aparece, arrastando.

## Salvamento e histórico

**Não existe botão Salvar.** Cada ação que você faz (mover, redimensionar, editar texto, alterar uma cor) é salva no instante em que você a conclui.

Por causa disso, também não há um **desfazer** tradicional. Em vez disso, o Hotglue mantém um histórico da página chamado *revisões*. Abra-o com o botão **Revisões** no editor (ou pressione <kbd>ctrl</kbd> + <kbd>z</kbd>, que se oferece para levar você até lá). Na visão de revisões você pode revisar versões anteriores da página. O Hotglue tira uma captura automática de uma página cerca de uma vez por hora enquanto ela está sendo editada, e guarda essas capturas por sete dias.

> [!tip] Trabalhe em movimentos pequenos e deliberados
> Como não há desfazer e as alterações são imediatas, vale a pena fazer as alterações uma de cada vez e dar uma olhada no resultado. Se algo der errado, o histórico de revisões é a sua rede de segurança, não uma tecla de desfazer.
