---
title: "Solução de sistemas lineares"
---

# Solução de sistemas lineares

Considere o seguinte circuito elétrico. 

![[attachments/Pasted image 20220926102430.png | 400]]

De acordo com as [Leis de Kirchoff](https://pt.wikipedia.org/wiki/Leis_de_Kirchhoff) a soma das tensões em cada malha e em cada nó é nula, então, podemos escrever o seguinte sistema. 

![[attachments/Pasted image 20220926103055.png|400]]

$$
\begin{align}
6i_1 + 5i_2 &= 10\\
i_1 - i_2 - i_3 &= 0\\
-5i_2 + 8i_3 + 2i_4 &= 0\\
3i_5 - 2i_4 &= 0\\
i_3 - i_4 - i_5 &= 0
\end{align}
$$
Trata-se de um sistema linear. De uma forma geral, pode-se formular esse tipo de problema da seguinte forma:

> [!INFO]
> Um sistema linear $Ax = b$ com $n$ equações e $n$ variáveis é dado por:
> $$\begin{align}
> a_{11}x_1 + a_{12}x_2 + \ldots + a_{1n}x_n &= b_1,\\
> a_{21}x_1 + a_{22}x_2 + \ldots + a_{2n}x_n &= b_2,\\
> \vdots&\\
> a_{n1}x_1 + a_{n2}x_2 + \ldots + a_{nn}x_n &= b_1.
> \end{align}$$
> com $a_{ij}$ e $b_i$ constantes e deseja-se determinar as variáveis $x_i$.

Os métodos para resolver esse tipo de problema pode ser classificados em:
1. Métodos diretos (ou eliminativos), que garantem teoricamente que uma solução será encontrada, caso exista.
2. Métodos iterativos. Métodos iterativos geram uma sequência de aproximações para a solução.
3. Métodos de Otimização. Métodos que constroem a função $F(X) = x^tAx - 2b^tx$ e tenta-se encontrar o seu mínimo, que é solução do sistema.

>[!INFO] Métodos diretos
> Exemplos de métodos diretos são [[Eliminação de Gauss]] e [[Decomposição LU]]

> [!INFO] Métodos iterativos
> Exemplos de métodos eliminativos são [[Método de Jacobi]] e [[Método de Gauss-Seidel]]


# Referências
- Sérgio Peters, & Julio Felipe Szeremeta. Cálculo numérico computacional (2019).
- Burden, R. L., Faires, J. D., & Burden, A. M. (2015). _Numerical analysis_. Cengage learning.