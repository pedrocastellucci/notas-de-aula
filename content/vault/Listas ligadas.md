---
alias: [listas ligadas, Lista ligada, lista ligada, listas encadeadas, lista encadeada]
---

# Listas Ligadas

Listas ligadas oferecem uma implementação simples e flexível para conjuntos dinâmicos de dados. 

## Definição

> Uma lista ligada é um conjunto de itens onde cada item é parte de um nó que também contem uma ligação para um nó. [[1998Sedgewick_AlgorithmInCPart1-4|Algorithms in C. Parts 1-4 (Sedgewick. 1998)]]
> Uma lista ligada é uma estrutura de dados em que os objetos são organizados em uma ordem linear em que a ordem é determinada por um ponteiro em cada objeto. [[2009Cormen_IntroductionToAlgorithms|Cormen et al. (2009)]]

## Análise

- A principal vantagem de uma lista ligada é a sua capacidade de reorganizar os itens de forma eficiente. 
	- Mas isso faz com que o acesso a itens arbitrários seja mais lento, porque a única forma de acessar um elemento é através das ligações de um nó para o seguinte. 
- Note que vetores também definem uma sequência de itens, mas a sequência é dada implicitamente pela posição de cada item no vetor. 

- Considere que se deseja armazenar a coleção de itens $x_0, x_1, \ldots, x_{n-2}, x_{n-1}$. Em uma lista ligada, os itens poderiam ser armazenados da seguinte forma.

![[LinkedList_Drawing 2021-10-2720.27.04.excalidraw]]

- O acesso à lista é feito exclusivamente através da referências *start*. Ou seja, para acessar o último elemento, é necessário percorrer todos os elementos através da ligação para o próximo nó. Ou seja, o acesso (e a busca) por um elemento na lista é $O(n)$. 

- O último nó da lista pode utilizar uma referência *nula* (*null*, *None*, *nullptr* etc). Outra opção é fazer com que o último nó faça uma referência ao primeiro definindo uma [[Lista ligada circular]].

- Uma das limitações de listas ligadas de forma simples está no fato de o percurso ser exclusivamente em um sentido. Para permitir percursos nos dois sentidos, pode-se usar uma [[Lista duplamente ligada]].

## Operações

Note que o código de diversas operações poderia ser simplificado se pudessem ser ignoradas algumas condições de contorno. Para isso, poderiam ser utilizados [[Nós Sentinelas]]. 

> Cuidado. Listas do Python não são listas ligadas. Veja [[Implementação CPython de listas]].
