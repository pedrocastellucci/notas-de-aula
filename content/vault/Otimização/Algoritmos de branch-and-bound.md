---
title: "Branch-and-bound"
alias: "branch-and-bound"
---

# A estratégia de Branch-and-bound

A estratégia de [[Algoritmos de branch-and-bound|Branch-and-bound]] foi proposta originalmente em 1960 por [[Ailsa Land]] e [[Alison Doig]] como método para solução de problemas discretos de otimização. 

Juntamente com [[Algoritmos de planos de corte]] constituem o framework [[Branch-and-cut]], base de diversos pacotes computacionais para problemas de [[Otimização Inteira]].

Para exemplificar a estratégia do [[vault/Otimização/Algoritmos de branch-and-bound|branch-and-bound]] vamos utilizar o [[Problema do Caixeiro Viajante]].

# O [[Problema do Caixeiro Viajante]]

Um vendedor deseja visitar as cidades $1, 2, \ldots, N-1$, partindo da sede de uma empresa na cidade $0$. O custo de viajar de uma cidade $i$ para uma cidade $j$ é $c_{ij}$, $i, j = 0, 1, \ldots, N-1$. O problema de determinar uma rota com o menor custo que visita todas as cidades exatamente uma vez é conhecido como [[Problema do Caixeiro Viajante]].

## Uma solução com enumeração explícita

Solução baseada na permutação da lista de cidades $(0, 1, 2, \ldots, N-1)$. É possível encontrar uma solução gerando todas as permutações da lista de cidades.

Por exemplo, se $N = 4$ basta avaliar todas as sequências $(N-1)! = 6$  sequências e escolher a de menor custo.
1.  $(0, 1, 2, 3)$	
2.  $(0, 1, 3, 2)$
3.  $(0, 2, 1, 3)$
4.  $(0, 2, 3, 1)$
5.  $(0, 3, 1, 2)$
6.  $(0, 3, 2, 1)$

A relação de recorrência para gerar as permutações de uma sequência $S = (0, 1, \ldots, N-1)$ de tamanho $N$ é dada por 

$$S_N = \bigcup_{C \notin S_{N-1}} \Big\{S_{N-1} C \Big\}$$
### Implementação utilizando [[Backtracking]]

Pode-se realizar uma numeração explícita da todas as permutações da sequência $S = (0, 1, \ldots, N-1)$, computar o custo de cada uma delas, identificando, assim uma solução ótima. Para isso, pode-se utilizar o código a seguir.

```python
def backtrack(sol, left, N, best=INFINITY, opt=None):
    if left == N:
        cost = sol.get_value()
        if cost < best:
            best = cost
            opt = deepcopy(sol)
    else:
		for i in range(left, N):
			sol.tour[left], sol.tour[i] = sol.tour[i], sol.tour[left]           
			best, opt = backtrack(sol, left+1, N, best, opt)
			sol.tour[left], sol.tour[i] = sol.tour[i], sol.tour[left]
    return best, opt
```

### Alguns testes

Foram gerados $N$ pontos aleatórios em uma área 100 x 100. O tempo computacional para se encontrar uma solução ótima do [[Problema do Caixeiro Viajante]] para esses pontos é apresentado na tabela a seguir, para diferentes valores de $N$.

| $N$   | Tempo (s) |
| --- | --------- |
| 5   | 0.001     |
| 6   | 0.003     |
| 7   | 0.006     |
| 8   | 0.030     |
| 9   | 0.213     |
| 10  | 1.999     |
| 11  | 21.636    |
| 12  | 312.102   |

### Análise do algoritmo

O algoritmo enumera todas as $(N-1)!$ soluções viáveis para o problema e compara o custo da solução atual com a melhor encontrada até o momento. Portanto, o tempo computacional do algoritmo é de complexidade $O(N!)$.

Melhorar as configurações de hardware ou utilizar uma linguagem como C/C++ poderia aumentar o tamanho dos problemas resolvidos no mesmo tempo computacional?

#### Em um mundo mais rápido

Conforme o número de cidades $N$ aumenta, o número de soluções também aumenta

| $N$     | Tempo (s)            |
| ----- | -------------------- |
| $5$   | $24$                 |
| $10$  | $362880$             |
| $20$  | $1\,2 \cdot 10^{17}$ |
| $100$ | $\approx 10^{156}$   |

Considerando um computador que consiga avaliar (computar o custo) de uma solução em $10^{-34}s$, seriam necessários $$\approx 10^{122}s.$$ Mas a idade do universo é da ordem de $10^{17}s$ (e contando...).

> A [Constante de Planck](https://en.wikipedia.org/wiki/Planck_constant) foi a menor constante física que eu consegui encontrar e tem valor da ordem de $10^{-34}$, expresso em unidades do Sistema Internacional.

Portanto, uma solução é investir em algoritmo que evitem enumerar todas as soluções explicitamente. 

## Uma enumeração ímplicita

Na verdade, não é necessário explorar todas as soluções explicitamente. Note que o algoritmo proposto adiciona uma cidade a cada chamada da função, ou seja, em qualquer chamada da função em que a condição $left == N$ não é verdadeira, existe uma solução parcial definida $p = (a_0, a_1, a_2, \ldots, a_i), i < N-1$. É possível calcular o custo de uma solução parcial $$c(p) = \sum_{j=0}^{i-1} c_{j, j+1}.$$
Se a solução parcial $p$ tiver um custo, $c(p)$, maior ou igual ao da melhor solução completa encontrada até o momento, não é necessário continuar explorando o ramo atual da árvore.  Por quê? Com essa modificação, há garantia de que uma solução ótima será encontrada? 

Essa estratégia de poda da árvore é conhecida como poda por qualidade. 

### Implementação com poda por qualidade

```python
def backtrack(sol, left, N, best=INFINITY, opt=None):
    if left == N:
        cost = sol.get_value()
        if cost < best:
            best = cost
            opt = deepcopy(sol)
    else:
        cur_value = sol.get_value(0, left)
        if cur_value < best:
            for i in range(left, N):
                sol.tour[left], sol.tour[i] = sol.tour[i], sol.tour[left]           
                best, opt = backtrack(sol, left+1, N, best, opt)
                sol.tour[left], sol.tour[i] = sol.tour[i], sol.tour[left]
    return best, opt
```

Com a poda por qualidade baseada no custo das soluções parciais é possível resolver problemas de dimensões maiores em tempo computacional similar.

| $N$   | Tempo (s) |
| --- | --------- |
| 5   | 0.002     |
| 6   | 0.003     |
| 7   | 0.005     |
| 8   | 0.009     |
| 9   | 0.029     |
| 10  | 0.097     |
| 11  | 0.843     |
| 12  | 4.303     |
| 13  | 24.263    |
| 14  | 61.984    |
| 15  | 325.719   |


### [[Algoritmos de branch-and-bound]], utilizando um [[limitante inferior]]

É possível utilizar uma poda que inclui informações otimistas sobre o custo a ser atingido caso se continue explorando determinado ramo da árvore.  Uma opção é utilizar a [[Problema da Árvore Geradora Mínima|Árvore Geradora Mínima]] dos nós que ainda não foram visitados pela solução parcial atual. 

Note que o custo de uma [[Problema da Árvore Geradora Mínima|Árvore Geradora Mínima]] considerando os $N$ nós é um limitante inferior (otimista) para o custo de uma solução do [[Problema do Caixeiro Viajante]] com os mesmo $N$ nós. 

- Seja $t$ um tour no grafo $G$. A remoção de uma aresta de $G$ produz um caminho $r$. Como os custos das arestas são não negativos, tem-se $c(r) \leq c(t)$. Como um caminho é também uma árvore, tem-se que o custo da Árvore Geradora Mínima (MST) é tal que $$c(MST) \leq c(r) \leq c(t).$$

Isso possibilita que a operação de poda inclua informações sobre a solução de um [[Problema da Árvore Geradora Mínima]] para eliminar ramos da árvore que não forneçam soluções melhores do que a atual. 

> Seja $z$ o valor da melhor solução conhecida até o momento, $P = (a_0, a_1, \ldots, a_i), i < N,$ a solução parcial para o [[Problema do Caixeiro Viajante]] e $T$ uma [[Problema da Árvore Geradora Mínima|Árvore Geradora Mínima]] contemplando todos os nós não visitados na solução atual, $j \notin P$. Então,  se $c(P) + c(T) \geq z$ pode-se podar o ramo atual da árvore (não é necessário explorar a solução parcial $P$).  Por quê? #pergunta

Para utilizar o limitante baseado na [[Problema da Árvore Geradora Mínima|Árvore Geradora Mínima]] pode-se modificar a implementação como feito a seguir. 

```python
def backtrack(sol, left, N, best=INFINITY, opt=None):
    if left == N:
        cost = sol.get_value()
        if cost < best:
            best = cost
            opt = deepcopy(sol)
    else:
        cur_value = sol.get_value(0, left)
        bound_value = get_mst_cost(sol.tour[left+1:], sol.dist)
        if cur_value + bound_value < best:
            for i in range(left, N):
                sol.tour[left], sol.tour[i] = sol.tour[i], sol.tour[left]           
                best, opt = backtrack(sol, left+1, N, best, opt)
                sol.tour[left], sol.tour[i] = sol.tour[i], sol.tour[left]
    return best, opt
```

Com isso, executando algumas instâncias, obteve-se o seguinte resultado

| N   | Tempo (s) |
| --- | --------- |
| 5   | 0.005     |
| 6   | 0.007     |
| 7   | 0.014     |
| 8   | 0.021     |
| 9   | 0.047     |
| 10  | 0.095     |
| 11  | 0.436     |
| 12  | 0.854     |
| 13  | 2.339     |
| 14  | 4.523     |
| 15  | 6.849     |
| 16  | 13.905    |
| 17  | 24.966    |
| 18  | 31.602    |
| 19  | 34.846    |
| 20  | 121.833   |
| 21  | 238.015   |
| 22  | 367.061   |


Quando se tem uma estratégia para conseguir um limitante otimista (inferior no caso de problemas de minimização e superior no caso de problemas de minimização), pode-se desenvolver um algoritmo de [[Algoritmos de branch-and-bound|Branch-and-bound]]. 

## Algumas conclusões

- Para resolver esse problema (e outros NP-difíceis) é necessário lidar com o crescimento exponencial do espaço de soluções. 
- O que fazer a cada novo problema encontrado?
	- Criar um algoritmo de enumeração explícita 
	- Encontrar propriedades que permitam a poda
		- Poda por qualidade
		- Poda por infactibilidade
	- Encontrar problemas auxiliares que forneçam bons limitantes inferiores
- Existe um arcabouço que já possui todas essas "funcionalidades". Inclusive com pacotes computacionais com toda a ideia de [[Algoritmos de branch-and-bound]] (e diversas outras) já implementada, sendo necessário, apenas, fornecer os dados de entrada. Para aprendermos a utilizar tais ferramentas, precisamos aprender [[Programação Linear Inteira Mista]].

# Referências

- [Land, Ailsa H., and Alison G. Doig. An automatic method for solving discrete programming problems. Econometrica
Vol. 28, No. 3 (Jul., 1960), pp. 497-520. ]([https://doi.org/10.2307/1910129](https://doi.org/10.2307/1910129 "This link opens in a new window")
- Palestra *Tuning a TSP Algorithm*. https://www.youtube.com/watch?v=SS5KfIFzfEE&list=FLQDy63aSs-IH4Zbniv8x4jA&index=4&t=4206s