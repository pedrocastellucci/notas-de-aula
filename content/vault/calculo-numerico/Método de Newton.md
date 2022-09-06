---
title: "Método de Newton"
alias: ["Método de Newton-Raphson", "método de Newton"]
---

# O método de Newton (ou Newton-Raphson)

## Notas históricas
Embora o nome do método seja derivado de [Isaac Newton](https://pt.wikipedia.org/wiki/Isaac_Newton). A descrição do método que vamos estudar é substancialmente diferente do utilizado originalmente por Newton. A primeira publicação desse método é datada de 1685. Em 1690, [Joseph Raphson ](https://en.wikipedia.org/wiki/Joseph_Raphson), publicou uma descrição simplificado. Por isso, o método é muitas vezes chamado de Método de Newton-Raphson. Newton e Raphson aplicaram o método exclusivamente para polinômios, foi apenas em 1740 que [Thomas Simpson](https://en.wikipedia.org/wiki/Thomas_Simpson) descreveu o método como um método iterativo para resolver equações não lineares usando [[Cálculo]]. Essencialmente, essa é a descrição que será apresentada aqui.

## Descrição do método

O método de Newton pode ser utilizado para resolver equações $f(x) = 0$, $f: \mathbb{C} \rightarrow \mathbb{C}$. Por enquanto, vamos nos concentrar no caso em que $f: \mathbb{R} \rightarrow \mathbb{R}$. Note que encontrar uma raiz para equação $f(x) = 0$ é equivalente a encontrar um zero da função $f(x)$.

Considere o polinômio $$P(x) = x^5 + x^2 - 1$$
Cujo o gráfico é dado a seguir:

<iframe src="https://www.desmos.com/calculator/ilgfeuouji?embed" width="500" height="500" style="border: 1px solid #ccc" frameborder=0></iframe>

Para encontrar uma raiz da equação $P(x) = 0$, a ideia do método é produzir uma aproximação inicial para $x_0$ para tal raiz. Por exemplo, $x_0 = 1$. 

No ponto $(x_0, P(x_0)) = (1, 1)$ utiliza-se uma aproximação linear para $P(x)$. Isto é, traça-se a reta $r(x)$ tangente a $P(x)$ em $x_0$. A reta é dada por:

$$r(x) = P(x_0) + P'(x_0)(x - x_0),$$
ou seja,  $r(x) = 1 + 7(x - 1)$.

<iframe src="https://www.desmos.com/calculator/6icuole2bi?embed" width="500" height="500" style="border: 1px solid #ccc" frameborder=0></iframe>

A próxima aproximação para a raiz de $P(x) = 0$ é dada pelo valor $x_1$ que correspondente ao ponto em que a reta $r(x)$ se encontra com o eixo horizontal. Então, é necessário encontrar o valor de $\Delta x= x_1 - x_0$. Note que $\frac{P(x_0)}{-\Delta x} = P'(x_0)$ e tem-se:

$$- \Delta x = \frac{P(x_0)}{P'(x_0)} \quad \Rightarrow \quad x_1 = x_0 - \frac{P(x_0)}{P'(x_0)}.$$
Então, pode-se repetir o processo para gerar uma sequência de aproximações $(x_0, x_1, x_2, \ldots)$ para uma raiz da equação $f(x) = 0$, definindo a relação de recorrência a seguir, para uma escolha de $x_0$.

$$x_{k+1} = x_k - \frac{f(x_k)}{f'(x_{k})}, \quad k = 1, 2, \ldots,$$
### Critérios de erro
Algumas medidas de erro que podem ser utilizadas como critério de parada para o Método de Newton.
- $|x_{k+1} - x_k| < \epsilon$. Esse critério pode não ser adequado quando a sequência converge lentamente.
- $\frac{|x_{k+1} - x_k|}{|x_{k+1}|} < \epsilon$. Interessante quando $x_{k+1}$ é muito pequeno (mas não nulo), ou muito grande.
- $|f(x_{k+1})| < \epsilon$. Esse critério pode não ser adequado quando $f(x_k)$ possui valores pequenos.
- $|f(x_{k+1})| + \frac{|x_{k+1} - x_k|}{|x_{k+1}|} < \epsilon$. Compõe dois anteriores, é mais conservador.

## Exemplos
- Utilizando o método de Newton para encontrar um zero da função $f(x) = cos(x) - x$,  com aproximação inicial $x_0 = 0$. 
	- Primeira iteração:
		- $x_0 = 0$.
		- $x_1 = x_0 - f(x_0)/f'(x_0) = 0 - (cos(0) - 0)/(-sin(0) - 1) = 1$.
		- $erro = \frac{|x_1 - x_0|}{|x_1|} = 1.$
	- Segunda iteração:
		- $x_1 = 1$.
		- $x_2 = x_1 - f(x_1)/f'(x_1) = 1 - (-0.4597)/(-1.841) = 0.7503$.
		- $erro = \frac{|0.7503 - 1|}{|0.7503|} = 0.3328$.
	- Terceira iteração:
		- $x_2 = 0.7503$.
		- $x_3 = x_2 - f(x_2)/f'(x_2) = 0.7503 - (-0.01882)/(-1.682) = 0.7391$.
		- $erro = \frac{|0.7391 - 0.7503|}{|0.7391|} = 0.01515$.

- Como um outro exemplo, considere a função $f(x) = x^{\frac{1}{3}}$. A relação de recorrência do método de Newton para essa função é dada por $$x_{k+1} = x_k - \frac{x^{\frac{1}{3}}}{\frac{1}{3}x^{-\frac{2}{3}}} = -2x_k.$$ Portanto, independente de qual aproximação inicial (não nula) for utilizada, a sequência gerada será divergente. Por exemplo, $x_0 = 1$ a sequência gerada seria $(1, -2, 4, -8, 16, -32, \ldots).$  Isso mostra que a sequência gerada pelo método de Newton não possui garantia de convergência. 

- Considere a equação polinomial $x^3 - 2x + 2 = 0$, ao se tentar encontrar uma raiz da equação utilizando o método de Newton, com $x_0 = 0$. Observe o que ocorre.
	- $x_{1} = x_0 - \frac{x_0^3 - 2x_0 + 2}{3x_0^2 - 2} = 0 - \frac{2}{-2} = 1$
	- $x_2 = x_1 - \frac{x_1^3 - 2x_1 +2}{3x_1^2-2} = 1 - \frac{1}{1} = 0$
	- $x_3 = 1, x_4 =0, \ldots,$ sem nunca convergir.
	- graficamente, tem-se o seguinte: <iframe src="https://www.desmos.com/calculator/epndu9typm?embed" width="500" height="500" style="border: 1px solid #ccc" frameborder=0></iframe>
	- Note que esse exemplo é apenas para ilustrar uma situação possível de oscilação entre os valores. Na prática, é possível encontrar uma raiz de polinômios cúbicas utilizando o [método de Cardano-Tartaglia](https://pt.wikipedia.org/wiki/Equa%C3%A7%C3%A3o_c%C3%BAbica). Aliás, a solução de equações cúbicas está relacionada a uma novela matemática e à invenção de números imaginárias ([saiba mais](https://youtu.be/cUzklzVXJwo)).  


Os exemplos anteriores lançam uma dúvida sobre o método. Afinal, o método de Newton é confiável? Será que ele é eficiente comparado ao [[Método da bipartição]] ou o [[Método da falsa-posição]]? Exploraremos tais aspectos a seguir.

## Considerações sobre a convergência

Vimos no exemplo da função $f(x) = x^{\frac{1}{3}}$ que não há garantia de convergência da sequência gerada pelo método de Newton. Outra pergunta importante é: no caso de convergência da sequência, essa convergência é necessariamente para a raiz de $f(x) = 0$?

Supondo que $x_{k},\ k = 0, 1, 2, \ldots$ converge para um valor final $\alpha$, isto é,
$$
     \lim_{k \to \infty} x_{k+1} = \lim_{k \to \infty}x_{k} = \alpha,
$$

 aplicando esses limites na  expressão de recorrência, tem-se:

$$
\lim_{k \to \infty} x_{k+1} = \lim_{k \to \infty} x_{k} - \lim_{k \to \infty}
\frac{f(x_{k})}{f'(x_{k})}, 
$$
$$\lim_{k \to \infty} x_{k+1} = \lim_{k \to \infty} x_{k} -
\frac{\lim_{k \to \infty}f(x_{k})}{\lim_{k \to \infty}f'(x_{k})}$$

Como $f(x)$ e $f'(x)$ são contínuas, tem-se:
$$
\lim_{k \to \infty} f(x_{k}) = f(\lim_{k \to \infty} x_{k}) 
$$
e $$\lim_{k \to \infty} f'(x_{k}) = f'(\lim_{k \to \infty} x_{k})
$$
  Então, 
$$
\lim_{k \to \infty} x_{k+1} = \lim_{k \to \infty} x_{k} - \frac{\displaystyle f(\lim_{k \to
    \infty}x_{k})}{\displaystyle f'(\lim_{k \to \infty} x_{k})}.
$$
Como $\displaystyle \lim_{k \to \infty}x_{k+1} = \lim_{k \to \infty}x_{k} = \alpha$, tem-se:

$$
\alpha = \alpha - \frac{f(\alpha)}{f'(\alpha)}
$$
Portanto, $\frac{f(\alpha)}{f'(\alpha)} = 0$ e $f(\alpha) = 0$, desde que $f'(\alpha) \neq 0$. Logo, $\alpha$ é solução de $f(x) = 0$. 
Assim, se a sequência gerada pela equação de recorrência for convergente, o seu limite sempre será solução de $f(x) = 0$.

## Considerações sobre a convergência

A convergência do método de Newton é quadrática.

## Método de Newton para raízes complexas

Considere o polinômio $P(x) = x^6 + 64$, que possui uma raiz complexa $x = 2i$. Para que o método de Newton consiga gerar uma sequência convergente para a raiz $x = 2i$, é necessário para que a aproximação inicial tenha uma componente imaginária $x_0 = a + bi, b \neq 0$. 

Por exemplo, supondo $x_0 = i$, tem-se:
$$x_1 = x_0 - \frac{x_0^6 + 64}{6x_0^5} = 11.5i,$$
$$x_2 = 9.58339i,$$
$$x_3 = 7.98629i,$$
$$x_4 = 6.5557i,$$
e, assim por diante, até a convergência. Note que se $x_0 = 1+i$, o valor de convergência é $1.7321 - 1.0000i$, que também é uma das raízes de $P(x) = 0$.

A convergência do método de Newton para as raízes de polinômios gera o chamado [Fractal de Newton](https://en.wikipedia.org/wiki/Newton_fractal). 
<a href="https://upload.wikimedia.org/wikipedia/commons/d/db/Julia_set_for_the_rational_function.png"><img alt="File:Julia set for the rational function.png" src="https://upload.wikimedia.org/wikipedia/commons/thumb/d/db/Julia_set_for_the_rational_function.png/800px-Julia_set_for_the_rational_function.png?20111026001115" decoding="async" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/d/db/Julia_set_for_the_rational_function.png/1200px-Julia_set_for_the_rational_function.png?20111026001115 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/d/db/Julia_set_for_the_rational_function.png/1600px-Julia_set_for_the_rational_function.png?20111026001115 2x" data-file-width="2000" data-file-height="1500" width="720" height="540"></a>

# Referências e outros materiais
- Peters, Sérgio, e Julio Felipe Szeremeta. Cálculo numérico computacional (2019).
- Newton's method produces this fractal, why don't we teach it in calculus classes? by 3Blue1Brown. Disponível em: https://youtu.be/-RdOwhmqP5s.
- Newton's method. Disponível em: https://en.wikipedia.org/wiki/Newton's_method