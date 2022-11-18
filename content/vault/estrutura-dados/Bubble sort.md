---
title: "Bubble sort"
---

# Ordenação por transposição

A ordenação por transposição (*Bubble Sort*) funciona realizando trocas de elementos adjacentes que estão fora de ordem em uma sequência. Se não for necessário realizar a troca de nenhum par de elementos, então a sequência já está ordenada. 

## Primeiras versões 
Uma primeira versão de um pseudo-código para o *Bubble Sort* é dada a seguir, considerando um vetor indexado de $1$ até $n$.

```cpp
changed = True
while changed == True:
	changed = False
	for i = 2 to v.length:
		if v[i-1] > v[i]:
			swap(v[i-1], v[i])
			changed = True
```

- O algoritmo pára? #pergunta 
	- Ele pára pois em um vetor ordenado, tem-se que $v[i-1] < v[i]$ para todo para $i=2, \ldots n$.
- Qual o número máximo de vezes em que o laço mais externo é executado? #pergunta 
	- O maior número de vezes é $n$, pois na $j$-ésima iteração do vetor, o $j$-ésimo maior valor do vetor é posicionado na posição $(n-j+1)$ do vetor. Isso permite uma implementação melhorada do algoritmo

```cpp
for j = 1 to v.length:
	for i = 2 to v.length:
		if v[i-1] > v[i]:
			swap(v[i-1], v[i])
```


### Análise do algoritmo *Bubble sort*
- O pior caso ocorre quando o vetor a ser ordenado está em ordem descrescente
	- Conforme as iterações do laço mais externo, o número de trocas realizadas pelo laço mais interno é (no pior caso), respectivamente, $$O((n-1) + (n-2) + \ldots + 1) = O\Big(\frac{n(n-1)}{2}\Big) = O(n^2).$$
	- Por uma argumentação semelhante, o número de comparações realizadas pelo algoritmo, no pior caso, também é $O(n^2)$.
- O melhor caso acontece quando o vetor já está ordenado. 
	- Nesse caso, são feitas $O(n^2)$ comparações e
	- nenhuma troca.

- A ordenação é feita de forma *inplace* portanto, é utilizada uma quantidade constante de memória. 

- Além disso, o algoritmo de ordenação é estável pois nunca há necessidade de inverter dois valores iguais adjacentes. 
	- O que acontece se a comparação for trocada de $v[i-1]> v[i]$ para $v[i-1] \geq v[i]$? #pergunta 


## Versões melhoradas

- Contudo, é possível realizar uma melhora no algoritmo a partir da observação de que o subvetor $v[n-j, \ldots, n]$ se encontra ordenado ao final da $j$-ésima iteração do laço externo. O laço mais interno, não precisa percorrer o subvetor $v[n-j, \ldots, n]$.

```cpp
for j = 1 to v.length:
	for i = 2 to (v.length-j+1):
		if v[i-1] > v[i]:
			swap(v[i-1], v[i])
```

- É possível fazer mais uma melhoria.
	- Observe que todos os elementos a partir da última troca de valores já estão ordenados. Portanto, as iterações seguintes do laço mais interno precisam percorrer o vetor apenas até a posição da última inversão de valores.


```cpp
lim_idx = n
for j = 1 to v.length:
	last_inv_idx = 1
	for i = 2 to lim_idx:
		if v[i-1] > v[i]:
			swap(v[i-1], v[i])
			last_inv_idx = i
	lim_idx = last_inv_idx
```

### Análises das versões melhoradas

- A análise de pior caso das versões melhoradas só se altera por fatores constantes. Portanto, no pior caso:
	- São realizadas $O(n^2)$ trocas e comparações e
	- no melhor caso, são realizadas $O(n)$ comparações e nenhuma troca.
- As versões melhoradas também são *inplace*.
- As versões melhoradas também são estáveis.