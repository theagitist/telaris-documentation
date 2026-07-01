# Manutenção e diagnóstico

Este capítulo reúne os detalhes operacionais: as abas **Chaves de API** e **Informação do PHP**, como a instância mantém a própria estrutura de banco de dados atual, e onde ficam as poucas configurações no nível de arquivo. Você visitará essas superfícies raramente, que é exatamente por que ajuda saber o que elas são antes de precisar delas.

## Chaves de API

O próprio front-end da instância lê conteúdo por uma API interna, e essa API é protegida por uma chave. A aba **Chaves de API** é onde essas chaves são gerenciadas: você pode ver as chaves que existem e gerar uma nova.

Para uma instância que foi preparada normalmente, uma chave padrão já existe e tudo funciona; você nunca precisa desta aba. Ela importa em duas situações:

- **Uma instância provisionada à mão sem chave.** Se uma instância foi preparada à mão em vez de pelo processo normal, ela pode não ter chave padrão, e a cena das visitantes ou as visões de administração não conseguem carregar conteúdo (um erro de "falha ao carregar"). Gerar uma chave aqui resolve isso.
- **Rotacionar uma chave.** Se uma chave deve ser substituída, gere uma nova aqui.

A menos que você esteja resolvendo um desses casos, deixe esta aba em paz.

## Informação do PHP

A aba **Informação do PHP** reporta o ambiente de servidor em que a instância roda: a versão do PHP, quais extensões importantes estão presentes, e a lista completa de extensões carregadas. É um diagnóstico somente leitura. Sua finalidade é responder, depressa, "este servidor tem o que Telaris precisa?" quando algo se comporta de forma estranha, sem você ter que entrar no servidor. Se você algum dia reportar um problema a quem gerencia o servidor, a informação de versão e extensões aqui é o que essa pessoa vai pedir.

## Como a estrutura do banco de dados fica atual

Telaris gerencia a própria estrutura de banco de dados. Quando a instância roda uma versão do código mais nova do que aquela para a qual o banco de dados foi preparado por último, ela traz a estrutura para o dia por conta própria, adicionando o que a nova versão precisa, na primeira vez que é necessário. Não há um passo separado de "rodar as migrações" para você executar depois de uma implantação; a instância cuida disso.

É por isso que implantar uma atualização é, no caso normal, só colocar o novo código no lugar; a instância faz o resto na próxima requisição. O **aviso de incompatibilidade de esquema** (veja *Backups e snapshots*) é a exceção, o sinal de que essa autoatualização não se completou, e o resto daquele capítulo cobre o que ele significa.

## As poucas configurações no nível de arquivo

Quase tudo o que uma administradora define vive no console e no banco de dados, que é onde você deve defini-lo. Um pequeno número de valores fundamentais, principalmente a conexão de banco de dados que a instância usa, vive em um arquivo de configuração no servidor, e não no console, porque a instância precisa deles antes de conseguir alcançar o próprio banco de dados para ler qualquer outra coisa. Você normalmente não vai tocar nesse arquivo; ele é definido uma vez quando a instância é instalada. As configurações que você *de fato* muda no dia a dia, o e-mail, o endereço da instância, o idioma padrão, o interruptor de edição, estão todas em *Configurações globais*, no console, justamente para que você não tenha que editar arquivos para operar a instância.

Se você não instalou a instância e algo neste nível parece errado (a instância não consegue alcançar o banco de dados, ou os links de e-mail apontam para o endereço errado), esse é o ponto de envolver quem preparou o servidor, ou de consultar a referência de instalação do próprio repositório de código.

## Coisas que vale a pena saber

- **A maioria dessas abas é "para o caso de", não "para o dia a dia".** Chaves de API e Informação do PHP são superfícies de solução de problemas; uma instância saudável raramente precisa de qualquer uma delas.
- **Implantar é colocar novo código no lugar; a instância atualiza a própria estrutura.** Você não roda migrações à mão.
- **O console é o lugar para configurações, não os arquivos.** Se você se pegar querendo editar um arquivo para mudar como a instância se comporta, confira *Configurações globais* primeiro; a configuração provavelmente está lá.
