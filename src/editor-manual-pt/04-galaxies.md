# Galáxias

Uma galáxia é, ao mesmo tempo, um continente, um ponto de vista, e uma posição editorial. É a unidade que sua operadora te entrega quando diz "você pode editar aqui"; é a unidade em que a visitante chega; é a unidade que você enquadra, nomeia, e modela. Este capítulo percorre criar uma galáxia, configurá-la, e as operações cotidianas sobre ela.

## Selecionar uma galáxia

O menu suspenso **Current Galaxy** no topo da tela inicial da editora é como você escolhe em qual galáxia está trabalhando. *All my galaxies* mostra buracos de minhoca de todos os lugares a que você tem acesso; selecionar uma galáxia específica filtra tudo abaixo para aquela.

A primeira coisa que o menu te ensina é a forma das suas responsabilidades editoriais: cada galáxia listada é uma galáxia que você pode editar. Se uma galáxia de uma colega está faltando, sua operadora não te atribuiu. (As visitantes da sua instância veem todas as galáxias públicas; as editoras só veem aquelas pelas quais são responsáveis.)

Quando você escolhe uma galáxia específica, três novos botões aparecem ao lado do menu suspenso:

![Tela inicial da editora com uma única galáxia selecionada: aparecem os botões View, Settings, Canvas](assets/images/editor-manual/03-editor-home-single-galaxy.png)

- **View** abre a galáxia em modo visitante, em uma nova aba. Use sempre que quiser ver como uma mudança fica do assento da visitante.
- **Settings** abre a configuração da galáxia. A maior parte deste capítulo é sobre o que está dentro daquele modal.
- **Canvas** abre a tela de palavras-chave, a superfície de desenho relacional coberta no capítulo 8.

## Criar uma galáxia

Se você pode ou não criar uma nova galáxia depende da configuração da sua operadora; algumas instâncias deixam as editoras criarem galáxias livremente, outras reservam a criação para administradoras. Se você tem permissão, o botão de nova galáxia está na mesma linha do seletor; se não, peça à sua operadora e ela cria uma para você.

Quando uma nova galáxia é criada, ela aparece vazia: zero buracos de minhoca, sem palavras-chave, tema padrão. O passo seguinte é preencher as configurações.

## Configurações da galáxia

Abra o botão **Settings** ao lado do seletor. Um modal abre:

![Modal Edit Galaxy: Name, Tagline, Visual Theme, Tags, ações em lote, e seletores de descoberta](assets/images/editor-manual/04-galaxy-settings-modal.png)

O modal é o lugar central onde você define o que uma galáxia é e como se comporta. Os campos, na ordem:

**Name** (obrigatório). O nome que as visitantes veem no seletor de galáxia e no topo da cena. Os nomes de galáxia não são únicos na rede, mas duas galáxias com o mesmo nome na mesma instância confundem; escolha algo legível e distinto. Você pode mudar o nome de uma galáxia a qualquer momento.

**Tagline** (opcional, curta). Uma descrição em uma linha mostrada ao lado ou abaixo do nome da galáxia na interface da visitante. A tagline não aparece na cena 3D; seu público principal é o seletor e a listagem pública.

**Visual Theme**. Um menu suspenso que escolhe a aparência da cena 3D: *Cosmic* (estrelas, planetas, foguetes) é o padrão e o mais comum; outros temas são *Simple*, *Abstract*, *Rectangles*, *Stripes*, e *Tech*. Escolha aquele cujo vocabulário combina com o conteúdo. O tema pode ser trocado a qualquer momento; a mudança vale para todas as visitantes imediatamente, mas não altera o que você criou, só como é renderizado.

**Tags** (opcional). Rótulos curtos que agrupam esta galáxia com outras. Duas galáxias que compartilham uma tag formam uma *união de galáxias*: visitantes que seguem a tag veem buracos de minhoca das duas de uma vez, cada um mantendo o estilo visual da sua galáxia de origem. Use tags quando várias galáxias forem irmãs em algum arranjo maior. O campo Tags autocompleta com tags que você usou em outras galáxias suas e com tags compartilhadas por galáxias prefixadas com o mesmo `[colchete]`.

**Bulk wormhole actions**. Dois botões que aplicam uma única configuração a todos os buracos de minhoca desta galáxia de uma vez.

- **Use images as icons (all wormholes)** faz com que cada buraco de minhoca com imagem renderize sua imagem como o nó 3D, em vez do ícone padrão do tema. Útil quando você tem uma galáxia de fotografias e quer que as fotos *sejam* a cena.
- **Revert all to theme icons** desfaz o anterior: cada buraco de minhoca volta ao ícone do tema, tenha imagem ou não.

Essas ações são em lote; cada buraco de minhoca pode ainda ser ajustado individualmente depois (capítulo 5).

**Discovery toggles**. Um conjunto de interruptores no rodapé do modal que controla como a visitante experimenta sua galáxia. Vêm desligados por padrão; ligue cada um quando quiser o recurso correspondente. Cada interruptor é coberto no capítulo 10 (Vistas de visitante), junto da função que controla.

Salve o modal com **Save**; feche sem mudanças com **Cancel** ou clicando fora. As alterações se aplicam às visitantes imediatamente.

## Enquadramento editorial

O enquadramento de uma galáxia é o parágrafo curto que a abre para as visitantes. É a resposta à pergunta *o que é esta galáxia?* antes da visitante ter encontrado qualquer buraco de minhoca. Dois lugares para escrevê-lo:

1. O campo **Tagline** no modal da galáxia, para o resumo em uma linha que aparece ao lado do nome da galáxia.
2. (Em algumas instâncias) um buraco de minhoca dedicado ao enquadramento dentro da galáxia, em geral o primeiro que a visitante vê ao entrar. Se sua instância usa esse padrão, sua operadora avisa.

Ambos são escolhas editoriais, não técnicas. Escreva o enquadramento na sua própria voz; a galáxia é sua para apresentar.

## Compartilhar buracos de minhoca entre galáxias por tags

Se você tem uma galáxia cujo conteúdo faz parte de uma constelação maior de trabalho (uma exposição com várias salas; um periódico com várias edições; uma série de coleções relacionadas), o campo **Tags** é como você diz isso. Adicione a mesma tag a cada galáxia que pertence ao conjunto; a união fica acessível às visitantes em `/tag/<tag-slug>` (sua operadora pode passar o link).

As tags não criam nem modificam buracos de minhoca. São puramente um arranjo de visualização: na vista da união, a visitante vê os buracos de minhoca de cada galáxia marcada juntos, mas cada um permanece na galáxia de origem. Edite uma galáxia, as outras ficam intactas.

## Retirar uma galáxia

Não há um botão de "apagar galáxia" para editoras na configuração típica de uma instância; se você realmente precisa retirar uma galáxia, peça à sua operadora e ela providencia. A razão da fricção é editorial: uma galáxia que foi ligada de fora (por um percurso, por um portal, por uma união de tags, pelo favorito de uma visitante) não some sem mais; o link fica escuro. A operadora decide como lidar com o link escuro.

O padrão mais comum não é apagar uma galáxia, e sim torná-la invisível para visitantes, mantendo-a do lado da edição, para que a decisão editorial possa ser revertida depois.

## Coisas que vale a pena saber

- **Você não pode mover uma galáxia.** Uma vez que uma galáxia tem um slug (a parte `/<nome-curto>` da URL), o slug é permanente. Renomear a galáxia muda o nome de exibição mas não o slug. Se a mudança de slug for crítica, a operadora pode providenciar, mas a URL muda para todas as pessoas com o link antigo.
- **O seletor de galáxia agrupa galáxias com o mesmo prefixo `[colchete]`.** Se sua instância usa prefixos entre colchetes (`[mocambos] Galaxy A`, `[mocambos] Galaxy B`), o seletor as agrupa visualmente. Os colchetes são uma convenção, não um recurso; use-os quando o agrupamento ajudar suas colegas editoras a encontrarem galáxias relacionadas.
- **Uma galáxia com zero buracos de minhoca é permitida.** Galáxias novas começam vazias e seguem editáveis. Não há exigência de um número mínimo de buracos de minhoca para salvar.
- **O tema visual só muda a aparência da cena.** Trocar de Cosmic para Tech não altera o que está dentro da galáxia; altera como os buracos de minhoca são *desenhados*. Experimente um tema; se não couber, volte para outro.
