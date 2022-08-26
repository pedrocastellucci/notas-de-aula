
# O caminho do cavalo

Um tema estratégico no xadrez é posicionar o cavalo em casas ideais no tabuleiro. Para explorar esse tema, é necessário calcular quantas movimentos o cavalo precisa realizar para sair de sua posição atual e atingir a posição de destino.

Considere um tabuleiro de xadrez. Cada casa no tabuleiro é identificada com um padrão (letra)(número) se referindo às "coordenadas" horizontal e vertical da casa. Um cavalo se movimento em "L". A figura a seguir mostra as casas para qual um cavalo, posicionado na casa d4, pode se movimentar. Essas casas são
- e6
- f5
- f3
- e2
- c2
- b3
- b5
- c6

```chesser
fen: 8/8/8/8/3N4/8/8/8 w KQkq - 0 1
```

# Objetivo do trabalho

Considerando um tabuleiro quadrado $8 x 8$ contendo apenas um cavalo, são dadas a posição inicial $x$ e a final $y$ do cavalo . Implemente um algoritmo que computa o número mínimo de movimentos necessários para que o cavalo saia de $x$ e chegue em $y$, supondo a movimentação do cavalo de acordo com as regras do xadrez (exemplificado na seção anterior). 

## Entradas e saídas

A entrada do algoritmo é dada em duas linhas contendo, respectivamente a posição inicial e a final do cavalo. Cada linha é uma string com a coordenada das posições. A coordenada é composta de uma letra (a, b, c, d, e, f, g, h) e um número (1, 2, 3, 4, 5, 6, 7, 8).

```
a1
b2
```

A saída deve possui o seguinte formato "Movimentos: $z$", com $z$ sendo um número inteiro indicando a quantidade mínima de movimentos necessários para o cavalo atingir o seu destino. Para o exemplo de entrada, a saída correta é:
```
Movimentos: 4
```