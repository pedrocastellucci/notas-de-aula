# Descrição

Considere $n$ cidades numeradas de $0$ a $n-1$ e interligadas por estradas de mão única. Um exemplo com $n=6$ é dado a seguir. 

![[Drawing 2022-05-02 16.48.43.excalidraw.md]]

Um caminho que liga duas cidades $i$ e $j$ é uma sequência tal que:
- A primeira cidade é $i$,
- a última cidade é $j$,
- se $h$ e $k$ aparecem uma seguida da outra no caminho, então existe uma estrada de $h$ para $k$.

O comprimento do caminho é o número de estradas presentes em tal caminho. A distância de uma cidade $i$ até outra $j$ é o comprimento do menor caminho de $i$ até $j$. Caso não exista caminho, a distância é considerada infinita.

## Problema

Como calcular a distância entre uma cidade de origem $i$ e todas as demais?

Uma ideia para resolver o problema é a seguinte:  
1. Apenas a cidade de origem é alcançável (visível).  
2. Em cada iteração, podem ser encontradas novas cidades (baseado nas estradas disponíveis). Para cada nova cidade encontrada, atualizam-se suas distâncias. 
3. Note a importância de armazenar as cidades descobertas em uma fila, preservando a ordem de descoberta e, assim, calculando as distâncias corretamente.  

Mas antes de implementar uma solução é recomendado ter uma estrutura de dados para representar a rede em si. Isso pode ser feito através de uma matriz binária $A_{n\times n}$, em que cada entrada da matriz $a_{ij}$ é igual a $1$ se existe uma estrada conectando $i$ a $j$ e 0, caso contrário. Como ficaria tal matriz para o exemplo apresentado? #pergunta 

Uma implementação da solução, que utiliza a class Queue para a fila é dada a seguir.

```python
def get_distances(A, x):
    '''Compute distances between x and every city
    in the distance matrix A'''
    n = len(A)
    dist = [-1]*n
    q = Queue(n)
    dist[x] = 0
    q.push(x)
    while(not q.is_empty()):
        y = q.pop()
        for i in range(n):
            if A[y][i] == 1 and dist[i] == -1:
                dist[i] = dist[y] + 1
                q.push(i)
    return dist

A = [
    [0, 0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 1],
    [0, 1, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 1],
    [0, 1, 0, 0, 0, 1],
    [0, 1, 0, 0, 0, 0]
]

start_node = 0
dist = get_distances(A, start_node)
print(dist)
```

### Análise da solução

#### Eficiência de tempo
O número de operações realizadas em uma instância com $n$ cidades é da ordem de $n^2$, $O(n^2)$. Isso porque, em cada iteração do laço externo, a cidade corrente $y$ é retirada da fila. Note que cada cidade entra na fila no máximo uma vez, sendo retirada também uma vez (no máximo). Portanto, o número de iterações do laço externo não supera $n$. 

Em cada iteração do laço interno do algoritmo, todas as $n$ cidades são verificadas para descobrir novas vizinhas de $y$. Assim, para cada iteração do laço externo, são feita $O(n)$ iterações do laço interno. 


#### Eficiência de espaço
A fila auxiliar ocupa espaço adicional $O(n)$. No entanto, a matriz de entrada ocupa espaço $O(n^2)$. Será que isso é necessário? Considere, por exemplo, uma representação de amizadas em rede social. A rede possui bilhões de usuários ("cidades"), mas cada usuário possui poucos amigos ("vizinhos").
