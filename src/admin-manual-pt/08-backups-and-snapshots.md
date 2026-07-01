# Backups e snapshots

Uma instância é conteúdo, e conteúdo deve ser recuperável. Telaris te dá duas ferramentas relacionadas: **backups** que você baixa e guarda, e **snapshots** que a instância tira e armazena para você, num agendamento se quiser. Este capítulo cobre as duas, e como restaurar.

## Backups (a aba Backup)

![A aba Backup: um painel Baixar um backup e um painel Restaurar a partir de um backup](assets/images/admin-manual-pt/09-backup.png)

A aba **Backup** tem duas metades:

- **Baixar um backup** produz um único arquivo que captura o conteúdo da instância, que o seu navegador baixa. Guarde-o em algum lugar seguro e fora do servidor. É a cópia que você tira antes de qualquer coisa arriscada, e a cópia que você usaria para mudar uma instância de lugar ou se recuperar de um servidor perdido.
- **Restaurar a partir de um backup** recebe um arquivo de backup e o carrega de volta na instância, substituindo o conteúdo atual. Restaurar é destrutivo para o que está lá agora, então Telaris confirma primeiro. Restaure em uma instância nova ou que se pretende sobrescrever; não restaure sobre conteúdo que você ainda quer.

Um backup é portátil: você pode restaurá-lo em outra instância para clonar ou migrar. Lembre, de *Configurações globais*, que a senha do e-mail nunca está em um backup; depois de restaurar, redigite as configurações de e-mail para que a instância restaurada possa enviar.

## Snapshots (a aba Snapshots)

Onde um backup é um arquivo de que você cuida, um **snapshot** é uma cópia que a instância guarda para você. A aba Snapshots tem três partes:

- **Criar snapshot agora** tira um snapshot sob demanda. Faça isso antes de uma mudança em massa ou de qualquer edição de que você não tem certeza, para que haja um ponto recente ao qual voltar.
- **Agendador de snapshots** tira snapshots automaticamente num intervalo que você define, e mantém um número rotativo deles, para que sempre haja um snapshot recente sem você ter que lembrar de fazer um. Ligue-o para qualquer instância cujo conteúdo importe.
- **Snapshots disponíveis** lista os snapshots à mão, mais recente primeiro, cada um restaurável no lugar.

Os snapshots são a rede de segurança do dia a dia: baratos, frequentes e por perto. Os backups são o seguro externo: menos numerosos, deliberados, e mantidos longe do servidor. Use os dois, os snapshots para "desfazer", os backups baixados para "o servidor se foi".

## Restaurar

Restaurar, seja de um backup baixado ou de um snapshot armazenado, substitui o conteúdo atual pelo conteúdo salvo. Como sobrescreve, trate-o como um ato ponderado:

1. Tenha certeza de que está restaurando a versão que você pretende. Os snapshots têm data e hora; confira a hora.
2. Entenda que as edições feitas desde aquele ponto terão sumido depois da restauração.
3. Em qualquer dúvida, baixe um backup do estado *atual* primeiro, para que até o estado que você está prestes a sobrescrever seja recuperável.

Quando uma restauração se completa, o console a confirma. Entre de novo se a sessão foi afetada, e confira uma galáxia por amostragem para confirmar que o conteúdo é o que você esperava.

## O aviso de incompatibilidade de esquema

Telaris mantém a estrutura do seu banco de dados em sintonia com o código em execução automaticamente; quando você implanta uma nova versão, a instância traz a própria estrutura para o dia por conta própria. Se o código e a estrutura do banco de dados alguma vez discordarem de um jeito que a instância não consegue reconciliar em silêncio, o console mostra um **aviso de incompatibilidade de esquema**. É um sinal de que uma implantação não terminou de forma limpa, não um estado de rotina. Se você o vir, a resposta segura é garantir que a instância está rodando a versão pretendida do código e deixá-la completar a atualização da estrutura; se ele persistir, esse é o momento de olhar a implantação ou pedir a quem gerencia o servidor. Não restaure um backup para "corrigir" um aviso de esquema; restaurar conteúdo não muda a incompatibilidade entre código e estrutura.

## Coisas que vale a pena saber

- **Faça backup antes de qualquer coisa irreversível.** Uma mudança em massa, uma restauração, uma exclusão grande: tire um snapshot ou baixe um backup primeiro. Custa segundos e salva o dia em que você precisar.
- **Mantenha ao menos um backup fora do servidor.** Um snapshot armazenado no mesmo servidor não ajuda se o servidor é o que você perde. Baixe um backup periodicamente e guarde-o em outro lugar.
- **A senha do e-mail não está em backups nem snapshots.** Depois de restaurar ou clonar, redigite as configurações de e-mail (*Configurações globais*).
- **Teste uma restauração antes de depender dela.** Se a recuperação importa, prove que um backup restaura de forma limpa em uma instância reserva uma vez, em vez de descobrir um problema durante uma recuperação real.
