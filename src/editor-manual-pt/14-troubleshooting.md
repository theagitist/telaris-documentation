# Resolução de problemas

As situações cotidianas em que uma editora se encontra, o que tentar, e quando perguntar à operadora. Este capítulo está organizado pelo sintoma, não pela causa; procure pelo que *você* vê, não pelo que está *tecnicamente* acontecendo.

## Não consigo entrar

**O que você vê**: o formulário de login recusa suas credenciais, ou você cai na página de login quando esperava já estar autenticada.

**O que tentar**, em ordem:

1. Confirme se o endereço de e-mail e a senha estão corretos. Ambos diferenciam maiúsculas de minúsculas.
2. Use o link **Esqueceu a senha?** abaixo do botão **Entrar**. Um e-mail com link de redefinição chega em menos de um minuto.
3. Verifique se você está no endereço da sua instância. Se sua operadora opera várias instâncias, seu login se aplica a uma só.

**Quando perguntar à sua operadora**: se o link de redefinição não chegar (cheque o spam antes), se o e-mail de redefinição volta como rejeitado, ou se você tem certeza de que a senha está correta e o formulário ainda recusa.

## Um buraco de minhoca que criei sumiu

**O que você vê**: um buraco de minhoca que você compôs já não está na lista.

**O que tentar**:

1. Confirme que o menu suspenso **Galáxia atual** está na galáxia certa (ou em *Todas as minhas galáxias*). O buraco de minhoca pode estar em uma galáxia diferente da esperada, especialmente se você usou o menu **Galáxia destino** dentro do modal do buraco de minhoca.
2. Use a caixa de busca da tela inicial da editora. Busque pelo nome do buraco de minhoca; se ele existe em qualquer galáxia que você pode editar, a busca encontra.
3. Verifique o filtro **Modificados hoje**; se você clicou nele sem querer, só as edições de hoje aparecem.

**Quando perguntar à sua operadora**: se a busca em **Todas as minhas galáxias** não retorna nada e você tem certeza de que salvou o buraco de minhoca. Ele pode ter sido apagado (por você, ou por outra editora); sua operadora talvez possa restaurar a partir de um snapshot.

## Não consigo editar um buraco de minhoca; o modal abre em modo de visualização

**O que você vê**: clicar na linha do buraco de minhoca abre um cartão de informações ou uma prévia somente leitura, não o modal de edição.

**O que você pode estar vendo**:

- O buraco de minhoca está em uma galáxia à qual você tem **acesso de leitura**, mas não de edição (algumas instâncias permitem que editoras vejam todas as galáxias mas só editem algumas). O buraco de minhoca é editável por outra editora.
- O buraco de minhoca foi **importado** de uma fonte externa (um arquivo irmão, uma comunidade ligada por bridge). Buracos de minhoca importados são somente leitura por design; mudanças devem acontecer na fonte.

**Quando perguntar à sua operadora**: se o buraco de minhoca foi composto nesta instância e você deveria ter direitos de edição, mas o modal ainda abre somente leitura.

## Um upload falha

**O que você vê**: o seletor de arquivo aceita o arquivo, o upload começa, e então aparece um erro, ou o modal fecha sem o arquivo anexado.

**O que tentar**:

1. Verifique o tamanho do arquivo. PDFs costumam ser limitados a 25 MB (sua operadora pode ter ajustado para outro valor); imagens e vídeos podem ter seus próprios limites.
2. Verifique o tipo do arquivo. Telaris suporta JPG e PNG (e a maioria dos formatos comuns) para imagens; MP4 para vídeo; MP3, OGG, e WAV para áudio; PDF para documentos. Arquivos de outros tipos são rejeitados no momento do upload.
3. Tente um arquivo menor ou outro formato. Se o original for grande demais, comprima ou transcodifique antes do upload.

**Quando perguntar à sua operadora**: se uploads falham consistentemente para arquivos dentro dos limites informados, ou se você precisa que o limite seja elevado.

## O chip de uma palavra-chave está no lugar errado na tela

**O que você vê**: um chip na tela de palavras-chave está sobreposto a outro, fora da área visível, ou flutuando em uma posição que não corresponde a onde você lembra de ter posto.

**O que tentar**:

1. Arraste o chip para onde você quer; a nova posição salva automaticamente.
2. Se muitos chips estão mal arranjados, use a opção **Redefinir todas as posições dos chips** no painel de ajuda da tela (o **?** no topo da tela).
3. Atualize a página; a tela busca o layout mais recente.

**Quando perguntar à sua operadora**: raramente. A tela é tolerante; quase todo problema se resolve arrastando.

## Uma mudança que fiz não aparece na vista da visitante

**O que você vê**: você salvou uma mudança na superfície de edição, mas uma visitante (ou você em outra aba) não a vê.

**O que tentar**:

1. Atualize a aba da visitante. Telaris não empurra atualizações ao vivo; a mudança chega no próximo carregamento da página.
2. Verifique se você salvou (com o botão de salvar do modal), e não fechou o modal com **Cancelar** ou clicando fora.
3. Verifique se você está olhando a mesma galáxia. A aba da visitante pode estar em uma galáxia diferente da que você editou.

**Quando perguntar à sua operadora**: se você salvou e atualizou e a mudança ainda não aparece depois de um minuto. Caches de borda podem levar um instante para invalidar; se persiste, é território da operadora.

## Um botão está desabilitado

**O que você vê**: um botão na tela inicial da editora ou em um modal está visível mas não clicável.

**O que você pode estar vendo**:

- O botão é **condicional a algo que você ainda não fez**. Por exemplo, o botão **Configurações** ao lado do seletor de galáxia só habilita quando uma galáxia específica está selecionada (não em *Todas as minhas galáxias*).
- O botão é **restrito pelo seu papel**. Se você é editora e a ação é só para administradoras, o botão pode aparecer mas permanecer desabilitado.

**Quando perguntar à sua operadora**: se você acredita que deveria ter acesso à ação e o botão ainda está desabilitado. Seu papel pode precisar de ajuste.

## Minha sessão expirou no meio de uma edição

**O que você vê**: um save falha com uma mensagem "unauthenticated" ou "please log in"; a superfície de edição te devolve à página de login.

**O que tentar**:

1. Faça login de novo. Sua sessão expira periodicamente; é normal.
2. Se você estava editando um buraco de minhoca quando a sessão expirou e a mudança não foi salva, talvez tenha perdido o trabalho desde o último save. O texto no modal às vezes é recuperável pelo comportamento de form-restore do navegador; se não, o buraco de minhoca volta ao último estado salvo.

**Quando perguntar à sua operadora**: se as sessões expiram com frequência incomum. A sessão padrão dura 30 dias com renovação por atividade; se você é deslogada em minutos, algo está estranho.

## Uma mensagem que mandei para outra editora parece perdida

**O que você vê**: você enviou uma mensagem in-app a outra editora (ou a uma operadora de instância) e a destinatária não respondeu, ou você não encontra a mensagem enviada.

**O que você pode estar vendo**:

- A destinatária ainda não abriu a caixa de entrada.
- A superfície de mensagens in-app pode viver em uma seção da interface administrativa à qual você não tem acesso. A maior parte da comunicação entre editoras se faz melhor fora de Telaris (e-mail, Signal, o que sua operadora e a sua equipe combinaram).

**Quando perguntar à sua operadora**: se a mensagem in-app é o canal canônico na sua instância e uma mensagem que você enviou por ela não chega à destinatária.

## Um buraco de minhoca abre um cartão de informações em branco

**O que você vê**: clicar em um buraco de minhoca abre o cartão de informações, mas sem descrição, sem mídia, sem palavras-chave.

**O que tentar**:

1. Verifique se o buraco de minhoca que você abriu é aquele para o qual você queria escrever conteúdo. Buracos de minhoca vazios são permitidos; eles simplesmente não têm corpo.
2. Abra o buraco de minhoca na superfície de edição e confirme que o campo **Descrição** tem o texto que você espera.
3. Se a descrição aparece no editor mas não na vista da visitante, atualize as duas abas do navegador.

**Quando perguntar à sua operadora**: se o buraco de minhoca tem conteúdo no editor mas está em branco na vista da visitante depois de atualizar.

## A cena 3D está lenta ou engasgando

**O que você vê**: a cena 3D da visitante demora a carregar, anima de forma travada, ou congela brevemente.

**O que você pode estar vendo**:

- Uma galáxia densa em um dispositivo mais antigo. A cena 3D roda no navegador da visitante; galáxias muito densas exigem muito de hardware de baixa potência.
- Uma galáxia com muitos buracos de minhoca em modo imagem-como-ícone (cada imagem entra na cena como uma textura).

**O que tentar**:

- Sugira que a visitante alterne para a **vista 2D** (capítulo 10), se estiver habilitada na galáxia.
- Para galáxias que você compõe, considere se todas as marcas image-as-icon são necessárias; uma galáxia com doze buracos de minhoca em imagem-ícone é mais rápida que uma com cinquenta.

**Quando perguntar à sua operadora**: se a lentidão é universal (toda visitante vê) e não específica de um dispositivo.

## Não sei quem opera esta instância

**O que você vê**: este manual fica te dizendo para "perguntar à sua operadora". Se você não sabe quem é, precisa saber.

**O que tentar**:

- Verifique o endereço da sua instância. Muitas instâncias têm uma página de contato em `/contact` ou uma página de governança em `/governance` que nomeia a operadora.
- Olhe o e-mail original que te convidou a ser editora. A remetente é, na maior parte das vezes, a operadora.
- Se nada disso, a próxima editora ou visitante com quem você falar sobre Telaris provavelmente sabe.

Se você não consegue identificar a operadora de jeito nenhum, isso, em si, é um tipo de problema que vale resolver; uma instância sem uma operadora alcançável é uma que vai à deriva.
