---
title: "Percursos em árvores"
alias: [percursos em árvores]
---

# Percursos em árvores

As principais estratégias para se percorrer uma árvore são: percurso em pré-ordem, percurso em pós-ordem e percurso em largura. Dependendo da tarefa a ser realizada, um percurso pode ser mais adequado que outro, facilitando a implementação. Todos os algoritmos implementados a seguir possuem custo $O(n)$, sendo $n$ o número de nós da árvore. Tente entender o porquê.

## Percurso em pré-ordem

^fa633f

No percurso em pré-ordem, a raiz da árvore é visitado primeiro, então são visitadas todas as subárvores filhas da raiz são visitadas recursivamente (também em pré-ordem). Caso a árvore seja ordenada, então as subárvore são visitadas de acordo com a propriedade de ordenação definida.

```python
def preorder(T):
	visit(T.root)
	for c in T.children():
		preorder(c)
```

Considere o exemplo a seguir com a árvore enraizada em $A$. 

![](https://mermaid.ink/img/pako:eNpV0M0OgjAMB_BXWXqGF9jBRByK-IGJHndpWBWiAzLHwRDe3bHswHrq799e2gnqXhFweBkcGvYQsmOutixNNyxbY8fWEpHyoMxrH-kQJLyKSMdIZVDhdVrjHEa51yXSNVIVVHndFkACmozGVrk7pyWRYBvSJIG7VqF5S5Dd7PZwtP3919XArRkpgXFQaEm06N6jgT_x86X5D4QzSz4)
O percurso em pré-ordem visita os nós na seguinte ordem: 
- A, B, F, G, C, D, H, K, L, I, J, E, M, N, O, P


## Percurso em pós-ordem

^9628fb

No percurso em pós-ordem, as subárvores da raiz são percorridas recursivamente (em pós-ordem) antes da raiz. Caso a árvore seja ordenada, então as subárvore são visitadas de acordo com a propriedade de ordenação definida.

```python
def postorder(T):	
	for c in T.children():
		postorder(c)
	visit(T.root)
```

Considere o exemplo a seguir com a árvore enraizada em $A$. 

![](https://mermaid.ink/img/pako:eNpV0M0OgjAMB_BXWXqGF9jBRByK-IGJHndpWBWiAzLHwRDe3bHswHrq799e2gnqXhFweBkcGvYQsmOutixNNyxbY8fWEpHyoMxrH-kQJLyKSMdIZVDhdVrjHEa51yXSNVIVVHndFkACmozGVrk7pyWRYBvSJIG7VqF5S5Dd7PZwtP3919XArRkpgXFQaEm06N6jgT_x86X5D4QzSz4)

O percurso em pós-ordem visita os nós na seguinte ordem: 
- F, G, B, C, K, L, H, I, J, D, M, N, P, O, E, A

## Percurso em largura (*breadth-first search*)

^bde67f

No percurso em largura, todos os nós com profundidade $p$ são visitados antes daqueles com profundidade $d+1$.

```python
def bfs(T):
	Q = Queue()
	Q.push(T.root)
	while(not Q.is_empty()):
		p = Q.deque()
		visit(p)
		for c in T.children(p):
			Q.push(c)
```

Considere o exemplo a seguir com a árvore enraizada em $A$. 

![](https://mermaid.ink/img/pako:eNpV0M0OgjAMB_BXWXqGF9jBRByK-IGJHndpWBWiAzLHwRDe3bHswHrq799e2gnqXhFweBkcGvYQsmOutixNNyxbY8fWEpHyoMxrH-kQJLyKSMdIZVDhdVrjHEa51yXSNVIVVHndFkACmozGVrk7pyWRYBvSJIG7VqF5S5Dd7PZwtP3919XArRkpgXFQaEm06N6jgT_x86X5D4QzSz4)

O percurso em largura visita os nós na seguinte ordem: 
- A, B, C, D, E, F, G, H, I, J, M, N, O, K, L, P


## Aplicações de percursos em árvores

- Contabilizar a memória ocupada pelos arquivos em um diretório (composto de arquivos que podem ser outros diretórios). 
- Copiar uma árvore.
- Deletar uma árvore


# Referências
- Goodrich, M. T., Tamassia, R., & Goldwasser, M. H. (2014). _Data structures and algorithms in Java_. John Wiley & Sons.