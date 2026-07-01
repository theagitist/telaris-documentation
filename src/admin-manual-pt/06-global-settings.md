# Configurações globais

A aba **Configurações globais** guarda os interruptores de toda a instância: como a instância se chama, qual galáxia recebe quem visita, qual o tamanho máximo de um envio, como as palavras-chave correspondem, como envia e-mail, em qual endereço responde, para qual idioma recorre por padrão, e se as editoras estão sequer habilitadas. Essas configurações são armazenadas no próprio banco de dados da instância, então você as muda aqui no console, e não editando arquivos no servidor.

![A aba Configurações globais: o nome da instância, a galáxia padrão, o limite de envio, o interruptor de correspondência aproximada, e (abaixo) as configurações de e-mail e do site](assets/images/admin-manual-pt/07-global-settings.png)

## Aspectos básicos da instância

O topo da aba reúne os fatos simples sobre a instância:

- **Nome.** O nome público da instância. Aparece do lado visitante e vira o rótulo da instância no diretório do Pluriverse se você solicitar publicação (capítulo 7). Em branco, assume por padrão a primeira parte do nome de host.
- **Galáxia padrão.** Qual galáxia quem visita vê na raiz do site, antes de escolher uma. Escolha a galáxia que deve ser a porta de entrada.
- **Tamanho máximo de PDF (MB).** O maior PDF que um buraco de minhoca pode carregar, em megabytes (25 por padrão). Quem edita e envia um arquivo maior é avisado de que o arquivo excede o limite. Aumente-o se seu conteúdo precisar e seu servidor tiver espaço.
- **Correspondência aproximada de palavras-chave.** O interruptor de toda a instância para a correspondência flexível descrita em *Galáxias e aglomerados*: quando ligado, grafias próximas conectam entre galáxias, não só palavras idênticas. Desligado por padrão. Um aglomerado pode sobrepor esse padrão nas próprias configurações.


## Configurações de e-mail

Quase tudo o que Telaris envia por e-mail, links de acesso, confirmações de inscrição, notificações, depende de a instância conseguir enviar e-mail. O formulário de configurações de e-mail é onde você prepara isso:

- **Host SMTP** e **porta** do seu retransmissor de e-mail.
- **Usuário** e **senha** do retransmissor.
- **Criptografia** (tipicamente TLS).
- **Endereço de remetente** e **nome de remetente** que os destinatários veem.

Dois auxílios acompanham o formulário:

- Um botão **Enviar email de teste** manda uma mensagem de teste a um endereço que você informa, para você confirmar que as configurações funcionam antes de depender delas.
- Um **aviso de não configurado**. Enquanto o e-mail não está preparado, o console mostra um aviso, e os lugares que dependem de e-mail (as configurações de auto-inscrição, por exemplo) o repetem, porque ligar um recurso que precisa de e-mail enquanto o e-mail está quebrado só produz falhas silenciosas.

Se o e-mail não estiver configurado, as contas sem senha não conseguem entrar e a auto-inscrição não pode funcionar, porque ambas dependem de links enviados por e-mail. Configure o e-mail antes de ligar qualquer uma das duas.

> [!important] A senha do e-mail é o único segredo aqui
> A senha SMTP é o único valor sensível nessas configurações. Telaris a trata de forma especial: ela nunca é incluída em nenhum backup, snapshot ou exportação de federação. Isso significa que é seguro compartilhar um backup, mas também que restaurar uma instância em outro lugar não leva a senha; você a redigita depois de uma restauração. O capítulo *Backups e snapshots* retoma isso.

## Configurações do site

Estas informam à instância sobre si mesma:

- **Nome de host da instância** e **URL base**: o endereço em que a instância é alcançada. Telaris os usa para construir os links que coloca nos e-mails, para que eles apontem ao lugar certo independentemente de como uma dada requisição chegou. Defina-os com o seu endereço público real.
- **Idioma padrão**: o idioma que uma visitante vê antes de qualquer escolha própria, um entre inglês, espanhol, português ou francês. Defina-o com o idioma do seu público.

Definir aqui o nome de host e a URL base significa que você não precisa editar à mão arquivos de configuração para deixar os links de e-mail corretos; o console é a fonte da verdade para eles.

## Os interruptores da instância

Um interruptor aqui decide um recurso inteiro da instância:

- **Permitir edição.** A ponta de instância da cascata de edição (veja *Controle de acesso de edição*). Desligue-o para congelar toda a edição na instância de uma vez, por exemplo quando um projeto terminou, mantendo cada conta e tudo o que foi criado. Ligado por padrão.

## Coisas que vale a pena saber

- **Estas configurações vivem no banco de dados, não em um arquivo.** Mudá-las aqui tem efeito sem tocar no servidor. Elas também prevalecem sobre os valores de reserva embutidos no arquivo de configuração da instância, então o console é onde você deve mudá-las.
- **Teste o e-mail depois de qualquer mudança.** O botão Enviar email de teste existe para que você nunca descubra um retransmissor quebrado por meio de uma editora que não conseguiu entrar. Use-o sempre que tocar nas configurações de e-mail.
- **O endereço de remetente deve ser um endereço real, autorizado a enviar, no seu domínio.** Retransmissores e destinatários rejeitam cada vez mais e-mails cujo endereço de remetente não está autorizado a enviar; defina-o como algo que o seu retransmissor tem permissão de enviar.
