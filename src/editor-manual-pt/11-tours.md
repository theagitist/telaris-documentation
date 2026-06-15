# Percursos

Um percurso é um caminho curado por uma galáxia. A editora escolhe o ponto de partida, escolhe a ordem, define um tempo de permanência em cada parada, e decide se o percurso volta ao começo ou termina. As visitantes podem começar o percurso por conta apertando Play; ou o percurso pode rodar sozinho quando a visitante ficar ociosa; ou pode começar no instante em que a visitante chega na galáxia. Este capítulo percorre cada caminho para compor um percurso e as considerações práticas.

Um percurso é **uma configuração de uma galáxia**, não um objeto separado. Ligar o percurso configura os buracos de minhoca existentes para serem visitados em uma ordem escolhida; desligar deixa os buracos de minhoca intactos. Uma galáxia carrega uma configuração de percurso por vez; se você quer dois percursos, publica uma cópia da galáxia com o segundo percurso.

## Onde se compõe

Um percurso vive dentro do modal **Configurações da galáxia**, na seção Discovery (o capítulo 4 apresenta o modal; o capítulo 10 apresenta os interruptores Discovery).

![Modal de configurações da galáxia na seção Discovery](assets/images/editor-manual-pt/12-galaxy-discovery-section.png)

O primeiro interruptor da seção Discovery é **Passeio automático**. Ligá-lo revela os campos de configuração do percurso:

- **Modo de início**.
- **Seleção de nós**.
- **Pausa em nós sem conteúdo** em cada parada.
- **Em loop** ligado / desligado.

Abaixo deles, um botão **Pré-visualizar passeio**.

## Modo de início

Escolha como o percurso começa:

- **Manual**: um pequeno botão **Play** aparece no canto inferior direito da cena 3D da visitante. O percurso começa quando a visitante o aperta. Use quando o percurso é um caminho *oferecido*, não um padrão.
- **Inativo**: o percurso começa automaticamente depois que a visitante fica inativa por um número configurável de segundos. O campo de limite de inatividade aparece abaixo desta opção. Use quando a galáxia for pensada para ser encontrada tanto interativamente (a visitante explora) quanto ambientalmente (a galeria desperta quando ninguém toca).
- **Imediato**: o percurso começa no instante em que a visitante chega na galáxia. A visitante pode parar o percurso a qualquer momento com os controles em cena. Use para galerias cuja experiência pretendida é o próprio percurso; o caminho da editora é a leitura canônica.

Não há resposta certa; cada opção serve a uma intenção editorial diferente. Galáxias autorais geralmente começam em **Manual** e graduam para **Inativo** ou **Imediato** conforme a editora encontra um caminho que vale como padrão.

## Seleção de nós

Escolha quais buracos de minhoca o percurso visita, e em que ordem:

- **Todos os nós**: cada buraco de minhoca da galáxia, na ordem em que foram criados. A seleção mais simples; útil para galáxias curtas em que todo buraco de minhoca tem o mesmo peso.
- **Apenas nós destacados**: somente buracos de minhoca marcados como acentuados. Use quando você quer que alguns buracos de minhoca estejam no percurso e outros permaneçam acessíveis mas em segundo plano. A marca de acentuar é definida por buraco de minhoca (capítulo 5).
- **Uma amostra aleatória de N nós**: escolhe N buracos de minhoca aleatórios a cada sessão. Um campo aparece para N. Use para galerias que devem soar frescas a cada revisita; a visitante vê uma fatia diferente toda vez.
- **Nós marcados com uma destas palavras-chave**: visita apenas buracos de minhoca que carregam uma de um conjunto escolhido de palavras-chave. Um seletor de palavras-chave aparece, parecido com o campo de chips do modal do buraco de minhoca. Use quando quiser um percurso *temático* (só buracos de minhoca marcados *medicinal*; só os marcados *native*).

Para percursos por palavras-chave marcadas, a ordem em que os buracos de minhoca são visitados é a ordem em que foram criados, filtrada pelo conjunto de palavras-chave. Não há campo de ordenação manual; se você precisa de uma sequência estritamente composta, a ordem em que cria os buracos de minhoca é a ordem que o percurso vai respeitar.

## Pausa em nós sem conteúdo

Um único número, em segundos, controlando quanto tempo o percurso pausa em cada buraco de minhoca antes de seguir. A permanência começa quando o cartão de informações do buraco de minhoca abre; o próximo é selecionado quando o tempo termina.

Um padrão útil são cinco a oito segundos; é longo o bastante para uma visitante ler uma descrição curta e olhar a imagem, curto o bastante para manter o ritmo em um percurso longo. Buracos de minhoca com áudio anexado costumam pedir permanência mais longa, para que o áudio se resolva antes de o percurso seguir; o capítulo 6 cobre as semânticas de loop de áudio.

A permanência é global ao percurso; a editora não pode (ainda) definir um tempo diferente por buraco de minhoca.

## Repetir o passeio ao terminar

Um único interruptor:

- **Ligado**: depois do último buraco de minhoca, o percurso volta ao primeiro e segue. Use para instalações de galeria ambiente em que a visitante pode entrar no meio do ciclo.
- **Desligado**: o percurso termina discretamente depois do último buraco de minhoca; a cena retorna ao modo interativo e a visitante pode explorar livremente. Use para percursos narrativos com começo e fim.

## Pré-visualizar um percurso

Abaixo dos campos de configuração do percurso, aparece um botão **Pré-visualizar passeio**. Selecioná-lo abre a vista da visitante em uma nova aba com o percurso rodando, independentemente de você ter salvo a configuração. É o jeito certo de conferir temporização, ordem, e permanência antes de publicar mudanças para visitantes.

A prévia reflete o que você inseriu no modal, não o que está salvo. Se você decide que a prévia está errada, mude os campos e selecione **Pré-visualizar passeio** de novo; a nova aba atualiza.

## Percursos e a marca Acentuar buraco de minhoca

A marca **Acentuar buraco de minhoca** (capítulo 5) se sobrepõe à seleção do percurso, mas não é a mesma coisa. Buracos de minhoca acentuados são *visualmente maiores* na cena 3D independentemente de um percurso visitá-los. A opção de seleção **Apenas nós destacados** do percurso é uma forma de usar a marca, mas você também pode acentuar buracos de minhoca que não estão no percurso e ter um percurso que inclui buracos de minhoca não acentuados.

O padrão que lê mais limpo:

- Use **Acentuar buraco de minhoca** para buracos de minhoca que devem se destacar visualmente o tempo todo.
- Use o percurso para especificar o *caminho narrativo*, que pode ou não coincidir com a ênfase visual.

## Percursos e a tela de palavras-chave

Um percurso por palavras-chave marcadas (seleção de nós definida como *Nós marcados com uma destas palavras-chave*) dá à editora um caminho pela galáxia que segue o vocabulário de palavras-chave que a tela compõe. As duas superfícies trabalham juntas: escolha primeiro na tela as palavras-chave que o percurso vai seguir, desenhe as relações entre elas, e depois configure o percurso para seguir esse caminho temático do lado da visitante.

A conexão é editorial, não estrutural; Telaris não exige que a tela esteja preenchida antes de configurar um percurso, mas o percurso resultante costuma parecer mais deliberado quando o vocabulário de palavras-chave foi trabalhado antes.

## Coisas que vale a pena saber

- **O auto-tour não pausa pelo áudio.** Se um buraco de minhoca tem uma trilha de áudio de 30 segundos e a permanência é de 8 segundos, o percurso segue aos 8 segundos enquanto o áudio continua tocando em segundo plano. Para deixar o áudio terminar, estenda a permanência.
- **A visitante sempre pode parar o percurso.** Um controle Stop ou Pause aparece durante um percurso em andamento; a visitante também pode clicar em qualquer lugar fora do cartão de informações para interromper. Os percursos devem soar oferecidos, não impostos.
- **Percursos Random-N mudam a cada sessão.** Uma visitante que revisita a página não vê os mesmos N buracos de minhoca; a seleção aleatória é refeita. Útil para sensação de ambiente; surpreendente se você esperava uma sequência estável.
- **Percursos por palavras-chave marcadas seguem a união das palavras escolhidas.** Um percurso definido com as palavras-chave *native* e *edible* visita todo buraco de minhoca marcado com **uma ou outra** *native* ou *edible* (ou ambas); não exige as duas.
- **Os percursos se restringem à galáxia atual.** Um percurso não pode visitar buracos de minhoca em outra galáxia; para caminhos entre galáxias, use portais (capítulo 9).
- **A vista 2D (capítulo 10) interage bem com percursos.** Uma visitante em modo 2D vê o percurso como uma sequência de chips destacados, não como movimento de câmera. A permanência continua valendo; só o visual fica mais plano.
