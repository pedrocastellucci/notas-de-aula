---
title: "Torre de Hanoi"
---

# O problema da Torre de Hanoi

> No grande templo de Benares, abaixo do domo que marca o centro do mundo, repousa uma placa de bronze em que estão fixados três pinos de diamante (...). Em um desses pinos, na criação, Deus colocou 64 discos de puro ouro, o maior disco repousando na placa de bronze, e os seguintes, um menor que o anterior, repousando um em cima do outro. Essa é a Torre de Brama. Dia e noite, sem descanso, monges transferem os discos de diamante de um pino para o outro de acordo com as leis imutáveis de Bramah. Essas leis permitem apenas o movimento de um disco por vez e que este disco só possa ser posto em um pino de forma que não haja disco menor sob ele. Quando os 64 discos tiverem sido transferidos do pino original para um dos demais, torre, templo e o mundo se tornará pó, e, com um trovão, desaparecerá.(Tradução livre de Hinz, Andreas M., et al. The Tower of Hanoi-Myths and Maths. Basel: Birkhäuser, 2013).

![[Pasted image 20220419154457.png|500]]

# Um algoritmo

```python
def hanoi(n, origin, aux, dest):
	if n == 0:
		return
	hanoi(n-1, origin, dest, aux)
	print("Disc %d: Moved from %s to %s" % (n, origin, dest))
	hanoi(n-1, aux, origin, dest)
hanoi(3, 'A', 'B', 'C')
```

### Análise da solução

Quantos movimentos $T(n)$ o algoritmo realiza para $n$ discos?
$$
\begin{align*}
     T(n) &= 2T(n-1) + 1 \\
     &= 4T(n-2) + 3\\
     &= 8T(n-3) + 7\\
     &\ \vdots \\
     &= 2^k T(n-k) + 2^k - 1
\end{align*}
$$

Portanto, o algoritmo realiza $O(2^n)$ operações. Mas e então, quando o mundo irá acabar? Em aproximadamente $2^{64}$ movimentos de discos. Supondo que fosse realizado um movimento por segundo, seriam necessários $18446744073709551616 \approx 1{,}84 \cdot 10^{19}$ segundos. Qual a idade do universo em segundos? #pergunta 

