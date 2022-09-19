---
title: "Árvores binárias implementadas em vetor"
---

# Implementaçao em vetor para árvores binárias

Considere uma [[Árvores binárias#^f23f12|árvore binária completa]] com $n$ nós. Para uma implementação em vetor, assume-se que a raiz é colocada na posição $0$ do vetor, para cada posição $i = 1, \ldots, n-1$, tem-se:

> $2i+1$: A posição do filho esquerdo do nó na posição $i$.
> $2i+2$: A posição do filho direito do nó na posição $i$.

Portanto, a árvore

[![](https://mermaid.ink/img/pako:eNpNzjsOgzAQBNCrWFvDBVxECph86qTcZoWXj4QNMnYRIe4eYzfeafZJU8wB_aoZJIyOtkl8FVoR7y7q-iaaEm1Gk6BKdBltwqPEM0MlvEq80V6BCgw7Q7OOE46rgOAnNowg46t5oLB4BLRnrFLw6-dne5DeBa4gbJo8q5nieANyoGXn8w9dTjle)](https://mermaid.live/edit#pako:eNpNzjsOgzAQBNCrWFvDBVxECph86qTcZoWXj4QNMnYRIe4eYzfeafZJU8wB_aoZJIyOtkl8FVoR7y7q-iaaEm1Gk6BKdBltwqPEM0MlvEq80V6BCgw7Q7OOE46rgOAnNowg46t5oLB4BLRnrFLw6-dne5DeBa4gbJo8q5nieANyoGXn8w9dTjle)

Seria representada no vetor:
| 0   | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A   | B   | C   | D   | E   | F   | G   | H   | I    |

Note que, com essa implementação, é possível obter o pai de um nó na posição $i$ fazendo $p(i) = \lfloor\frac{i}{2}\rfloor$, ou seja, com custo $O(1)$. 

Essa implementação de árvores em vetores podem ser utilizadas na implementação de [[Heap|heaps]].

## Comentários, observações e perguntas

- Considere uma árvore completa com $d$ níveis cheios, quantas posições precisariam ser alocadas no vetor para armazenar tal árvore? #pergunta 
- Qual a desvantagem de armazenar árvores não completas em vetor, da forma apresentada? #pergunta 


# Referências
- Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2022). _Introduction to algorithms_. MIT press.