---
alias: [busca binária, Busca Binária]
---

# Algoritmo de busca binária

Uma das operações frequentes em dados é a busca (ou pesquisa). Essa operação consiste em, dado um elemento, verificar se ele está presente em uma coleção. 

Aqui, vamos considerar o problema da busca em uma coleção linear de dados armazenada em um vetor. 

> **Busca sequencial**. O algoritmo mais simples para encontrar um elemento em um vetor consiste em percorrer o vetor, elemento a elemento. 

A **busca sequencial** em um vetor com $n$ elementos é um algoritmo cujo o pior caso é $O(n)$. No entanto, caso o conjunto de dados esteja ordenado é possível uma sofisticação.

Considere um vetor $v$ armazenando os seguintes valores, nesta ordem: 

$$3, 10, 14, 15, 25, 40, 65, 78, 83, 99, 100.$$ Para se iniciar uma busca pelo valor $x = 78$ por exemplo, pode-se verificar o elemento no meio do vetor $v[m] = 40$:
1. Caso $x = v[m]$ o elemento foi encontrado.
2. Caso $x < v[m]$, então reinicia-se o algoritmo apenas com a primeira metade do vetor.
3. Caso $x > v[m]$, então reinicia-se o algoritmo com a segunda metade do vetor.

Note que o algoritmo é naturalmente recursivo. Embora implementações iterativas sejam frequentes. 

## Análise do algoritmo

O algoritmo inicia com um vetor de tamanho $n$, após a primeira iteração, o algoritmo reinicia com um vetor de tamanho, aproximadamente, $\frac{n}{2}$. Na iteração seguinte, $\frac{n}{4}$. Ou seja, é gerada a sequência: 

$$n, \frac{n}{2}, \frac{n}{4}, \ldots, 1$$
O número de termos dessa sequência é $O(log\ n)$, que é a complexidade da busca binária em um vetor em número de operações. 

- Qual seria a complexidade desse algoritmo se implementado em uma [[Listas ligadas|lista ligada]]? #pergunta 
# Referências

- Ziviani, Nivio. _Projeto de algoritmos: com implementações em Pascal e C_. Vol. 2. Luton: Thomson, 2004.