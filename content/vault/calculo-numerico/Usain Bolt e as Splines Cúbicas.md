---
title: "Usain Bolt e as Splines Cúbicas"
---

Nos jogos olímpicos de Beijing, China, em 2008, os oito homens mais rápidos do mundo participaram da prova dos 100 metros rasos. Um deles era o jamaicano de 21 anos [Usain Bolt](https://pt.wikipedia.org/wiki/Usain_Bolt).

<iframe width="560" height="315" src="https://www.youtube.com/embed/oetnQgsoN-o?controls=0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

[Usain Bolt](https://pt.wikipedia.org/wiki/Usain_Bolt) quebrou o recorde mundial dos 100 metros rasos, correndo os 100 metros em 9.69 segundos. Uma velocidade média de $\frac{100}{9.69} = 10.32 m/s$.  Mas qual teria sido sua velocidade máxima ao longo do percurso?

Isso pode ser estimado a partir do tempo necessário para percorrer os primeiros 10 metros, 20 metros, ...., 100 metros cujas informações estão na tabela a seguir. Note que a velocidade máxima pode ter sido atinginda entre as distâncias medidas (na marca de 75m) por exemplo.

| Distância (m) | Tempo (s) | Velocidade média (km/h)|
| ------------- | --------- | ---------------- |
| 0             | 0.00      | 0.00             |
| 10            | 1.85      | 19.4             |
| 20            | 2.87      | 35.3             |
| 30            | 3.78      | 39.6             |
| 40            | 4.65      | 41.4             |
| 50            | 5.50      | 42.4             |
| 60            | 6.32      | 43.9             |
| 70            | 7.14      | 43.9             |
| 80            | 7.96      | 43.9             |
| 90            | 8.79      | 43.4             |
| 100           | 9.69      | 40.0             |


O comando a seguir plota um gráfico dos pontos *tempo x distância*, no Octave. 

```matlab
times = [0 1.85 2.87 3.78 4.65 5.50 6.32 7.14 7.96 8.79 9.69];
dists = 0:10:100;
scatter(dists, times);
```

# Qual a velocidade máxima atingida pelo corredor durante a prova?

Considere a função $s(t)$ que relaciona a distância percorrida até o instante $t \geq 0$. A derivada $\frac{d s(t)}{dt}$ representa a velocidade em cada instante $t$, bastando, com isso, encontrar o máximo de $d(t)$. Infelizmente, a tabela apresenta apenas dados discretos, impossibilitando o cálculo de $\frac{d s(t)}{dt}$. No entanto, podemos utilizar [[Splines cúbicas]] para obter uma aproximação para $s(t)$.


## Aproximação por [[Splines cúbicas]]

Para os $m+1 = 11$ pontos fornecidos. **Supondo uma tendência linear nos extremos**, $S_1 = S_{11} = 0$, pode-se utilizar o seguinte sistema.

$$
\begin{bmatrix}
2(h_1 + h_2) & h_2           & & \\
h_2          & 2(h_2 + h_3)  & h_3 & \\
             & \ddots        & & \\
			 & h_{m-1}        & 2(h_{m-1} + h_{m})& \\
\end{bmatrix} \begin{bmatrix}
S_2\\
S_3\\
\vdots\\
S_{m}
\end{bmatrix}= 
6 \begin{bmatrix}
\frac{y_3 - y_2}{h_2} - \frac{y_2 - y_1}{h_1}\\
\frac{y_4 - y_3}{h_3} - \frac{y_3 - y_2}{h_2}\\
\vdots\\
\frac{y_{m+1} - y_{m}}{h_{m}} - \frac{y_{m} - y_{m-1}}{h_{m-1}}\\
\end{bmatrix}
$$

A solução do sistema fornece os valores de $S = [0, S_2, \ldots, S_{m}, 0]$. Isso permite o cálculo de $a_i$,  $b_i$,  $c_i$  e $d_i$, $i = 1, \ldots, m$, para uma função aproximadora de $$s(t) \approx \tilde{s}_i(t) = a_i(t - t_i)^3 + b_i(t - t_i)^2 + c_i(t - t_i) + d_i, \quad [t_i, t_{i+1}], \quad  i = 1, \ldots, m.$$

Como a velocidade (aproximada) é dada por:  

$$\frac{d \tilde{s}_i(t)}{dt} = 3a_i(t - t_i)^2 + 2b_i(t - t_i) + c_i, \quad [t_i, t_{i+1}], \quad  i = 1, \ldots, m$$ pode-se encontrar um ponto de máximo (aproximado) para $s(t)$ calculando 

$$\max_{i \in \{1, \ldots, m\}}  \frac{d \tilde{s}_i(t)}{dt}.$$
Para calcular o $\displaystyle \max_{i \in \{1, \ldots, m\}} \frac{d \tilde{s}_i(t)}{dt}$, pode-se encontrar um ponto crítico utilizando $\frac{d^2 \tilde{s}_i(t)}{dt} = 0$ para cada um dos intervalos $[t_i, t_{i+1}], i \in \{1, \ldots, m\}$.

Como 
$$\frac{d^2 \tilde{s}_i(t)}{dt} = 6a_i(t - t_i) + 2b_i = 0, \quad i \in \{1, \ldots, m\},$$ 
então, o ponto crítico (máximo ou mínimo) ocorre em $$t_{c} = t_i - \frac{b_i}{3a_i}.$$ Com isso, tem-se que a velocidade crítica (máxima ou mínima) em cada intervalo $[t_i, t_{i+1}], i \in \{1, \ldots, m\}$:

$$\frac{d \tilde{s}_i(t_c)}{dt} = 3a_i(t_c - t_i)^2 + 2b_i(t_c - t_i) + c_i, \quad i \in \{1, \ldots, m\}.$$

Note ainda que é necessário garantir que o ponto de mínimo ocorre dentro do domínio de cada função, $[t_i, t_{i+1}], i \in \{1, \ldots, m\}$, e pode ser necessário avaliar a função nos extremos do intervalo.

---

# Código no Octave para plotar a velocidade em cada ponto

```matlab
clear;  % Clearing workspace

times = [0 1.85 2.87 3.78 4.65 5.50 6.32 7.14 7.96 8.79 9.69];
dists = 0:10:100;

m = length(times) - 1;

#scatter(times, dists);
#hold on;
for i = 1:m
  h(i) = times(i+1) - times(i);
endfor

% Assuming a linear tendency on the extremes
A(1, 1) = 2*(h(1) + h(2)); A(1, 2) = h(2);
for i=2:m-2
  A(i, i-1) = h(i);
  A(i, i) = 2*(h(i) + h(i+1));
  A(i, i+1) = h(i+1);
endfor
A(m-1, m-2) = h(m-1); A(m-1, m-1) = 2*(h(m-1) + h(m));

for i=1:m-1
  B(i) = (dists(i+2) - dists(i+1))/h(i+1) - (dists(i+1) - dists(i))/h(i);
end

B = 6*B';

S = linsolve(A, B);
S = [0; S; 0]

for i=1:m
  a(i) = (S(i+1) - S(i))/(6*h(i));
  b(i) = S(i)/2;
  c(i) = (dists(i+1) - dists(i))/h(i) - (S(i+1)*h(i) + 2*S(i)*h(i))/6;
  d(i) = dists(i);
endfor

for i=1:m
  x = times(i):0.01:times(i+1);
  plot(x, 3*a(i)*(x - times(i)).^2 + 2*b(i)*(x - times(i)) + c(i), "linewidth", 2);
  hold on;
endfor
```

--- 
# Referências 

- Strogatz, Steven. _Infinite powers: How calculus reveals the secrets of the universe_. Houghton Mifflin Harcourt, 2019.
- https://sportsscientists.com/2008/08/beijing-2008-men-100m-race-analysis/
