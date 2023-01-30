---
title: "Quicksort"
---

# Quicksort

O algoritmo de ordenação *Quicksort*, assim como o [[Mergesort]] se utiliza do paradigma de divisão-e-conquista. Em linhas gerais, seu algoritmo pode ser divido em três passos:

1. Divisão: particione o vetor $v[p..r]$ em dois subvetores (possivelmente vazios) $v_1 = v[p..(q-1)]$ e $v_2 = v[(q+1).. r]$ de forma que todos os elementos em $v_1$ não ultrapassem o valor de $v[q]$ que, por sua vez, não ultrapassa os valores em $v_2$.
2. Conquista: Ordene os dois subvetores $v_1$ e $v_2$ utilizando o *quicksort* recursivamente.
3. Combinação: Como os dois subvetores estão ordenados, a combinação deles em um vetor completo $v[p..r]$ resulta em um vetor ordenado.

Em termos de pseudo-código, tem-se o seguinte.

```cpp
quicksort(v, p, r):
	if p < r:
		q = partition(v, p, r)
		quicksort(v, p, q-1)
		quicksort(v, q+1, r)
```

Para ordenador o vetor completamente, a chamada inicial deve ser *quicksort(v, 1, v.length)* considerando um vetor indexado de $1$ até $v.length$. 

A chave para o funcionamento do algoritmo é o procedimento de partição (particionamento).

## Particionamento

O algoritmo de partição funciona da seguinte forma.

```cpp
partition(v, p, r)
	x = v[r]
	i = p-1
	for j = p to (r-1)
		if v[j] <= x
			i = i + 1
			swap(v[i], v[j])
	swap(v[i+1], v[r])
	return i+1
```
	
No começo de cada iteração do laço, para qualquer índice $k$ no vetor
1. Se $p \leq k \leq i$, então $A[k] \leq x$.
2. Se $i+1 \leq k \leq j-1$, então $A[k] > x$.
3. Se $k = r$, então $A[k] = x$.

Acompanhe o algoritmo no exemplo a seguir (extraído de [[2009Cormen_IntroductionToAlgorithms|Cormen et al. (2009)]]).

![[Pasted image 20221123133719.png]]

Note que, ao final, o vetor é de fato particionado na posição indicada pelo algoritmo. 

### Análise do particionamento

O custo computacional do algoritmo de particionalmento é $O(n)$ para um vetor de tamanho $n$ no pior caso. 


## Análise do *quicksort*

O custo computacional do *quicksort* depende da qualidade do particionamento. Um bom particionamento é aquele que divide o vetor aproximadamente ao meio. 

- No pior caso, o particionamento produz um vetor de tamanho zero e outro vetor com $n-1$ elementos. Seja $T(n)$ o número de chamadas da função *quicksort* para um vetor de tamanho $n$, então
	- $T(n) = T(0) + T(n-1) + 1 = T(n-1) + 2$, o que resulta em $O(n)$ chamadas.
		- Como em cada chamada é realizado um particionamento, com custo $O(n)$, então o custo total é $O(n^2)$ operações.
- No melhor caso, o particionamento produz dois vetores de tamanho aproximadamente $\frac{n}{2}$. Portanto, o custo de cada chamada da função é dado por:
	- $$\begin{align} T(n) &=  2T\Big(\frac{n}{2}\Big) + O(n)\\ & = 2\Bigg[2T \Big(\frac{n}{4}\Big) + O(n)\Bigg] + O(n) = 4T\Big(\frac{n}{4}\Big) + 3O(n) \\ &= 2\Bigg[2T \Big(\frac{n}{8}\Big) + O(n)\Bigg] + 3 O(n) =  8T\Big(\frac{n}{8}\Big) + 5O(n)\\ &= 2\Bigg[2T \Big(\frac{n}{16}\Big) + O(n)\Bigg] + 5 O(n) = 16T\Big(\frac{n}{16}\Big) + 7O(n). \end{align}$$ No caso geral, tem-se $$T(n) = 2^{k}T\Big(\frac{n}{2^{k}}\Big) + (2k - 1)O(n), \quad k = 1, \ldots, log\ n.$$ Para $k = log\ n$, tem-se: $$T(n) = nT(1) + (2log\ n - 1)O(n) = O(n\ log\ n)$$ O caso médio do *Quicksort* é muito mais próximo de melhor caso do que do pior. Por isso, *Quicksort* costuma ter um custo computacional (tempo) menor do que outros algoritmos cujos piores casos são $O(n\log\ n)$ como o [[Heapsort]].

- Qual o tempo computacional do *Quicksort* apresentado quando todos os elementos possuem o mesmo valor? #pergunta 
- Qual o tempo computacional do *Quicksort* quando o vetor está ordenado de forma descrescente? #pergunta 