---
alias: Árvore B+
---

# Árvores B+

- Na prática, a variante de [[Árvores B]] mais implementada para sistemas de larga escala baseados em memória secundária são as [[Árvores B+]]. Em casos mais complexos, pode-se utilizar uma variante conhecida como [[Árvores B*]].
- Quando os dados são estáticos, as buscas costumam ser bastante eficientes. O desafio costuma ser como deixar inserções e remoções eficientes. 
- Considere a situação em que se deseja armazenar uma lista ordenada, mas para manter certa flexibilidade, a lista será quebrada em pedaços que podem ser atualizados de forma eficiente. As ideias que motivam as árvores B+ são as seguintes.
	- Considerando que os dados vão ser armazenados em disco, é interessante que os pedaços possuam tamanho de um bloco no disco, permitindo leitura e escrita de forma eficiente. 
	- Para inserir em um bloco já cheio, pode-se particioná-lo em dois, cada um com aproximadamente metade dos elementos. 
	- Não é desejável que um bloco fique com poucos elementos, então pode-se juntar dados de dois blocos que estão com poucos elementos. 
	- Mas como saber em qual bloco realizar as operações? Isto é, como realizar a busca?

- As principais diferenças na estrutura das Árvores B+ em relação às [[Árvores B]] são:
	- Os nós internos armazenam apenas as chaves, para guiar as buscas, e não os valores dos registros. 
	- Os registros são armazenados apenas nos nós folhas. 
	- Os nós folhas são conectados como em uma [[Listas ligadas|Lista ligada]] para permitir uma busca sequencial rápida.

![[ArvoresB+exemplo.excalidraw]]

## Exercícios
- Detalhe uma opção para as estruturas de dados que podem utilizadas nos nós de uma árvore B+ que suporta as operações de busca, inserção e remoção. Quais são seus campos principais?
- Considere que se deseja buscar por todos os elementos cujas as chaves estão em um intervalo específico $[a, b]$. 
	- Descreva um algoritmo para realizar tal operação em uma Árvore B+. 
	- Descreva um algoritmo para realizar tal operação em uma [[Árvore B]]. 
	- Compare as soluções dos itens anteriores. 

# Referências
- Shaffer, Clifford A. A practical introduction to data structures and algorithm analysis. Upper Saddle River, NJ: Prentice Hall, 1997.

