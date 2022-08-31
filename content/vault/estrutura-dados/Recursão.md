---
title: "Recursão"
---

# Introdução
> To iterate is human, to recurse is divine (Laurence Peter Deutsch)

- Recursão é um conceito genérico presente em várias disciplinas e na própria natureza.
- Uma entidade (ou conceito) é recursivo quando é composto por instâncias menores dele mesmo (ou similares). 
- Alguns exemplo (Figura retirada de [[2017Sanchez_IntroductionRecursiveProgramming|Introduction to recursive programming. Sanchez (2019)]]): 
	- ![[Pasted image 20220412150007.png]]
	- Há também entidades menos concretas que são identificadas como recursivas. Por exemplo a sequência $(s_1, s_2, \ldots, s_n)$ definida de acordo com $$s_n = s_{n-1} + s_{n-2}.$$ A fórmula define que o $n$-ésimo termo da sequência é dado pela soma dos dois anteriores. Portanto, os termos da sequência são definidos a partir deles mesmos. Note que não é apenas uma sequência que é definida a partir da fórmula. 
		- Quais são exemplos de sequências que são definidas pelas fórmula apresentada #pergunta 
			- Tipicamente, se utiliza $s_1 = s_2 = 1$, o que define a [[Sequência de Fibonacci]].

## Alguns exemplos
- A [[Sequência de Fibonacci]] pode ser entendida como uma função definida da seguinte forma. $$F(n) = \begin{cases}1, & n = 1, \\ 1, & n = 2,\\ F(n-1) + F(n-2), & n \geq 3.\end{cases}$$
	- Note a existência de dois tipos de expressão:
		- Casos-base: Casos em que o resultado pode ser obtido de forma trivial ($n=1$ e $n=2$).
		- Casos recursivos: Casos em que há dependência de instâncias menores (mais simples) da própria função $(n \geq 3)$.
		- Em uma definição recursiva, é necessário ter pelo menos um caso-base? #pergunta 

```python
 def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)
```

- Outra função intrinsicamente recursiva é a fatorial de um número positivo $n$. $$n! = 1 \cdot 2 \cdot 3 \ldots \cdot n.$$ No entanto, não há uma dependência explícita da própria função fatorial. Para expressá-la de forma recursiva é necessário observar que $n! = (n-1)! \cdot n$. Com isso, tem-se: $$n! = \begin{cases} 1, & n = 1, \\ (n-1)! \cdot n & n \geq 2. \end{cases}$$
	- Qual o caso-base e qual o caso recursivo da função fatorial? #pergunta 

```python
def fat(n):
    if n == 0:
        return 1
    else:
        return fat(n-1)*n
```

- De forma similar, o problema de se calcular a soma dos $n$ primeiros números positivos pode ser formulado de forma recursiva. Uma função que representa a solução do problema é $$S(n) = 1 + 2 + \ldots + n.$$ Novamente, não é direta a definição recursiva de $S$. É necessário notar que $$S(n) = S(n-1) + n.$$
	- Para esse problema, como pode ser escrita a função recursiva? Identificando o caso-base e o caso recursivo #pergunta 

## Desenvolvendo uma solução recursiva*

O desenvolvimento de soluções recursivas para um problema depende da definição do(s) caso(s)-base e do(s) caso(s) recursivos. Em geral, o primeiro passo é definir casos-base e o maior desafio está em descrever os casos recursivos. Para isso, é necessário entender dois conceitos importantes:
1. Decomposição do problema
2. Indução

### Decomposição de um problema

A decomposição é um conceito importante não apenas no conceito de recursão. Trata-se da ideia de quebrar problemas complexos em problemas menores (mais simples) que sejam mais fáceis de expressar, computar ou resolver. No contexto de recursão, a decomposição de um problema consiste em quebrá-lo em subproblemas, alguns similares ao original. Com isso, a solução do problema original passa a consistir em resolver e combinar as soluções do subproblemas. É importante observar que a decomposição em subproblemas deve aproximar o problema original do(s) caso(s) base. 

- Considere o problema de encontrar a soma dos $n$ primeiros números positivos: $S(n) = 1 + 2 + \ldots + n$. Enquanto o caso base é $S(1) = 1$, é possível decompor o problema de diversas formas para definir os casos recursivas. 
	- Uma possibilidade é reduzir $n$ em apenas uma unidade. Nesse caso, o objetivo seria definir $S(n)$ em função de $S(n-1)$. 
		- Qual seria uma outra possibilidade? #desafio

- Considere o problema de computar a soma dos elementos em uma lista $L = [a_0, a_1, \ldots, a_{n-1}]$, $S(L) = \sum_{i=0}^{n-1}a_i$
	- O problema pode ser decomposto diminuindo o seu tamanho em uma unidade $$S(L) = \begin{cases}0, & n = 0,\\ S(L[0:n-1]) + a_{n-1}, & n > 0.\end{cases}$$
		- Qual é o caso-base e o caso recursivo do exemplo acima? #pergunta 
	- Uma opção, que também diminui o problema em uma unidade é $$S(L) = \begin{cases}0, & n = 0,\\ a_0 + S(L[1:n]), & n > 0.\end{cases}$$
		- Qual é o caso-base e o caso recursivo do exemplo acima? #pergunta
	- Também é possível separar o problema ao meio $$S(L) = \begin{cases}0, & n = 0,\\ a_0, & n = 1, \\ S(L[0:n//2]) + S(L[n//2:n]), & n > 1.\\ \end{cases}$$
		- Qual(is) o(s) caso(s)-base e o(s) caso(s) recursivo(s) do exemplo acima? #pergunta 
	- Os códigos a seguir implementam cada uma das alternativas, respectivamente.
	
```python
def sum_first1(L):
	n = len(L)
	if n == 0:
		return 0
	else:
		return sum_first1(L[0:n-1]) + L[n-1]

def sum_first2(L):	
    if len(L) == 0:
        return 0
    else:
        return L[0] + sum_first2(L[1:])

def sum_first3(L):
    n = len(L)
    if n == 0:
        return 0
    elif n == 1:
        return L[0]
    else:
        return sum_first3(L[0:n//2]) + sum_first3(L[n//2:])
```


	
### Indução

O termo *indução* é relacionado a provas matemáticas por indução. A ideia principal é que, ao se desenvolver uma solução recursiva, deve-se assumir que o código recursivo já funciona para instâncias menores (mais simples) do problema que se deseja resolver (mesmo que ele ainda não esteja implementado). 

Uma prova por indução é composta por duas partes:
1. O caso-base. Verificar que a fórmula é válida para o menor caso possível $n_0$.
2. O passo indutivo. Assumir que a fórmula é verdadeira para um valor genértico $n$ (hipótese indutiva). Em seguida, usando a hipótese indutiva, mostrar que a fórmula também é válida para $n+1$. 

Se for possível mostrar os dois passos, então se diz que a fórmula é válida para qualquer $n \geq n_0$.

#### Exemplo de prova por indução

Considere a seguinte afirmação. A soma dos $n$ primeiros números positivos $S(n) = \sum_{i=1}^{i=n} i$   pode ser calculada com a seguinte fórmula $$S(n) = \frac{n(n+1)}{2}.$$
1. Caso-base. Para mostrar o caso-base basta verificar que para $n=1$ tem-se $$1 = S(1) = \frac{1(1+1)}{2}.$$
2. Para mostrar o passo indutivo é necessário mostrar que $$S(n+1) = \frac{(n+1)(n+2)}{2},$$ assumindo que $$S(n) = \frac{n(n+1)}{2}$$é verdadeira. Para isso, note que $$S(n+1) = \sum_{i=1}^n i + (n+1).$$ Mas $\sum_{i=1}^n i = S(n) = \frac{n(n+1)}{2}$. Então, $$S(n+1) = \sum_{i=1}^n i + (n+1) = \frac{n(n+1)}{2} + n + 1 = \frac{n^2 + 3n + 2}{2} = \frac{(n+1)(n+2)}{2}.$$
O passo indutivo na prova costuma ser mais complicado, assim como o caso recursivo em um algoritmo recursivo. Quais as semelhanças entre os passos da prova por indução e o desenvolvimento de uma solução recursiva (como as que foram realizadas anteriormente)? #pergunta 


## Programação imperativa e programação declarativa

Os paradigmas de programação são estratégias gerais para o desenvolvimento de software.

- A programação imperativa se concentrar em definir como os programas funcionam, com o código descrevendo examente o fluxo de execução das instruções e o estado do programa. Esse é o paradigma seguido por uma solução iterativa.
- Uma solução recursiva segue o paradigma declarativo, que se concentrar em definir o que um programa deveria realizar. A programação funcional segue esse conceito.

## Exemplos de problemas
- [[Torre de Hanoi]]
- [[Exponenciação melhorada]]

# Referências
- [[2017Sanchez_IntroductionRecursiveProgramming|Introduction to recursive programming. Sanchez (2019)]]