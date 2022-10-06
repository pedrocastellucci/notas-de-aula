---
title: "Teorema de Taylor"
---

Uma das ideias centrais da Série de Taylor é aproximar funções não polinomais por funções polinomiais. 

> [!INFO] O Teorema de Taylor
> Seja $k \geq 1$ um número inteiro e $f: \mathbb{R} \rightarrow \mathbb{R}$ uma função $k$ vezes diferenciável em um ponto $a\in \mathbb{R}$. Então, exite uma função $h_k: \mathbb{R} \rightarrow \mathbb{R}$ tal que
> $$f(x) = f(a) + f'(a)(x-a) + \frac{f''(a)}{2}(x-a)^2 + \ldots + \frac{f^{(k)}}{k!}(x - a)^k + h_k(x)(x-a)^k$$ 
> com $\displaystyle \lim_{k \rightarrow \infty} h_k(x) = 0.$

Em termos práticos, isso implica que a função $f(x)$ pode ser aproximado pelo polinômio de Taylor, na vizinhança de um ponto $a \in \mathbb{R}$

Por exemplo, considere a função $f(x) = cos(x)$. Na vizinhança de $a = 0$, tem-se:

$$f(x) = cos(x) = 1 - \frac{1}{2}x^2 + \frac{1}{24}x^4 + \ldots$$
Quanto maior o número de termos adicionados à série, melhor é a aproximação.

<iframe src="https://www.desmos.com/calculator/rp0vhqtcps?embed" width="600" height="500" style="border: 1px solid #ccc" frameborder=0></iframe>


# Referências
- Vídeo do Canal 3Blue1Brown. Séries de Taylor - Capítulo 10, Essência do Cálculo. https://youtu.be/3d6DsjIBzJ4