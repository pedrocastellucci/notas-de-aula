# Competição de ordenação de listas ligadas

Considere [[Listas duplamente encadeadas]]

- Os valores fornecidos são números inteiros no intervalo $[0, 10^9]$. 
- A class *Node* permite acesso às referências para a célula anterior e posterior (*prev* e *next* respectivamente), mas não ao valor armazenado no nó (célula). Isto é, o valor é considera um atributo privado da classe *Node*.
- Deve ser implementad a função *sort*, que recebe um objeto da classe *DoubleLinkedList*.
- A função de ordenação *sort* deve ser externa à classe *DoubleLinkedList*.
- Ordenação crescente
- A conferência é feita percorrendo a lista no primeiro ao último elemento e também na direção oposta. 
- Qualquer dúvida referente ao trabalho deve ser postada no fórum público indicado na página da disciplina no Moodle.
- A equipe que conseguir mais pontos vence a competição. A contagem dos pontos é feita da seguinte forma:
	- Não sei a forma ainda
- A equipe vencedora precisa explicar o seu algoritmo em uma apresentação de no máximo 15 minutos na aula seguinte à finalização da competição. 


```python
from random import randint

class Node:

    def __init__(self, val=None, prev=None, next=None):
        self.__val = val
        self._prev = prev
        self._next = next

    def val(self):
        return self.__val

    def print_node(self):
        print(self.__val, end="")


class DoubleLinkedList:
    
    def __init__(self):
        self._head = Node(0)
        self._tail = Node(1e+9)
        self._head._next = self._tail
        self._tail._prev = self._head

    def append(self, val):
        new_node = Node(val, self._tail._prev, self._tail)
        self._tail._prev._next = new_node
        self._tail._prev = new_node

    def print(self):
        pivot = self._head._next
        while(pivot != self._tail):
            pivot.print_node()
            print(end= " ")
            pivot = pivot._next
        print()

    def print_rev(self):
        pivot = self._tail._prev
        while(pivot != self._head):
            pivot.print_node()
            print(end=" ")
            pivot = pivot._prev
        print()


def swap(a, b):
    a._prev._next = b
    b._next._prev = a
    a._next, a._prev, b._prev, b._next = b._next, b, a._prev, a


def sort(LL):    
    if LL._head._next == LL._tail:
        return
    swapped = True
    while swapped:
        swapped = False
        i = LL._head._next
        while i._next != LL._tail and i != LL._tail:            
            if i.val() > i._next.val():
                swap(i, i._next)                
                swapped = True                
            i = i._next
            


if __name__ == "__main__":
    dll = DoubleLinkedList()
    for i in range(10000):
        dll.append(randint(0, 100000))
    #dll.print()
    sort(dll)
    #print("Finished sorting")
    #dll.print()
    #dll.print_rev()

```