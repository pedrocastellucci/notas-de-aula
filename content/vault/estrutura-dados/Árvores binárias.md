---
title: "Árvores binárias"
alias: [árvore binária]
---

# Árvores binárias

> [!CITE] (Goodrich et al, 2013)
> Um árvore binária é uma [[árvore]] ordenada em que:
> - Cada nó possui no máximo dois filhos.
> - Cada filho é nomeado com filho da esquerda e filho da direita.
> - O filho da esquerda precede o da direita.

Uma árvore binária é chamada de **própria** se cada nó tem zero ou dois filhos (caso contrário a árvore é chamada de **imprópria**). Portanto, em uma árvore binária própria, cada nó interno possui dois filhos.

Também, é possível definir uma árvore binária de forma recursiva.
> [!CITE] (Goodrich et al, 2013)
> Uma árvore binária $T$ é vazia ou consiste de:
> - um nó $r$, chamado de raiz da árvore $T$;
> - uma árvore binária (possivelmente vazia), chamada de subárvore esquerda de $T$;
> - uma árvore binária (possivelmente vazia), chamada de subárvore direita de $T$.

Uma outra definição que nos será útil é a de árvore completa.
> [!INFO]
> Uma árvore binária é completa se em todos os seus níveis, com possível exceção do último, estão completamente cheios e todos os nós estão o mais à esquerda possível.

^f23f12

## Exemplos

Árvores binárias podem ser utilizadas para representar operações aritméticas. Por exemplo, a expressão "A*B+C*D-E" pode ser representada pela árvore binária a seguir. 

[![](https://mermaid.ink/img/pako:eNpdj7EOwjAMRH_F8kibgY4ZkIDyBWUjDFZjaEWTViEZUNV_J02XKvbid7qTzjO2o2aU-HY0dXCvlYU4AoQ4QbGHG2xUJDJhOD4Oz01aIannjC9ZpNpHqqReIRNig3WxRMPOUK9juXn1KPQdG1Yo46nJfRQqu0QfBT82P9ui9C5wiWHS5LnuKf5kUL5o-PLyB1CmQQY)](https://mermaid.live/edit#pako:eNpdj7EOwjAMRH_F8kibgY4ZkIDyBWUjDFZjaEWTViEZUNV_J02XKvbid7qTzjO2o2aU-HY0dXCvlYU4AoQ4QbGHG2xUJDJhOD4Oz01aIannjC9ZpNpHqqReIRNig3WxRMPOUK9juXn1KPQdG1Yo46nJfRQqu0QfBT82P9ui9C5wiWHS5LnuKf5kUL5o-PLyB1CmQQY)

- [[Árvores de decisão]]
- Árvores de [[Branch-and-bound]]

## Propriedades de uma árvore binária

> [!INFO]
> Seja T uma árvore binária completa com $n >0$ nós. Então $T$ possui altura $h$ mínima.

> [!INFO]
> A altura de uma árvore binária completa $T$ com $n$ nós é $h = \lfloor log\ n \rfloor$. 
> Pode-se mostrar tal propriedade utilizando indução.
>> Se $n = 1$, então $h = \lfloor log\ n \rfloor = 0$, provando o caso base.
>> Para $n > 1$, suponha que o resultado é válido para todas as árvores com $n-1$ nós. Seja $T'$ a árvore obtida pela remoção dos $k$ nós do último nível de $T$. Logo $T'$ é uma árvore cheia com $n' = n - k$ nós. Pela hipótese indutiva, $h(T') = \lfloor log\ n' \rfloor$. Além disso, $T'$ é uma árvore cheia, tendo portando $n' = 2^{m+1}-1$ nós, sendo $m$ a altura de $T'$. Então $$h(T) = 1 + h(T') = 1 + m = log\ (n' + 1).$$ Mas $1 \leq k \leq n'+1$, portanto $\lfloor log\ (n' + 1) \rfloor = \lfloor log\ (n' + k) \rfloor < log\ (2n' + 2)$. Portanto, $$h(T) = log\ (n' + 1) = \lfloor log\ (n' + k) \rfloor = \lfloor log\ (n) \rfloor$$

## Percurso em-ordem em árvores binárias

Além dos [[vault/estrutura-dados/Percursos em árvores|percursos em árvores]] já definidos, em árvores binárias também há o percurso em-ordem (ou ordem simétrica)

```python
def inorder(T, root):
	if (root):
		inorder(T, root.left)
		visit(root)
		inorder(T, root.right)
```

## Implementações de árvore binária

É possível implementar árvores binárias utilizando uma estrutura encadeada, em que cada nó é possui referências para o filho da esquerda e da direita respectivamente. 

<iframe src="https://excalidraw.com/#json=HDqoj4NnCNbcTraYTnsmE,KhO4A-xOZ_MYLIO47iTFVA" height="600" width="600" title="Binary tree linked implementation"></iframe>

Para codificar tal solução é possível utilizar uma estrutura (ou classe) como a seguir:

```python
class Node:
	def __init__(self):
		self.value = None
		self.left = None
		self.right = None
```

Os algoritmos de busca, inserção e remoção frequentemente se aproveitam de outras propriedades como no caso de [[Árvores binárias de busca]].

Outra opção é utilizar uma [[Árvores binárias implementadas em vetor|implementação em vetor]], que é utilizada em situações mais específicas, como na implementação de um [[Heap|heap]].

# Referências
- Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2009). Introduction to Algorithms. third. _New York_.
