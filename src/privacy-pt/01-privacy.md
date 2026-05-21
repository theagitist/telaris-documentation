# Privacidade

> [!warning] Rascunho
> Este documento é provisório. Está em curso uma versão final do aviso de privacidade que substituirá este rascunho. Para perguntas no intervalo, escreva a quem mantém a instância que você está usando.

Telaris é um arquivo de conhecimento decolonial de grau investigativo. A postura de privacidade descrita aqui se aplica a **www.telaris.ca** (o site que você está lendo) e ao **software de Telaris** que roda em instâncias operadas por pessoas independentes. Cada instância é operada por uma pessoa independente e pode carregar avisos de privacidade adicionais próprios; esses avisos governam o conteúdo da instância. Este documento cobre o resto.

## O que www.telaris.ca coleta

O site em `www.telaris.ca` é uma única página estática. Não executa uma ferramenta de análise, não coloca rastreadores publicitários, não instala cookies, e não coleta informação pessoal das visitantes. A página é servida através de Cloudflare; os registros padrão de acesso de Cloudflare (IP truncado, agente de usuário, URL solicitada, status de resposta, carimbo de tempo) são mantidos por períodos curtos segundo a política da própria Cloudflare. Além desses registros de acesso, o site não registra visitas.

O site faz link para PDFs baixáveis e para instâncias independentes de Telaris. Seguir um desses links leva a outra página; este aviso não governa o que acontece lá.

## O que as instâncias de Telaris podem coletar

As instâncias individuais (qualquer site que rode o software de Telaris, incluindo as três listadas em *Instâncias ativas* na página inicial) podem coletar uma pequena quantidade de informação necessária para que o software funcione:

- **Contas de edição.** Cada instância mantém uma lista de pessoas autorizadas a adicionar conteúdo. O nome da editora, seu e-mail e um hash de senha são armazenados enquanto a conta estiver ativa. Quem opera a instância pode remover contas de edição mediante solicitação.
- **Conteúdo editorial.** Os buracos de minhoca, galáxias, palavras-chave, descrições, mídias enviadas, e as relações entre todos eles são armazenados por cada instância. Esse é o conteúdo que a visitante vê. A soberania editorial é o princípio: a editora decide o que é publicado; nada é revisado antes de aparecer.
- **Consentimento da comunidade de origem.** Quando uma comunidade de origem contribui com material a uma instância, o consentimento dessa comunidade governa o material. A retirada do consentimento é definitiva e é executada por quem opera a instância sem negociação.
- **Registros de acesso do servidor.** As instâncias podem manter registros de acesso de curta duração para fins operativos (depuração, mitigação de abusos). Os endereços IP, quando armazenados, são processados com uma chave do servidor (hash); IPs em texto claro não são retidos.

## O que Telaris não faz

- **Sem publicidade.** Sem rastreadores de terceiros, sem rede de publicidade, sem perfilamento comportamental.
- **Sem treinamento de IA sobre o corpus.** O conteúdo de Telaris não é usado para treinar modelos de IA, nem interna nem externamente.
- **Sem varredura de conteúdo por terceiros.** O conteúdo não é enviado a serviços externos para moderação ou classificação.
- **Sem venda de dados.** As contas de edição, o conteúdo e os registros de acesso não são vendidos nem compartilhados com terceiros para fins publicitários ou comerciais.

## Federação e conteúdo entre instâncias

Quando as instâncias de Telaris se federam (uma funcionalidade prevista, ainda não ativa no momento deste rascunho), o conteúdo que uma editora publica explicitamente para um parceiro de federação viaja para a instância desse parceiro sob assinaturas criptográficas. A instância receptora hospeda um espelho do conteúdo; a instância de origem mantém sua soberania.

As contas de edição e os e-mails de quem opera **não** cruzam as fronteiras da federação. A comunicação entre quem opera é mediada por um relé que oculta os endereços de e-mail nos dois lados.

## Retirada do consentimento

Uma comunidade de origem, uma editora, ou qualquer pessoa cujo material esteja hospedado em uma instância de Telaris pode retirar o consentimento a qualquer momento. Quem opera a instância é responsável por honrar a retirada. A retirada remove o material; não exige negociação; é definitiva.

## Contato

Cada instância de Telaris lista o endereço de contato de quem a opera no site da própria instância. Use esse canal para perguntas de privacidade específicas de uma instância. Para perguntas sobre www.telaris.ca, sobre o software em si, ou sobre este aviso, contate quem mantém o projeto na página **/governance** (em breve).

## Versão

Rascunho, 2026-05-21. Não substitui uma versão anterior. Será revisado antes de sua publicação definitiva.
