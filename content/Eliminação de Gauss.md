---
title: "Eliminação de Gauss"
---

# Eliminação de Gauss

O método da eliminação de Gauss é um método eliminativo para a solução de sistemas lineares, $Ax = b$. O método está baseado em uma propriedade da Álgebra Linear que garante que uma solução $x$ do sistema $Ax=b$ obedece qualquer combinação linear das equações do sistema. A ideia fundamental é transformar o sistema linear $Ax=b$ em um [[Sistemas lineares equivalentes|sistema linear equivalente]] de mais fácil solução através do processo de escalonamento.

São utilizadas três operações para simplificar o sistema linear a ser resolvido:
1. Uma equação $L_i$ pode ser multiplicada por uma constante não nula $\lambda$ com o resultado substituindo a equação $L_i$. $(\lambda L_i) \rightarrow (L_i)$
2. Uma equação $L_j$ pode ser multiplicada por uma constante $\lambda$ e somada à equação $L_i$ com o resultado substituindo $E_i$. $(E_i + \lambda E_j) \rightarrow (L_i)$
3. As equações $L_i$ e $L_j$ podem ser permutadas. 

Como uma sequência finita dessas operações, pode-se simplificar o sistema $Ax = b$.


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

## Pivoteamento parcial

## Pivoteamento total


# Referências
- Peters, Sérgio, e Julio Felipe Szeremeta. Cálculo numérico computacional (2019).
- Burden, R. L., Faires, J. D., & Burden, A. M. (2015). _Numerical analysis_. Cengage learning.