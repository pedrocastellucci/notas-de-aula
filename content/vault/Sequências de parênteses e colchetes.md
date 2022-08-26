# Sequências bem casadas de parênteses e colchetes

- Uma sequência de parênteses é colchetes é dita bem formada se parênteses e colchetes estão casados de maneira correta. 
	- Sequência bem formada: ( ( ) [ ( ) ] )
	- Sequência mal formada: ( [ ) ]
- Mais formalmente, se uma sequência $S$ de parênteses e colchetes é bem formada então $$S = \begin{cases} \mbox{Sequência vazia,}\\ (S)S,\\ [S]S.\end{cases}$$
- Como implementar um algoritmo que identifique se uma sequência está bem formada ou não?
	- Uma solução é se basear em um [[Pilha]], observando que um caracter fechando um parênteses (ou colchetes), fecha o último parênteses (ou colchetes) que foi aberto. Ou seja, é um padrão do tipo [[LIFO]]. 
		- Processa-se a sequência, caracter por caracter, da esquerda para a direta.
			- Sempre que se encontra um caracter abrindo um parênteses ou colchetes, adiciona-o na pilha. 
			- Sempre que se encontra um caracter fechando um parênteses ou colchetes, verifica-se o topo da pilha. 
				- Se a pilha estiver vazia, a sequência não é bem formada.
				- Se o topo da pilha casa com o caracter atual, então, remove-se o caracter da pilha e segue-se para o próximo caracter na sequência;
					- caso contrário, a sequência não é bem formada.
		- Terminada a sequência, se a pilha estiver vazia, então tem-se uma sequência bem formada. Se ainda houver elemento na pilha, então a sequência não é bem formada.

```python
def is_well_formed(S):
    i = 0
    stack = Stack()
    while i < len(S):
        c = S[i]
        if c == "(" or c == "[":
            stack.push(c)
        elif c == ")":
            if stack.is_empty():
                return False
            elif stack.peek() == "(":
                stack.pop()
        elif (c == ']'):
            if stack.is_empty():
                return False
            elif stack.peek() == "[":
                stack.pop()
        i += 1
    return stack.is_empty()
```

- Como ficaria a implementação se fosse utilizada uma lista ligada para implementação da [[Pilha]]? #pergunta 

## Análise da solução

### Eficiência de tempo

Considere a análise de pior caso (Qual é um pior caso? #pergunta). Cada iteração do laço possui tempo constante, $O(1)$. Isso pois as operações da Pilha podem ser todas implementadas em $O(1)$. Cada um dos $n$ caracteres da sequência precisa ser processado uma única vez, no pior caso, portanto, o algoritmo tem eficiência de tempo $O(n)$. 

### Eficiência de espaço

O número de elementos na pilha nunca ultrapassa $O(n)$ no pior caso. Portanto, o algoritmo possui complexidade de espaço $O(n)$. 

Forneça um exemplo de sequência de tamanho $n$ que faz com a Pilha fique, em algum momento, com $n$ elementos. #exercício 