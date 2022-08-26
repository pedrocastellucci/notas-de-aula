# Avaliação de expressões aritméticas

- Considere que se deseja avaliar expressões aritméticas como a seguinte, **que começa e termina com parênteses**:

$$ (1 + ((2 + 3) *  (4 * 5)))$$
- Um algoritmo para isso é o Algoritmo de Duas Pilhas desenvolvido por E. W. [[Dijkstra]]. O algoritmo utiliza duas pilhas, uma para operadores outra para operandos. Processa-se a string da esquerda para direita, um caracter por vez, da seguinte forma. 
	- Adiciona-se *operandos* na pilha de operandos.
	- Adiciona-se *operadores* na pilha de operadores.
	- Ignora-se parênteses "esquerdos", (.
	- Ao se encontrar um parêntese "direito", remove-se um operador da pilha correspondente, remove-se o número adequado de operadores da pilha correspondente e adiciona-se o resultado da operação na pilha de operandos.
	- Após o processamento do útimo parêntese "direito", tem-se um único valor na pilha, que é o resultado da expressão.  

## Referências
- Sedgewick, Robert, e Kevin Wayne. _Algorithms_ (4a Edição). Addison-Wesley Professional, 2011.