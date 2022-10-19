---
title: "Resolução de EDOs"
---

- Métodos baseados no [[Teorema de Taylor]]

## Um exemplo que vai e volta

Equação do pêndulo

$$\frac{d^2\theta}{dt^2} + \frac{g}{L} sin(\theta) = 0$$
- $L$ é o comprimento do pêndulo
- $g \approx 9.81\frac{m}{s^2}$ é a constante gravitacional 

Para valores pequenos de $\theta$ pode-se utilizar a aproximação $sin(\theta) \approx \theta$ simplificando o processo de solução da EDO.

A equação diferencial de segunda ordem que representa o movimento do pêndulo, pode ser convertida em um sistema de EDOs de segunda ordem. Para isso, seja $y_1 = \theta$, tem-se:

- $\dot{\theta} = \dot{y_1} = y_2$
- $\ddot{\theta} = \dot{y_2} = -\frac{g}{L}sin(y_1)$

A relação de recorrência para resolver o PVI utilizando o [[Método de Euler]] é dada por:
- $y_1^{(k+1)} = y_1^{(k)} + h y_2^{(k)}$
- $y_2^{(k+1)} = y_2^{(k)}-h\frac{g}{L}sin(y_1^{(k)})$

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

As relações de recorrência, utilizando o [[Métodos de Runge-Kutta|Método de Runge-Kutta]] de segunda ordem são

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


# Referências

- Burden, R. L., Faires, J. D., & Burden, A. M. (2015). _Numerical analysis_. Cengage learning.