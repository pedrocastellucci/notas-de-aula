---
title: "Heapsort"
---

# Ordenação com o *Heapsort*

O algoritmo de ordenação *heapsort* pode ser considerado uma sofisticação do [[Selection sort]] (ordenação por seleção). Frequentemente, quando é necessário projetar um algoritmo que faz requisições frequentes ao menor (ou maior) elemento de um coleção um [[Heap]] pode ser útil. Esse é o caso do algoritmo de ordenação por seleção.

Em uma iteração do [[Selection sort]], é feita uma requisição pelo menor elemento que está na porção ainda não ordenada do vetor. Com isso, surge a ideia do *Heapsort*: 
- Adicionar os elementos de vetor em um *Heap*.
- Em cada iteração, extrair um elemento do *Heap* e 
- colocá-lo na posição correta do vetor.

Cada extração no *heap* possui custo $O(log\ n)$ e são necessários $n$ extrações, portanto, o *heapsort* é um algoritmo $O(n\ log\ n)$.

O pseudo-código a seguir ilustra tal implementação considerando um vetor $v$ indexado de $1$ até $v.length$. Note que, para a operação *downheap*, apenas a parte do vetor que não está ordenada é passada como parâmetro. Ou seja, a cada iteração o maior elemento é posicionado corretamente no vetor.

```cpp
for i=2 to v.length
	upheap(v, i)
	
for i=v.length to 2
	swap(v[1], v[i])
	downheap(v[1..(i-1)], 1)
```

- O algoritmo é, de fato, $O(n\ log \ n)$ pois tanto o primeiro quanto o segundo laço executam $O(n)$ vezes e as operações de *upheap* e *downheap* possuem custo $O(log\ n)$.
- A ordenação ocorre *inplace* portanto o custo de memória adicional utilizada é constante, $O(1)$. 
- O algoritmo de *heapsort* não é estável. 
- Embora o algoritmo já seja $O(n\ log\ n)$ é possível melhorar o passo de construção do *heap*.

## Construindo a *heap*

Para construir um *heap* a partir de um vetor não ordenado, podemos partir da observação de que a metade direita de um vetor pode ser considerada como vários *heaps* de tamanho unitário (folhas da árvore). 

Seja $v[1, \ldots, n]$ um vetor não ordenado. Os elementos 
$v[(\lfloor \frac{n}{2}\rfloor+1) .. n]$ podem ser considerados *heap* com apenas um elemento. Com isso, para construir um *heap*, pode-se utilizar a operação *downheap* em cada elemento da primeira metade do vetor, como mostra o algoritmo a seguir.

```cpp
for i = floor(v.length/2) to 1:
	downheap(v, i)
```


### Análise da construção da *heap*

Uma análise apressada pode levar a uma complexidade $O(n log \ n)$ pois uma chamada para a função *downheap* possui custo $O(n)$. No entanto, observe que:
- Para os $\frac{n}{2}$ últimos elementos do vetor, nenhuma troca é realizada. 
- Para os próximos $\frac{n}{4}$ elementos do vetor, no máximo 1 troca é realizada.
- Para os próximos $\frac{n}{8}$ elementos do vetor, no máximo 2 trocas são realizadas. 
- Em geral temos, no pior caso, $\frac{n}{2^{(k+1)}}$ elementos realizando $k$ trocas, para $k = 0, \ldots, log \ n-1$.
- Com isso, o número total de trocas é limitado por $$\frac{n}{2}0 + \frac{n}{4}1 + \frac{n}{8}2 + \ldots + \frac{n}{ (2^{log\ n})}(log\ n - 1)$$ de forma condensada, tem-se $$\sum_{i=0}^{log\ n - 1}\frac{n}{2^{i+1}}i = \frac{n}{2} \sum_{i=1}^{log\ n - 1}\frac{i}{2^{i}}$$
Para avaliar tal expressão, note que  $$\sum_{i=0}^{log\ n - 1}\frac{i}{2^{i}} \leq \sum_{i=1}^{\infty}\frac{i}{2^{i}}.$$ Mas 
$$\begin{align}\sum_{i=1}^{\infty}\frac{i}{2^{i}} &= &\frac{1}{2} & + \frac{2}{4} + \frac{3}{8} + \frac{4}{16} + \ldots\\ 
	& = & \frac{1}{2} & + \frac{1}{4} + \frac{1}{8} + \frac{1}{16} + \ldots +\\
	& + & 0 &+  \frac{1}{4} + \frac{1}{8} + \frac{1}{16} + \ldots +\\
	& + & 0 &+ 0 + \frac{1}{8} + \frac{1}{16} + \ldots +\\
	& + & 0 &+ 0 + 0 + \frac{1}{16} + \ldots +\\
\end{align}$$
Como $$\sum_{i=\ell}^{\infty} \frac{1}{2^i} = \frac{1}{2^{(\ell-1)}},$$ pois se trata de uma série geométrica infinita. Então, tem-se:  
$$\sum_{i=1}^{\infty}\frac{i}{2^{i}} = 1 + \frac{1}{2} + \frac{1}{4} + \frac{1}{8} + \ldots = 1 + 1 = 2$$
Portanto, o custo do algoritmo de construir a *heap* a partir de um vetor não ordenado pode ser descrito mais especificamente como:

$$O\Big(\frac{n}{2} \sum_{i=1}^{log\ n - 1}\frac{i}{2^{i}}\Big) \leq O\Big(\frac{n}{2} \sum_{i=1}^{\infty}\frac{i}{2^{i}}\Big) = O\Big(\frac{n}{2} 2\Big) = O(n).$$

> Como demonstrado, construir uma heap a partir de um vetor não ordenado pode ser feito em custo linear no tamanho do vetor.

## Versão melhorada do heapsort

Combinando a construção do *heap* em ordem linear com as ideias apresentadas anteriormente, tem-se uma versão melhorada do *heapsort*.

```cpp
for i = floor(v.length/2) to 1:
	downheap(v, i)
	
for i=v.length to 2
	swap(v[1], v[i])
	downheap(v[1..(i-1)], 1)
```

### Análise do algoritmo

A análise da versão melhorada é a mesma feita anteriormente, com exceção de que, na versão melhorada, a construção do *heap* é feita em tempo linear, $O(n)$.

No algoritmo de *heapsort* o número de trocas e de comparações é equivalente em termos de análise assintótica, ambos são $O(n\ log \ n)$. 

- Qual o custo do algoritmo se ele for aplicado em um vetor ordenado de forma crescente? #pergunta 
- Qual o custo do algoritmo se ele for aplicado em um vetor ordenado de forma descrescente? #pergunta 

## Implementação do heapsort em Python

O Python oferece o pacote *heapq* que empacota algumas operações para *heaps* de **mínimo**. Para a implementação do algoritmo de *heapsort*, no entanto, é necessário multiplicar todos os valores por -1, para que seja implementado o algoritmo apresentado

```python
import heapq

def downheap(values, i, n):
    left = 2*i + 1
    right = 2*i + 2
    max_child = None
    if left <= n:
       max_child = left
       if right <= n and values[max_child] > values[right]:
           max_child = right
    if max_child is not None and (values[i] > values[max_child]):
        values[i], values[max_child] = values[max_child], values[i]
        downheap(values, max_child, n)


def heapsort(values):
    heapq.heapify(values)    
    for i in range(len(values)-1, 0, -1):
        values[0], values[i] = values[i], values[0]
        downheap(values, 0, i-1)

```

Uma opção seria adaptar o algoritmo para utilizar um *heap* de mínimo, o que pode ser feito utilizando um *heap* separado de um vetor. Nesse caso, no entanto, a ordenação deixa de ser *inplace*. Em geral, a versão apresentada é preferida. 