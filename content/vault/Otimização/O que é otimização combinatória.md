---
title: "Otimização combinatória"
alias: [otimização combinatória]
---

# Introdução à otimização combinatória

Problemas combinatórios consistem em encontrar um (ou vários) elementos de um conjunto que satisfaz (em) restrições pré-definidas. Existem alguns tipos de problemas diferentes: 

1. Encontrar uma solução satisfazendo um conjunto de restrições.
2. Encontrar todas as soluções satisfazendo um conjunto de restrições.
3. Encontrar uma solução ótima de acordo com uma função objetivo. 

Problemas de Otimização Combinatória são problemas combinatórios que potencialmente admitem mais de uma solução e essas soluções são diferenciadas por uma medida de qualidade, a função objetivo. 

Diversos problemas de otimização combinatória são NP-difíceis. Simplificadamente, isso faz com que o tempo de resolução cresça exponencialmente com o tamanho do problema. Por isso, algoritmos baseados na enumeração explícita de cada solução viável conseguem resolver apenas instâncias pequenas de tais problemas. Por isso, frequentemente, instâncias de interesse prático, demandam por estratégias mais sofisticadas de solução. 

Duas dessas estratégias são: métodos exatos e métodos heurísticos. Os métodos exatos, como o branch-and-cut, são métodos que garantem a otimalidade da solução encontrada desde que uma demanda por recursos computacionais (tempo e memória) possa ser atendida. Métodos heurísticos são métodos que relaxam a busca por soluções ótimas em prol da obtenção de uma solução boa em tempo computacional reduzido.

![[attachments/Pasted image 20220908151703.png]]

Dentre os métodos exatos está o arcabouço conhecido como [[Branch-and-cut||branch-and-cut]]. A implementação de algoritmos de [[vault/Otimização/Branch-and-cut|branch-and-cut]] para um problema costuma ser não trivial. Para garantir a eficiência de tais algoritmos é necessário combinar estratégias de pré-processamento, exploração de árvores de branch-and-bound, planos de corte, entre outros. Nesse caso, é necessário construir problemas auxiliares para a obtenção de limitantes duais para o problema a ser resolvido. O arcabouço de branch-and-cut é de tamanha importância que há diversos pacotes computacionais que fornecem uma implementação pronta como [[Gurobi]], [[SCIP]], [[CPlex]] e [[Cbc]]. Para utilizar tais pacotes é necessário conseguir escrever o problema utilizando o paradigma de [[vault/Otimização/Modelagem para programas lineares inteiros|Programação Linear e Inteira]]. 

Métodos de solução heurísticos relaxam a garantia de otimalidade da solução em prol de reduzir os recursos computacionais necessários, em geral, deseja-se obter uma solução de boa qualidade (não necessariamente ótima) mais rapidamente. Existem diversas estratégias heurísticas, meta-heurísticas, que podem ser aplicadas a inúmeros problemas. Entre eles estão [[algoritmos genéticos]], [[algoritmos de colônias de formigas]], [[otimização por enxame de particulas]], [[busca tabu]], [[simulated annealing]], [[iterated local search]], [[variable neighborhood search]],  e muitos outros.