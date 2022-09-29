---
title: "Método de Jacobi"
---

```python
def jacobi(A, b, x, stop_error=1e-10, max_iter=1000):
    iter = 0
    error = compute_erro(A, b, x)
    n = len(x)
    x_ant = np.copy(x)
    while error > stop_error and iter < max_iter:
        for i in range(n):
            sum1 = np.dot(A[i, :i], x[:i])
            sum2 = np.dot(A[i, i+1:], x[i+1:])
            x_ant[i] = 1/A[i, i]*(b[i] - sum1 - sum2)
        x = np.copy(x_ant)
        error = compute_erro(A, b, x)
        iter += 1
    return x
```