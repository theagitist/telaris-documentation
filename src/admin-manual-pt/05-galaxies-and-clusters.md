# Galáxias e aglomerados

As abas **Galáxias** e **Aglomerados** são a visão da administradora de todo o conteúdo da instância. Uma editora vê apenas as suas próprias galáxias; você vê toda galáxia, incluindo as importadas de outros lugares, e pode agrupá-las em aglomerados. Este capítulo cobre as duas abas.

## A aba Galáxias

![A aba Galáxias: uma tabela de toda galáxia na instância com seu aglomerado, sua dona e se é importada](assets/images/admin-manual-pt/05-galaxies-list.png)

A aba Galáxias lista toda galáxia da instância, seja quem for que a fez. De cada galáxia você vê a qual aglomerado ela pertence (se houver), quem é sua dona, e se é **importada** de outra instância. A partir daqui você alcança as configurações de uma galáxia do mesmo jeito que sua editora faria, e pode mover uma galáxia para dentro ou para fora de um aglomerado.

A criação do dia a dia de uma galáxia (seu tema, seus buracos de minhoca, suas palavras-chave) é trabalho de edição e vive no Manual do editor. O que é específico de você como administradora é a visão de instância inteira: ver tudo de uma vez, e as duas preocupações abaixo, conteúdo importado e aglomerados.

## Galáxias importadas (somente leitura)

Se a sua instância assina uma galáxia publicada por outra instância (veja *Federação e o Pluriverse*), essa galáxia aparece aqui como **importada**. Uma galáxia importada é um espelho: seu conteúdo é copiado para a sua instância para que as visitantes possam vê-lo, mas a autoridade sobre ele fica com a instância que o publicou.

- As galáxias importadas são **somente leitura** para todo mundo na sua instância, editoras e administração igualmente. Você não pode mudar o conteúdo delas, porque a mudança tem que acontecer na fonte.
- Uma ação **Atualizar** puxa a última versão de uma galáxia importada da sua fonte, para que o seu espelho acompanhe as edições feitas na origem. A federação também atualiza os espelhos num agendamento; Atualizar é o botão manual de "agora".
- Se a fonte para de publicar a galáxia para você, ou você para de assinar, o espelho é removido. O conteúdo importado nunca foi seu para guardar; ele está presente só enquanto a assinatura existir.

O capítulo de federação cobre assinar, publicar e bloquear por inteiro. Aqui basta saber que as galáxias importadas aparecem nesta lista, são somente leitura, e podem ser atualizadas.

## A aba Aglomerados

Um **aglomerado** agrupa galáxias. Os aglomerados são como uma família de galáxias relacionadas é apresentada junta e como algumas configurações da instância são limitadas a um subconjunto de galáxias em vez de à instância inteira.

![A aba Aglomerados: uma lista de aglomerados de galáxias, cada um com as galáxias que contém](assets/images/admin-manual-pt/06-clusters-list.png)

Na aba Aglomerados você pode criar um aglomerado, nomeá-lo e colocar galáxias nele. Uma galáxia pertence a no máximo um aglomerado por vez. Os aglomerados importam para uma administradora por duas razões:

- São um nível na **cascata de edição** (veja *Controle de acesso de edição*): você pode desligar a edição de um aglomerado inteiro de uma vez.
- São um escopo para a **correspondência de palavras-chave**, abaixo.

A auto-inscrição também pode colocar automaticamente a galáxia pessoal de cada nova editora em um aglomerado por instância, de modo que todas as galáxias pessoais de uma chamada aberta fiquem juntas em vez de espalhadas pela lista.

## Correspondência de palavras-chave (exata e aproximada)

Telaris traça conexões entre buracos de minhoca que compartilham uma palavra-chave. Por padrão a correspondência é **exata**: dois buracos de minhoca se conectam só quando carregam exatamente a mesma palavra. Você pode afrouxar isso para a correspondência **aproximada**, de modo que grafias próximas também se conectem: um plural e seu singular, um pequeno erro de digitação, uma variação leve.

A correspondência aproximada é um interruptor, e pode ser definida em dois escopos:

- para a **instância inteira** (o interruptor fica na aba Configurações globais, veja *Configurações globais*), de modo que toda galáxia use a correspondência aproximada, ou
- para um **aglomerado** (nas próprias configurações desse aglomerado), de modo que só as galáxias daquele aglomerado a usem.

Ela vem **desativada por padrão**; as conexões permanecem exatas até você ligá-la. Uma salvaguarda evita que a correspondência aproximada superconecte palavras curtas muito comuns, então ligá-la não inunda a rede de vínculos espúrios, mas ainda é uma mudança que as suas editoras verão (novas linhas de relação surgindo entre palavras-chave quase iguais entre galáxias). Ligue-a quando o vocabulário do seu conteúdo varia na grafia e você quer que essas variantes se conectem; deixe-a desligada quando as suas palavras-chave são controladas e você quer que só correspondências exatas tracem uma linha.

## Coisas que vale a pena saber

- **Você vê tudo; as editoras veem o que é seu.** A aba Galáxias é o único lugar com a instância inteira à vista. Use-a para auditar o que existe, quem é dono e o que veio de fora.
- **Importada não é sua.** As galáxias importadas somente leitura são uma cortesia de outra instância, presentes enquanto a assinatura durar. Não as trate como backup nem como seu conteúdo.
- **A correspondência aproximada é uma escolha editorial por instância ou por aglomerado**, não por buraco de minhoca. Se as editoras perguntam por que palavras-chave quase iguais estão (ou não estão) conectando, este interruptor é a resposta.
