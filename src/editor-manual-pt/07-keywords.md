# Palavras-chave

Palavras-chave são rótulos curtos que você anexa a buracos de minhoca. São como Telaris conecta conteúdo sem pastas. Uma palavra-chave é a diferença entre uma galáxia que é uma *lista* e uma galáxia que é uma *teia*; o resto, no dia a dia da editora, é construído sobre isso.

Este capítulo cobre atribuir palavras-chave a partir do modal do buraco de minhoca, a paleta de chips, e as operações em lote para trabalhar com muitos buracos de minhoca de uma vez. A **tela** de palavras-chave (a superfície de desenho relacional) tem seu próprio capítulo (8).

## Atribuir palavras-chave

Palavras-chave são atribuídas dentro do modal do buraco de minhoca, no campo **Palavras-chave** ao lado do nome do buraco de minhoca (veja o capítulo 5 para o modal completo). O campo é uma entrada de chips:

- Digite uma palavra-chave e aperte **Enter** ou **vírgula** para adicioná-la como chip.
- Clique no **×** do chip para removê-lo.
- A mesma palavra-chave pode ser adicionada em qualquer caixa; Telaris casa sem diferenciar maiúsculas e minúsculas, então *native* e *Native* são a mesma palavra-chave.

Conforme você digita, sugestões aparecem:

- Palavras-chave já usadas **nesta galáxia** aparecem primeiro.
- Palavras-chave usadas em **galáxias irmãs** (galáxias que compartilham o prefixo `[colchete]` da galáxia atual) aparecem em seguida.
- Outras palavras-chave recentes aparecem por último.

Aceitar uma sugestão é o mesmo que digitar a palavra inteira. Telaris não exige que você use sugestões; você pode sempre digitar uma palavra-chave nova, e nesse caso ela passa a integrar a galáxia.

## Escolher bem as palavras-chave

A decisão mais importante sobre palavras-chave é **quão poucas usar**. Um buraco de minhoca com três palavras-chave bem escolhidas é mais legível do que um com vinte. Cada palavra-chave que você adiciona é uma conexão com todo outro buraco de minhoca que carregue a mesma palavra; se a conexão não for significativa, o caminho da visitante pela galáxia fica ruidoso.

Algumas regras práticas:

- **Uma por qualidade que o buraco de minhoca genuinamente encarna**. *Native* em uma planta que é nativa; *edible* em uma que é de fato consumida. Não *plant* em todo buraco de minhoca de uma galáxia de plantas; essa palavra-chave não carrega sinal.
- **Reutilize antes de inventar.** Quando duas editoras descrevem a mesma ideia com palavras diferentes (*medicinal* e *healing*), o vínculo conceitual fica escuro. Olhe o autocomplete; se uma palavra próxima da sua já existe, prefira-a.
- **Evite palavras-chave que você nunca buscaria.** Uma palavra-chave que ninguém (visitante ou editora) digitaria em um campo de busca é uma que não faz trabalho nenhum.

Não há fila de revisão nem vocabulário central. Cada editora decide as palavras-chave de cada buraco de minhoca; o sistema confia em você. O capítulo 13 fala sobre soberania editorial em detalhe.

## A paleta de chips

Cada palavra-chave recebe uma cor pastel determinística, escolhida pelo texto da palavra. A cor é **a mesma** para aquela palavra em toda galáxia da sua instância: visitantes que aprenderam que *native* é o chip esverdeado em uma galáxia o reconhecem na hora em outra.

É também por isso que renomear uma palavra-chave muda a cor: a cor é ligada ao texto, não a um id interno. Se você renomeia *medicinal* para *healing*, a cor do chip muda. (Na prática: renomeie raramente; fundir é uma operação mais limpa.)

## Editar palavras-chave em um buraco de minhoca existente

Abra o modal **Editar** do buraco de minhoca (capítulo 5). O campo **Palavras-chave** mostra os chips existentes. Adicione chips como acima; remova com o ×; salve. As mudanças se aplicam no próximo carregamento da página da visitante.

## Operações em lote: o modal Bulk-by-keyword

Quando você precisa agir sobre **todo buraco de minhoca que carrega uma certa palavra-chave** de uma vez, o modal **Ação em massa por palavra-chave** é a superfície. Abra a partir da tela inicial da editora, na fileira de botões ao lado de **Novo buraco de minhoca**:

![Modal Ação em massa por palavra-chave: escolha uma palavra-chave, escolha Excluir ou Mover, veja a contagem, aplique](assets/images/editor-manual-pt/09-bulk-by-keyword-modal.png)

O modal se limita à **galáxia atual**: só pode agir sobre buracos de minhoca dentro da galáxia selecionada. Passos:

1. **Escolha uma palavra-chave** no menu suspenso. O menu lista cada palavra-chave da galáxia, com sua contagem de uso ao lado. Telaris atualiza a contagem de buracos de minhoca embaixo conforme você muda a seleção, para que você sempre saiba o que a ação vai atingir.
2. **Escolha uma ação**:
   - **Excluir os buracos de minhoca correspondentes** remove cada buraco de minhoca que carrega a palavra-chave escolhida. As deleções são permanentes (vale o mesmo cuidado do capítulo 5; pergunte à operadora sobre um snapshot antes de qualquer coisa irreversível).
   - **Movê-los para outra galáxia** aparece com um menu suspenso adicional quando selecionada. Os buracos de minhoca são transferidos para a galáxia escolhida junto com suas palavras-chave e mídia.
3. **Aplicar** executa a operação. **Cancelar** descarta sem mudanças.

O modal de ação em massa é uma ferramenta afiada. Duas formas de torná-la menos afiada:

- Tire um snapshot antes da operação, se sua operadora te habilitou para tirar snapshots, ou peça que ela tire.
- Faça uma busca rápida (a caixa de busca na tela inicial da editora) pela palavra-chave antes de abrir o modal, para ver exatamente quais buracos de minhoca serão afetados e confirmar que nenhum deles foi mantido por engano.

## Sinônimos (apelidos por galáxia)

O modelo de palavras-chave de Telaris trata o uso da mesma palavra em duas galáxias como a **mesma palavra-chave**. Não existe mecanismo de apelidos por galáxia no v1 do lançamento; se você quer que *medicinal* em uma galáxia seja tratada como a mesma palavra-chave que *healing* em outra, a jogada prática é **renomear uma para casar com a outra**, fazendo as duas galáxias convergirem em uma única palavra.

Se a intenção editorial é exatamente o oposto (uma palavra que significa coisas diferentes em duas galáxias e não deve conectá-las), use palavras diferentes em cada galáxia. Precisão conceitual é mais útil do que esperteza sintática aqui.

## Contagem de palavras-chave na vista da visitante

Quando o recurso de descoberta **Chips de palavra-chave** da galáxia está ligado (o capítulo 4 cobre o interruptor; o capítulo 10 cobre a experiência da visitante resultante), a visitante vê uma fileira de chips no rodapé da cena 3D mostrando as palavras-chave mais usadas. Clicar em um chip esmaece todo buraco de minhoca que *não* carrega aquela palavra-chave.

Esse é um filtro suave (não remove buracos de minhoca da cena, só os esmaece), e é uma das principais formas de visitantes navegarem por uma galáxia sem instruções. As palavras-chave que você escolhe são a navegação: palavras-chave claras significam uma cena clara.

## Coisas que vale a pena saber

- **Um buraco de minhoca sem palavras-chave é permitido, mas silencioso.** As visitantes ainda podem alcançá-lo por busca de nome ou clicando no 3D; não vão alcançá-lo pela camada de chips. Use zero palavras-chave quando o papel do buraco de minhoca for puramente solitário.
- **Nomes de palavras-chave são buscados na caixa de busca da tela inicial da editora** junto com nomes e descrições de buracos de minhoca. Buscar por uma palavra-chave é a forma mais rápida de auditar quais buracos de minhoca a carregam.
- **Renomear uma palavra-chave atualiza em toda a instância.** Renomear *medicinal* renomeia em toda galáxia que usa a palavra. Não há renome por galáxia.
- **Apagar uma palavra-chave remove de todo buraco de minhoca que a carrega.** Os buracos de minhoca sobrevivem; o chip cai. As deleções acontecem pela tela de palavras-chave (capítulo 8); não estão no modal Ação em massa por palavra-chave, que apaga buracos de minhoca, não palavras-chave.
- **Não há número máximo de palavras-chave por buraco de minhoca**, mas, na prática, três a sete dão boa legibilidade. Passando de dez, a faixa de chips no cartão de informações começa a quebrar feio.
