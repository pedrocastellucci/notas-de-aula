# Tabelas de símbolos

Uma tabela de símbolos é uma estrutura para armazenar elementos de forma que possam ser encontrados de forma eficiente utilizando chaves. 

Cada entrada da tabela armazena um par chave-valor e  
frequentemente se consideram chaves únicas.

As operações básicas de um [[Tipo Abstrato de Dados]] Tabela de Símbolos são:

- busca(k): Busca pelo elemento que possui a chave $k$. 
- insere(k, v): Insere o par chave-valor ($k$ e $v$ respectivamente). Caso o par já exista o valor $v$, associado à chave $k$, é atualizado.
- remove(k): Remove o elemento com chave $k$ da tabela.

Note que todas as operações têm a chave com pivô.


## Implementação em vetor

Uma das formas mais simples de se implementar uma tabela de símbolos é armazenar os pares chave-valor como itens de um vetor (ou de uma [[Listas ligadas|lista encadeada]]). Com isso, as operações busca, inserção e remoção são feitas diretamente no vetor.

```python
class Table:
    
    class Item:
        def __init__(self, key, val):
            self.key = key
            self.val = val

    def __init__(self, size=0):
        self.table = [None]*size

    def update(self, key, val):
        pos = self.__search(key)
        if pos is None:
            item = self.Item(key, val)
            self.table.append(item)
        else:
            self.table[pos].val = val
    
    def insert(self, key, val):
        self.update(key, val)

    def remove(self, key):
        pos = self.__search(key)
        if pos is not None:
            self.table.pop(pos) 

    def search(self, key):
        pos = self.__search(key)
        if pos is None:
            return None
        else:
            return self.table[pos].val

    def __search(self, key):
        for pos, item in enumerate(self.table):
            if item.key == key:
                return pos
        return None  

    def __str__(self):
        to_print = ""
        for item in self.table:
            to_print += str(item.key) + ": " + str(item.val) + "\n"     
        return to_print
```


### Análise das operações

Nesse caso, as operações de busca, inserção e remoção, no pior caso, são todas $O(n)$. Por quê? #pergunta 

Quais complexidades seriam alteradas se fosse utilizada uma [[Listas ligadas|Lista ligada]]? #pergunta 

Considerando que a tabela de símbolos é tipicamente utilizada em algoritmos que precisam de uma operação de busca eficiente, uma implementação a ser considerada é utilizando um vetor ordenado pelas chaves. 

## Implementação em vetor ordenado

Para a implementação em vetor ordenado, a inserção precisa garantir a ordenação entre as chaves. No pior caso, a inserção pode levar ao deslocamento de todos os elementos do vetor. Portanto, a inserção continua sendo $O(n)$.

A remoção é feita da mesma for que no caso sem ordenação ($O(n)$). 

A grande vantagem da implementação em vetor ordenado é a possibilidade de se utilizar a [[busca binária]] para encontrar uma chave. 

```python
class Table:
    
    class Item:
        def __init__(self, key, val):
            self.key = key
            self.val = val

    def __init__(self):
        self.table = []

    def update(self, key, val):
        if self.is_empty():
            self.table.append(self.Item(key, val))
        pos = self.__search(key)
        if self.table[pos].key != key:
            item = self.Item(key, val)
            self.table.insert(pos+1, item)
        else:
            self.table[pos].val = val
    
    def insert(self, key, val):
        self.update(key, val)

    def remove(self, key):
        if self.is_empty():
            raise Exception("Table is empty")
        pos = self.__search(key)
        if pos is not None:
            self.table.pop(pos) 

    def search(self, key):
        if self.is_empty():
            return None
        pos = self.__search(key)
        if self.table[pos].key != key:
            return None
        else:
            return self.table[pos].val

    def __search(self, key):
        left = 0
        right = len(self.table)-1
        while left <= right:            
            mid = (left+right)//2
            if self.table[mid].key == key:
                return mid
            elif self.table[mid].key < key:
                left = mid+1
            else:
                right = mid-1
            mid = (left+right)//2
        return mid

    def is_empty(self):
        return len(self.table) == 0

    def __str__(self):
        to_print = ""
        for item in self.table:
            to_print += str(item.key) + ": " + str(item.val) + "\n"     
        return to_print

```

### Análise das operações

Com a utilização da busca binária e do vetor ordenado a operação de busca passa a ter um custo de $O(log\ n)$ operações. Note que as operações de inserção e remoção continuam sendo $O(n)$. Por que? #pergunta 

## Aplicações de tabelas de símbolos

- [[Contagem de frequência de palavras]]

## Referências
- Notas de aula do Prof. Dr. Mário Felice. http://www.aloc.ufscar.br/felice/ensino/2019s2aed1/aula24.pdf. Acessado é 3 de Maio de 2022