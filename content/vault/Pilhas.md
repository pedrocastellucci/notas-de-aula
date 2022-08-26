---
alias: [Pilha]
---

# Pilha (Stack)

## Definição 

- Estrutura para armazenar um conjunto de elementos, com o seguinte comportamento. 
	- Novos elementos são sempre inseridos no topo da Pilha. 
	- Somente pode ser retirado o elemento que está no topo da Pilha. 
	- L.I.F.O.: *Last-in, First-out*.
		- O último elemento a entrar é o primeiro a sair. 

![[Pilha_exemplo_2021-08-20.excalidraw]]

## Operações primitivas

- *create()*: Cria uma nova Pilha.
- *isEmpty()*: Verifica se a Pilha está vazia.
- *isFull()*: Verifica se a Pilha está cheia. 
- *push(x)*: Insere novo elemento, x, na Pilha. 
- *pop()*: Remove elemento da Pilha.

> A operação *top()*, que retorna o elemento do topo da Pilha sem removê-lo, pode ser implementada como uma operação *não primitiva*? #task

## Exercícios

- Exercícios. Considerando as operações definidas. Desenvolva algoritmos para a solução dos seguintes problemas
	- Um algoritmo que recebe uma Pilha $P_1$ e transfere todos os seus elementos para uma Pilha $P_2$
	- Um algoritmo que recebe duas pilhas $P_1$ e $P_2$ e responde qual delas possui mais elementos. 
	- Um algoritmo que recebe uma Pilha $P$ e um elemento $x$ e responde se $x$ está presente em $P$.

### [[Projetos de implementação com Pilhas]]

- Implementação com alocação sequencial e estática de Pilha
	- Exemplo de solução de problema que não respeita o Tipo Abstrato de Dados, acessando elementos dependente da implementação.
		- Como implementar uma operação que consulta o topo da Pilha, sem removê-lo. 

### Implementações para Pilha

#### Pilha com alocação sequencial e estática de memória

Uma implementação em Python é dada a seguir

```python
class Stack:
    def __init__(self):
        self.__items = []

    def isEmpty(self):
        return self.__len__() == 0

    def push(self, item):
        self.__items.append(item)

    def pop(self):
        return self.__items.pop()

    def peek(self):
        return self.__items[len(self.__items)-1]

    def __len__(self):
        return len(self.__items)
```

Como adicionar o método *isFull* na implementação anterior? #pergunta  

#### Pilha com alocação encadeada e dinâmica de memória

Uma implementação em Python é dada a seguir. Nesta versão, a class *Node* é aninhada na classe *Stack*. Note também a utilização de uma exceção no caso da tentativa de remoção de elementos de uma Pilha vazia. 

```python
class EmptyStackException(Exception):
    pass

class Stack:

    class Node:
        def __init__(self, v=None):
            self._value = v
            self._next = None

    def __init__(self):
        self._head = self.Node()

    def is_empty(self):
        return self._head._next is None

    def push(self, x):
        new_node = self.Node(x)
        new_node._next = self._head._next
        self._head._next = new_node

    def pop(self):
        if self.is_empty():
            raise EmptyStackException("Stack is empty")
        else:
            x = self._head._next._value
            self._head._next = self._head._next._next
            return x

    def peek(self):
        if self.is_empty():
            raise EmptyStackException("Stack is empty")
        else:
            return self._head._next._value
```


### Pilhas "Inteligentes"

- Pilhas inteligentes. Adicionar comportamentos específicos da aplicação na estrutura de dados Pilha ou utilizar Pilhas burras e implementar o comportamento fora da estrutura de dados. Pilhas inteligentes podem herdar comportamentos de Pilhas "burras"