---
title: "Árvores"
---

# Introdução

Árvores são estruturas de dados não lineares. Uma organização não linear é mais rica do que uma organização linear, em que há uma relação simples de predecessor ou sucessor entre dois objetos no conjunto. Em uma árvore, há relações **hierárquicas** com elementos sendo ancestrais ou descendentes de outro. 

Um exemplo é a relação de orientação acadêmica da árvore a seguir.

## Definições e propriedades

> [!CITE] (Goodrich et al, 2014)
> Uma árvore $T$ é um conjunto de nós (que armazenam elementos) de forma que os nós possuem relação de pai-filho da seguinte forma:
>> -  Se $T$ é não vazia, ela contém um nó chamado **raiz**, que não possui pai.
>> - Cada nó em $v \in T$, que não é a raiz, possui um único pai $w \in T$ (cada nó com pai $w$ é chamado de filho de $w$).

Note que essa definição é recursiva, de forma que uma árvore $T$ é vazia ou consiste de uma raiz que possui um conjunto sub-árvores filhas.

> [!INFO] Outras definições
> - Dois nós que são filhos de um mesmo pai são chamadas de irmãos.
> - Um nó é chamado de **externo** se não possui filhos (também são chamados de **folhas**.
> - Um nó é chamado de **interno** se possui pelo menos um filho.
> - Um nó $u$ é ancestral de $v$ se $u = v$ ou se $u$ é ancestral do pai de $v$.
> - Um nó $v$ é descendente de um nó $u$ se $u$ é um ancestral de $v$.
> - Uma **aresta** em uma árvore $T$ é um par de nós $(u, v)$ tal que $u$ é pai de $v$, ou vice-versa
> - Um **caminho** em uma árvore $T$ é uma sequência de nós em $T$ de forma que quaisquer dois nós consecutivos na sequência formam uma aresta de $T$.
> - Uma árvore é **ordenada** se existe uma relação de ordem linear entre os filhos de qualquer nó.

### Profundidade e altura de uma árvore

> [!INFO]
> Seja $p$  um nó da árvore. A profundidade de $p$ é o número de ancestrais que $p$ possui, com exceção dele mesmo

- Note que, pela definição, 
	- se $p$ é a raiz da árvore então a profunidade de $p$ é zero; 
	- senão a profundidade de $p$ é igual a profundidade do pai de $p$ mais um.
Com isso, pode-se construir o seguinte algoritmo, que computa a profundidade de um nó $p$.

```python
def depth(p):
	if (isRoot(p)):
		return 0
	else:
		return 1 + depth(parent(p))
```

O algoritmo tem custo de pior caso $O(d_p)$ em que $d_p$ é a profundidade do nó $p$.

> [!INFO]
> A altura de um nó $p$ de uma árvore $T$:
> - é igual a zero se $p$ é folha da árvore;
> - caso contrário, é igual a um a mais do que a maior altura do seu maior filho.

```python
def height(p):
	if (isLeaf(p)):
		return 0
	else:
		return 1 + max(height(p) for p in p.children())
```

O custo de pior caso do algoritmo para a altura é $O(n)$ visto que, se chamado a partir da raiz da árvore, todos os nós serão percorridos e o custo para cada chamada da função é constante. 

Repare na ordem com que os nós da árvore são percorridos tanto no algoritmo para o cálculo da profundidade quanto da altura. Um tema importante em estruturas não lineares é como realizar o percurso nessas estruturas. Ou seja, como visitar todos os seus elementos de forma eficiente. 

## Percursos em árvores

As principais estratégias para se percorrer uma árvore são: percurso em pré-ordem, percurso em pós-ordem e percurso em largura. Dependendo da tarefa a ser realizada, um percurso pode ser mais adequado que outro, facilitando a implementação. Todos os algoritmos implementados a seguir possuem custo $O(n)$, sendo $n$ o número de nós da árvore. Tente entender o porquê.x

### Percurso em pré-ordem

No percurso em pré-ordem, a raiz da árvore é visitado primeiro, então são visitadas todas as subárvores filhas da raiz são visitadas recursivamente (também em pré-ordem). Caso a árvore seja ordenada, então as subárvore são visitadas de acordo com a propriedade de ordenação definida.

```python
def preorder(T):
	visit(T.root)
	for c in T.children():
		preorder(c)
```

Considere o exemplo a seguir com a árvore enraizada em $A$. 

[![](https://mermaid.ink/img/pako:eNpV0M0OgjAMB_BXWXqGF9jBRByK-IGJHndpWBWiAzLHwRDe3bHswHrq799e2gnqXhFweBkcGvYQsmOutixNNyxbY8fWEpHyoMxrH-kQJLyKSMdIZVDhdVrjHEa51yXSNVIVVHndFkACmozGVrk7pyWRYBvSJIG7VqF5S5Dd7PZwtP3919XArRkpgXFQaEm06N6jgT_x86X5D4QzSz4)](https://mermaid.live/edit#pako:eNpV0M0OgjAMB_BXWXqGF9jBRByK-IGJHndpWBWiAzLHwRDe3bHswHrq799e2gnqXhFweBkcGvYQsmOutixNNyxbY8fWEpHyoMxrH-kQJLyKSMdIZVDhdVrjHEa51yXSNVIVVHndFkACmozGVrk7pyWRYBvSJIG7VqF5S5Dd7PZwtP3919XArRkpgXFQaEm06N6jgT_x86X5D4QzSz4)

O percurso em pré-ordem visita os nós na seguinte ordem: 
- A, B, F, G, C, D, H, K, L, I, J, E, M, N, O, P


### Percurso em pós-ordem

No percurso em pós-ordem, as subárvores da raiz são percorridas recursivamente (em pós-ordem) antes da raiz. Caso a árvore seja ordenada, então as subárvore são visitadas de acordo com a propriedade de ordenação definida.

```python
def postorder(T):	
	for c in T.children():
		postorder(c)
	visit(T.root)
```

Considere o exemplo a seguir com a árvore enraizada em $A$. 

[![](https://mermaid.ink/img/pako:eNpV0M0OgjAMB_BXWXqGF9jBRByK-IGJHndpWBWiAzLHwRDe3bHswHrq799e2gnqXhFweBkcGvYQsmOutixNNyxbY8fWEpHyoMxrH-kQJLyKSMdIZVDhdVrjHEa51yXSNVIVVHndFkACmozGVrk7pyWRYBvSJIG7VqF5S5Dd7PZwtP3919XArRkpgXFQaEm06N6jgT_x86X5D4QzSz4)

O percurso em pós-ordem visita os nós na seguinte ordem: 
- F, G, B, C, K, L, H, I, J, D, M, N, P, O, E, A

### Percurso em largura (*breadth-first search*)

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

[![](https://mermaid.ink/img/pako:eNpV0M0OgjAMB_BXWXqGF9jBRByK-IGJHndpWBWiAzLHwRDe3bHswHrq799e2gnqXhFweBkcGvYQsmOutixNNyxbY8fWEpHyoMxrH-kQJLyKSMdIZVDhdVrjHEa51yXSNVIVVHndFkACmozGVrk7pyWRYBvSJIG7VqF5S5Dd7PZwtP3919XArRkpgXFQaEm06N6jgT_x86X5D4QzSz4)

O percurso em largura visita os nós na seguinte ordem: 
- A, B, C, D, E, F, G, H, I, J, M, N, O, K, L, P


# Referências
- Goodrich, M. T., Tamassia, R., & Goldwasser, M. H. (2014). _Data structures and algorithms in Java_. John Wiley & Sons.