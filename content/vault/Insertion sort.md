# Ordenação por inserção

A ordenação por inserção funciona da mesma forma que muitas pessoas  ordenam cartas em sua mão. 

1. Inicia-se com uma mão vazia.
2. Remove-se então uma carta da mesa, inserindo-a na posição correta na mão.
	1. Para encontrar a posição correta, percorre-se as cartas na mão da direita para a esquerda.

Note que a qualquer momento, o conjunto de cartas na mão está ordenado.

## Um pseudo-código

Considerando vetores indexados de $1$ a $n$, o pseudo-código a seguir implementa a ordenação por inserção.
```c
for j=2 to v.length
	key = v[j]
	i = j - 1
	while i > 0 and v[i] > key
		v[i+1] = v[i]
		i = i-1
	v[i+1] = key
```

### Análise do algoritmo

- Seja $v$ um vetor com $n$ elementos. 
	- Um pior caso acontece quando o vetor, inicialmente, está ordenado de forma descrescente.
		- Em uma iteração $j$ do laço mais externo, o elemento $A[j]$ será comparado com $(i-1)$ elementos. Portanto, a cada iteração do laço mais externo, são realizadas, respectivamente $$O(1 + 2 + 3 + (n-1)) = O\Big(\frac{n(n-1)}{2}\Big) = O(n^2)$$ comparações.
		- No pior caso, também são realizadas $O(n^2)$ trocas de valores
	- No melhor caso, com o vetor já ordenado, toda comparação $v[i] > key$ do pseudocódigo é falsa, portanto, 
		- Não é realizada nenhuma troca;
		- São realizadas $O(n)$ comparações. 

- A ordenação é realizada de forma *inplace*, mantendo o custo de memória constante, $O(1)$. 
- O algoritmo de ordenação por inserção é estável.