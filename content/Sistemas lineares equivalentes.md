---
title: "Sistemas lineares equivalentes"
---

# Sistemas lineares equivalentes

Seja $S$ um sistema linear com $m$ equações e $n$ incógnitas, $Ax = b$. Um sistema linear equivalente a $S$ é um sistema que pode ser obtido por meio da combinação das seguintes operações: 

1. Permutar duas equações de $S$.
2. Multiplicar uma das equações de $S$ por um número real $\lambda \neq 0$
3. Somar a uma das equações do sistema uma outra equação desse sistema multiplicada por um número real. 

(Para o ponto 2, considere que) Se $x^*$ é solução de $S$, então, tomando (sem perda de generalidade) a primeira linha do sistema, tem-se $$a_{11}x_1 + \ldots + a_{1n}x_n = b_1.$$ Multiplicando a primeira linha por $\lambda$, para obter um sistema $S_1$ tem-se:
$$(\lambda a_{11})x_1 + \ldots + (\lambda a_{1n})x_n = \lambda b_1.$$
Para a qual $x^*$ também é solução.

(Para o ponto 3) É possível mostrar que um sistema $S_1$, gerado a partir de $S$ pela soma de duas equações, possui a mesma solução de $S$ ou são ambos ($S_1$ e $S$), incompatíveis. Callioli et al. (1990) deixam a prova desse ponto como exercício, deve ter sido por um bom motivo, então eu também vou deixar. 

# Referências
- Carlos Callioli, Hygino Domingues, Roberto Costa. Álgebra linear e aplicações 6ª Edição