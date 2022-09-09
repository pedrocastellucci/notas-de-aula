---
title: "Árvores"
---

# Introdução

Árvores são estruturas de dados não lineares. Uma organização não linear é mais rica do que uma organização linear, em que há uma relação simples de predecessor ou sucessor entre dois objetos no conjunto. Em uma árvore, há relações **hierárquicas** com elementos sendo ancestrais ou descendentes de outro. 

Um exemplo é a relação de orientação acadêmica da árvore a seguir.

## Definições e propriedades

> [!CITE] (Goodrich et al, 2014)
> Uma árvore $T$ é um conjunto de nós (que armazenam elementos) de forma que os nós possuem relação de pai-filho da seguinte forma:
>> -  Se $T$ é não vazia, ela contém um nó chamado **raiz**, que não possui pai.
>> - Cada nó em $v \in T$, que não é a raiz, possui um único pai $w \in T$ (cada nó com pai $w$ é chamado de filho de $w$).

Note que essa definição é recursiva, de forma que uma árvore $T$ é vazia ou consiste de uma raiz que possui um conjunto sub-árvores filhas.

> [!INFO] Outras definições
> - Dois nós que são filhos de um mesmo pai são chamadas de irmãos.
> - Um nó é chamado de **externo** se não possui filhos (também são chamados de **folhas**.
> - Um nó é chamado de **interno** se possui pelo menos um filho.
> - Um nó $u$ é ancestral de $v$ se $u = v$ ou se $u$ é ancestral do pai de $v$.
> - Um nó $v$ é descendente de um nó $u$ se $u$ é um ancestral de $v$.
> - Uma **aresta** em uma árvore $T$ é um par de nós $(u, v)$ tal que $u$ é pai de $v$, ou vice-versa
> - Um **caminho** em uma árvore $T$ é uma sequência de nós em $T$ de forma que quaisquer dois nós consecutivos na sequência formam uma aresta de $T$.
> - Uma árvore é **ordenada** se existe uma relação de ordem linear entre os filhos de qualquer nó.

### Altura e profundidade de uma árvore

## Percursos em árvores


# Referências
- Goodrich, M. T., Tamassia, R., & Goldwasser, M. H. (2014). _Data structures and algorithms in Java_. John Wiley & Sons.