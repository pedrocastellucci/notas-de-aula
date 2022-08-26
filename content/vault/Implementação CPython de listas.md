# Implementação CPython de listas

Na linguagem de programação Python, a estrutura de dados lista está embutida. Apesar do nome a lista do Python (na implementação CPython) não é uma [[Listas ligadas|Lista ligada]]. Trata-se, na verdade, de um vetor de ponteiros. 

> Um ponteiro é um tipo de dado que armazena um endereço de memória.

A estrutura básica é um vetor de ponteiros para objetos do Python. Por exemplo, na lista

```python
L = [10, 20, 30, 40, 50]
```

os valores $10, 20, 30, 40$ e $50$ estão armazenados cada um em uma posição de memória para um número inteiro. Internamente, o CPython armazena as posições de memória em que tais objetos (do tipo inteiro) estão localizados. 

![[CPythonListImplementation2021-10-27 21.36.06.excalidraw]]

Note que os valores que estão na lista não estão, necessariamente, em sequencia na memória. Quais são consequências disso? #pergunta

## Função append

Ao se utilizar a função *append*:

```python
L = [10, 20, 30, 40, 50]
L.append(60)
```

Um novo elemento é adicionado à lista. O que significa que o CPython armazena um novo endereço no vetor, correspondendo à localização em memória do novo valor. 

## A função remove

A função remove endereço do elemento a ser removido, copiando todos os valores subsequentes para a posição imediamente anterior. Sendo portanto de complexidade $O(n)$.



# Referências

http://www.laurentluce.com/posts/python-list-implementation/