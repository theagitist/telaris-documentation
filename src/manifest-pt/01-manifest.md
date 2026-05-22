# Manifesto

> [!warning] Rascunho
> Este Manifesto é um rascunho, escrito em 2026-05-21. Será refinado à medida que a documentação amadureça.

Uma declaração do que Telaris é, do que recusa, e dos princípios que o sustentam. Escrita para qualquer pessoa que se aproxime do projeto desde fora: uma possível operadora, uma comunidade de origem que considera contribuir, uma estudante que lê a documentação, uma curadora que pondera usar o software. O resto da documentação se apoia nas posições nomeadas aqui.

## O que Telaris é

Um projeto de arquivo de conhecimento decolonial. Relacional, não hierárquico, federado entre pares, fiado por significado. O conteúdo vive em **galáxias**: agrupamentos de pequenas unidades de conteúdo (uma passagem, uma imagem, um som, um trecho de filme, um documento) que se conectam por meio de **palavras-chave** compartilhadas. Não há pastas, nem pais, nem trilhas de navegação, nem algoritmo; a estrutura é um rizoma mantido por editoras e lido pela visitante como uma cena tridimensional.

Telaris é um projeto de pesquisa de pós-graduação no Instituto de Gênero, Raça, Sexualidade e Justiça Social (GRSJ) da Universidade da Colúmbia Britânica. É software de código aberto operado por pessoas independentes em diferentes países e comunidades, não uma plataforma com um único dono.

## Decolonial como método, não como metáfora

"Decolonial" nomeia uma prática, não uma estética. A prática tem consequências concretas em como Telaris é desenhado e operado:

- Recusa de reduções categóricas impostas: não há vocabulário central, nem ontologia obrigatória, nem chefia editorial.
- Soberania dos dados para as comunidades de origem: as pessoas cujo material está hospedado em uma instância de Telaris mantêm autoridade sobre ele; a retirada de consentimento é definitiva e é executada sem negociação.
- Soberania editorial para quem edita: cada editora decide o que publicar nas galáxias que cuida; não existe fila de revisão, nem fluxo de aprovação.
- Soberania operativa para quem administra instâncias: cada operadora roda sua instância sob suas próprias regras; nenhuma autoridade central dita conteúdo ou acesso.

São escolhas de método, não palavras de ordem. Aparecem no código (sem funcionalidade de fila de revisão, sem tabela de vocabulário central, sem anulação do administrador de plataforma) tanto quanto na documentação.

## Localização até o fim

Um padrão comum em software é localizar os textos visíveis e deixar os identificadores, os códigos de erro, as chaves de estado e outros tokens em inglês. Telaris se recusa a isto. A lógica implícita de "os identificadores em inglês são neutros; o que se traduz é o inglês visível" pressupõe que o significado vive em inglês; que no momento em que um sistema deixa de ser inglês, precisa ficar abstrato ou aleatório. É o mesmo padrão colonial numa camada mais silenciosa.

Na prática: todo token que possa chegar a quem usa ou a quem opera fora do código fonte é invariante por idioma. Os códigos de erro da API tomam a forma `<status-http>.<subcódigo-de-3-dígitos>` (RFC 9457 Problem Details), p. ex., `404.001`. Carregam significado pela posição, não por uma abreviação em inglês. O mesmo princípio se estende às chaves de estado, às categorias de log e a qualquer identificador futuro que cruze do código fonte para uma superfície visível. Quando falta a tradução para um idioma, o que aparece é o próprio código, não a cadeia original em inglês: o pior caso visível é o identificador documentado, não um inglês por padrão não declarado.

Os identificadores do código fonte (nomes de variáveis, nomes de funções, caminhos de arquivos, chaves internas de configuração) permanecem em inglês: vivem no contexto de desenvolvimento e são lidos diariamente. A linha está em se o token chega a quem usa ou a quem opera fora do código.

## O que Telaris não é

Uma recusa clara é uma posição mais clara que um manifesto longo.

- **Não é uma plataforma.** Não há dono único. Não há catálogo central. Não há publicidade. Não há rastreamento. Não se vende nem se compartilha dados para fins comerciais.
- **Não é um corpus de treinamento para IA.** O conteúdo de Telaris não é usado para treinar modelos de IA, nem internamente nem externamente. O corpus não é enviado a fornecedoras de modelos de linguagem para moderação, classificação, sumarização, nem qualquer outro propósito.
- **Não é uma hierarquia.** Não há estrutura em árvore sobre o conteúdo. Não há fila de revisão editorial. Não há "melhor conteúdo" promovido por um algoritmo.
- **Não é extrativo.** O conteúdo contribuído por comunidades de origem não se torna propriedade de Telaris. Quem edita não perde autoria ao publicar em Telaris. Quem opera não tem direitos sobre o conteúdo editorial além do que o contrato de cada instância tornar explícito.
- **Não é anônimo por padrão.** A atribuição viaja com a obra. A autoria da editora é registrada; o nome da comunidade de origem é registrado; a licença (quando fornecida) é registrada. O anonimato fica disponível quando uma editora ou comunidade o solicita, não por padrão.

## Princípios, seis

**1. Soberania editorial.** Quem edita decide o que publicar nas galáxias que cuida. Não há fila de revisão, nem vocabulário aprovado centralmente, nem palavra-chave "errada". O custo é responsabilidade: a escolha de quem edita é de quem edita; o software não a policia.

**2. Consentimento da comunidade de origem.** Quando uma comunidade contribui com material, o consentimento dessa comunidade governa o material. A retirada de consentimento é definitiva. A remoção é executada pela operadora sem negociação, independentemente da posição editorial que essa operadora possa ter.

**3. Soberania operativa.** Cada instância de Telaris é administrada por uma pessoa independente sob suas próprias regras. Não há autoridade central sobre as operadoras. Elas concordam com um pequeno conjunto de compromissos de rede (identidade criptográfica, honrar as retiradas de federação, ater-se a estes princípios) mas, fora isso, governam suas instâncias de modo independente.

**4. Federação, não P2P puro.** As galáxias têm origens autoritativas únicas; as instâncias pares as espelham em modo leitura; não há conflitos de mesclagem, nem edição de qualquer lugar. A federação é bilateral e baseada em consentimento: duas operadoras se federam apenas quando ambas concordam, e qualquer uma pode retirar-se a qualquer momento. A terminologia recusa tanto a afirmação desonesta de "P2P puro" (que Telaris não é) quanto o padrão de plataforma com uma autoridade central (que Telaris recusa).

**5. Recusa do padrão de plataforma.** A cada decisão de design se faz a mesma pergunta: *isto importa o padrão de plataforma que Telaris foi construído para recusar?* Login único, telemetria publicitária, moderação central, algoritmos comportamentais, formatos fechados, vocabulários cativos. A resposta determina se a decisão entra.

**6. Software de código aberto, conteúdo licenciado por quem edita.** O software da instância de Telaris é de código aberto sob GPL v3; a camada central de coordenação (o Pluriverso, quando publicada) é AGPL v3. O conteúdo editorial carrega a licença que a editora ou comunidade de origem fornece, anexada a cada peça de conteúdo. O software é entregue; o conteúdo não é anexado à entrega.

## De onde vem Telaris

O projeto se chama *Telaris* (do latim *tela*, uma rede tecida). Apoia-se em:

- *Designs for the Pluriverse* e *Pluriversal Politics* de Arturo Escobar.
- *The Darker Side of Western Modernity* de Walter Mignolo.
- *Constructing the Pluriverse* organizado por Bernd Reiter.
- *Discurso sobre o colonialismo* de Aimé Césaire.
- Os arquivos Mocambos / Baobáxia e a tradição quilombola do arquivo digital comunitário.
- *African Fractals* de Ron Eglash, por uma compreensão fractal-como-estrutura ancorada fora do cânone matemático europeu.
- O conhecimento florestal dos povos indígenas do Noroeste do Pacífico e a metáfora da rede micorrízica em Suzanne Simard e Robin Wall Kimmerer, pela imagem de troca mútua da federação.

São referências, não autoridades. O projeto se situa em conversa com este corpo de trabalho e contribui com um pequeno artefato técnico. A correção do artefato em relação à política que reivindica é o teste em torno do qual a documentação está estruturada.

## O que é este documento

Uma declaração de posição, mantida curta de propósito. A arquitetura completa, as convenções editoriais, os manuais operacionais e a especificação de federação vivem em seus próprios documentos. Leia este para saber onde Telaris está; leia os outros para saber como funciona.
