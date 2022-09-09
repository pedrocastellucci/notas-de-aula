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

- Grafos valorados ou ponderados

> [!INFO] 
> Um grafo é valorado quando um peso (ou valor) é associado a cada aresta. Ou seja, $G = (V, E, w)$ em que $V$ e $E$ são os conjuntos de vértices e arestas respectivamente e $w: e \in E \rightarrow \mathbb{R}$ é uma função que mapeia um aresta no seu peso correspondente. 

- Exemplos de situações com grafos ponderados
	- Taxas de importação/exportação
	- Distâncias no mapa de uma cidade

> [!INFO]
> Um grafo $G = (V, E)$ é chamado de orientado (ou direcionado) se $E$ for formado por pares ordenados, $E = \{(i, j): i, j \in V\}$. Ou seja, as ligações entre os vértices possuem direção. Cada ligação é chamada de arco.   

- Exemplos de grafos direcionados
	- Árvore genealógica
	- Árvore filogenética
	- Herança em orientação a objetos
	- Malha viária (com as direções das rodovias)

- Grau de um vértice
- Grafo completo

# Estruturas de dados para grafos
- Lista de adjacências
- Matriz de adjacências

# Percursos em grafos
- Busca em largura
- Busca em profundidade

# Referências
- Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2009). Introduction to Algorithms. third. _New York_.
- Sedgewick, R., & Wayne, K. (2014). _Algorithms_. Addison-Wesley Professional.
- Goodrich, M. T., Tamassia, R., & Goldwasser, M. H. (2014). _Data structures and algorithms in Java_. John Wiley & Sons.
- Notas de aula do Prof. Rafael Santiago. http://www.inf.ufsc.br/~r.santiago