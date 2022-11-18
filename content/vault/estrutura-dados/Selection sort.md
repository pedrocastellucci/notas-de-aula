---
title: "Selection sort"
---

# Ordenação por seleção

- A ideia da ordenação por seleção é a seguinte: 
	- A cada iteração $i$, encontra-se o $i$-ésimo menor elemento do vetor, e então troca-o com o elemento na posição $i$.

Um pseudo-código da ordenação por seleção é dado a seguir.

```cpp
for i=1 to v.length-1:
	min = i;
	for j = i+1 to v.length:
		if v[j] < v[min]:
			min = j
	swap(v[i], v[min])
```

- Note que, ao final de cada iteração, o subvetor $v[1..i]$ está ordenado.

## Análise do algoritmo
- Encontra o menor elemento em um vetor não ordenado de tamanho $n$ tem custo $O(n)$. Essa tarefa é realizada pelo laço mais interno $n$ vezes. No entanto, a cada iteração do laço externo, o subvetor utilizado na busca é menor. Portanto, o custo total dessa busca é $$O((n-1) + (n-2) + \ldots + 2) = O(n^2).$$
	- No pior caso (e no melhor), são realizadas:
		- $O(n^2)$ comparações.
		- $O(n)$ trocas.
		- O fato de o custo do algoritmo não ser tão dependende da configuração do vetor (um vetor quase ordenado, por exemplo) é tido como uma desvantagem.
- O algoritmo é *inplace*, possuindo um custo de memória constante, $O(1)$.
- A ordenação por seleção **não** é estável.
- A cada iteração, o algoritmo de ordenação por seleção busca pelo menor elemento restante. A busca pelo menor elemento pode ser feita de forma mais eficiente com a utilização de uma [[Heap]]. Isso dá origem ao algoritmo de ordenação [[Heapsort]].