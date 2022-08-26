# Introdução

O problema de ordenação pode ser definido como:

> Dada uma sequência de valores $S = (a_1, a_2, \ldots, a_n)$, encontre uma permutação de $S$, $S' = (a_1', a_2', \ldots, a_n')$ tal que $a_1' \leq a_2' \leq \ldots \leq a_n'$

Frequentemente, a sequência é fornecida como um vetor com $n$ elementos, mas também pode ser representada de outra forma como uma [[Listas ligadas|Lista ligada]].

## Por que ordenar?

- A aplicação precisa de dados ordenados. Por exemplo, ordenar a ordem de transações bancárias.
- Algoritmos utilizam a ordenação como uma subrotina. Por exemplo, um programa que apresenta objetos renderizados na tela que estão um sob o outro. 
- Algoritmo para o problema de ordenação revelam técnicas no projeto de algoritmos que podem ser utilizadas em outras situações.
- É possível provar um limitante inferior para o problema de ordenação. Como os melhores limitantes superiores são iguais aos inferiores assintoticamente, sabe-se que alguns algoritmos de ordenação são ótimos, assintoticamente.

# Algoritmos de ordenação

[[Insertion sort]]
[[Bubble sort]]
[[Selection sort]]
[[Heapsort]]
[[Mergesort]]
[[Quicksort]]

## Algoritmo de ordenação estável

> Um algoritmo de ordenação é estável se ele preserva a ordem relativa entre elementos que possuem a mesma chave. 

# Embaralhando um vetor
Um algoritmo famoso para produzir um embaralhamento de um vetor é o [[Embaralhamento de Knuth]], também conhecido como [[Embaralhamento de Knuth|Embaralhamento de Fisher-Yates]].

# Referências
- [[1998Sedgewick_AlgorithmInCPart1-4|Algorithms in C. Parts 1-4 (Sedgewick. 1998)]]
- [[2009Cormen_IntroductionToAlgorithms|Cormen et al. (2009)]]
- Prof. Dr. Mário Felice (UFSCar), notas de aula.