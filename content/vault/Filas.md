---
alias: Fila
---

# Introdução

## Implementação de fila em vetor circular

```python
class Queue:
    def __init__(self, max_size):
        self.__items = [None]*(max_size + 1)
        self.__size = 0
        self.__first = 0
        self.__last = 0

    def is_empty(self):
        return self.__first == self.__last

    def is_full(self):
        return (self.__last + 1) % len(self.__items) == self.__first

    def push(self, item):
        if self.is_full():
            raise Exception("Queue is full")
        self.__size += 1
        self.__items[self.__last] = item
        self.__last = (self.__last + 1) % len(self.__items)

    def pop(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        item = self.__items[self.__first]
        self.__size -= 1
        self.__first = (self.__first + 1) % len(self.__items)
        return item

    def size(self):
        return self.__size
```

## Implementação de fila em estrutura encadeada

A implementação utiliza uma estrutura encadeada circular para implementar uma fila.

```python
class Queue:
    class Node:
        def __init__(self, data=None, next=None):
            self._data = data
            self._next = next
        def __str__(self):
            return str(self._data)

    def __init__(self):
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def first(self):
        if self.is_empty():
            raise Exception("List is empty")
        return self.tail._next._data

    def last(self):
        if self.is_empty():
            raise Exception("List is empty")
        return self.tail._data

    def push(self, e):
        newest = self.Node(e)
        if self.is_empty():
            self.tail = newest
            newest._next = newest
        else:
            newest._next = self.tail._next
            self.tail._next = newest
            self.tail = newest
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise Exception("List is empty")
        answer = self.tail._next._data
        if self.size == 1:
            self.tail = None
        else:
            self.tail._next = self.tail._next._next
        self.size -= 1
        return answer
```

- Qual a complexidade de cada operação envolvida? #pergunta 
- Quais as modificações que seriam necessárias caso não se utilizasse uma estrutura circular? #pergunta 

- [[Projetos de implementação com Filas]]