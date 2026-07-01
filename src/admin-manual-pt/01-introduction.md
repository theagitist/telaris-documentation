# Introdução

Este manual é para quem administra uma instância de Telaris: a administradora. Uma administradora não é o mesmo que uma editora. Uma editora cria galáxias, buracos de minhoca e conexões dentro do arquivo; uma administradora decide quem pode editar, como a instância se comporta, se e como ela se conecta a outras instâncias, e como seus dados são mantidos em segurança. Se o seu trabalho diário é criar conteúdo, o Manual do editor é o seu livro; este é para as superfícies que uma editora nunca vê.

## Três papéis

Ajuda manter três papéis distintos, porque este manual, o Manual do editor e o dia a dia de operar uma rede de Telaris falam cada um a um deles.

- **Editora.** Alguém com uma conta de editora na sua instância. Faz login, cria conteúdo e vê apenas a superfície de edição. O Manual do editor é escrito para essa pessoa.
- **Administradora (você).** Alguém com uma conta de administração na sua instância. Você alcança o **Console de administração** e gerencia contas, galáxias, configurações, backups e a participação da sua instância na rede mais ampla. Este manual é escrito para você.
- **Operadora do Pluriverse.** A pessoa que opera o site central de coordenação (o Pluriverse) através do qual uma família de instâncias se federa. Grande parte desse trabalho é o mesmo console de administração que você já conhece; as partes específicas de operar o Pluriverse estão reunidas no capítulo de federação. Em uma rede pequena, a administradora e a operadora do Pluriverse costumam ser a mesma pessoa.

Uma única conta pode, claro, ser ao mesmo tempo de edição e de administração. A distinção é sobre *superfícies*, não sobre pessoas: o console de administração é um lugar separado da tela inicial da editora, alcançado à parte, e este manual é o seu guia para ele.

## Como alcançar o Console de administração

O Console de administração fica no caminho `/admin` da sua instância (por exemplo, `https://sua-instancia.exemplo.org/admin`). Você precisa estar autenticada com uma conta que tenha a função de administração; uma conta de edição comum que abra `/admin` é recusada.

No alto do console há uma fileira de abas. Cada uma é um capítulo deste manual:

- **Galáxias** e **Aglomerados**: a visão da administradora de todo o conteúdo da instância, incluindo conteúdo importado de outros lugares. Coberto em *Galáxias e aglomerados*.
- **Usuárias**: toda conta na instância, e as ferramentas para criar, editar, verificar e remover. Coberto em *Usuárias* e *Auto-inscrição de editoras*.
- **Backup** e **Snapshots**: fazer e restaurar cópias da instância inteira. Coberto em *Backups e snapshots*.
- **Configurações globais**: o email, o próprio endereço da instância, o idioma padrão, e o interruptor de instância para editoras. Coberto em *Configurações globais*.
- **Pluriverse**: a participação da sua instância em uma federação de instâncias. Coberto em *Federação e o Pluriverse*.
- **Chaves de API** e **Informação do PHP**: detalhes operacionais e diagnósticos. Coberto em *Manutenção e diagnóstico*.

## O que este manual pressupõe

Ele pressupõe que a instância já está instalada e em funcionamento, e que você consegue entrar como administradora. Não cobre instalar Telaris em um servidor do zero; isso é uma questão do método de implantação que você escolheu (um checkout direto, uma imagem de contêiner, ou uma instância hospedada provisionada para você), e o README do repositório de código é a referência para isso. O que este manual cobre é tudo o que você faz *depois* que a instância está no ar: operá-la bem, mantê-la segura e decidir quão aberta ela é.

## Uma nota sobre idioma e termos

O console, como o resto de Telaris, é totalmente traduzido. As telas mostradas aqui estão em inglês; o seu console pode estar em espanhol, português ou francês, e os rótulos diferem de acordo. Onde este manual nomeia um controle, ele nomeia o rótulo em português; encontre o mesmo controle no seu idioma pela sua posição, que é a mesma em todos os idiomas.

Telaris também mantém uma separação deliberada entre as palavras que visitantes e editoras leem e as palavras que o código usa. Você verá *galáxia*, *buraco de minhoca* e *portal* na interface; os dados subjacentes os chamam de *constellation*, *node* e *portal*. Este manual usa as palavras da interface por toda parte. O glossário no fim reúne os termos que uma administradora encontra.
