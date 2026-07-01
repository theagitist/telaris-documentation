# Usuárias

A aba **Usuárias** é onde vive toda conta da instância. Este capítulo cobre as contas que você mesma cria; o próximo cobre as contas que as pessoas criam por conta própria via auto-inscrição, que compartilha a mesma lista.

![A aba Usuárias: uma tabela de contas com nome, e-mail, função e ações por linha](assets/images/admin-manual-pt/02-users-list.png)

## A lista de contas

A lista mostra toda conta: administração e edição juntas. De cada conta você vê o nome, o endereço de e-mail, a função e, quando relevante, se ela foi verificada (o próximo capítulo explica a verificação). Uma contagem no cabeçalho informa quantas contas existem.

Cada conta tem um menu de ações de linha para editar e remover, descrito abaixo.

## Funções

Telaris tem duas funções:

- **Editora.** Pode entrar e criar conteúdo, dentro de qualquer acesso que tenha recebido (veja *Controle de acesso de edição*). Não pode alcançar o console de administração.
- **Administradora.** Pode fazer tudo o que uma editora faz, e pode alcançar o console de administração. Conceda esta função com parcimônia; toda administradora pode mudar configurações, ler toda conta e remover conteúdo.

A função de uma conta é definida quando você a cria e pode ser alterada ao editar a conta.

## Criar uma conta

Selecione **Nova conta**. Um formulário pede o nome da nova conta, o endereço de e-mail, a função e, opcionalmente, uma senha.

- **Nome** é como a pessoa é apresentada, e o nome que as galáxias próprias de uma editora recebem se você usar as convenções de nomeação do próximo capítulo.
- **E-mail** é a identidade da conta e o endereço para o qual Telaris escreve (links de acesso, notificações). Precisa ser único na instância.
- **Função** é editora ou administração, como acima.
- **Senha** é opcional. Se você definir uma, a pessoa pode entrar com ela. Se deixar em branco, a conta entra pelo link por e-mail sem senha descrito abaixo. Muitas administradoras deixam em branco e deixam as pessoas usarem links por e-mail, de modo que não há senha para gerenciar nem para vazar.

Salve, e a conta aparece na lista imediatamente.

## Acesso sem senha

Contas de Telaris não precisam de senha. Uma conta sem senha entra pedindo um link por e-mail: a pessoa digita o e-mail na página de login, Telaris envia um link de uso único, e segui-lo faz o login. É o mesmo mecanismo que uma editora auto-inscrita usa.

Para isso funcionar, a instância precisa conseguir enviar e-mail. Se o e-mail não estiver configurado, os links por e-mail não podem ser entregues e as contas sem senha não conseguem entrar. O capítulo *Configurações globais* cobre configurar o e-mail e o aviso que o console mostra quando ele não está definido.

## Editar uma conta

Abra o menu de ações de uma linha e escolha **Editar** para mudar o nome, o e-mail, a função, a senha ou o estado de verificação de uma conta. As mudanças salvam como uma única operação; se você mudar vários campos de uma vez, todos entram em vigor juntos.

Mudar o e-mail de uma conta muda o endereço para o qual Telaris escreve e a identidade com que a pessoa entra. Mudar a função de editora para administração concede acesso ao console imediatamente; mudar no sentido contrário o remove.

## Importação em lote

Quando você precisa criar muitas contas de uma vez (uma turma, um grupo, um coletivo de trabalho), use a **Importação em lote**. Ela recebe uma lista de contas, tipicamente como um CSV com uma coluna para cada campo (nome, e-mail, função), e as cria de uma só vez. Contas cujo e-mail já existe são reportadas em vez de duplicadas, então reexecutar uma importação é seguro.

A importação em lote é a ferramenta certa para dar entrada a um grupo conhecido. Para um grupo que você não conhece de antemão (uma chamada aberta a colaboradoras), a auto-inscrição, no próximo capítulo, encaixa melhor.

## Remover uma conta

Escolha **Excluir** no menu de ações de uma linha. Telaris confirma primeiro, porque remover uma conta é permanente.

Se a conta possui uma **galáxia pessoal** (uma galáxia criada para aquela editora, segundo as convenções de nomeação do próximo capítulo), Telaris pergunta o que fazer com ela: remover a galáxia junto com a conta, ou manter a galáxia e seu conteúdo no lugar. Excluir a conta nunca apaga conteúdo silenciosamente; você é sempre consultada. Mantenha a galáxia quando o conteúdo deve sobreviver ao acesso da pessoa; remova-a quando a conta e sua galáxia eram uma coisa descartável (uma conta de teste, uma demonstração de curso).

## Coisas que vale a pena saber

- **Não há como ver uma senha.** As senhas são armazenadas de modo que nem você consegue lê-las de volta. Se alguém esquecer a sua, ou limpe-a (para que use links por e-mail) ou defina uma nova; você não pode recuperar a antiga.
- **Uma administradora pode ver toda conta e toda galáxia.** A privacidade que limita as editoras ao próprio trabalho não se aplica a você. Trate a lista, e o conteúdo por trás dela, com a discrição que o acesso implica.
- **Excluir a última conta de administração te trancaria para fora.** Telaris não vai deixar a instância sem nenhuma administração; mantenha ao menos uma conta de administração em que você consiga entrar antes de remover outras.
