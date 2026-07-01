# Controle de acesso de edição

Ter uma conta de editora é uma coisa; poder editar uma dada galáxia é outra. Telaris separa as duas, para que você decida não só *quem* é editora, mas *o que* cada editora pode tocar. Este capítulo cobre os dois mecanismos: o interruptor de edição que pode ser desligado em vários níveis, e o acesso por assento que limita uma editora a galáxias específicas.

## O interruptor de edição (uma cascata)

A edição pode ser ligada ou desligada em quatro níveis, do mais amplo ao mais estreito:

- a **instância inteira**,
- um **aglomerado** de galáxias,
- uma única **galáxia**,
- uma única **conta**.

O interruptor cai em cascata: desligar a edição num nível mais amplo a desliga para tudo que estiver dentro dele, a menos que algo mais estreito a religue. Desligar a edição da instância detém todas as editoras; desligá-la para um aglomerado detém a edição nas galáxias daquele aglomerado; e assim por diante. A edição vem **ligada por padrão** em todos os níveis, então uma instância nova se comporta como você esperaria e você só recorre a esses interruptores quando quer deter algo.

**A administração é isenta.** A cascata nunca tranca uma administradora para fora da edição; ela governa as editoras. Isso é deliberado, para que você não desligue por acidente a sua própria capacidade de corrigir as coisas.

### Quando você usaria

- **Um curso ou projeto terminou.** Desligue a edição da instância (ou daquele aglomerado) para congelar o conteúdo mantendo cada conta e tudo o que foi feito. É exatamente o que uma instância de demonstração faz quando seu curso acaba: contas e conteúdo permanecem, mas nada novo pode ser editado.
- **Uma galáxia está em revisão ou sendo repassada.** Desligue a edição só daquela galáxia enquanto ela se assenta, sem afetar o resto da instância.
- **Uma editora deve pausar.** Desligue a edição de uma única conta sem tocar em ninguém mais.

O interruptor **Permitir edição** em *Configurações globais* é a ponta de instância desta cascata; os níveis de aglomerado, galáxia e conta são alcançados onde essas coisas são gerenciadas.

## Acesso por assento: somente leitura e leitura e escrita

A edição estar *ligada* ainda não significa que uma editora pode editar *tudo*. Uma editora trabalha nas galáxias em que tem um **assento**, e cada assento é ou:

- **leitura e escrita**, a editora pode mudar o conteúdo da galáxia, ou
- **somente leitura**, a editora pode ver a galáxia na sua visão de edição mas não pode mudá-la.

Uma editora sempre tem leitura e escrita nas galáxias que criou. Assentos em outras galáxias são concedidos: você (ou os padrões de auto-inscrição) dá a uma editora um assento em uma galáxia, no nível que você escolher. Um assento somente leitura é como você deixa alguém estudar ou consultar uma galáxia, ou usá-la como modelo, sem poder alterá-la. Somente leitura é também como o conteúdo importado se comporta para todo mundo: conteúdo espelhado de outra instância é somente leitura para as suas editoras, porque a autoridade sobre ele vive na sua fonte (veja *Galáxias e aglomerados*).

Os dois mecanismos se combinam. Uma editora pode mudar uma galáxia só quando a edição está ligada para ela em toda a cascata **e** ela detém um assento de leitura e escrita naquela galáxia. Se qualquer um faltar, a galáxia abre para ela num estado de visualização, não de edição.

## Coisas que vale a pena saber

- **Desligado por padrão não é nada; os interruptores são de exclusão.** Você nunca precisa ligar a edição. Você a desliga quando quer deter algo, e a religa quando termina.
- **Congelar não é apagar.** Desligar a edição mantém cada conta e tudo o que foi criado; só impede novas mudanças. É a forma segura de encerrar um projeto sem descartá-lo.
- **Somente leitura é uma escolha de primeira classe, não uma menor.** Grande parte do valor de um arquivo compartilhado é poder mostrar uma galáxia a colaboradoras que não devem alterá-la. Conceda assentos somente leitura sem hesitar.
