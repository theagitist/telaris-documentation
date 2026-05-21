# Glossário

Cada conceito nomeado no manual da editora, em um só lugar. Estilo de dicionário; cada entrada diz o que o termo significa e qual capítulo o percorre.

**2D view**. Uma superfície alternativa para a visitante (capítulo 10) que renderiza a galáxia como uma grade plana de chips de buraco de minhoca. Alternada pela visitante; o alternador é habilitado na seção Discovery do modal de configurações da galáxia.

**Accentuate**. Uma marca por buraco de minhoca (capítulo 5) que o renderiza maior e mais proeminente na cena 3D. Frequentemente pareada com auto-tour para ênfase narrativa.

**Anotação (linha)**. Veja *Tela de palavras-chave*.

**Atribuição de imagem** (*image attribution*). Um campo de texto livre ao lado de uma imagem enviada (capítulo 6) para crédito ou notas de licença. Viaja com a imagem para o rodapé do cartão de informações.

**Áudio**. Um tipo de mídia que um buraco de minhoca pode carregar, independente do visual primário. Interruptores opcionais de autoplay e loop. Capítulo 6.

**Auto-tour**. Um percurso que roda sozinho por uma galáxia (capítulo 11), configurado na seção Discovery das configurações da galáxia. Modos: manual, idle, immediate.

**Bracket prefix**. Uma convenção de nomeação (por exemplo, `[exhibit] Room A`) que agrupa galáxias em uma família visível no seletor e em uma URL de união `/[exhibit]`. Capítulo 12.

**Bulk by keyword**. Um modal (capítulo 7) que opera sobre cada buraco de minhoca da galáxia atual que carrega uma palavra-chave escolhida: apagá-los em lote, ou movê-los em lote para outra galáxia.

**Buraco de minhoca**. A menor unidade de conteúdo em Telaris. Uma única passagem de texto, imagem, vídeo, PDF, áudio, ou composto. Capítulo 5.

**Canvas**. Forma curta de *tela de palavras-chave* (capítulo 8). A superfície de desenho onde editoras dispõem chips de palavras-chave e desenham relações entre eles.

**Chip**. A pílula pastel que representa uma palavra-chave na interface da editora. Cada palavra-chave tem uma cor determinística pelo texto; a cor é a mesma em todo lugar da instância.

**Cluster**. Um agrupamento de galáxias gerido pela administração que se comporta como uma galáxia por si só. As editoras não compõem clusters; veem-nos no seletor se tiverem acesso. O capítulo 12 cobre o comportamento de união em geral.

**Cosmic theme**. O tema visual padrão de uma galáxia: estrelas, planetas, foguetes. Outros temas: Simple, Abstract, Rectangles, Stripes, Tech. Capítulo 4.

**Description**. O corpo de texto de um buraco de minhoca, exibido dentro do cartão de informações. Aceita markdown básico. Capítulo 5.

**Discovery**. A seção do modal de configurações da galáxia que liga e desliga recursos do lado da visitante: auto-tour, idle spotlight, keyword chips, related wormholes, 2D view. Capítulo 4 (modal) e capítulo 10 (lado da visitante).

**Dwell time**. O número de segundos que um auto-tour pausa em cada buraco de minhoca antes de seguir. Capítulo 11.

**Editora**. O papel atribuído a uma pessoa que cria conteúdo. Distinto da operadora (que opera a instância). Este manual é escrito para editoras.

**Galáxia**. A maior unidade com que uma editora trabalha. Uma coleção de buracos de minhoca relacionados, mais um enquadramento, um tema, e um conjunto de tags. Capítulo 4.

**Galaxy tag**. Um rótulo curto (capítulo 4) adicionado a uma galáxia no seu modal de configurações. Duas galáxias com a mesma tag formam uma união; visitantes em `/tag/<slug>` veem as duas. Capítulo 12.

**Icon**. A representação 3D de um buraco de minhoca na cena. Por padrão, o ícone do tema da galáxia; pode ser personalizado por buraco de minhoca (capítulo 6).

**Idle spotlight**. Um recurso Discovery (capítulo 10) que ilumina suavemente um buraco de minhoca diferente a cada N segundos quando a visitante está ociosa.

**Info card** (cartão de informações). O painel que abre sobre a cena 3D quando uma visitante clica em um buraco de minhoca. Contém o nome do buraco de minhoca, o visual primário, a descrição, o áudio, as palavras-chave, e o botão Open Link. Capítulo 10.

**Instância**. Uma única implantação de Telaris em um endereço web. Sua instância é aquela cuja URL está na barra de endereço. Múltiplas instâncias podem se federar (conteúdo entre instâncias é território da operadora).

**Keyword chips**. (1) As pílulas pastel mostradas dentro da superfície de edição para editar palavras-chave. (2) O recurso Discovery que pinta uma faixa de chips no rodapé da cena da visitante; visitantes clicam em um chip para esmaecer os buracos de minhoca que não a carregam. Capítulo 10.

**Loop**. (1) O interruptor de loop de áudio: uma trilha reinicia depois de terminar. (2) O interruptor de loop de percurso: o auto-tour volta ao começo depois do último buraco de minhoca. Capítulo 6 e capítulo 11.

**Manual**. (1) Este documento. (2) Um modo de início do auto-tour em que a visitante precisa apertar Play. Capítulo 11.

**Mídia**. O nome coletivo de imagem, vídeo, áudio, PDF, e código de embed anexados a um buraco de minhoca. Capítulo 6.

**Multigaláxia**. O nome geral para vistas que mostram mais de uma galáxia ao mesmo tempo. Conseguido por tags, prefixo entre colchetes, ou lista explícita por URL. Capítulo 12.

**Object**. O tipo padrão de Wormhole. Um Object carrega conteúdo (descrição, mídia). Contraste com Portal. Capítulo 5.

**Operadora**. O papel da pessoa que opera a instância de Telaris. As editoras não executam tarefas da operadora (instalação, federação, gestão de chaves). Quando este manual diz "pergunte à sua operadora", é esta pessoa.

**Palavra-chave**. Um rótulo curto anexado a buracos de minhoca (capítulo 7). Dois buracos de minhoca que compartilham uma palavra-chave estão conectados. Palavras-chave casam sem diferenciar maiúsculas e são globais por texto em toda a instância.

**PDF**. Um tipo de mídia para documentos. Embutido no cartão de informações da visitante com um leitor na própria página. Capítulo 6.

**Per-peer keys, Pluriverso, federação**. Conceitos do domínio da operadora. Não relevantes para editoras; cobertos no Manual de Administração.

**Percurso**. Veja *Auto-tour*.

**Portal**. Um buraco de minhoca cujo tipo é Portal: em vez de conter conteúdo, aponta para outra galáxia. Visitantes que o abrem atravessam. Capítulo 9.

**Preview tour**. Um botão ao lado da configuração do auto-tour (capítulo 11) que abre uma vista da visitante em uma nova aba com o percurso rodando, para você conferir a configuração antes de salvar.

**Primary visual** (visual primário). A imagem, vídeo, ou PDF único que um buraco de minhoca carrega. Mutuamente exclusivos (as três abas compartilham um slot). Áudio e código de embed são separados. Capítulo 6.

**Random N**. Um modo de seleção de nó do auto-tour: escolhe N buracos de minhoca aleatórios a cada sessão. Capítulo 11.

**Related wormholes**. Um recurso Discovery: o cartão de informações mostra até cinco chips de buracos de minhoca que compartilham pelo menos uma palavra-chave com o aberto; clicar salta para o relacionado. Capítulo 10.

**Slug**. A forma curta e segura para URL do nome de uma galáxia ou buraco de minhoca. As galáxias têm um slug visível na barra de endereço. Slugs não mudam uma vez definidos.

**Snapshot**. Um backup da instância inteira, do lado da operadora. Editoras não tiram snapshots; o Manual de Administração cobre.

**Soberania**. Veja *Soberania editorial*.

**Soberania editorial**. O princípio de que as editoras decidem o que entra em uma galáxia e como é marcado, sem fila de revisão nem vocabulário central. Capítulo 13.

**Source community** (comunidade de origem). Uma comunidade cujo trabalho é hospedado em uma galáxia de Telaris. O consentimento da comunidade é o chão editorial; a retirada do consentimento é final. Capítulo 13.

**Tagged keywords**. Um modo de seleção de nó do auto-tour: visitar apenas buracos de minhoca que carregam alguma de um conjunto escolhido de palavras-chave. Capítulo 11.

**Tela de palavras-chave**. A superfície de desenho que ocupa toda a janela (capítulo 8), onde editoras dispõem chips de palavras-chave e desenham linhas de relação entre eles. Apenas desktop.

**Theme**. O estilo visual de uma galáxia: cosmic, simple, abstract, rectangles, stripes, tech. Escolhido no modal de configurações da galáxia. Capítulo 4.

**Union** (união). Veja *União de galáxias*.

**União de galáxias**. Uma vista que mostra os buracos de minhoca de duas ou mais galáxias juntas, mantendo cada um na galáxia de origem. Alcançada por tags de galáxia, prefixo entre colchetes, ou URL `?galaxies=` explícita. Capítulo 12.

**Use as wormhole icon**. Um interruptor por buraco de minhoca que renderiza a imagem do buraco de minhoca como seu ícone na cena 3D, substituindo o padrão do tema. Capítulo 6.

**View** (botão). Um botão ao lado do seletor de galáxia que abre a galáxia atual em modo visitante, em uma nova aba. Capítulo 4.

**Visitor view** (vista da visitante). A cena 3D (ou 2D) que as visitantes veem. Conduzida pelas escolhas da editora no modal do buraco de minhoca e no modal de configurações da galáxia. Capítulo 10.

**Vista multigaláxia**. Uma união de várias galáxias que as visitantes podem navegar como se fosse uma única cena, com cada buraco de minhoca mantendo o tema visual da sua galáxia de origem. Capítulo 12.

**Visitante**. A leitora de uma galáxia. Uma visitante lê o conteúdo que a editora publica; não vê a superfície de edição. A vista da visitante é o que aparece depois de um clique no botão View ou de uma URL direta.

**Wormhole**. Veja *Buraco de minhoca*.

**Wormhole type** (tipo de buraco de minhoca). Um campo no modal do buraco de minhoca: Object (padrão, carrega conteúdo) ou Portal (carrega uma galáxia de destino). Capítulo 5 e capítulo 9.
