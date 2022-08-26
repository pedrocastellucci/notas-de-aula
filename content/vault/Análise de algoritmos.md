---
title: "Análise de algoritmos"
---


# Análise de algoritmos

## O que é complexidade computacional?

A complexidade computacional de um algoritmo é uma medida da quantidade de recursos computacionais utilizados. Esses recursos são: Tempo e espaço (memória).

O tempo de execução é determinado por dois fatores:
- O custo de execução de cada comando.
	- Depende do computador, compilador, linguagens de programação, sistema operacional entre outros.
- A frequência de execução de cada comando.
	- Depende do algoritmo e da entrada.

A separação desses dois fatores permite uma análise de algoritmos independente da plataforma computacional. 

Operações elementares:
- Operação com número de passos constante.

### Exemplos

Qual a quantidade de memória e o número de operações utilizados pela função a seguir, que recebe uma lista $L$? #pergunta 

```
function count_even(L):
	count = 0
	for x in L:
		if x % 2 == 0:
			count = count+1
	return count	
```

O que acontece com a memória utilizada e o número de operações conforme o tamanho da lista $L$ varia? #pergunta 

> A análise de complexidade de algoritmos busca caracterizar a quantidade de memória e o número de operações conforme o tamanho da entrada aumenta. 

Um outro exemplo é o algoritmo a seguir.
```
# Considera a lista L indexada a partir do zero
function f(L):
	i = 0
	n = len(L)
	while i < n/2:
		L[i], L[n-i-1] = L[n-i-1], L[i]
		i = i+1
```

- O que o algoritmo realiza? #pergunta 
	- Inverte a lista $L$.
- O algoritmo executa as mesmas operações para qualquer lista de tamanho $n$. Cada passo executado corresponde à troca de posição entre dois elementos da lista. Ou seja, cada passo corresponde à execução de uma iteração do laço. Além disso, são executados $n/2$ passos. 

#### Soma e produto de matrizes

Considere duas matrizes $A=(a_{ij})$ e $B=(b_{ij})$, ambas com dimensão $n \times n$. A obtenção da matriz soma $C_{ij}$ pode ser realizada pelo seguinte algoritmo.
```python
for i = 1, ..., n
	for j = 1, ..., n
		c[i, j] = a[i, j] + b[i, j]
```

Cada passo do algoritmo corresponde à execução de uma soma $a_{ij} + b_{ij}$. Quantas vezes essa soma será realizada? #pergunta 

Para a obtenção da matriz produto $\displaystyle D_{ij} = \sum_{1\leq k \leq n}a_{ik}b_{kj}$
```python
for i = 1, ..., n
	for j = 1, ..., n
		c[i, j] = 0
		for k = 1, ..., n
			c[i, j] = c[i, j] + a[i, j]*b[k, j]
```

O comando mais executado no algoritmo é a linha $c[i, j] = c[i, j] + a[i, j]*b[k, j]$. Quantas vezes ela é executada? #pergunta

## Notação Big-O

> A notação Big-O (Grande O) descreve matematicamente como o uso de recurso varia em relação às variáveis de entrada.


### Alguma regras

- Ignorar as constantes. Termos de ordem menor são relevantes apenas para entradas pequenas. 

#### Alguns exemplos $O(n)$
- $O(a + n)$ = $O(n)$ se $a$ é constante
```
function count_even(L):
	count = 0
	for x in L:
		if x % 2 == 0:
			count = count+1
	return count	
```

- $O(n + n) = O(2n) = O(n)$
```
	function min_max1(L):
		small = +infinity
		big = -infinity
		for x in L:
			small = min(small, x)
		for x in L:
			big = max(big, x)
		return small, big
```

```
	function min_max1(L):
		small = +infinity
		big = -infinity
		for x in L:
			small = min(small, x)
			big = max(big, x)
		return small, big
```


#### Comportamento assintótico
- Ignorar termos de ordem menor. Termos de ordem menor são relevantes apenas para entradas pequenas. Estamos interessados em casos com entradas grandes ($n \rightarrow \infty$). 
	- Por quê? #pergunta 


## Complexidade de pior caso

Há algoritmos em que o número de operações executadas depende da entrada. 

```
function busca(x, v):
	i = 0
	while i < n:
		if x == v[i]
			return True
		i = i + 1
	return False
```

Nesses casos, frequentemente, o interesse está na complexidade de pior caso, isto é, o caso que está relacionada com o maior número de operações. Outro caso importante é a análise de caso médio, isto é, em determinar, na média, qual a complexidade do algoritmo. Essa análise pode ser bastante sofisiticada e, em geral, está fora do escopo deste material.

## Algumas classes de complexidade

### Ordem de complexidade linear, $O(n)$

```
function busca(x, v):
	i = 0
	while i < n:
		if x == v[i]
			return True
		i = i + 1
	return False
```

### Ordem de complexidade quadrática, $O(n^2)$
Supondo que as listas $va$ e $vb$ possuem $n$ elementos.

```
function busca(va, vb):
	for x in va:
		for y in vb:
			if x == y:
				return True
	return False
```

### Ordem de complexidade logarítimica, $O(log\ n)$

Quantas vezes é necessário dividir um número positivo $n > 0$ pela metade para chegar à unidade?

```
function divisoes(n):
	i = 0
	while n != 1:
		n = n//2
		i = i+1
	return i
```

### Comparação entre classes

Os gráficos a seguir apresentam uma comparação visual entre as classes. No eixo horizontal está o tamanho do problema e no eixo vertical o custo (ambos em escala arbitrária).

![[Pasted image 20220419152228.png|500]]

![[Pasted image 20220419152332.png|500]]

![[Pasted image 20220419152407.png|500]]

# Referências e outros materiais
- Complexidade de Algoritmos I - Noção Intuitiva. Canal do Youtube: Programação Dinâmica. https://youtu.be/KVlGx-9CuO4
- Notação do O Grande - Complexidade de Algoritmos II. Canal do Youtube: Programação Dinâmica. https://youtu.be/UQzCFkRbIrE
- [[2011Sedgewick_Algorithms|Algorithms (Sedgewick e Wayne. 2011)]]
- Big O Notation. Canal do Youtube Hacker Hank. https://www.youtube.com/watch?v=v4cd1O4zkGw
- J. Szwarcfiter e L. Markenzon (1994). Estruturas de dados e seus algoritmos (2a Edição). 
