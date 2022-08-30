---
title: "Árvores B"
alias: Árvore B
---

# Árvores B

- Diversos sistemas de bancos de dados utilizam Árvores B (ou variantes) para armazenar as informaçẽos.
- Generalização de [[Árvores binárias de busca]].
- É uma árvore semi balanceada.
- É interessante para armazenar itens em memória principal ou secundária. 
	- [[Árvore AVL]] e [[Árvores preto-e-vermelho]] não são adequadas para memória secundária
- Objetivo: Minimizar número de operações de movimentação de dados (escrita/leitura)
- Foi criada para lidar com situações em que o índice possui um número grandes de chaves, apenas uma pequena fração delas pode ser gerenciada de forma eficiente em memória principal.
- A organização de índices utilizado uma árvore B permite busca, inserção e remoção em tempo $O(log_t n)$  onde $n$ é o tamanho do índice e $t$ um parâmetro a ser definido.

> Uma árvore B, $T$, possui as seguintes propriedades:
	>> Cada nó $x$ armazena $x_n$ chaves $x_{k_1} \leq x_{k_2} \leq \ldots \leq x_{k_n}$.
	>> Cada nó interno contém $x_{n+1}$ referências $x_{c_1}, x_{c_2}, \ldots, x_{c_{n+1}}$ para seus filhos.
	>> As chaves $x_{k_i}$ delimitam os valores das chaves armazenadas em cada subárvore. Seja $k_i$ uma chave armazenada na subárvore com raiz $x_{c_i}$, então: $$k_1 \leq x_{k_1} \leq k_2 \leq x_{k_2} \leq \ldots \leq x_{k_{x_n}} \leq k_{x_n + 1}.$$
	>> Todas as folhas possuem a mesma profundidade
	>> Nós possuem um número máximo e mínimo de chaves que podem armazenar. Esses limitantes são expressões em funções de um parâmetro $t \geq 2$, denominado de grau mínimo da árvore B. 
	>>> Cada nó com exceção da raiz possui pelo menos $t - 1$ chaves. Todo nó interno com exceção da raiz possui no mínimo $t$ filhos. 
	>>> Todo nó possui no máximo $2t-1$ chaves. Todo nó interno possui no máximo $2t$ filhos. 

- A árvore B mais simples possui $t=2$. Cada nó interno possui 2, 3 ou 4 filhos (ou seja, é uma 2-3-4 árvore).

![[ArvoreBexemplo.excalidraw|900]]


- O número de acessos ao disco em uma Árvore B é proporcional a altura da árvore, para a maiora das operações

- Teorema: 
> Seja $n \geq 1$, então para qualquer árvore B com $n$ chaves, altura $h$ e grau mínimo $t \geq 2$ tem-se $$h \leq log_t \frac{n+1}{2}.$$ Ou seja, a altura é $O(log_t n)$ 

- Demonstração
- A raiz da árvore contém pelo menos uma chave e todos os demais nós contém pelo menos $t-1$ chaves. Ou seja, existem pelos menos:
	 - $2$ nós com profundidade $1$;
	 - $2t$ nós com profundidade $2$;
	 - $2t^2$ nós com profundidade 3;
	 - ...
	 - $2t^{(h-1)}$ nós com profundidade $h$.
 - Ou seja, o número de nós $n$ satisfaz $$n \geq 1 + (t-1)\sum_{i=1}^h (2t^{(i-1)}) = 1 + 2(t-1)\frac{(t^h-1)}{t-1}.$$ Portanto $n \geq 2t^h - 1$, resolvendo para $h$ tem-se a prova do teorema.

## Operações elementares em uma árvore B

Para os algoritmos a seguir é suposto:
- node[i]: retorna a chave na posição $i$ presente em $node$. 
- node.n: retorna o número de elementos em $node$.
- O método node.is_leaf() responde se $node$ é uma folha.
- node.child[i]: returna a $i$-ésima subárvore enraizada em $node$.

### Busca

A busca em uma árvore B é análoga a uma busca em uma [[Árvores binárias de busca|Árvore binária de busca]]. Em cada nó, é necessário verificar qual a subárvore que potencialmente contém o elemento de interesse.

```
find(key, node):
	i = 0
	while i < node.n and key > node[i]:
		i = i + 1
	if i < node.n and key == node[i]:
		return node, i
	else if node.is_leaf():
		return None
	else:
		find(key, node.child[i])	
	
```

A complexidade da busca é proporcional a altura da árvore, portanto $O(log_t \ n)$. Note que, quanto maior o grau mínimo da árvore, $t$, menor o número de chamadas recursivas. Por quê? #pergunta

Do ponto de vista de gerenciamento de arquivos. Suponha que foi utilizado uma estratégia de acesso indexado sequencial, mas o índice é grande o suficiente para não poder ser armazenado todo na memória principal. Como uma árvore B pode ser utilizada eficientemente nessa situação? #pergunta [[Organização de arquivos#Arquivo indexado sequencial]]

### Inserção

O processo de inserção é relativamente mais sofisticado do que no caso de [[Árvores binárias]]. Inicialmente, se busca pela folha onde será realizada a inserção. No entanto, não se pode simplesmente criar um novo nó para inserir o elemento, pois isso implicaria em uma violação das propriedades definidores de uma árvore B. Qual propriedade? #pergunta 

Nesse caso, o objetivo é inserir o elemento no próprio nó folha, que pode estar cheio. Para lidar com tal situação, pode ser necessário realizar uma operação de particionamento do nó folha (*split*). 

#### Split

Um nó que está cheio, possui $2t-1$ chaves. A operação de *split* é feita dividindo o nó cheio em dois $x$ e $y$ com $t-1$ chaves cada. O elemento com a chave mediana, $node[t-1]$, é "promovido" para o nó pai, identificando o ponto de divisão entre os elementos de $x$ e $y$. Contudo, caso o nó pai também esteja cheio, é necessário realizar o *split* antes de inserir. Ou seja, a operação de *split* pode gerar uma reação em cadeia, até a raiz da árvore. 

Utilize o simulador https://www.cs.usfca.edu/~galles/visualization/BTree.html:
1. Escolha a opção Max. Degree = 4. Equivalente $t = 2$.
2. Insira as chaves 10, 20 e 30, respectivamente. Note que uma nova inserção implica em um *overflow* da raiz. Ou seja, será necessária uma operação de *split*.
3. Insira a chave 0. Note que o nó na posição $t-1 = 1$ foi promovido, marcando o ponto de separação entre as duas subárvores geradas. 
4. Insira as chaves 2, 3 e 40 respectivamente. Com uma inserção seguinte da chave 35, qual chave seria promovida e como ficariam os dois novos nós gerados? #pergunta 
5. Insira a chave 35.
6. Insira a chave 4 e a 50, respectivamente. Qual o estado final da árvore se for inserida a chave 55? #pergunta
7. Insira a chave 55. 

#check (Cormen, pg 493)
> As with a binary search tree, we can insert a key into a B-tree in a single pass down the tree from the root to a leaf. To do so, we do not wait to find out whether we will actually need to split a full node in order to do the insertion. Instead, as we travel down the tree searching for the position where the new key belongs, we split each full node we come to along the way (including the leaf itself). Thus whenever we want to split a full node y, we are assured that its parent is not full.

### Remoção

Como é possível remover elementos de nós internos, e não apenas de nós folha, a operação de remoção pode implicar na reorganização de alguns elementos da árvore. Suponha que a busca pelo elemento a ser removido começa no nós raiz $x$

1. Se a chave $k$ está em $x$ e $x$ é um nó folha. Remova $k$ de $x$.
2. Se a chave $k$ está em $x$ e $x$ é um nó interno $x$:
	1. Se o filho $y$ que precede $k$ no nó $x$ possui pelo menos $t$ chaves, encontre o predecessor $k'$ de $k$ na subárvore cuja raiz é $y$. Recursivamente remova $k'$ e substitua $k$ por $k'$ em $x$.
	2. Se $y$ possui menos de $t$ chaves, verifique se o filho $z$ que sucede $k$ em $x$. Se $z$ possuir pelo menos $t$ chaves, encontre o sucessor $k'$ de $k$ na subárvore cuja raiz é $z$. Recursivamente remova $k'$ e substitua $k$ por $k'$ em $x$.
	3. Caso ambos, $y$ e $z$, possuam $t-1$ chaves, faça uma junção (*merge*) de $z$  em $y$ ($k$ também é movido para $y$) e $y$ passa a conter $2t-1$ chaves. Então, destrua $z$ e recursivamente remove $k$ de $y$.
3. Se a chave $k$ não está presente em $x$ e $x$ é um nó interno $x$: Determine a raiz $x.c_i$ da subárvore que (potencialmente) contém $k$. Se $x.c_i$ possui apenas $t-1$ chaves, execute um dos passos a seguir para garantir que a busca continua em um nó com pelo menos $t$ chaves. Então, continue recursivamente do filho apropriado de $x$
	1. Se $x.c_i$ possui apenas $t-1$ chaves mas possui um irmão imediato com $t$ chaves, mova uma chave de $x$ para $x.c_i$, mova a chave do irmão imediato de $x.c_i$ para $x$.
	2. Se $x.c_i$ e ambos os seus irmãos possuem $t-1$ chaves, faça o *merge* de $x.c_i$ com um dos irmãos (movendo uma chave de $x$ para o novo nó). 

Considere o exemplo a seguir de [[2009Cormen_IntroductionToAlgorithms|Cormen et al. (2009)]] para uma árvore com $t = 3$.

![[Pasted image 20220715163554.png]]

![[Pasted image 20220715163604.png]]

Considere uma árvore com $n$ elementos. Em que tipo de nó (folha ou interno), o ocorre o maior número de remoções? #pergunta

## Árvores B e gerenciamento de arquivos

Uma das motivações primordiais da proposição da estrutura de dados Árvore B é no contexto de gerencia de arquivos com acesso indexado sequencial. Nesse estratégia, é criado um índice auxiliar com a posição das chaves dos registros que estão armazenados em memória secundária. Quando o índice auxiliar pode ser armazenado completamente em memória primária, há um grande ganho de eficiência na operação de busca, em relação a ter que buscar em um arquivo em memória secundária. Por outro lado, pode não ser possível armazenar todo o índice em memória primária. Nessa situação, pode ser interessante armazenar o índice em uma estrutura de Árvore B. 

Uma vantagem de se utilizar árvore B nesse caso é a possibilidade de armazenar os nós mais altos da árvore na memória principal, minimizando o número de requisições à memória secundária. Além disso, durante a busca, se for necessário carregar novos dados em memória, isso é feito lendo um bloco de informações (e não apenas um único valor, como seria no caso de outras [[Árvores binárias]]).

Uma desvantagem dessa estratégia é a de que são armazenadas, em cada nó, referências para cada valor na memória secundária, além do valor em si (os registros propriamente ditos). Isso reduz consideravelmente o número de chaves que pode ser armazenadas na memória principal, aumentando o número de acessos à memória secundária. Para reduzir essa desvantagem, podem ser utilizadas [[Árvores B+]].


## Comparações com outras formas de organização de índices

De acordo com o artigo original [[Árvores B#^bf7c66]], algumas vantagens de se utilizar Árvores B são:
- Não há degradação de performance se a taxa de ocupação do dispositivo de armazenamento for alta
- A ordem natural das chaves é mantida.
	- Permite processamentos de busca por predecessores, sucessores, busca por registros iniciando com em uma chave definida etc
- Se buscas, inserções e remoções forem feitas em batches, o processamento é muito eficiente, essencialmente processando o arquivo sequencialmente. Desde que seja feita uma ordenação das requisições pela chave.

# Referências
- INE 5408 - Estruturas de Dados - Aulas 6.6 e 6.7 - Árvores-B, conceitos, algoritmos & exemplos. https://youtu.be/zkVGGbmjTH4
- Bayer, Rudolf, and Edward McCreight. "Organization and maintenance of large ordered indexes." Software pioneers. Springer, Berlin, Heidelberg, 2002. 245-262. ^bf7c66
- [[1998Sedgewick_AlgorithmInCPart1-4|Algorithms in C. Parts 1-4 (Sedgewick. 1998)]]
- [[2009Cormen_IntroductionToAlgorithms|Cormen et al. (2009)]]
- https://www.geeksforgeeks.org/introduction-of-b-tree/