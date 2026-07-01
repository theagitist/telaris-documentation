# Vistas de visitante

O trabalho da editora é lido por visitantes. Quase toda escolha editorial que você faz aparece, em algum momento, do lado da visitante, seja diretamente (a descrição, a mídia, as palavras-chave), seja indiretamente (as relações desenhadas na tela de palavras-chave, a forma como os buracos de minhoca são marcados). Este capítulo é o seu mapa do que as visitantes veem, e dos interruptores do lado da editora que dão forma a tudo isso.

A vista da visitante se alcança seguindo qualquer URL de visitante da sua instância: tipicamente o slug da galáxia, às vezes sem slug nenhum (sua operadora pode confirmar o caminho de entrada).

![Cena 3D da visitante para a galáxia de demonstração Coastal plants](assets/images/editor-manual-pt/13-visitor-scene.png)

## A cena 3D

A vista padrão da visitante é uma cena tridimensional onde cada buraco de minhoca é um pequeno objeto flutuando no espaço sobre o fundo do tema escolhido para a galáxia. O mouse da visitante rotaciona a vista; rolar ou pinçar dá zoom; clicar em um buraco de minhoca abre seu cartão de informações.

O que você escolhe como editora que se mostra aqui:

- **O tema da galáxia** (capítulo 4) controla a aparência: quais ícones renderizam os buracos de minhoca, como é o fundo, como é a iluminação.
- **O interruptor Usar como ícone do buraco de minhoca** em cada buraco de minhoca (capítulo 5) decide se aquele buraco de minhoca renderiza como sua imagem (quando ligado) ou como o ícone padrão do tema (quando desligado).
- **A marca Acentuar buraco de minhoca** em um buraco de minhoca o renderiza maior e mais proeminente na cena.
- **A marca Mostrar palavras-chave** imprime as palavras-chave do buraco de minhoca como rótulos flutuantes ao lado do ícone.

Essas quatro escolhas interagem: uma galáxia de buracos de minhoca acentuados, com imagens como ícones e palavras-chave à mostra, é uma cena agitada; uma galáxia de buracos de minhoca com ícones do tema e sem rótulos é uma cena quieta. Não existe modo "certo"; escolha o registro visual que combina com o registro editorial do conteúdo.

## O cartão de informações

Uma visitante que clica em um buraco de minhoca vê seu **cartão de informações** abrir sobre a cena. O cartão contém, em ordem:

- O **nome** do buraco de minhoca no topo.
- O **visual primário** (imagem, vídeo, ou PDF) abaixo do nome, dimensionado ao cartão.
- A **descrição** como um parágrafo de corpo.
- O **player de áudio** se houver áudio anexado.
- O **código de embed** se algum foi fornecido.
- Uma fileira de **chips de palavras-chave** no rodapé do cartão, cada um clicável.
- O botão **Abrir link** se o buraco de minhoca carrega uma URL.

Quando a visitante clica em um chip de palavra-chave no cartão de informações, a cena esmaece os buracos de minhoca que não carregam aquela palavra-chave. O cartão se fecha. Essa é uma das principais formas pelas quais visitantes navegam por tags, em vez de por nome.

## Os interruptores de Descoberta

O modal de configurações da galáxia traz uma seção Descoberta (o capítulo 4 apresentou o modal; aqui está o que cada interruptor faz do lado da visitante):

![Modal de configurações da galáxia rolado até os interruptores de Descoberta](assets/images/editor-manual-pt/12-galaxy-discovery-section.png)

Cada interruptor vem desligado por padrão. Ligue um quando quiser o recurso correspondente.

### Passeio automático

Um percurso que roda sozinho pela galáxia. Quando ligado, opções adicionais aparecem:

- **Modo de início** (manual, inativo, imediato):
  - **Manual**: a visitante precisa apertar um botão de reprodução para iniciar o percurso.
  - **Inativo**: o percurso começa automaticamente depois que a visitante não interage com a cena por um certo número de segundos (configurável).
  - **Imediato**: o percurso começa assim que a visitante chega na galáxia.
- **Seleção de nós** (todos, apenas destacados, amostra aleatória de N, marcados por palavra-chave):
  - **Todos os nós**: o percurso visita cada buraco de minhoca da galáxia em ordem.
  - **Apenas nós destacados**: visita apenas os buracos de minhoca acentuados.
  - **Uma amostra aleatória de N nós**: escolhe N buracos de minhoca aleatórios a cada sessão; o número é configurável.
  - **Nós marcados com uma destas palavras-chave**: visita apenas buracos de minhoca que carregam alguma de um conjunto escolhido de palavras-chave. A lista de palavras-chave é definida em um sub-campo que aparece quando esta opção é selecionada.
- **Pausa em nós sem conteúdo** em segundos em cada parada, antes de o percurso seguir para o próximo.
- **Repetir o passeio ao terminar**: quando ligado, o percurso volta ao começo depois da parada final; quando desligado, encerra discretamente.

Um botão **Pré-visualizar passeio** aparece junto dos campos de Passeio automático; selecioná-lo abre a vista da visitante em uma nova aba com o percurso rodando, para você conferir a temporização sem salvar a configuração.

O capítulo 11 percorre percursos em maior profundidade.

### Foco em inatividade

Quando ligado, a cena ilumina suavemente um buraco de minhoca diferente a cada N segundos quando a visitante está ociosa. Diferente do passeio automático, não move a câmera nem abre cartões de informações; só traz um buraco de minhoca para a frente, com leveza, como um museu mudando a iluminação da sala.

Duas configurações:

- **Limite de inatividade** em segundos antes de o destaque começar.
- **Seleção** (todos, apenas destacados).

O foco em inatividade cabe bem em galáxias de tom ambiente (um ciclo de poemas; uma sequência de fotografias); dá à sala algo a fazer quando a visitante parou de clicar.

### Chips de palavra-chave

Quando ligado, a cena pinta uma faixa de chips pastel no rodapé da tela da visitante, um chip por palavra-chave mais usada na galáxia. As visitantes podem clicar em um chip para esmaecer cada buraco de minhoca que não a carrega.

Use quando a galáxia tem um vocabulário forte de palavras-chave pelo qual visitantes naturalmente navegariam; desligue quando as palavras-chave são granulares demais ou numerosas demais para que chips sejam úteis.

### Buracos de minhoca relacionados

Quando ligado, um cartão de informações abre com até cinco chips de buracos de minhoca **relacionados** no rodapé: outros buracos de minhoca (nesta galáxia ou em galáxias irmãs) que compartilham pelo menos uma palavra-chave com o aberto. A visitante pode clicar em um chip para saltar diretamente para o relacionado.

Essa é a principal forma pela qual visitantes viajam lateralmente por uma rede sem abrir um portal. Ligue quando quiser que a visitante descubra a teia; desligue quando quiser que a visitante permaneça concentrada em um buraco de minhoca por vez.

### Vista 2D

Quando ligado, um pequeno alternador **3D / 2D** aparece no topo da tela da visitante. Mudar para 2D colapsa a cena em um mapa plano de chips de buraco de minhoca: cada chip é o ícone do buraco de minhoca mais o nome. A vista 2D carrega mais rápido e é mais fácil de escanear; algumas visitantes preferem para encontrar um buraco de minhoca específico depressa.

O mapa 2D pode ser **ampliado e deslocado** (role ou pince para ampliar, arraste para deslocar), e um controle **Fit** (Ajustar) traz todos os buracos de minhoca à vista de uma vez, para que nada fique empilhado fora da tela, por mais buracos de minhoca que a galáxia tenha. Quando há mais de uma galáxia em vista (uma união de galáxias, capítulo 12), a lista de galáxias ao lado do mapa esmaece as galáxias para as quais você não está apontando, e cada chip de buraco de minhoca leva o nome da sua galáxia como prefixo, para que você distinga buracos de minhoca de mesmo nome.

A escolha da visitante entre 3D e 2D persiste no navegador (ela não precisa ficar escolhendo de novo).

## Rodapés de procedência e atribuição

Quando a procedência editorial de um buraco de minhoca carrega uma atribuição (`Image attribution`, crédito de comunidade de origem, ou um aviso de espelhamento federado), o cartão de informações mostra como uma pequena linha de rodapé abaixo da descrição.

Não há interruptor global para esconder rodapés de procedência; se o seu trabalho credita uma fotógrafa ou uma comunidade de origem, esse crédito aparece sempre que o buraco de minhoca é aberto. Atribuição autoral e consentimento da comunidade de origem são preocupações editoriais de primeira classe; o capítulo 13 cobre a disciplina editorial em torno deles.

## Coisas que vale a pena saber

- **A visitante vê o que você publicou, não o seu rascunho.** Não há um modo "preview" separado da vista publicada; quando você salva um buraco de minhoca ou uma configuração de galáxia, o próximo carregamento da página da visitante reflete a mudança. Para pré-visualizar uma mudança sem afetar visitantes, você precisaria fazer a mudança em uma galáxia que ainda não é pública.
- **A cena 3D roda no navegador da visitante.** Dispositivos mais antigos ou computadores de baixa potência podem ter dificuldade com galáxias muito densas. O alternador para a vista 2D é o remédio padrão.
- **Áudio com reprodução automática pode ser bloqueado pelo navegador da visitante.** A maioria dos navegadores não permite que áudio comece sem a interação da visitante. Se você liga o Reproduzir automaticamente (capítulo 6) e uma visitante relata que não há som, esta é a causa mais provável; o primeiro clique da visitante na página costuma desbloquear o áudio. Uma galáxia com uma paisagem sonora mostra um pequeno controle de **som ligado/desligado** na cena; na primeira vez que uma visitante o liga, a paisagem sonora começa (vale a mesma regra do gesto do navegador).
- **Os interruptores de Descoberta são independentes entre si.** Passeio automático e foco em inatividade podem estar ligados ao mesmo tempo (o spotlight entra se o percurso termina ou não começou). Escolha as combinações que casam com sua intenção editorial; os interruptores não se condicionam mutuamente.
