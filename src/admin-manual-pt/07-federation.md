# Federação e o Pluriverse

Instâncias de Telaris podem ficar sozinhas, ou podem juntar-se a uma **federação**: uma família de instâncias independentes que podem ver e compartilhar as galáxias umas das outras sem que nenhuma delas mande. Este capítulo cobre o lado da sua instância nisso, e, para quem opera o site de coordenação, a superfície extra que vem junto.

A federação é opcional. Muitas instâncias nunca a ligam, e um curso ou um arquivo pessoal raramente precisa dela. Recorra a este capítulo quando você quiser que a sua instância faça parte de uma rede mais ampla de instâncias de Telaris.

## O formato da coisa

Uma federação é coordenada por um **Pluriverse**: um site central que mantém o diretório de instâncias membras e as ajuda a se encontrarem e a confiarem umas nas outras. O Pluriverse é um coordenador, não um dono; ele não guarda o conteúdo de ninguém, e nenhuma instância presta contas a ele por decisões editoriais. Cada instância permanece soberana sobre as próprias galáxias.

Entre duas instâncias, o compartilhamento funciona numa direção de cada vez:

- uma instância **publica** uma galáxia a um par em que confia, e
- o par **assina** e puxa um **espelho somente leitura** daquela galáxia (as galáxias importadas do capítulo anterior).

Nada é compartilhado até que existam tanto uma relação de confiança quanto uma decisão de publicar. A federação é opcional em cada passo: você escolhe juntar-se, você escolhe em quem confiar, você escolhe o que publicar, e você pode retirar qualquer parte disso.

## Juntar-se a um Pluriverse

A participação da sua instância é gerenciada na aba **Pluriverse** do console. Juntar-se é um fluxo de solicitação e admissão: a sua instância se candidata a um Pluriverse, e a operadora daquele Pluriverse a admite. Uma vez admitida, a sua instância aparece no diretório e pode começar a formar confiança com pares.

![A aba Pluriverse em uma instância ainda não federada: o formulário para entrar no Pluriverse com a URL, o nome e o contato de operação da instância](assets/images/admin-manual-pt/08-pluriverse.png)

## A lista de pares

A aba Pluriverse mostra os pares que a sua instância conhece, cada um com seu estado: descoberta (conhecida mas ainda sem confiança), confiável (existe uma relação de confiança mútua), ou bloqueada. Uma ação **Atualizar** atualiza a lista a partir do Pluriverse agora, em vez de esperar a atualização agendada. Há também um caminho avançado para adicionar um par à mão, para um par que você conhece diretamente, que pede que você reconfirme, porque adicionar um par à mão pula a apresentação do diretório.

## Estabelecer confiança

Antes de duas instâncias poderem compartilhar, elas estabelecem **confiança**: um aperto de mão em que cada uma confirma a identidade da outra e ambas concordam em ser pares. Você inicia ou aceita um aperto de mão a partir da lista de pares; quando ele se completa, o estado do par vira confiável nos dois lados. A confiança é mútua e simétrica; ela não compartilha, por si só, nenhum conteúdo. Ela só torna o compartilhamento possível.

## Publicar as suas galáxias

Para deixar um par confiável espelhar uma das suas galáxias, você a **publica** para aquele par. A publicação é por galáxia e por par: você decide, para cada par, qual das suas galáxias ele pode puxar. Uma galáxia que você não publicou é invisível aos pares, mesmo os confiáveis.

Publicar compartilha o conteúdo da galáxia, incluindo sua mídia, numa forma que o par pode verificar que veio de você sem alteração. Você pode **retratar** uma publicação depois; o espelho do par é então removido na sua próxima puxada. Publicar é uma oferta permanente, não um envio único: enquanto ela se mantém, o espelho do par acompanha as suas edições.

## Assinar as galáxias de um par

A outra direção: quando um par confiável publica uma galáxia para você, você pode **assiná-la** e puxar um espelho somente leitura. O espelho aparece na sua aba Galáxias como uma galáxia importada (capítulo anterior), somente leitura, atualizável. Você pode cancelar a assinatura para remover o espelho. O que você pode assinar é o que os seus pares escolheram publicar para você; você não pode puxar uma galáxia que não foi publicada para você.

## Bloquear um par

Se você precisa cortar uma relação, **bloqueie** o par. O bloqueio é a parada forte: ele remove quaisquer espelhos que você puxou dele, retira qualquer coisa que você publicou para ele, e para o compartilhamento nas duas direções. O bloqueio é deliberadamente uniforme, ele não deixa conteúdo pela metade, então é a forma limpa de encerrar uma relação que deu errado. Desbloquear depois devolve o par ao estado meramente descoberta; não restaura o conteúdo que o bloqueio removeu, que teria que ser republicado e puxado de novo.

## Para a operadora do Pluriverse

Se você opera o site de coordenação em vez de só uma instância membra, você tem uma responsabilidade extra: a **admissão**. Novas instâncias se candidatam ao seu Pluriverse, e você decide quais admitir no diretório. A admissão é um passo de triagem; você está decidindo quem pertence a esta federação em particular. A superfície do console para isso deixa você revisar uma candidatura pendente e admiti-la ou recusá-la. Além da admissão, a operadora mantém o diretório honesto: removendo uma instância que ficou permanentemente silenciosa, e respondendo se uma membra reporta um problema com um par.

Operar um Pluriverse não te dá poder sobre o conteúdo ou as escolhas editoriais das membras. Dá a você a lista de convidadas, não o arquivo.

## Coisas que vale a pena saber

- **A federação é inteiramente opcional e reversível.** Você se junta por escolha, confia por escolha, publica por escolha, e pode retirar em cada nível. Nada federa por padrão.
- **As galáxias importadas são somente leitura e impermanentes** (capítulo anterior). Trate a galáxia publicada de um par como uma vista ao vivo, não como a sua cópia.
- **O bloqueio é uniforme e final para o conteúdo que remove.** É a ferramenta certa para encerrar uma relação ruim de forma limpa; não é uma pausa. Use a confiança e o publicar/retratar para ajustes mais suaves.
- **A soberania é o ponto inteiro.** Nenhuma instância, nem o Pluriverse, prevalece sobre as decisões editoriais de outra. O único poder que uma fonte tem sobre um espelho é parar de publicar; o único poder que você tem sobre o que importou é parar de assinar.
