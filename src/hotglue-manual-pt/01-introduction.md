# Introdução

Este manual é para qualquer pessoa que componha uma **página Hotglue**: um layout visual de formato livre onde texto, imagens, vídeo e som ficam exatamente onde você os coloca, sem nenhuma grade ou modelo dizendo para onde devem ir. Se uma caixa de texto comum parece rígida demais para o visual que você quer dar a um conteúdo, o Hotglue é a superfície que, em vez disso, oferece uma tela em branco.

## O que é o Hotglue

O Hotglue é um editor visual de páginas. Você arrasta objetos para uma página, move e redimensiona cada um à mão, e o que você organiza é o que quem visita vê. Não há colunas a preencher nem forma fixa: uma página pode ser tão larga e tão alta quanto você quiser, e um objeto pode sobrepor outro, ficar sobre um fundo colorido ou flutuar onde você o colocar.

Duas coisas fazem o Hotglue parecer diferente da maioria dos editores, e ajuda conhecê-las desde o começo:

- **Não existe botão Salvar.** Cada movimento, redimensionamento e edição é salvo no instante em que você o faz. Você nunca precisa lembrar de salvar, e também não há "descartar alterações". Se quiser recuar de um erro, o Hotglue mantém um histórico (veja *revisões* em *A tela*).
- **O que você edita é o que é publicado, imediatamente.** Quando você altera uma página, a alteração fica disponível para quem visita na hora. Não há uma etapa de publicação separada nem cache a limpar.

## De onde vem o Hotglue

O Hotglue não é originalmente nosso. Foi criado por Danja Vasiliev e Gottfried Haider e ficou conhecido por meio do serviço hospedado em hotglue.me. Foi construído como uma reação deliberada contra as convenções do design web comum: em vez de modelos, colunas e hierarquias arrumadinhas, ele oferece uma tela livre onde o layout é não linear e o posicionamento é inteiramente seu. Esse espírito, romper com os padrões habituais da web e convidar a uma composição criativa e não planejada, é exatamente por que o Telaris o utiliza.

O projeto original não está mais em desenvolvimento ativo na origem. Seu código continua disponível e aberto, licenciado sob a Licença Pública Geral GNU versão 3 (GPL-3.0):

- Projeto de origem: <https://hotglue.me> e o código em <https://github.com/k0a1a/hotglue2>

## A versão Telaris do Hotglue

Este manual descreve a **versão Telaris do Hotglue**, que mantemos e desenvolvemos ativamente como um fork. Ela permanece de código aberto sob a mesma licença GPL-3.0, e nosso código é público:

- Fork do Telaris: <https://github.com/theagitist/hotglue2>

Como o desenvolvemos nós mesmos, o Hotglue dentro do Telaris tem uma série de recursos que não existem no original. A maior parte do que este manual cobre é compartilhada com o Hotglue clássico, mas os recursos a seguir foram adicionados ou substancialmente aprimorados para o Telaris:

- **Suporte a imagens WebP**, ao lado de JPEG, PNG e GIF.
- **Uma interface de edição renovada**, com um conjunto moderno de ícones e um visual mais limpo, com a identidade do Telaris.
- **Mais fontes de vídeo.** As incorporações funcionam com YouTube, Vimeo e PeerTube, incluindo vídeos do PeerTube hospedados em qualquer servidor federado.
- **Um editor de imagens completo dentro da página** (baseado no miniPaint) para desenhar uma nova imagem ou retocar uma existente sem sair da página.
- **Modo soundboard**, em que uma página publicada se torna tocável: toque nos blocos de vídeo para disparar clipes, com áudio hospedado por você próprio mixado para que vários soem ao mesmo tempo.
- **Acessibilidade em telefones e telas pequenas.** As páginas publicadas se ajustam automaticamente para caber em telas estreitas, então um layout construído largo continua utilizável num telefone.
- **Integração ao Telaris**, incluindo controle de acesso por pessoa que edita, anexar páginas a buracos de minhoca e a visão de gestão **Conteúdo hotglue** descrita mais adiante neste manual.
- **Interface localizada.** O editor está disponível em inglês, espanhol, português e francês: os menus, dicas e avisos da tela, o editor de imagens dentro do aplicativo e os controles do Telaris ao redor deles (a visão de Conteúdo hotglue, a barra de ferramentas, os botões e os diálogos) seguem o idioma em que você está trabalhando.

Quando este manual menciona um desses recursos, está descrevendo a versão Telaris especificamente. Se você já usou o Hotglue em outro lugar, essas são as diferenças a esperar.

## Como este manual está organizado

Os capítulos vão de como você entra, à tela em si, a cada tipo de conteúdo que você pode adicionar, e depois à gestão das suas páginas e a como elas aparecem para quem visita.

1. **Entrando.** Chegar ao editor Hotglue no Telaris, e quem pode editar o quê.
2. **A tela.** O modo de edição, os dois menus, e como posicionar, mover, redimensionar e organizar objetos.
3. **Adicionando conteúdo.** Imagens, texto, vídeo da web, desenhos, som e ferramentas de objeto.
4. **Gerenciando páginas.** A visão de Conteúdo hotglue: criar, nomear, atribuir e arrumar páginas.
5. **Como aparece nos telefones.** O que quem visita vê numa tela pequena, e dicas para criar pensando nisso.
6. **Atalhos de teclado.** Todos os atalhos numa única tabela.
7. **Glossário.** As partes nomeadas, definidas brevemente.

## Convenções

- **Caminhos de menu** aparecem assim: <span class="menu-path">menu PAGE &rarr; alterar a cor de fundo</span>.
- **Botões e dicas** aparecem em negrito: **Nova página**, **colocar na página**, **Buraco de minhoca atribuído**.
- **Atalhos de teclado** usam <kbd>alt</kbd> + <kbd>o</kbd>.
- O *itálico* introduz um termo na primeira vez em que ele aparece.

> [!note] Quando algo dá errado
> Se uma página não carregar, ou se o editor se comportar de um jeito que este manual não descreve, procure quem administra a sua instância (quem **opera**). Este manual foca no que você pode fazer quando tudo está funcionando como esperado.
