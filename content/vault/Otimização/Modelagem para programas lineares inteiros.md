---
title: "Modelagem para programas lineares inteiros"
---


# Programas Lineares Inteiros Mistos

$$\min c^Tx + h^Ty$$

sujeito a

$$Ax + Gy \leq b,$$
$$x \in \mathbb{Z}^n_+,$$
$$y^p \geq 0.$$

Onde os parâmetros são valores racionais:
- $c^T = (c_1, \ldots, c_n)$ ,
- $h^T = (h_1, \ldots, h_n)$,
- $A = (a_{ij})$ é uma matrix $m \times n$,
- $G = (g_{ij})$ é uma matrix $m \times p$,
- $b = (b_1, \ldots, b_m)^T$.

E as variáveis:
- $x = (x_1, \ldots, x_n)^T$, $n$ variáveis inteiras,
- $y = (y_1, \ldots, y_p)^T$, $p$ variáveis contínuas.

Para um problema de Programação Linear Inteira Mista, parâmetros são valores racionais determinísticos definidos antecipadamente. As variáveis representam decisões que podem ser tomadas. Cada atribuição de valores para as variáveis é chamado de **solução**. Uma solução pode ser:

> Solução viável (ou factível). Atende todas as restrições do problema.

> Solução inviável (ou infactível). Deixa de atender pelo menos uma restrição do problema.

## Um primeiro exemplo: O [[Problema da mochila]]

### O [[Problema da mochila]]

> No Problema da mochila, há uma mochila com capacidade $C$ e $n$ tipos de items, cada tipo item $i \in \{1, \ldots, n\}$ possui um peso e um valor $w_i$ e um valor, respectivamente. Qual é a quantidade de cada tipo de item que deve ser colocada na mochila de forma a maximizar o valore carregado, sem ultrapassar a capacidade da mochila?

Para elaborar um modelo é necessário definir quais são as variáveis do problema. Uma primeira tentativa é observar quais são as decisões a serem tomadas. Nesse caso, isso é suficiente para definir as variáveis:

- $x_i \in \mathbb{Z}⁺$: A quantidade de itens do tipo $i \in \{1, \ldots, n\}$ a serem carregadas na mochila. 

Para a construção do modelo é necessário escrever duas informações utilizando as variáveis e os parâmetros do problema: 
- O peso do conjunto de itens escolhidos.
	- Note que a expressão $w_1 x_1$ define o peso total dos itens de tipo $1$ escolhidos. Portanto
	- A expressão $w_1 x_1 + w_2x_2 + \ldots + w_nx_n$ compute o peso total dos itens escolhidos. A expressão pode ser escrita concisamente como $$\sum_{i=1}^nw_ix_i$$
- O valor do conjunto de itens escolhidos.
	- Com um racicínio análogo ao feito para o peso dos itens, tem-se: $$\sum_{i=1}^nv_ix_i$$

Com isso, a função objetivo do problema pode ser escrita como $$\max \sum_{i=1}^n v_ix_i$$ sujeito as restrições $$\sum_{i=1}^nw_ix_i \leq C,$$ $$x \in \mathbb{Z}^+.$$

Exemplos de implementações podem ser visto [[Problema da mochila#^091f1b]].

## Artifícios de modelagem

### Modelando relações lógicas com variáveis

Considere uma situação em que há um conjunto $S$ e a cada item do conjunto está associada uma variável binária $x_i, i \in S$. Semelhante ao [[Problema da mochila]]. Algumas situações frequentes em modelagem são exemplificadas a seguir.

#### No máximo $N$ elementos

Caso seja necessário que no máximo $N$ elementos do conjunto sejam selecionados:

$$\sum_{i \in S} x_i \leq N.$$

#### Pelo menos $N$ elementos

Caso seja necessário que no máximo $N$ elementos do conjunto sejam selecionados:

$$\sum_{i \in S} x_i \geq N.$$

#### Exatamente $N$ elementos

Caso seja necessário que exatamente $N$ elementos do conjunto sejam selecionados:

$$\sum_{i \in S} x_i = N.$$

Essa situação é análoga a um ou-exclusivo entre duas variáveis  $x_1 + x_2 = 1$

#### Se ... então... ($a \Rightarrow b$)

Considere duas variáveis binárias $x_a, x_b \in \{0, 1\}$ e que se deseja modelar a situação em que $x_a = 1 \Rightarrow x_b = 1$. Por exemplo, há situações em que a escolha de um item do conjunto implica na escolha de outro (do mesmo ou de outro conjunto). Isto é, se $x_a = 1$ então $x_b = 1$, $a, b \in S$.

$$x_a \leq x_b.$$

- Considerando $x_a, x_b \in \{0, 1\}$. Como modelar as seguintes situações? #pergunta 
	- $x_a = 0 \Rightarrow x_b = 0$
	- $x_a = 1 \Rightarrow x_b = 0$
	- $x_a = 0 \Rightarrow x_b = 1$
	- $x_a = 0 \Leftrightarrow x_b = 0$
	

Outra situação frequente é envolvendo uma variável binária $x_a \in \{0, 1\}$, um valor $L \geq 0$ e uma variável continua $y \geq 0$, tal que $$x_a = 1 \Rightarrow y \geq L.$$  Para modelar tal situação é possível utilizar a restrição $$L x_a \leq y.$$ Um raciocínio similar é utilizado no [[Problema de bin packing]].

#### Um exemplo

Uma empresa está considerando expandir suas operações para dois novos estados $A$ e $B$. Também, está considerando construir no máximo um novo depósito, mas a localização do depósito é restrita à localização da nova fábrica. O capital disponível é de 10 milhões. Os demais valores relacionados a tais escolhas é apresentado a seguir.

Para modelar o problema com o paradigma de Programação Inteira, considere as variáveis binárias

$$x_j = \begin{cases}1\quad \mbox{em caso afirmativo},\\ 
0\quad \mbox{em caso negativo},\end{cases}\quad (j = 1, 2, 3, 4).$$

| Decisão                    | Variável | Retorno previsto (R\$) | Investimento necessário (R\$)| 
| -------------------------- | ------------------- | ---------------- | ----------------------- |
| Construir fábrica em $A$?  | $x_1$             |     9 milhões             | 6 milhões                        |
| Construir fábrica em $B$?  | $x_2$         |     5 milhões             | 3 milhões                        |
| Construir depósito em $A$? | $x_3$         |   6 milhões               | 5 milhões                        |
| Construir depósito em $B$? | $x_4$     |    4 milhões              | 2 milhões                        |

- Seja $Z$ o retorno previsto por cada decisão. O retorno total em milhões de dólares.
	-	$$Z = 9x_1 + 5x_2 + 6x_3 + 4x_4.$$
- Como o capital disponível é de 10 milhões, uma restrição do modelo é 
	- $$6x_1 + 3x_2 + 5x_3 + 2x_4 \leq 10.$$
- No máximo um depósito será construído:
	- $$x_3 + x_4 \leq 1.$$
- Depósitos são só construídos se uma fábrica também for.
	- $$x_3 \leq x_1.$$
	- $$x_4 \leq x_2.$$

O modelo completo é dado por:

$$\max Z = 9x_1 + 5x_2 + 6x_3 + 4x_4$$
 
 sujeito a

$$6x_1 + 3x_2 + 5x_3 + 2x_4 \leq 10.$$
$$x_3 + x_4 \leq 1.$$
$$x_3 \leq x_1.$$
$$x_4 \leq x_2.$$
$$x_j \in \{0, 1\} \quad j = 1, 2, 3, 4$$


Este exemplo foi adaptado de [[2014Hillier_IntroductionToOperationsResearch|Hillier e Lieberman (2014)]].
O exemplo é um tipo de [[Problema de localização de facilidades]].


### Pelo menos uma restrição atendida

Considere duas restrições como as a seguir

$$\begin{cases}2x_1 + 3x_2 \leq 20,\\ 5x_1 + 2x_2 \leq 18.\end{cases}$$

Deseja-se que pelo menos uma dessas restrições seja atendida, mas não necessariamente ambas. 

Uma forma de realizar isso é utilizar uma variável auxiliar $y \in \{0, 1\}$.

$$y = \begin{cases}0, \mbox{ se } 2x_1 + 3x_2 \leq 20 \\ 1, \mbox{ se } 5x_1 + 2x_2 \leq 18 \\\end{cases}$$

Então, seja $M$ um número grande, podemos modelar a situação como:

$$\begin{cases}2x_1 + 3x_2 \leq 20 + My,\\ 5x_1 + 2x_2 \leq 18 + M(1 - y).\end{cases}$$

Essa técnica é útil, por exemplo, para modelos do [[Problema de corte e empacotamento]].

### $K$ de $T$ restrições atendidas

A ideia anterior pode ser adaptada para atender $K$ de um conjunto com $T$ restrições. Considere as $T$ restrições a seguir.

$$a_{11}x_{1} + \ldots + a_{1n}x_n \leq b_1,$$
$$a_{21}x_{1} + \ldots + a_{2n}x_n \leq b_2,$$
$$\vdots$$
$$a_{T1}x_{1} + \ldots + a_{Tn}x_n \leq b_T,$$

das quais é necessário atender pelo menos $K$. Para isso, seja $y_i \in \{0, 1\}, i=1, \ldots, T$, que recebe valor $0$ se a $i$-ésima restrição é atendida. 

Então, pode-se escrever

$$a_{11}x_{1} + \ldots + a_{1n}x_n \leq b_1 + My_1,$$
$$a_{21}x_{1} + \ldots + a_{2n}x_n \leq b_2 + My_2,$$
$$\vdots$$
$$a_{T1}x_{1} + \ldots + a_{Tn}x_n \leq b_M + My_2,$$
$$\sum_{i=1}^Ty_i = T - K$$


### Custo fixo

O custo fixo ocorre quando há um custo inicial para um atividade. Por exemplo, o setup de uma atividade e o início de uma corrida de aplicativo. 

Como exemplo, considere que foi feito um pedido para um aplicativo de transporte, o custo por quilômetro de viagem é de $c$, mas é pago um custo fixo, ao início da corrida de $k$. O objetivo é modelar a função de custo $f(x)$ em função da distância percorrida $x$.	

$$f(x) = \begin{cases}k + cx \mbox{ se $x > 0$,} \\ 0, \mbox{ se } x \leq 0.\end{cases}$$

Para a construção do modelo, pode-se utilizar uma variável auxiliar $y \in \{0, 1\}$ que toma valor 1 se $x > 0$ e 0 caso contrário. 

Com isso, pode-se definir $$z = f(x, y) = ky + cx,$$ com a adição da restrição $$x \leq My,$$ onde $M$ é um valor grande.


## Aplicações

- De [[2020Wolsey_IntegerProgramming|Wolsey (2020)]]
	> *Scheduling* de trens. A agenda de alguns trens é periódica. Para cada linha, os tempos de viagem entre as estações é conhecido e o tempo de permanência em cada estação deve estar dentro de um intervalo. Dois trens viajando na mesma linha devem estar separados por um dado número de minutos. Para permitir a conexão de passageiros entre dois trens deve haver um intervalo entre a chegada do trem A e a partida do trem B. O problema é encontrar uma agenda factível para um conjunto de trens e linhas

	> Escalonamento de tripulação aérea

	> Planejamento de produção

	> Planejamento da geração de eletricidade

	> Telecomunicações

	> Tratamento de radio-terapia

	> Programas de transplante de rins

	> Problemas de corte

# Referências
- Wolsey, Laurence A. _Integer programming_. John Wiley & Sons, 2020.
- Hillier, F. S., and G. J. Lieberman. "edition 10. Introduction to operations research." (2014).
