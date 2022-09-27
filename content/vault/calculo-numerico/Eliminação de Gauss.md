---
title: "Eliminação de Gauss"
alias: ["eliminação de Gauss"]
---

# Eliminação de Gauss

O método da eliminação de Gauss é um método eliminativo para a solução de sistemas lineares, $Ax = b$. O método está baseado em uma propriedade da Álgebra Linear que garante que uma solução $x$ do sistema $Ax=b$ obedece qualquer combinação linear das equações do sistema. A ideia fundamental é transformar o sistema linear $Ax=b$ em um [[vault/calculo-numerico/Sistemas lineares equivalentes|sistema linear equivalente]] de mais fácil solução através do processo de escalonamento.

São utilizadas três operações para simplificar o sistema linear a ser resolvido:
1. Uma equação $L_i$ pode ser multiplicada por uma constante não nula $\lambda$ com o resultado substituindo a equação $L_i$. $(\lambda L_i) \rightarrow (L_i)$
2. Uma equação $L_j$ pode ser multiplicada por uma constante $\lambda$ e somada à equação $L_i$ com o resultado substituindo $L_i$. $(L_i + \lambda L_j) \rightarrow (L_i)$
3. As equações $L_i$ e $L_j$ podem ser permutadas. 

Como uma sequência finita dessas operações, pode-se simplificar o sistema $Ax = b$, transformando-o em um sistema equivalente $A_1x=b_1$ com $A_1$ triangular superior.

## Exemplo

Considere o sistema $Ax = b$ a seguir. 

$$
\left\{
\begin{alignat}{4}
&x_1 + 2x_2 + x_3 = 8\\
-2&x_1 + x_2 + 3x_3 = 9\\
4&x_1 - x_2 - x_3 = -1
\end{alignat}
\right.
$$
Pode-se escrever o sistema utilizando a forma matricial estendida $[A\ \vdots\ b]$.

$$
\begin{bmatrix}
1 & 2 & 1 & 8\\
-2 & 1 & 3 & 9\\
4 & -1 & -1 & -1
\end{bmatrix}
$$
Para o processo de triangularização, tomam-se os elementos da diagonal principal de $A$ como pivôs para anular os elementos abaixo da diagional, um por vez. Portanto, utilizando como pivô o elemento $a_{11} = 1$ tem-se:

1. $\lambda = \frac{a_{21}}{a_{11}} = -2$ e $(L_2 - \lambda L_1) \rightarrow (L_2)$.
2. $\lambda  = \frac{a_{31}}{a_{11}} = 4$ e $(L_3 - \lambda L_1) \rightarrow (L_3).$

Resultando na matriz:

$$
\begin{bmatrix}
1 & 2 & 1 & 8\\
0 & 5 & 5 & 25\\
0 & -9 & -5 & -33
\end{bmatrix}.
$$

Então, se utiliza o pivô $a_{22} = 5$ para dar anular os elementos da segunda coluna abaixo da diagonal.
1. $\lambda = \frac{a_{32}}{a_{22}} = -9$ e $(L_3 - \lambda L_2) \rightarrow (L_3)$.

e tem-se:
$$
\begin{bmatrix}
1 & 2 & 1 & 8\\
0 & 5 & 5 & 25\\
0 & 0 & 4 & 12
\end{bmatrix}.
$$

Note que a matriz $A$ foi transformada em $A_1$ triangular superior. A vantagem de resolver sistemas triangulares é que basta realizar substitução de variáveis. 

Para o exemplo apresentado, o procedimento de retro-substituição é dado por
$$
\begin{align}
x_3 &= \frac{12}{4} = 3\\
x_2 &= \frac{1}{5}(25 - 5x_3) = 2\\
x_1 &= \frac{1}{1}(8 - x_3 - 2x_2) = 1\\
\end{align}
$$
O procedimento da Eliminação de Gauss pode ser dividido em dois passos:
1. Realizar a triangularização do sistema.
2. Realizar a retrossubstituição das variáveis.

> [!Warning] Pivôs nulos
> No caso de um pivô nulo $a_{kk}$, é necessário buscar nas linhas $i > k$ por um pivô não nulo. Preferencialmente, busca-se pelo maior pivô em módulo. Um procedimento conhecido como **pivoteamento parcial**.

## Avaliando o erro

Considere o sistema

$$
\left\{
\begin{align}
&0.896x_1 + 1.664x_2 + 0.386x_3 = 2\\
&0.842x_1 + 1.568x_2 - 0.414x_3 = 0\\
-&0.638x_1 + 1.768x_2 + 0.558x_3 = 0\\
\end{align}
\right.
$$

Resolvendo utilizando eliminação de Gauss, com 4 casas decimais de precisão.

#todo Resolver o sistema


Uma medida de erro frequentemento utilizada é relacionada a o resíduo de cada equação $$R_i = a_{i1}x_1 + a_{i2}x_2 + \ldots a_{in}x_n - b_i.$$
No caso de não haver erros numéricos, espera-se que os resíduos $R_i, i =1, 2, \ldots, n$ sejam nulos. Na prática, se utiliza como critério de erro o maior resíduo absoluto $$erro = \max\{|R_i|: i = 1, 2, \ldots, n\}.$$

## Pivoteamento parcial


## Pivoteamento total

## Uma implementação

```python
def gauss_elimination(A):
    # Matriz A é a matriz estendida do sistema
    n = A.shape[0]
    for k in range(n-1):
        for i in range(k+1, n):
            q = A[i, k]/A[k, k]
            for j in range(k+1, n+1):                
                A[i, j] = A[i, j] - q * A[k, j]
            A[i, k] = 0.0
    x = np.zeros(n)
    x[n-1] = A[n-1, n]/A[n-1, n-1]
    for i in range(n-2, -1, -1):
        x[i] = (A[i, n] - np.dot(A[i, i+1:n], x[i+1:]))/A[i, i]
    return x
```

### Análise do custo do algoritmo

# Referências
- Peters, Sérgio, e Julio Felipe Szeremeta. Cálculo numérico computacional (2019).
- Burden, R. L., Faires, J. D., & Burden, A. M. (2015). _Numerical analysis_. Cengage learning.