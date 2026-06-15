# A tela de palavras-chave

A tela de palavras-chave é onde você compõe o mapa conceitual de uma galáxia. Os buracos de minhoca te dão objetos; as palavras-chave te dão formas de marcar esses objetos; a tela é onde você desenha, à mão, as relações **entre as próprias palavras-chave**. Dois chips se inclinam mais perto porque a editora decidiu que se pertencem. Dois chips têm uma linha desenhada entre eles porque a editora decidiu dizer *estas duas ideias estão ligadas, e eis por quê*.

Este capítulo percorre a superfície, suas affordances de desenho, e a disciplina editorial de usá-la bem.

## Abrir a tela

Selecione a galáxia em que quer trabalhar a partir da tela inicial da editora. Quando uma galáxia específica está selecionada, três botões aparecem ao lado do seletor de galáxia; o terceiro é **Tela**. Selecione-o. A tela abre em uma nova aba.

> [!warning] Apenas desktop
> A tela é uma superfície apenas para desktop. Em um celular ou tablet, as interações de chip e linha não se comportam bem; o botão Tela fica escondido nesses contextos. Se você precisa trabalhar o arranjo de palavras-chave de uma galáxia a partir de uma tela pequena, a lista de buracos de minhoca e o campo de palavras-chave dentro do modal de cada buraco de minhoca ainda funcionam; a tela não.

## O que você vê

A tela abre em uma cena escura, ocupando toda a janela, com as palavras-chave da galáxia dispostas como chips pastéis sobre uma grade de pontos:

![Tela de palavras-chave: chips pastéis com linhas de relação desenhadas entre eles, sobre um fundo escuro de grade pontilhada](assets/images/editor-manual-pt/10-keyword-canvas.png)

Cada chip é uma palavra-chave. A cor do chip coincide com a cor usada em outros lugares do aplicativo: *native* aqui é o mesmo esverdeado que aparece em uma linha de buraco de minhoca. Os chips derivam ligeiramente quando a tela está ociosa (uma simulação física suave mantém o conjunto vivo); arrastar um chip o fixa no lugar a partir de então.

As linhas entre chips são **relações** que a editora desenhou. Cada linha tem dois pontos finais (os chips que conecta), uma anotação opcional (uma frase explicando a conexão), e um registro de quem a desenhou e quando.

A barra superior carrega:
- **Voltar**: te devolve à tela inicial da editora para esta galáxia.
- O nome da galáxia.
- **?**: abre um pequeno painel de ajuda listando cada interação de teclado e mouse da tela.
- **Pronto** (ou **Salvando…**): um pequeno indicador de status confirmando que a tela salvou sua mudança mais recente.

## Desenhar uma relação

Duas formas de desenhar uma linha entre dois chips:

1. **Clique-clique**: clique no ponto-âncora de um chip (um pequeno círculo que aparece no chip ao passar o mouse), depois clique no ponto-âncora de outro chip. Uma linha se encaixa.
2. **Arrasto**: pressione no ponto-âncora de um chip e arraste até o outro; solte. Mesmo resultado.

Quando a linha aparece, um campo inline curto te deixa digitar uma anotação opcional. Enter salva a anotação; Escape deixa a linha sem anotação. A anotação fica visível quando uma visitante (ou outra editora) passa o mouse sobre a linha depois.

A linha **se prende às bordas dos chips** conforme você movimenta os chips. Arraste o chip *native* atravessando a tela; a linha até *salt-tolerant* segue. Não há roteamento manual da linha; a geometria se resolve sozinha.

## Mover e arranjar chips

- **Arraste** um chip para reposicioná-lo. A nova posição é salva automaticamente.
- A tela lembra a posição **por editora**: cada editora tem sua própria vista da tela. Duas editoras trabalhando na mesma galáxia não brigam por posições de chip; cada uma vê seu próprio arranjo, e a vista da visitante usa o layout mais recente ou um mesclado (consulte sua operadora sobre a configuração da sua instância).
- Chips que você não moveu flutuam em uma deriva suave, lentamente se acomodando em um layout influenciado pelas linhas de relação (chips ligados por uma linha são puxados, gentilmente, um na direção do outro). A deriva para assim que você arrasta um chip; a partir desse momento, o chip está fixo.

Este é o pequeno segredo da tela: o layout que você vê é em parte trabalho da simulação e em parte das escolhas editoriais que você fez. Duas galáxias cujas editoras não desenharam nenhuma relação parecem poeira na grade de pontos; duas galáxias cujas editoras desenharam muitas parecem constelações.

## Editar ou apagar uma relação

Passe o mouse sobre uma linha; um pequeno menu de contexto aparece com duas opções:

- **Editar nota**: muda a anotação anexada à linha.
- **Excluir**: remove a relação inteira.

As deleções são permanentes no nível da linha (não há desfazer dentro da tela), mas os pontos finais (os chips) permanecem na tela. Você pode redesenhar uma relação entre os mesmos dois chips depois; a nova linha é um registro fresco no histórico subjacente, não uma restauração da anterior.

## Renomear e fundir palavras-chave

Clique com o botão direito (ou pressione longamente em touch) em um chip para abrir suas opções:

- **Renomear**: muda a palavra. O renome se aplica a cada buraco de minhoca que carrega a palavra-chave em toda galáxia da instância, porque as palavras-chave são globais por texto. A cor do chip muda para casar com o novo texto (as cores são determinísticas pela palavra).
- **Fundir em…**: selecione outro chip da tela em que esta palavra-chave deve se fundir. Após a fusão, cada buraco de minhoca que carregava a palavra-chave de origem agora carrega a palavra-chave de destino. O chip de origem desaparece.
- **Excluir**: remove a palavra-chave de cada buraco de minhoca que a carregava na instância.

São ferramentas afiadas. Fundir é a mais gentil das três (sem perda de dados; apenas rerotulagem), depois renomear (também sem perda de dados; a palavra muda mas as conexões ficam), depois apagar (a palavra-chave desaparece; os buracos de minhoca sobrevivem sem ela). Opere em um dia tranquilo se a galáxia tem muitas editoras.

## Reset em lote

A tela expõe duas operações de reset em lote pelo painel de ajuda **?**:

- **Redefinir todas as posições dos chips** nesta galáxia: cada chip volta a uma posição uniforme padrão. Use quando o layout acumulou bagunça e você quer começar de novo.
- **Redefinir todas as relações** nesta galáxia: apaga toda linha de relação desta galáxia. Os chips permanecem. Use quando quiser redesenhar o mapa conceitual do zero.

Ambos se limitam à **galáxia atual**; não tocam em outras galáxias.

## Quando usar a tela (e quando não)

A tela é mais útil quando:

- As palavras-chave de uma galáxia carregam uma estrutura que vale mostrar (algumas são irmãs, algumas são opostas, algumas estão restritas a uma sub-região do conteúdo).
- Um ponto editorial vive **entre** palavras-chave, e não dentro de uma só. *Native* sozinha é só um rótulo; *native* desenhada próxima a *salt-tolerant* com uma anotação ("most natives here tolerate salt") é uma observação.
- Você quer uma superfície de trabalho para pensar. A tela é um caderno de rascunho para o vocabulário da galáxia, além de um artefato público.

A tela é **menos útil** para:

- Galáxias pequenas (menos de dez buracos de minhoca; a contagem de chips costuma ser baixa demais para um layout interessante).
- Galáxias cujas palavras-chave são em sua maioria nomes próprios ou exclusivas a um único buraco de minhoca; a tela é para relações *entre* conceitos, e conceitos isolados não têm com o que se relacionar.

Se uma galáxia nunca parece pedir que se abra a tela, isso é um desfecho bom. A tela é oferecida, não exigida.

## Coisas que vale a pena saber

- **A tela salva cada mudança automaticamente.** Não há botão Salvar. O indicador **Salvando…** / **Pronto** no alto à direita reflete o estado da persistência.
- **Não há desfazer na superfície da tela.** Um movimento errado se corrige com outro movimento; uma deleção acidental, redesenhando a linha. Se algo der muito errado, pergunte à sua operadora sobre um snapshot.
- **A visitante não vê os chips diretamente.** A tela é uma superfície da editora; o que as visitantes veem na cena 3D é influenciado pelo arranjo das palavras-chave (quais buracos de minhoca compartilham palavras; quais chips têm relações), mas elas não olham para a grade de chips em si.
- **As anotações das linhas aparecem para a visitante apenas ao passar o mouse** no painel de buracos de minhoca relacionados (o capítulo 10 traz o detalhe do lado da visitante). A anotação é parte do artefato público; escreva-a para uma leitora futura, não para você mesma.
