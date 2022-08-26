---
alias: [TAD, TADs, Abstract Data Type]
---

# Tipo abstrato de dados

- Os programas de uma linguagem procedural ou orientada a objetos manipulam dados. Os tipos de dados são uma forma de classificar os dados que uma variável pode armazenar. 
	- Diferentes linguagens de programação definem diferentes tipos de dados.
		- Em [[C++]], por exemplo, os tipos de dados podem ser organizados da seguinte forma
		- ![[Excalidraw/data_type_cpp.excalidraw.md|500]]
	- Cada tipo de dado possui também operações associadas (+, -, *, / etc)

## Atendente de biblioteca

Dia cheio na biblioteca, diversos estudantes estão em uma fila, alguns para fazer devolução, outros retirada, de livros. 

Em um determinado momento do dia, há $N$ estudantes interessados em devolver ou retirar um livro cada. Os estudantes estão separados em duas filas:
- (i) Fila de retirada. Nesse fila, a atendente precisa registrar a retirada na ficha do aluno.
- (ii) Fila de devolução. Os estudantes dessa fila podem deixar seus livros na pilha de devolução. Cada livro devolvido é colocado em cima do livro anterior. 

A cada instante, a atendente precisa decidir se atende um estudante da fila de retirada ou se processa um livro da pilha de devolução. Para tomar sua decisão ela lança uma moeda e realiza a ação dependendo do resultado do lançamento. Tanto o processamento da retirada, quanto o da devolução, demora 1 minuto. 

### Primeira implementação

Tal situação é simulado pelo código a seguir:
```python
from random import random, seed
from time import sleep
seed(0)
N = 10

# Creating the queues and the stack
e_devolucao = []
e_retirada = []
pilha_devolucao = []
for i in range(N):
    coin = random()
    if coin > 0.5:
        e_devolucao.append(i+1)
    else:
        e_retirada.append(i+1)

while len(e_devolucao) > 0 or len(e_retirada) > 0 or len(pilha_devolucao) > 0:
    print("Fila de devolucao:\t ", e_devolucao)
    print("Fila de retirada:\t ", e_retirada)
    print("Pilha de devolvidos:\t ", pilha_devolucao)
    coin = random()
    if coin > 0.5 and len(e_retirada) > 0:
        s = e_retirada.pop(0)
        print(f"Estudante {s} retirou livro")
    elif len(pilha_devolucao) > 0:        
        b = pilha_devolucao.pop(-1)
        print(f"Processado livro devolvido do estudante {b}")
    
    if(len(e_devolucao) > 0):
        b = e_devolucao.pop(0)
        print(f"Estudante empilhou o livro {b}")
        pilha_devolucao.append(b);
    print()
    sleep(1)  # Simulating a minute
```

- A legibilidade do código pode ser melhorada de diferentes formas:
	- Função para a geração dos dados para simulação
	- Função para a impresão de resultados 
	- Funções para o gerenciamento das filas e da pilha
	- Outras ideias?
	- Utilização dos Tipos Abstratos de Dados:
		- [[Filas|Fila]]
		- [[Pilhas|Pilha]]

### Uma versão utilizando [[Filas]] e [[Pilhas|Pilha]]

- Compare a legibilidade do código anterior com a seguinte, que utiliza as estruturas de dados [[Filas|Fila]] e [[Pilhas|Pilha]]. O código omite a implementação das classes [[Filas|Fila]] e [[Pilhas|Pilha]].
	- Considere que os Tipos Abstrato de Dados Fila e Pilha possuem as operações:
		- push(item): Insere item no conjunto.
		- pop(item): Remove item do conjunto
		- is_empty(): Retrona True caso a coleção esteja vazia, False caso contrário.


```python
from random import random, seed
from time import sleep
seed(0)
N = 10

def create_data(N):
    # Creating the queues and the stack
    e_devolucao = Fila()
    e_retirada = Fila()
    pilha_devolucao = Pilha()
    coin = Coin()
    for i in range(N):
        if coin.heads():
            e_devolucao.push(i+1)
        else:
            e_retirada.push(i+1)
    return e_devolucao, e_retirada, pilha_devolucao

def all_empty(a, b, c):
    return a.is_empty() and b.is_empty() and c.is_empty()

def print_filas(a, b, c):
    print("Fila de devolucao:\t ", a)
    print("Fila de retirada:\t ", b)
    print("Pilha de devolvidos:\t ", c)

N = 10
fila_devolucao, fila_retirada, pilha_devolucao = create_data(N)
coin = Coin()

while all_empty(fila_devolucao, fila_retirada, pilha_devolucao) == False:
    print_filas(fila_devolucao, fila_retirada, pilha_devolucao)    
    if coin.heads() and fila_retirada.is_empty() == False:
        s = fila_retirada.pop()
        print(f"Estudante {s} retirou livro")
    elif pilha_devolucao.is_empty() == False:        
        b = pilha_devolucao.pop()
        print(f"Processado livro devolvido do estudante {b}")    
    if(fila_devolucao.is_empty() == False):
        b = fila_devolucao.pop()
        print(f"Estudante {b} empilhou o livro")
        pilha_devolucao.push(b);
    print()
    sleep(1)  # Simulating a minute
```

Note que não é necessário conhecer a implementação exata das estruturas de dados [[Filas|Fila]] e [[Pilhas|Pilha]] para entender o código. Basta saber o resultado de cada operação disponível para o respectivo tipo de dado. 

- [[Filas]] e [[Pilhas]] estão entre os tipos abstratos de dados mais simples. Diversos outros serão apresentados ao longo do curso
	- [[Listas encadeadas]]
	- [[Tabelas hash]]
	- [[Árvores]]
	- [[Grafos]]

- Exemplos mais genéricos de tipos abstratos de dados:
	- Relógio:
		- Dados: Horas e minutos
			- Operações: Incrementar um minuto
		- Tipo Fração para operações matemáticas.
			- Dados: Numerador e denominador
			- Operações: Soma, adição, multiplicação e divisão.
		- FreeCell: Pilhas de cartas

## O que é um Tipo Abstrato de Dados

> -	Um Tipo Abstrato de Dados (TAD) é um tipo de dado (um conjunto de valores e operações nesses valores) que é acessado *somente* através de uma interface. [[1998Sedgewick_AlgorithmInCPart1-4|Algorithms in C. Parts 1-4 (Sedgewick. 1998)]]
>     -	Os dados armazenados devem ser manipulados *exclusivamente* através dos operadores do TAD.
>     - O programa que utiliza a interface é chamada de cliente e o programa que utiliza o tipo de dados é uma *implementação*.	

> An abstract data type is a data type whose representation is hidden from the client. [[2011Sedgewick_Algorithms|Algorithms (Sedgewick e Wayne. 2011)]]

- Encapsulamento é um dos conceitos fundamentais de Programação Orientada a Objetos.
	- Permite o desenvolvimento independente de aplicações clientes e implementação de algoritmos
	- Permite a melhoria de implementações sem afetar as aplicações clientes
	- A API desenvolvida é base para desenvolvimentos futuros (reusabilidade)
	- Limita o potencial de erros
	- Aumenta a legibilidade do código cliente

### Quando identificar os tipos abstrato de dados
- Fases de desenvolvimento de software
	- Análise
	- Projeto. Nessa fase são identificados os Tipos Abstratos de Dados a serem utilizados. 
	- Implementação
	- Teste  
	- Manutenção

### Vantagens da utilização de TADs
- Facilidade de programação
- Preservação da integridade dos dados
- Independência e portabilidade de código
- Maior potência de reutilização

# Referências
- [[2014Ferrari_EstruturaDadosComJogos|Estruturas de Dados com Jogos (Ferrari et al. 2014)]]
- [[2011Sedgewick_Algorithms|Algorithms (Sedgewick e Wayne. 2011)]]
- [[2019Forouzan_CppProgrammingObjectedOrientedApproach|C++ Programming - An Object-Oriented Approach (2019)]]