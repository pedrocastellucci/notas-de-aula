---
title: "O problema do caixeiro viajante"
alias: [TSP, problema do caixeiro viajante, Problema do caixeiro viajante]
---

# 
# O Problema do Caixeiro Viajante

Um vendedor deseja visitar as cidades $0, 1, 2, \ldots, n-1$, partindo de uma delas. O custo de viajar de uma cidade $i$ para uma cidade $j$ é $c_{ij}$, $i, j = 0, 1, \ldots, n-1$. O problema de determinar uma rota com o menor custo que visita todas as cidades exatamente uma vez é conhecido como Problema do Caixeiro Viajante.



## Modelo de programação linear inteira

- Variáveis
	- $x_{ij} \in \{0, 1\}$: Indica se um arco $(i, j)$ é utilizado ou não.
	- $0 \leq u_i \leq n-1$: Indica a ordem do $i$ nó na rota.
- Função objetivo:
	- $$\min \sum_{i = 0}^{n-1} \sum_{j=0}^{n-1} c_{ij}x_{ij}$$
- Restrições
	- $$\sum_{j=1, i \neq j}^n x_{ij} = 1 \quad i \in \{0, 1, \ldots, n-1\}$$
	- $$\sum_{j=1, i \neq j}^n x_{ji} = 1 \quad i \in \{0, 1, \ldots, n-1\}$$
	- $$u_j \geq u_i + 1 - (n-1)(1 - x_{ij}) \quad i, j \in \{1, 2, \ldots, n-1\}, i \neq j$$
	- $$x_{ij} \in \{0, 1\} \quad i, j \in \{0, 1, \ldots, n-1\}$$
	- $$0 \leq u_i \leq n-1 \quad i \in \{0, 1, \ldots n-1\}$$
	

## Exemplo de código

### [[Gurobi]]

### [[Python-mip]]

```python
from random import randint, seed
from itertools import product
from mip import Model, xsum, minimize, BINARY, CONTINUOUS

seed(2)
def generate_data(n_points):
    points = []
    for i in range(n_points):
        points.append((randint(0, 100), randint(0, 100)))        
    return points

def compute_dist_matrix(points):
    dist = {}
    for i, p1 in enumerate(points):
        for j, p2 in enumerate(points):
            dist[i, j] = ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**0.5
    return dist

def plot_solution(points, tour):
    import matplotlib.pyplot as plt    
    xs, ys = zip(*points)
    plt.scatter(xs, ys)
    lines_x = []
    lines_y = []
    for v in tour:
        lines_x.append(xs[v])
        lines_y.append(ys[v])
        plt.annotate(v, (xs[v]*1.01, ys[v]*1.01), fontsize=10)
    lines_x.append(xs[tour[0]])
    lines_y.append(ys[tour[0]])
    plt.plot(lines_x, lines_y)    
    plt.grid('on')
    plt.show()

n_points = 20
V = set(range(n_points))
points = generate_data(n_points)
c = compute_dist_matrix(points)

model = Model()
x = {}
for i in V:
    for j in V:
        x[i, j] = model.add_var(var_type=BINARY, name="x[%d, %d]" % (i, j))

u = [model.add_var(var_type=CONTINUOUS, lb=0, ub=n_points-1, name="u[%d]" % i)
    for i in V]

model.objective = minimize(xsum(c[i, j]*x[i, j] for i in V for j in V))

for i in V:
    model += xsum(x[i, j] for j in V - {i}) == 1

for i in V:
    model += xsum(x[j, i] for j in V - {i}) == 1

for (i, j) in product(V - {0}, V - {0}):
    if i != j:
        model += u[j] >= u[i] + 1 - (n_points-1)*(1 - x[i, j])

model.optimize()

if model.num_solutions > 0:
    print("Solution found:")
    print("Used arcs:")
    for (i, j) in product(V, V):
        if x[i, j].x > 0.5:
            print("({}, {})".format(i, j))
    tour = sorted(list(V), key=lambda i:u[i].x)
    print("Tour:", tour)
#    plot_solution(points, tour)
```

### [[Or-tools]]

