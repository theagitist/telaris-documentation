# Portais

Um portal é um tipo especial de buraco de minhoca. Em vez de carregar conteúdo próprio, carrega um destino: outra galáxia. Uma visitante que abre um portal atravessa. A cena se dissolve, uma nova galáxia carrega, o portal se fecha atrás dela. Os portais são como uma editora constrói pontes intencionais entre galáxias.

Este capítulo cobre quando usar um portal em vez de uma palavra-chave compartilhada, como criar um, e o pequeno conjunto de convenções editoriais que mantém uma rede de portais legível.

## Quando o portal é a ferramenta certa

Telaris já te oferece duas formas de conectar conteúdo entre galáxias:

1. **Palavras-chave compartilhadas**: um buraco de minhoca na galáxia A e um na galáxia B, ambos marcados com *intertidal*, formam uma conexão *passiva*. Uma visitante que segue *intertidal* em qualquer das galáxias aterrissa em uma vista que mostra as duas.
2. **Tags de galáxia**: galáxia A e galáxia B compartilhando a tag *coast* criam uma união; as visitantes que seguem `/tag/coast` veem os buracos de minhoca das duas galáxias juntos.

Um portal é um terceiro tipo de conexão, muito mais *ativo*: a editora diz, em efeito, *deste buraco de minhoca, vá para lá agora*. É a ferramenta certa quando:

- A conexão é **direcional e deliberada**. Uma palavra-chave compartilhada é uma rede; um portal é uma seta.
- A galáxia de destino é uma **continuação da conversa**, não apenas um tópico relacionado. A leitora deve sair da galáxia atual e chegar em outra, não navegar nas duas ao mesmo tempo.
- Você quer que o portal em si **apareça na cena 3D** como um objeto navegável. Um portal é renderizado como um nó 3D distinto; as visitantes o reconhecem e o clicam deliberadamente.

Se nenhuma dessas três coisas se aplica, uma palavra-chave ou uma tag de galáxia geralmente é a melhor escolha.

## Criar um portal

Um portal é um buraco de minhoca cujo Wormhole type está definido como **Portal**. A partir do modal New Wormhole:

![Modal New Wormhole com Wormhole type ajustado para Portal: aparece um menu Target Galaxy](assets/images/editor-manual-pt/11-portal-type-selector.png)

Passos:

1. Abra **New Wormhole** na tela inicial da editora (ou abra o modal de edição de um buraco de minhoca existente e mude seu tipo).
2. Defina **Wormhole type** como **Portal**. Um campo **Target Galaxy** aparece, com um menu suspenso listando cada galáxia a que você tem acesso.
3. Escolha a galáxia de destino no menu suspenso. O botão ao lado, **Create New Galaxy**, é um atalho para o caso em que o destino ainda não existe; selecioná-lo te deixa criar a galáxia de destino inline. Na maioria das vezes, você escolhe uma galáxia existente.
4. **Nomeie** o portal de forma legível. Um portal é um buraco de minhoca, então o nome aparece em listas e na cena 3D; escolha um nome que sinalize a jornada, não só o destino. *To the tide pools* lê melhor que *Tide pools*.
5. Adicione uma **Description** se quiser que um parágrafo curto apareça quando a visitante abre o cartão de informações do portal. A descrição é mostrada brevemente antes da jornada à galáxia de destino começar; trate-a como uma frase de soleira.
6. Opcional: atribua algumas **palavras-chave**. Os portais podem carregar palavras-chave como qualquer outro buraco de minhoca; isso ajuda o portal a aparecer na descoberta por palavras-chave.
7. Salve.

O portal agora aparece na lista de buracos de minhoca com a etiqueta **Portal** na coluna Type, e como um nó distinguível na cena 3D.

## O que as visitantes experimentam

Uma visitante que clica em um portal na cena 3D vê:

- O cartão de informações do portal abre, como em qualquer buraco de minhoca.
- O cartão mostra o nome do portal, a descrição, e (dependendo das configurações da instância) um botão de chamada, **Travel** ou nome semelhante.
- Ativar a chamada fecha a galáxia atual e carrega o destino.
- Na galáxia de destino, a visitante chega à entrada da galáxia (a posição inicial padrão), não a um buraco de minhoca específico.

A visitante pode usar o botão Voltar do navegador para retornar à galáxia de origem. Telaris **não** coloca automaticamente um portal de retorno na galáxia de destino; se você quer que a jornada seja de ida e volta, precisa colocar um portal correspondente à mão.

## Portais de ida e volta

Quando você coloca um portal de A para B, considere se também quer um portal de B de volta para A. Os dois são independentes: cada um é um buraco de minhoca na sua galáxia. Não existe um conceito de "portais ligados".

A decisão é editorial:

- **Sim, coloque um portal de retorno** quando as duas galáxias são parceiras iguais em uma conversa; visitantes que chegam em B devem ser convidadas de volta a A com a mesma naturalidade com que foram convidadas de A para B.
- **Não, deixe o retorno implícito** quando o caminho natural da visitante é de mão única (A é a galáxia que enquadra; B é a resposta; a visitante volta pelo navegador, se voltar).

Se você coloca um portal de retorno, nomeie-o pelo destino para o qual leva, não por "voltar". *To the coastal plants* lê melhor que *Back* ou *Return*.

## Portais e a tela de palavras-chave

Os chips de palavras-chave de um portal aparecem na tela de palavras-chave como os de qualquer outro buraco de minhoca. Um portal marcado com *intertidal* contribui à teia de conexões de *intertidal*. Às vezes as editoras marcam portais com uma palavra-chave específica, como *portal*, para que possam ser filtrados da descoberta por palavras-chave (algumas visitantes podem não querer saltos cheios de portais); na nossa galáxia de demonstração, o buraco de minhoca-portal carrega a tag *portal* por exatamente essa razão.

## Coisas que vale a pena saber

- **Um portal só pode apontar para uma galáxia por vez.** Se você quer um "hub" que se ramifica para muitas galáxias, a resposta é muitos portais, não um só. Você pode colocar vários portais em uma única galáxia, cada um apontando para um destino diferente.
- **O menu suspenso de destino lista só galáxias que você pode editar.** Se a galáxia para a qual você quer abrir um portal está em outra instância, isso é território da federação e cabe à operadora; a superfície de edição não compõe portais entre instâncias.
- **Um portal pode ser redirecionado** editando-o e escolhendo outra galáxia no campo Target Galaxy. As visitantes que tinham o portal favoritado continuam aterrissando na galáxia que estiver selecionada agora. Planeje isso ao mudar destinos depois de publicar.
- **Um portal apontando para sua própria galáxia** é tecnicamente permitido, mas funcionalmente inútil: a visitante aterrissa de volta de onde veio. A interface não vai te impedir, mas o resultado é nada.
- **Apagar um portal remove o buraco de minhoca por inteiro.** A galáxia de destino fica inalterada; só a conexão se perde. Os portais próprios do destino (se houver) continuam funcionando.
- **Portais não carregam mídia.** Têm um nome, uma descrição, e palavras-chave, além da galáxia de destino. Os campos de imagem, vídeo, áudio e PDF continuam no modal mas devem ficar vazios para portais; se você os preenche, são simplesmente ignorados pela experiência da visitante.
