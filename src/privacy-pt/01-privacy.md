# Privacidade

Telaris é um arquivo de conhecimento decolonial de grau investigativo. Este aviso se aplica a **www.telaris.ca** (o site que você está lendo) e ao **software de Telaris** que roda em instâncias operadas por pessoas independentes. Cada instância é operada por uma pessoa independente e pode carregar avisos de privacidade adicionais próprios que governam o conteúdo daquela instância; este aviso cobre o resto.

## O que www.telaris.ca coleta

O site em `www.telaris.ca` é um pequeno conjunto de páginas informativas estáticas. Não executa nenhuma ferramenta de análise, não coloca rastreadores publicitários, não instala cookies e não coleta informação pessoal de quem o visita. O site é servido através de Cloudflare; os registros padrão de acesso de Cloudflare (IP truncado, agente de usuário, URL solicitada, status de resposta, carimbo de tempo) são mantidos por pouco tempo segundo a política da própria Cloudflare. Além desses registros de borda, o site não registra visitas.

O site faz link para documentos baixáveis e para instâncias independentes de Telaris. Seguir um desses links leva você a outro site; este aviso não governa o que acontece lá.

## O que uma instância de Telaris coleta

Qualquer site que rode o software de Telaris pode coletar uma pequena quantidade de informação necessária para que o software funcione:

- **Contas de edição.** Cada instância mantém uma lista de quem está autorizado a adicionar conteúdo. De cada pessoa editora guarda um nome, um e-mail, pronomes opcionais e carimbos de tempo de início de sessão, enquanto a conta estiver ativa. Uma conta também pode ter um hash de senha, mas a senha é opcional: em vez disso, uma pessoa editora pode entrar por um link de uso único enviado por e-mail a cada vez, e nesse caso nenhuma senha é guardada. Veja *Suas informações e o que você pode solicitar como pessoa editora* mais abaixo.
- **Cadastro autônomo (apenas se quem opera ativar).** Algumas pessoas operadoras abrem a sua instância ao cadastro autônomo de pessoas editoras. Quando está ativado, qualquer pessoa pode solicitar uma conta de edição informando um nome e um e-mail; o e-mail é confirmado por um link de uso único antes de a conta poder ser usada. Uma solicitação que nunca é confirmada é removida automaticamente após um curto período. O cadastro autônomo fica desativado a menos que quem opera decida ativá-lo; na maioria das instâncias as contas de edição continuam sendo criadas por quem opera.
- **Conteúdo editorial.** Os buracos de minhoca, as galáxias, as palavras-chave, as descrições, os arquivos enviados e as relações entre eles são guardados em cada instância. É o conteúdo que quem visita vê. A soberania editorial é o princípio: quem edita decide o que se publica, e nada é revisado antes de ser mostrado.
- **Consentimento da comunidade de origem.** Quando uma comunidade de origem contribui com material, o consentimento dessa comunidade governa o material. A retirada do consentimento é definitiva e a instância a acata sem negociação.
- **Registros de acesso do servidor.** Uma instância pode manter registros de acesso de curta duração para fins operacionais, como depuração e mitigação de abuso. Quando o software registra um endereço IP (por exemplo no seu registro de auditoria de ações), cabe a quem opera decidir por quanto tempo conservá-lo; o software aplica um hash aos IPs com uma chave do servidor quando pode, e não conserva IPs em texto claro nas suas próprias tabelas.

## Suas informações e o que você pode solicitar como pessoa editora

Se você tem uma conta de edição em uma instância, seja porque quem opera a criou para você ou porque você se cadastrou por conta própria, o seguinte se aplica a você.

- **Por que guardamos os seus dados: porque você aceitou.** Antes de poder usar o editor, é pedido que revise estes documentos e os aceite: no seu primeiro início de sessão se quem opera criou a sua conta, ou no momento do cadastro se você se juntou por conta própria. A sua aceitação é registrada junto com a versão de cada documento, de modo que uma revisão posterior pede de novo. Você pode retirar o seu consentimento a qualquer momento.
- **O que é guardado sobre você:** o seu nome, o seu e-mail, os pronomes que você informar, carimbos de tempo de início de sessão, o conteúdo editorial que você publica e um registro de auditoria das ações administrativas que você realiza (no qual o seu e-mail é guardado apenas como um hash com sal, nunca em claro). Se você usa senha, o seu hash é guardado; se em vez disso você entra por links enviados por e-mail, nenhuma senha é guardada. Os tokens de acesso de uso único e de curta duração (para os links por e-mail que iniciam a sua sessão, confirmam um cadastro ou permitem definir uma senha) são guardados apenas como hashes, e apenas até serem usados ou expirarem.
- **O que você pode solicitar:** você pode pedir a quem opera a sua instância que mostre os dados que tem sobre você, que os corrija ou que apague a sua conta e o seu conteúdo. Você pode retirar o consentimento, o que remove o seu acesso e, se você pedir, o seu conteúdo. Quem opera a sua instância atende a esses pedidos; eles não são negociados, e a eliminação é definitiva.
- **Conservação:** os dados da conta são mantidos enquanto a conta estiver ativa e removidos quando você pede. O registro de auditoria de ações é mantido por um período limitado definido por quem opera (o padrão é 365 dias) por motivos de prestação de contas, e depois é depurado.

## Registros e conservação entre instâncias

O software de Telaris não faz nenhuma promessa geral sobre a conservação de registros, porque a rotação de registros vive na infraestrutura própria de cada pessoa operadora (o seu servidor web, o seu sistema operacional, o seu provedor de borda). O que é constante em toda parte é isto: a **aplicação** não registra a atividade de navegação de quem visita. O único dado pessoal de visita que existe é o endereço IP que fica nos registros próprios do servidor ou da borda de quem opera, regido pela conservação que essa pessoa definir.

As instâncias operadas pela Polivoxia rotacionam os seus registros de servidor aos 14 dias; é um valor recomendado, não uma promessa que obrigue outras pessoas operadoras. Cada uma define a sua própria conservação e é responsável por ela, e recomendamos uma conservação curta ou a anonimização de IP como a postura mais coerente com os valores deste projeto.

## O que Telaris não faz

- **Sem publicidade.** Sem rastreadores de terceiros, sem rede publicitária, sem perfilamento de comportamento.
- **Sem treinamento nem análise de IA sobre o corpus.** O conteúdo de Telaris não é usado para treinar nem alimentar modelos de IA, nem interna nem externamente.
- **Sem varredura de conteúdo por terceiros.** O conteúdo não é enviado a serviços externos para moderação ou classificação.
- **Sem venda de dados.** As contas de edição, o conteúdo e os registros nunca são vendidos nem compartilhados com terceiros para fins publicitários ou comerciais.

## Federação e conteúdo entre instâncias

Quando as instâncias de Telaris se federam, o conteúdo que uma pessoa editora publica explicitamente para uma instância parceira viaja até essa instância sob assinaturas criptográficas. A instância receptora hospeda uma réplica; a instância de origem mantém a soberania e pode retratar o conteúdo, o que remove a réplica.

As contas de edição e os e-mails de quem opera **não** cruzam os limites da federação. A comunicação entre pessoas operadoras passa por um relé que oculta os e-mails dos dois lados.

## Retirada do consentimento

Uma comunidade de origem, uma pessoa editora ou qualquer pessoa cujo material esteja hospedado em uma instância de Telaris pode retirar o seu consentimento a qualquer momento. Quem opera essa instância é responsável por acatá-lo. A retirada remove o material; não requer negociação; é definitiva.

## Contato

Para perguntas sobre uma instância específica, contate quem a opera, cujo endereço consta no site da própria instância. Para perguntas sobre www.telaris.ca, sobre o software em si ou sobre este aviso, use a página de [Contato](https://www.telaris.ca/contact); a governança do projeto e a pessoa operadora a quem contatar sobre como os dados são tratados são descritas na página de [Governança](https://www.telaris.ca/governance).

## Versão

Versão 1.0, em vigor desde 2026-06-04. É a primeira versão publicada; substitui o rascunho anterior. Quando este aviso mudar de uma forma que afete quem edita, a versão é incrementada e é pedido que se revise a nova versão no próximo início de sessão.
