# Versão recursiva do cálculo da exponenciação

O cálculo da exponenciação $x^n$, com $n$ inteiro e positivo pode ser feito através da seguinte formulação recursiva $$x^n = \begin{cases}x & \mbox{se } n = 1,\\ x\cdot x^{n-1} & \mbox{se } n > 1.\end{cases}$$
Implemente a função recursiva para o cálculo da exponenciação. #exercício
Com essa função, o cálculo da exponenciação $x^n$ é $O(n)$. Por quê? #pergunta 

## Versão melhorada

Uma formulação melhor é a seguinte. 
$$x^n = \begin{cases}
x & \mbox{se } n = 1,\\
x^{\frac{n}{2}}\cdot x^{\frac{n}{2}} & \mbox{se $n$ é par,}\\
x \cdot x^{\frac{n}{2}}\cdot x^{\frac{n}{2}} & \mbox{se $n$ é ímpar}. 
\end{cases}$$
A função recursiva pode ser implementada da seguinte forma.

```python
def pot(x, n):
    if n == 1:
        return x    
	total = pot(x, n//2)
	total = total*total
	if n % 2 == 0:
		return total
	else:
		return total*x
```


### Análise do algoritmo

Para uma análise intuitiva, podemos observar que a cada chamada recursiva o problema é dividido aproximadamente ao meio. Com isso, o número de chamadas recursivas é da ordem de $log (n)$. Como, a cada chamada, é realizada um número constante de operações. O algoritmo é $O(log(n))$.

Qual o custo computacional do algoritmo implementado a seguir #exercício 

```python
def pot(x, n):
    if n == 1:
        return x    
	total = pot(x, n//2)*pot(x, n//2)
	if n % 2 == 0:
		return total
	else:
		return total*x
```