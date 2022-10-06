---
title: "Códigos de Huffman"
---


# Códigos de Huffman

Códigos de Huffman são capazes de realizar compressão de dados sem perda de informação (*lossless*). Economias de 20 a 90% são típicas, dependendo do tipo de dado a ser comprimido.

Aqui, se considera um dado com uma série de caracteres. O algoritmo de Huffman utiliza uma tabela com a frequência de cada caracter para construir uma forma ótima de representar cada caracter como uma *string* de *bits*.

## Exemplo

Suponha um arquivo de 100000 caracteres de dados que se deseja comprimir. É observado que os caracteres no arquivo aparecem com uma certa frequência e apenas seis caracteres diferentes aparecem. Para utilizar um código de tamanho fixo, seriam necessários 3 bits para cada caracter, mas também é possível utilizar um código de tamanho variável, como mostra a tabela.

|                            | a   | b   | c   | d   | e    | f    |
| -------------------------- | --- | --- | --- | --- | ---- | ---- |
| Frequência (em milhares)   | 45  | 13  | 12  | 16  | 9    | 5    |
| Código de tamanho fixos    | 000 | 001 | 010 | 011 | 100  | 101  |
| Código de tamanho variável | 0   | 101 | 100 | 111 | 1101 | 1100 |

Utilizando um código de tamanho fixo, seriam utilizados $3 \cdot (45 + 13 + 12 + 16 + 9 + 5)\cdot 10^3 = 300000$ bits. Mas utilizando o código de tamanho variável proposto, seriam utilizados $(1 \cdot 45 + 3 \cdot 13 + 3 \cdot 12 + 3 \cdot 16 + 4 \cdot 9 + 4 \cdot 5) \cdot 10^3 = 224000$ bits. Resultando numa economia de 66000 *bits* (aproximadamente 25%). Na verdade, essa é uma forma ótima de representar esses dados. 

# Códigos de prefixo

Serão considerados apenas códigos tais que cada palavra-código (*codeword*) não é prefixo de uma outra palavra-código. Códigos de prefixo possuem a vantagem de simplificar a decodificação.

## Árvores de decodificação para o exemplo

[![](https://mermaid.ink/img/pako:eNptkLsOgkAQRX9lM9WSaMKKmDiFiYrvUrtdipVdlChoEAoj_rsjEhqc6ibnninuC6KbsYBwyvX9zA6ByhjdlAvXdVi_P2GVW7GZ1Dj0wy4TFZtz33d-pI6tFPDBH0DGgntuA-pOayxlhGIQdhA5K3lE4TWoftBaay6GTgeQs5EGxahx6lbrbGWMfpeQtJMWxyH0ILV5qhND07y-PQXF2aZWAVI0Or8oUNmberosbvtnFgEWeWl7UN6NLmyQaFo0BYz19WHfH4grXGI)](https://mermaid.live/edit#pako:eNptkLsOgkAQRX9lM9WSaMKKmDiFiYrvUrtdipVdlChoEAoj_rsjEhqc6ibnninuC6KbsYBwyvX9zA6ByhjdlAvXdVi_P2GVW7GZ1Dj0wy4TFZtz33d-pI6tFPDBH0DGgntuA-pOayxlhGIQdhA5K3lE4TWoftBaay6GTgeQs5EGxahx6lbrbGWMfpeQtJMWxyH0ILV5qhND07y-PQXF2aZWAVI0Or8oUNmberosbvtnFgEWeWl7UN6NLmyQaFo0BYz19WHfH4grXGI)

## Construindo uma árvore com o código de Huffman

Seja $C$ um conjunto de $n$ caracteres e a cada caracter $c \in C$ está associado a uma frequência *c.freq*.  O algoritmo a seguir constrói uma árvore correspondendo ao melhor código com uma lógica *bottom-up.* Ele inicia com um conjunto de $|C|$ nós folhas e realiza $|C|-1$ operações de junção para construir uma árvore. O algoritmo utiliza uma fila de prioridade (de mínimo) de caracteres, com a prioridade sendo *c.freq*. O resultando de uma junção é um novo objeto cuja a frequência é a soma dos dois operandos.

```
function huffman_tree(C)
	n = |C|
	Q = C
	for i = 1 to n-1
		crie um novo nó z
		z.left = x = EXTRACT_MIN(Q)
		z.right = y = EXTRACT_MIN(Q)
		z.freq = x.freq + y.freq
		INSERT(Q, z)
	return EXTRACT_MIN(Q)  // Raiz da árvore
```

### Análise do algoritmo

Assumindo que a fila de prioridade seja implementada com um [[Heap]] de mínimo, a construção do [[Heap]], para uma cadeia com $n$ caracteres pode ser feita em $O(log(n))$. O laço de repetição executa $(n-1)$ vezes, como cada operação da [[Heap]] possui custo $O(log(n))$, o laço contribui com $O(nlog(n))$ para o custo do algoritmo. É possível implementá-lo em $O(n log (log(n)))$ utilizando uma [[Árvore de Van Emde Boas]]. 

# Referências

- Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2009). Introduction to Algorithms. third. _New York_.