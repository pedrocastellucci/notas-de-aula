# Introdução

- Todo dado, variável ou objeto definido ou criado em um programa requer uma espaço na memória do computador. No entanto, a memória é um recurso limitado, compartilhado entre diversos "competidores":
	- Sistema operacional
	- Softwares aplicativos
	- Diversas variáveis (e estruturas de dados) do próprio programa

- A forma de realizar essa gerencia de memória varia entre as linguagens de programação.
	- Em algumas (e.g. Java e Python), o gerenciamento de memória é transparente para o programador; 
	- em outras, como C, o programador é responsável por, explicitamente, fazer as requisições de alocação e desalocação de memória (*malloc*, *calloc*, *free*). 

- De uma forma geral, há dois processos de alocação de memória:
	- Alocação estática. Realizada em tempo de compilação.
	- Alocação dinâmica. Realizada em tempo de execução.


# Alocação estática e dinâmica de memória

## Alocação estática de memória

- Variáveis são alocadas de modo permanente até o final da chamada da função (ou final da execução do programa).
- É feita antes da execução do programa.
- Utiliza uma [[Pilhas|Pilha]] para o gerenciamento da alocação de memória.
- Espaço de memória alocado não pode ser reutilizado.
- Exemplo: Utilização de um array, em C, como no código a seguir. Note que toda a memória que será necessária para a execução do código pode ser definida previamente.

```c
#include <stdio.h>
int main(void){
    int v[100];
    for (int i = 0; i < 100; i++)
        printf("%d ", v[i]);
    return 0;
}
```
- O que o código anterior imprime? #pergunta 


## Alocação dinâmica de memória
- Variáveis são alocadas apenas se o comando específico for executado.
- Permite reutilização do espaço de memória. 
- O programador pode liberar memória durante o tempo de execução do programa. 
- Algumas linguagens utilizam explicitamente comandos para criação de ponteiros para objetos e objetos (e.g. o operador *new* e *delete* em C++; *malloc*, *calloc* e *free* em C).
- Memória alocada de uma uma região de memória conhecida como *heap* (não confundir com a estrutura de dados [[Heap]]), que não é utilizado pelas variáveis do programa. Um conjunto de *bytes* consecutivos é alocado para o armazenamento da variável sendo criada. 
	- Como saber quais blocos de memória estão livres? #pergunta 
- Exemplos: Em uma [[Listas ligadas|Lista ligada]] sempre que são criadas ou destruídas novas células. Na alocação do array como exemplificado a seguir, em C.

```c
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int *v;
    int n;
    scanf("%d", &n);
    v = malloc(n * sizeof(int));
    if (v == NULL) {
        exit(-1);
    }
    for(int i = 0; i < n; i++) {
        printf("%d ", v[i]);
    }
    free(v);
}
```
- O que imprime o código a seguir? #pergunta 

- Em [[Python]] todos os objetos são armazenados na heap. 
- A stack é utilizada para controlar as chamadas de função.

## Leiature da memória de um programa em C

![[memory_layout_c.excalidraw]]

O leiaute da memória de um programa em C, pode ser dividido nos seguintes segmentos:
- Stack ([[Pilha]]): Variáveis locais, parâmetros de funções, endereços de retorno.
- *Heap*: Memória alocada dinamicamente (*malloc* e *free*).
- *Uninitialized data*: Variáveis globais e estática não inicializadas.
- *Initialized data*: Variáveis estáticas inicializadas.
- *Text*: Código do programa (para onde apontam os endereços de retorno).

- O modelo básico de gerencia de memória assume um grande bloco de memória contínua. Periodicamente, requisições por uma quantidade de memória são feitas. O gerenciador precisa encontrar um bloco de memória contínuo capaz de satisfazer a requisição. Isso é chamado de alocação de memória. 
	- O gerenciador de memória, tipicamente retorna uma informação (*handle*) que permite ao usuário (programador) recuperar os dados que são armazenados na memória alocada. 
	- Memória que foi alocada pode, eventualmente, retornar para o gerenciador de memória. Esse processo é chamada de desalocação de memória. 
- Quando há um padrão bem definido (alocação estática) nas alocações e desalocações o gerenciamento pode ser bastante simples. 
- O caso em que as requisições e desalocações são feitas em uma ordem arbitrária é mais complicado. Ou seja, gerenciar a alocação dinâmica de memória pode ser mais complicado.


# Gerenciamento de memória alocada dinamicamente

- Memória é vista como um grande vetor, quebrado em pedaços de diferentes tamanhos, no qual alguns pedaços estão livres, outros ocupados (ou reservados). Os blocos livres são conectados (em termos lógicos).
	- Qual estrutura de dados pode ser utilizada para gerenciar a lista de espaços livres? #pergunta 
		- De acordo com Goodrich (2011), uma lista duplamente ligada é uma escolha popular.
- Quando uma requisição é feita, é necessário encontrar um bloco de memória grande o suficiente para satisfazer a requisição.
- É possível não haver um bloco do tamanho exato para satisfazer a requisição, o que pode gerar fragmentação na memória.
	- ![[free-spaces-memory-2022-02-18.excalidraw]]
	- Framentação externa: Ocorre quando há muitos blocos pequenos livres na memória. 
	- Fragmentação interna: Ocorre quando se aloca um espaço que não é utilizado. Alguns esquemas de gerenciamento de memória permitem alguma fragmentação interna para simplificar o gerenciamento ou reduzir a fragmentação externa.
	- Há diversas estratégias para reduzir a framentação de memória.
		- Vide [[1997Shaffer_PracticalIntroductionDataStructuresAlgorithms]]


## Métodos de encaixe sequencial (*Sequential fit methods*)

- Métodos de encaixe sequencial buscam por "bons" blocos para satisfazer uma requisição. 
- Os métodos apresentados aqui assumem que os blocos livres são organizados em uma [[Lista duplamente ligada]].
	- A abordagem mais simples consiste em armazenar uma lista duplamente ligada em que cada nó contém uma referência para um bloco de memória. Essa abordagem é suficiente caso haja espaço para armazenar a lista separadamente.
	- Uma segunda abordagem consiste em utilizar os blocos de memória disponíveis diretamente. Nesse caso, um bloco precisa ter tamanho suficiente para armazenar as referências necessárias (e possivelmente outras informações). Essa abordagem é mais complicada, mas utiliza menos memória. 

- **First-fit**. O método mais simples de atender uma requisição de tamanho $m$ (*bytes*), consiste em percorrer a lista de espaços livres até que um bloco de tamanho pelo menos $m$ seja encontrado. Qualquer espaço adicional no bloco é mantido na lista de espaços livres.
	- Uma melhoria pode ser obtida se, ao invés de sempre iniciar a busca no início da lista, for armazenada a posição da última inserção e iniciar a busca desse ponto. Essa melhoria reduz o número de verificações de espaços pequenos que podem se acumular no início da lista. 
	- Uma desvantagem é o fato de blocos grandes acabarem sendo quebrados em vários pequenos, potencialmente impedido o atendimento de requisições maiores no futuro. Para reduzir essa desvantagem, pode-se utilizar a estratégia **best-fit**.
- **Best-fit**. Essa estratégia busca pelo *menor* bloco capaz de atender a requisição.
	- Uma desvantagem é a necessidade de se percorrer a lista toda a cada nova requisição.
	- Outra desvantagem é que os espaços restantes de cada bloco são, potencialmente, pequenos. Ou seja, há um aumento na fragmentação externa para reduzir a chance de não poder atender uma requisição maior no futuro. Para reduzir a fragmentação externa pode-se utilizar a estratégia **worst-fit**.
- **Worst-fit**. Essa estratégia sempre busca pelo maior bloco livre, independente do tamanho da requisição.
	- Quais as vantagens e desvantagens dessa estratégia? #pergunta 

- Pensando nas estratégias apresentadas, quais estruturas de dados, além de uma [[Listas ligadas|Lista ligada]] poderiam ser utilizadas de forma eficiente? #pergunta 
- Qual estratégia é a melhor?
	- Depende do padrão de requisições esperado.
- Em geral, 
	- Busca na lista de espaços livres é $O(n)$ no pior caso.
	- Realizar a fusão de blocos livres adjacentes é relativamente complicado.
	- É necessário usar espaço adicional para a lista. 
	- Uma opção é utilizar o chamado *Buddy System*. Vide [[1997Shaffer_PracticalIntroductionDataStructuresAlgorithms]]


## Garbage collection
- Periodicamente, o ambiente de execução pode notar que a memória disponível na *heap* está pequeno ou notar que não é possível satisfazer uma requisição. Em alguns casos, pode não haver memória suficiente. Então, a única opção do gerenciador de memória é retornar um erro. Em outros casos, o sistema pode buscar por espaços que não estão sendo mais utilizados e devolvê-los para  a lista de espaços disponíveis. Esse processo é conhecido como *garbage collection*.
- Em alguns casos, a memória necessária pode estar espalhada em vários blocos (fragmentação externa). Nesses casos, pode ser possível/necessário compactar a memória livre movendo os blocos reservados para que os blocos livres fiquem todos juntos. 
	- Um desafio dessa estratégia é que a aplicação precisa ser capaz de lidar com os seus dados potencialmente trocando de lugar na memória. Uma solução seria retornar um *handle* que é um segundo nível de referência. O *handle* armazena o endereço de uma variável que referencia a posição de memória. O *handle* nunca muda de posição, mas o valor apontado pelo *handle* pode se alterar. 
- Outra estratégia é o *garbage collection* propriamente dito. É necessário haver um mecanimo para identificar objetos que não serão mais utilizados
	- Contagem de referências
	- Detecção de ciclos
- Há diversos algoritmos para realizar o *garbage collection*, um dos mais utilizados é o algoritmo *mark-sweep*.

# Gerenciamento de memória em Python

- Utiliza uma heap contendo todos os objetos e estruturas de dados do Python. 
	- O gerenciamento dessa heap é garantido pelo *Python memory management*.
		- O *Python memory management* lida com:
			- Compartilhamento
			- Fragmentação
			- Pré-alocação
			- *Caching*

- No nível mais baixo, existe um alocador de memória que garante a existência de memória na heap para armazenar todos os dados relacionados ao Python através da interação com o gerenciador de memória do sistema operacional. 
- Acima do alocador de memória, existem diversos alocadores que operam na mesma heap e implementam políticas específicas de gerenciamento de memória considerando as peculiaridades de cada objeto. 
	- Inteiros são gerenciados de forma diferente de strings, tuplas e dicionários, por exemplo. 
	- O *Python memory management* delega parte do trabalho aos gerenciadores de objetos específicos, mas garante que eles operem dentro do espaço da heap. 

- Todo o trabalho de gerenciamento da heap é realizado pelo próprio interpretador e o usuário (programador) não tem controle sobre ele. Para evitar corrupção de memória, não se deve tentar manipular objetos do Python a partir das funções exportados pela biblioteca do C (*malloc, calloc, realloc* e *free*).

- Embora grande parte da gerencia de memória seja feita automaticamente pelo Python, o conhecimento de tais mecanismos possibilita melhores práticas de programação.
	- Alguns exemplos podem ser vistos em: https://towardsdatascience.com/memory-management-in-python-6bea0c8aecc9

# Referências 
- [[1985Aho_dataStructureAlgorithms|Data Strucutres and Algorithms (Aho et al. 1985)]]
- [[1997Shaffer_PracticalIntroductionDataStructuresAlgorithms]]
- Goodrich, Michael T., Roberto Tamassia, and David M. Mount. _Data structures and algorithms in C++_. John Wiley & Sons, 2011.
- Material do professor Dr. Mário Felice. Disponível em: http://www.aloc.ufscar.br/felice. Acessado em Fev/2022.
- Memory Management. Disponível em: https://docs.python.org/3/c-api/memory.html. Acessado em Fev/2022