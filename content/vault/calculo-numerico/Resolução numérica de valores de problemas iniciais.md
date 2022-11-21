---
title: "Resolução de EDOs"
---

- Métodos baseados no [[Teorema de Taylor]]

## Um exemplo que vai e volta

Considere um pêndulo de comprimento $\ell$ como o da figura a seguir. 

![[attachments/Pasted image 20221101142955.png|300]]

De acordo com a [Segunda Lei de Newton](https://pt.wikipedia.org/wiki/Leis_de_Newton), sabemos que $F = ma$. No pêndulo, ao longo do eixo de movimento (linha verde na figura), temos apenas a projeção da força gravitacional $mgsin(\theta)$. Note que, no eixo perpendicular ao movimento a tração e $mgcos(\theta)$ se equilibram. Portanto $$F = -mgsin(\theta) = ma,$$ implicando em $a = -gsin(\theta)$. O sinal negativo evidencia o fato de que a aceleração $a$ e o movimento do ângulo $\theta$ apontam para direções opostas. 
Mas o comprimento do arco $s = \ell \theta$, então $$v = \frac{ds}{dt} = \ell \frac{d\theta}{dt}.$$ Portanto, $$a = \frac{d^2 \theta}{dt^2} = \ell \frac{d\theta}{dt}.$$
Com isso, tem-se a uma [[equação diferencial ordinária]] que representa o movimento pendular.

>[!INFO] Equação do pêndulo
> $$\frac{d^2\theta}{dt^2} + \frac{g}{\ell} sin(\theta) = 0$$

- $\ell$ é o comprimento do pêndulo
- $g \approx 9.81\frac{m}{s^2}$ é a constante gravitacional 

Para valores pequenos de $\theta$ pode-se utilizar a aproximação $sin(\theta) \approx \theta$ simplificando o processo de solução da EDO.

A equação diferencial de segunda ordem que representa o movimento do pêndulo, pode ser convertida em um sistema de EDOs de segunda ordem. Para isso, seja $y_1 = \theta$, tem-se:

- $\dot{\theta} = \dot{y_1} = y_2$
- $\ddot{\theta} = \dot{y_2} = -\frac{g}{\ell}sin(y_1)$

Considerando as condições iniciais $\theta(t = 0) = \frac{\pi}{4}$ e $\dot{\theta}(t=0) = 0$, e o domínio $[0, T]$, a relação de recorrência para resolver o PVI utilizando o [[Método de Euler]] é dada por:

$$
\begin{align}
&y_1^{(k+1)} = y_1^{(k)} + h y_2^{(k)}\\
&y_2^{(k+1)} = y_2^{(k)}-h\frac{g}{\ell}sin(y_1^{(k)})\\
&t^{(k+1)} = t^{(k)} + h, 
\end{align}
$$

para $k = 1, \ldots, \lfloor\frac{b-a}{n} \rfloor$ para $n$ subdivisões do domínio.

```python
import matplotlib.pyplot as plt
import math

def pendulum_func(y1, y2):
    return y2, -g/L*math.sin(y1)

g = 9.81 # m/s^2
L = 0.1 # meters
y1 = math.pi/4  # 45 degrees
y2 = 0  # Initial velocity is zero
t = 0
T = 1 # Simulate until 1 second
n = 100 # How many discretization steps
h = (T-t)/n
positions = [(t, y1)]
while t < T:
    ret = pendulum_func(y1, y2)
    y1, y2 = y1 + h*ret[0], y2 + h*ret[1]
    t += h
    positions.append((t, y1)) # Saving to plot

t, y = zip(*positions)
plt.plot(t, y)
plt.show()
```

Uma alternativa seria a utilização do [[Métodos de Runge-Kutta|Método de Runge-Kutta]] de segunda ordem. Para isso, pode-se usar as seguintes relações de recorrência com as funções $f_1(t, y_1, y_2) = y_2$ e $f_2(t, y_1, y_2) = -\frac{g}{\ell}sin(y1)$

$$
  \begin{align}
    & y_1^{(k+1)} = y_1^{(k)} + 0.5h(K_1^{f_1} + K_2^{f_1}),\\
    & y_2^{(k+1)} = y_2^{(k)} + 0.5h(K_1^{f_2} + K_2^{f_2}),\\
    & t^{(k+1)} = t^{(k)} + h
  \end{align}
$$
  em que
$$
  \begin{align}
    & K_1^{f_1} = f_1(t^{(k)}, y_1^{(k)}, y_2^{(k)}),\\
    & K_1^{f_2} = f_2(t^{(k)}, y_1^{(k)}, y_2^{(k)}),
\end{align}
$$
e
$$
\begin{align}
    & K_2^{f_1} = f_1(t^{(k)} + h, y_1^{(k)} + h K_1^{f_1}, y_2^{(k)} + h K_1^{f_2}),\\
    & K_2^{f_2} = f_2(t^{(k)} + h, y_1^{(k)} + h K_1^{f_1}, y_2^{(k)} + h K_1^{f_2})
\end{align}
$$



```python
import matplotlib.pyplot as plt
import math

def pendulum_func(y1, y2):
    return y2, -g/L*math.sin(y1)

g = 9.81 # m/s^2
L = 0.1 # meters
y1 = math.pi/4  # 45 degrees
y2 = 0  # Initial velocity is zero
t = 0
T = 1 # Simulate until 1 second
n = 100 # How many discretization steps
h = (T-t)/n
positions = [(t, y1)]
while t < T:
    K1 = pendulum_func(y1, y2)
    K2 = pendulum_func(y1 + h*K1[0], y2+h*K1[1])
    y1, y2 = y1 + h/2*(K1[0] + K2[0]), y2 + h/2*(K1[1] + K2[1])
    t += h
    positions.append((t, y1)) # Saving to plot

t, y = zip(*positions)
plt.plot(t, y)
plt.show()
```

Ambas as soluções, com o [[Método de Euler]] e com o [[Métodos de Runge-Kutta|Método de Runge-Kutta]] de segunda ordem, possuem limitações conforme o valor de $T$ aumenta, devido ao acúmulo de erros numéricos ao longo das iterações.  Experimente com diferentes valores de $T$ para verificar o problema. 

- Para diferentes valores de $T$ compare os resultados dos dois métodos, para determinar qual dos métodos é mais preciso #tarefa
- Implemente o [[Métodos de Runge-Kutta|Método de Runge-Kutta]] de quarta ordem para o problema e compare sua precisão com os demais. #desafio 

## Montando uma animação

Com a solução do PVl, é possível montar uma animação como faz o código a seguir.

```python
import math
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

def pendulum_func(y1, y2):
    return y2, -g/L*math.sin(y1)

def init():    
    ax.set_xlim(-1.4*L, 1.4*L)
    ax.set_ylim(-1.2*L, 0.1)
    return line,

def update(frame):
    theta = frame
    x = np.sin(theta)*L
    y = -np.cos(theta)*L
    thisx = [0, x]
    thisy = [0, y]
    line.set_data(thisx, thisy)
    return line,

g = 9.81 # m/s^2
L = 0.1 # meters
y1 = math.pi/4  # 45 degrees
y2 = 0  # Initial velocity is zero
t = 0
T = 1.31 # Simulate until this time
n = 100 # How many discretization steps
h = (T-t)/n
positions = [(t, y1)]
while t < T:
    K1 = pendulum_func(y1, y2)
    K2 = pendulum_func(y1 + h*K1[0], y2+h*K1[1])
    y1, y2 = y1 + h/2*(K1[0] + K2[0]), y2 + h/2*(K1[1] + K2[1])
    t += h
    positions.append((t, y1)) # Saving to plot

t, y = zip(*positions)
fig, ax = plt.subplots()
xdata, ydata = [], []
line, = ax.plot([], [], 'o-', lw=1)
fps = 30
ani = FuncAnimation(fig, update, frames=y,
                    init_func=init, blit=True, interval=1000/fps)
plt.show()
```

# Referências

- Burden, R. L., Faires, J. D., & Burden, A. M. (2015). _Numerical analysis_. Cengage learning.
- Pendulum (Mechanics). Wikipedia. Disponível em: https://en.wikipedia.org/wiki/Pendulum_(mechanics). Acessado em Novembro de 2022.
- Simple pendulum with friction and forcing | Lecture 27 | Differential Equations for Engineers. Disponível em https://youtu.be/SZWn7x4g-Vo. Acessado em Novembro de 2022.