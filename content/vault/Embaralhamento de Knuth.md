---
alias: [Embaralhamento de Fisher-Yates]
---

# Embaralhamento de Knuth

[[Donald Knuth]] propôs um algoritmo que retorna uma permutação aleatória de um vetor. A ideia do algoritmo é a seguinte:

- Dada uma permutação de um vetor, percorre-se o vetor da esquerda para a direita
	- na iteração $i$, escolhe-se uniforme e aleatoriamente um elemento do sufixo do vetor ($v[i+1, \ldots, n$]) para trocar com o elemento da posição corrente.

Uma implementação em [[C++]] é dada a seguir.

```cpp
#include <stdlib.h>
#include <time.h>
#include <vector>

void knuth_shuffle(vector<int>& v){
    srand (time(NULL)); // Always a different seed.
    for (auto i = v.size() - 1; i > 0; i--)
    {  
        auto j = rand() % (i + 1);
        int aux = v[i];
        v[i] = v[j];
        v[j] = aux;        
    }
}
```