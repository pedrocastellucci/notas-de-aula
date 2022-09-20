---
title: "Estruturas de dados para grafos"
---

# Introdução

Existem diversas formas de representar um grafo computacionalmente. Duas formas consideradas clássicas são (i) Lista de adjacências e (ii) Matriz de adjacências. 


## Lista de adjacências

> [!INFO] Lista de adjacências
> - Para cada vértice $v \in V$, há uma coleção $I(v)$ de todos os vértices incidentes em $v$. Tradicionalmente, $I(v)$ é uma lista.
> - Para grafos direcionados pode se manter listas separadas de entrada ($I_{in}(v)$) e saída do nó ($I_{out}(v)$).
> - A coleção $V$ pode ser mantida em uma lista.

![[attachments/Pasted image 20220920121758.png]]

## Matriz de adjacências

> [!INFO] Matriz de adjacências
> - Utiliza uma matriz $n$ por $n$, $A$, para manter informações sobre as arestas.
> - Cada célula $A[i, j]$ mantém uma referência para a aresta $(u, v)$ em que $u$ é o vértice com índice $i$ e $v$ é o vértice com índice $j$.

![[attachments/Pasted image 20220920121810.png]]

# Comparação entre as implementações

- Na lista de adjacências é possível percorrer todos os nós adjacentes a outro nó, $v$, em tempo $O(grau(v))$
- A representação em matriz de adjacências permite acessar qualquer aresta com custo $O(1)$.
- O espaço adicional utilizado pela matriz de adjacências é $O(n^2)$ enquanto que na lista de adjacências é $O(n + m)$. Portanto, para grafos esparsos (poucas arestas ou arcos) o lista de adjacências é vantajosa.