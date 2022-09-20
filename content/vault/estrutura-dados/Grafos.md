---
title: "Grafos"
alias: [grafo, grafos]
---

# Introdução e definições

Problemas envolvendo grafos emergem em diversas áreas da computação. Por isso, estruturas de dados e algoritmos para lidar com tais situações são fundamentais. 

> [!INFO]
> Um grafo $G = (V, E)$ é composto por um conjunto de vértices $V$ e um conjunto de arestas $E$. Os vértices são unidades (elementos ou entidades) e arestas indicam relações (ligações ou conexões) entre vértices, $E = \{\{i, j\} : i, j \in V\}$.

- Exemplos:
	- Fronteiras entre países
	- Colaboração entre pesquisadores
	- Relações em uma rede social
	- Mapa de uma cidade: vértices são cruzamentos
	- Rede de distribuição de energia


![](https://mermaid.ink/img/pako:eNqNU0tuwjAQvUo0a3KB7AqUripVou2GdDGNB2LJsenERmoRR-quN-BidX7QxAGaSPHMvDfPlvNmD5kRBAlsGLd59DxPdeSfKWMpVRTHcfTgJGpcrJo1WjDqjEp8C4hLx1JjQRcUgvIrafpypEJkZpQp3iWufHD8qaJwtydiFxSnRsmd7_Pr8Xs32oaMG4cyAO54Q9rKkXO-sDt3nGi3oP5GfezCMfukWS5Ve5ed1rXmmn6NUF3Y_wQGV3EGaomB2v2HQ2F4UO3-YFNuOSNIl40Z4pQGJmqtGJquy_4at0G6b_XCBAriAqXwvt9XSAo2Jy8CiQ8FrdEpm0KqD56Kzprlp84gsexoAm4r0NJcop-YApI1qtJXSUhr-LGZpXqkDr9QOBIv)

> [!INFO] 
> Um grafo é valorado quando um peso (ou valor) é associado a cada aresta. Ou seja, $G = (V, E, w)$ em que $V$ e $E$ são os conjuntos de vértices e arestas respectivamente e $w: e \in E \rightarrow \mathbb{R}$ é uma função que mapeia um aresta no seu peso correspondente. 

- Exemplos de situações com grafos ponderados
	- Taxas de importação/exportação
	- Distâncias no mapa de uma cidade

> [!INFO]
> Um grafo $G = (V, E)$ é chamado de orientado (ou direcionado) se $E$ for formado por pares ordenados, $E = \{(i, j): i, j \in V\}$. Ou seja, as ligações entre os vértices possuem direção. Cada ligação é chamada de arco.   

- Exemplos de grafos direcionados
	- Árvore genealógica
	- Herança em orientação a objetos
	- Malha viária (com as direções das rodovias)

![](https://mermaid.ink/img/pako:eNptkU1PwzAMhv9K5BOI9Q9EXBBjEoeddkOVkJt4ndV8QD40weh_Jy1rGR25xH4cv3pjn0B5TSBBGYxxzdgGtLUT5Tw4tmjE_VdViXVW3TXdcDxc0xdqAv7BUtyxSwJbWuJdCuxa0ZLTFC6LQ0vcoi3hze2iYDHRBEfbo73TDxCzaEPYPXrjw1yIR7ZTY0nfM6puyvtLveFjs141eI_8Sc9uQ5RmrNA9Yfq3fxzBr6HGeyM4vh7Z6BmG7Ba904EVWAoWWZe9jCo1pANZqkGWUNMes0k11K4vTzEnv_twCmQKmVaQ33SZz3mTIPdoYqGkOfmwPe96uPpvoweZfg)

> [!INFO] O grau de um vértice
> - O **grau** de um vértice $v$, $d_v$, é definido como a quantidade de arestas que se conectam com $v$. Em um grafo direcionado, pode-se definir:
> - O grau de saída de um vértice $d_v^+$ como o número de arcos que estão saindo de $v$.
> - O grau de entrada de um vértice $d_v^-$ como o número de arcos que chegam em $v$.

> [!INFO] Grafo completo
> Um grafo é chamado de completo $G=(V, E)$  se $E = V \times V$.

> [!HINT] Soma dos graus dos vértices
> Um resultado útil para análise de algoritmos é o seguinte: A soma dos graus de todos os vértices de um grafo 
> $$\sum_{v \in V} d_v = 2|E|.$$

## O tipo abstrato de dados grafo

Algumas operações frequentes para o tipo abstrato de dados grafo $G$ são as seguintes:
- G.getVertices(): Retorna uma coleção com os vértices de $G$.
- G.getArestas(): Retorna uma coleção com as arestas de $G$.
- G.getAdjacentes(v): Retorna uma coleção com os vértices adjacentes ao vértice $v$. 
	- Em um grafo direcionado, pode-se definir funções para coletar os vértices que são pontos de chegada e saída para $v$, respectivamente.
- G.getDegree(v): Retorna o grau do vértice $v$.
- e.getOposto(v): Retorna o vértice oposto a $v$ na aresta $e$.

Durante a implementação o custo de cada operação depende das [[Estruturas de dados para grafos|estruturas de dados utilizadas para representar o grafo]]. 

# Percursos em grafos
- Busca em largura
- Busca em profundidade

# Referências
- Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2009). Introduction to Algorithms. third. _New York_.
- Sedgewick, R., & Wayne, K. (2014). _Algorithms_. Addison-Wesley Professional.
- Goodrich, M. T., Tamassia, R., & Goldwasser, M. H. (2014). _Data structures and algorithms in Java_. John Wiley & Sons.
- Notas de aula do Prof. Rafael Santiago. http://www.inf.ufsc.br/~r.santiago