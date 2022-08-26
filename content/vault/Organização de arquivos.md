# Busca em arquivos

Algoritmos eficientes para busca em arquivos são de grande importância prática. A busca em arquivos é necessária para lidar com grande quantidade de dados. Um dos desafios do desenvolvimento desses algoritmos é a dependência do hardware utilizado para o armazenamento. 

> Arquivo: Conjunto de dados em um dispositivo de armazenamento secundário (externo).
	>> Qual a diferência entre memória primária e secundária?

## Dispositivos de armazenamento externo

> It is safe to assume that the devices that we use to store huge amounts of information are built to support efficient and straightforward implementations of search ([[1998Sedgewick_AlgorithmInCPart1-4|Algorithms in C. Parts 1-4 (Sedgewick. 1998)]]).

- Dipositivos de armazenamento externo são muito mais lentos do que a memória do computador, mas possuem alta capacidade de armazenamento.  
	- A estruturas de dados podem sacrificar memória para compensar em eficiência.

### Dispositivos de acesso sequencial

- A organização de dados em blocos contínuos em uma fita ou disco é chamada de acesso sequencial. 
- Frequentemente, os registros são armazenados de forma ordenada por chave. 
	- As inserções e remoções podem ser custosas, pois implicam em reorganização do arquivo.
- Buscar elemento a elemento não é rápido o suficiente.
- É simples e fácil de projetar.
- Operações são caras.
- Acesso direto não é possível.
- Fitas magnéticas.
- Tipicamente útil apenas para backup por ser muito lento.


### Dispositivos de acesso direto (aleatório)

- Na organização de acesso direto, os registros são armazenados em posições relativas ao início do arquivo.
	- Discos rígidos permitem acesso direto.
- Não há necessidade de armazenar os registros sequencialmente na memória. 
- Não é necessário ordenar o arquivo.
- É possível acessar os registros desejados imediatamente.
- É custoso, possuindo menos espaço de armazenamento em relação a dispositivos de acesso sequencial.
- Disco, CD, disquete, SSD.
- Útil para 
	- Dados que sofrem buscas frequentemente.
	- Dados muito alterados.

#### Memória secondária em disco rígido

Um disco rígido é tipicamente composto de vários pratos (discos) que rotacionam. Os dados são lidos de e escritos em um prato com os braços. Os braços rotacionam em um eixo pivô comum. Uma trilha é "caminho" no disco definido quando o disco rotacionada e a cabeça de leitura/escrita permanece parada.

Discos são mais baratos e com maior capacidade do que as tecnologias utilizadas na memória principal, no entanto, são consideravelmente mais lentos. Embora os discos rotacionem em uma velocidade de dezenas de milhares de rotações por minutos (e.g. 15000 RPM) uma rotação ainda ocorre em $\frac{1}{15000} \approx 0.07$ milissegundos, o que algumas ordens de magnitude mais lento do que o tempo de acesso da ordem de nanossegundos ($10^{-9}$) usualmente encontrados em chips de silício. Ou seja, se for necessário esperar por uma rotação do disco, é possível realizar 10000 acessos à memória principal nesse mesmo intervalo.

Para tentar reduzir o tempo de espera dos movimentos mecânicos de um disco, os dados armazenados são divididos em páginas (blocos) de mesmo tamanho (para um disco típico, uma página pode ter tamanho de $2^{11}$ a $2^{14}$ bytes). Uma vez que a cabeça de leitura/escrita esteja posicionada corretamente, o processo de leitura/escrita é essencialmente eletrônico é pode ser feito de forma mais eficiente.

Tipicamente, acessar uma página de informações salva em disco é mais lento do que examinar toda a informação lida. 

![[harddisk-representation.excalidraw]]


## Gerência de arquivos

> Conjunto de métodos e técnicas para fazer operações sobre dados em arquivos de forma eficiente. 

- Acessar frequentemente os arquivos (para busca, inserções ou remoções) é muito lento.
	- Solução 1: Carregar todos os dados na memória para manipulá-los e então reescrevê-los em disco ao final das operações:
		- Dados podem não caber em memória.
		- Ler e escrever *todos* os dados pode tomar muito tempo. 
			- Suponha que você quer comprar um item em uma loja online. Seria necessário, por exemplo, ler todo o estoque da loja para mostrar os produtos disponíveis. 
			- Como garantir que todas as operações realizadas foram de fato salvas? (p.e. em uma queda de energia).
			- Tipicamente, uma pequena fração dos dados é de fato utilizada. 

- Princípio básico: Organizar os dados de forma a minimizar o número de acessos à memória secundária. 
	- Organização dos dados é mais rígida em um arquivo.
	- Técnicas de indexação. Dados brutos estão em arquivos mais rígidos e são criados arquivos de índices para acelerar os acessos.

## Tipos de arquivos

### Arquivos de formato variável

- Unidade de endereçamento é o byte.
- São tratados como arquivos de acesso sequêncial.
- Arquivo texto.
- É trabalhado inteiramente na memória. 

### Arquivos de registros
- São organizados em unidades maiores que bytes, com tamanhos sempre iguais, chamados de registros. 
	- Em algumas linguagens de programação, o registro pode ser utilizado como unidade de endereçamento
		- fseek
		- Feito o acesso pode-se realizar operações sobre registro
- Técnicas de gerência de arquivos são voltadas aos arquivos de registros. 

## Organização de arquivos

- Objetivo: Fornecer caminhos de acesso aos registros durante as operações de recuperação e atualização de dados.
- As buscas devem ser o mais eficiente possível.
- Depende dos tipos de consultas permitidas.
	- Consulta simples (por uma chave).
	- Consulta em faixa (salário  > 500).
	- Consulta booleana (utilizando composições lógica 'e' e 'ou').
- Modos de recuperação e atualização.

### Arquivos sequenciais

- Um registro seguido do outro.
- Leitura sequencial.
- Escrita sempre no final do arquivo.
- Indexação por chave primária.
	- Pode-se manter o arquivo ordenado por chave primária.
		- Acesso sequencial é mais rápido em um disco.
		- Inclusão e remoção bastante custosas. Soluções:
			- Cópia; ou
			- utilizar algoritmo da lista ordenada.

#### Exemplo de inclusão

Algoritmo para inserir registro na posição $i$: 
1. Copiar registros do $0$ até $i-1$ em um novo arquivo $F$.
2. Adicionar novo registro ao final de $F$. 
3. Copiar o restante do arquivo original em $F$. 

### Arquivo indexado sequencial
- Os registros são armazenados de forma ordenada no arquivo.
- Mantém um índice de acesso. 
	- Esse índice é carregado na memória principal para se manusear o arquivo.
	- O índice mantém pares chave-valor:
		- a chave $k$ é correspondente a uma chave no conjunto de registros em disco;
		- o valor é uma referência para a posição de início de uma sequência de registros no arquivo. Essa sequência contém todos os registros com chaves que não ultrapassam o valor de $k$.
			- Isso é necessário em casos em que o índice é muito grande. Se o índice for pequeno, pode-se armazenar a posição de todos os registros no arquivo. 
- Mantém área de overflow. Todas as inserções são realizadas na área de overflow. 
	- Note que isso pode violar a propriedade de manter o arquivo ordenado. 
	- É preciso atualizar o arquivo periodicamente, para inserir os registros que estão na área de overflow de forma ordenada.
	- A área de overflow é implementada como uma lista encadeada (cada item possui uma referência para o próximo elemento na sequência).
		- É possível implementar uma área de overflow de forma que os registros fiquem ordenados, mantendo a inserção sempre na última posição do arquivo? #pergunta 
- A remoção é feita marcando os registros como excluído
	- Durante o processo de atualização (e busca), os registros marcados como excluídos são ignorados.
- A vantagem desse método é que simples de ser implementado.
- A desvantagem é o potencial alto custo das atualizações periódicas, devido a forma com que o método lida com as inserções. 

No caso mais simples, pode-se incluir no arquivo de índices a chave e uma referência para o endereço de cada elemento. No entanto, o próprio arquivo de índices pode ser grande demais, nesse caso, pode-se utilizar índices multníveis que, essencialmente, são índices de índices. Essa estratégia é conhecida como índices multi-níveis. As estruturas de dados conhecidas como [[Árvores B]] permitem o crescimento do nível de índices baseado na necessidade e em um tamanho de índice (número de chaves) pré-definido.

![[gerencia_arquivos_indexados.excalidraw|700]]

# Referências 
- [[1998Sedgewick_AlgorithmInCPart1-4|Algorithms in C. Parts 1-4 (Sedgewick. 1998)]].
- Aula 8.1- Introdução à Gerência de Arquivos. https://youtu.be/iNG4l5mWzgU
- Chapter 12. CS3 Data Structures & Algorithms. OpenDSA. https://opendsa.cs.vt.edu/ODSA/Books/CS3/html/LinearIndexing.html