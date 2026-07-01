# Auto-inscrição de editoras

Além de criar contas à mão, uma instância pode deixar as pessoas se **inscreverem por conta própria** como editoras. Isso vem desativado por padrão. Quando você o ativa, uma visitante pode solicitar uma conta de editora por um formulário, confirmar o e-mail e começar a editar, sem que você crie a conta antes. Este capítulo cobre quando usar e cada interruptor que o governa.

A auto-inscrição é configurada no console de administração (as configurações de auto-inscrição; na maioria das instâncias elas ficam junto dos outros controles de conta). O recurso inteiro é uma única decisão com vários botões: *pessoas estranhas devem poder se tornar editoras aqui, e sob quais limites?*

## Quando usar

Ative para uma chamada aberta: um arquivo comunitário convidando colaboradoras, um curso onde estudantes se registram sozinhas, um projeto público que quer uma barreira baixa para quem quer ajudar. Deixe desativado para uma instância fechada onde cada editora deve ser alguém que você adicionou deliberadamente. Você pode ativar por um tempo (a duração de um curso, o período de uma chamada) e desativar de novo; as contas existentes não são afetadas quando você o faz.

## Ativar

O controle de auto-inscrição tem um interruptor principal. Enquanto está desativado, o formulário de inscrição fica fechado: quem o alcança vê um aviso de que a inscrição não está aberta, e o link de inscrição fica oculto na tela de login. Enquanto está ativado, o formulário fica aberto e o link aparece.

Ativá-lo revela os limites abaixo. Defina-os antes de anunciar a chamada, não depois.

## Os limites

- **Teto.** Um número máximo de editoras auto-inscritas. Uma vez atingido o teto, o formulário se fecha sozinho e o link de inscrição desaparece até você elevar o teto ou remover algumas contas. Use-o para evitar que uma chamada aberta fuja do seu controle. O teto conta editoras auto-inscritas, não contas que você mesma criou.
- **Limite de domínios de e-mail.** Uma lista opcional de domínios de e-mail que podem se inscrever (por exemplo, o domínio de uma universidade para um curso). Quando definida, só endereços nesses domínios podem completar a inscrição; qualquer outro é recusado. Deixe vazia para permitir qualquer endereço.
- **Nomeação da galáxia pessoal.** Quando alguém se inscreve, Telaris pode criar uma **galáxia pessoal** para essa pessoa trabalhar. Você escolhe como ela é nomeada: a partir do nome completo, ou só do primeiro nome. Só o primeiro nome é o padrão que preserva a privacidade, porque um nome de galáxia é público; um nome completo em um título de galáxia fica visível a toda visitante. Escolha nomes completos só quando essa exposição for aceitável para o seu contexto.
- **Acesso padrão.** Novas editoras auto-inscritas podem receber assentos em galáxias de demonstração, somente leitura ou leitura e escrita, para chegarem com algo para olhar ou trabalhar. *Controle de acesso de edição* explica os assentos.

## Como uma editora auto-inscrita entra

Uma editora auto-inscrita **não tem senha**. Ela entra toda vez pelo link por e-mail: digita o endereço, recebe um link de uso único, segue-o. É por isso que o e-mail precisa estar configurado para a inscrição funcionar; se a instância não pode enviar e-mail, ninguém consegue confirmar uma inscrição nem entrar depois. O capítulo *Configurações globais* cobre o e-mail.

Como a inscrição depende inteiramente do e-mail, o fluxo é: a pessoa envia o formulário, Telaris lhe escreve para confirmar que o endereço é dela, e só depois que ela segue essa confirmação é que passa a ser uma editora de verdade. Uma inscrição não confirmada ainda não é uma conta e é limpa automaticamente se nunca for confirmada.

## Verificação

Uma editora auto-inscrita pode editar assim que confirma o e-mail; você não precisa aprová-la antes. A **verificação** é um passo separado e opcional que diz "eu reconheço esta pessoa". Quando você verifica uma conta:

- a pessoa pode definir uma senha, deixando de ficar limitada aos links por e-mail, e
- Telaris avisa a ela que foi verificada.

A verificação **não** condiciona a edição. Uma editora auto-inscrita não verificada já é uma editora plena; a verificação é uma marca de reconhecimento e uma conveniência (a senha), não uma permissão. As contas não verificadas ficam destacadas na lista de contas para que você veja num relance quem entrou mas ainda não foi reconhecida.

## Manter seguro

- **Um teto é a sua válvula de segurança.** Um formulário aberto sem teto pode ser inundado. Defina um teto com que você se sinta confortável moderando, e eleve-o deliberadamente.
- **O limite de domínios delimita a chamada.** Para um curso ou uma organização, um limite de domínios de e-mail transforma "qualquer pessoa" em "qualquer pessoa daqui", que costuma ser o que você de fato quis dizer.
- **Primeiro nome por padrão.** A menos que você tenha um motivo em contrário, mantenha a nomeação da galáxia pessoal no primeiro nome, para que o nome completo de ninguém vire um título de galáxia público sem seu aval.
- **Desative quando a chamada terminar.** Uma inscrição deixada aberta indefinidamente é um convite permanente que você pode ter esquecido. Feche-a quando o motivo de tê-la aberto passar; as contas já feitas permanecem.
