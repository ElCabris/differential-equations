Antes de siquiera empezar a calcular la convergencia del resultado de una serie de pontencia, un teorema fundamental nos da una garantía sobre la convergencia:

> **Teorema**: Si $x_0$ es un **punto ordinario** de la ecuación diferencial $P(x)y'' + Q(x)y' + R(x)y = 0$, entonces la solución en serie de potencias $y = \sum_{n = 0}^{\infty} c_n(x-x_0)^{n}$ existe y es **única**. Ademas, la serie converge al menos en un intervalo $|x-x_0| < R$, donde  $R$ es la distancia de $x_0$ hasta la singularidad (punto no ordinario) más cercana en el plano complejo.


## Ejemplo conceptual
Imagina la ecuación $(x^2 + 1)y'' + xy' + y = 0$, y queremos una solución al rededor de $x_0 = 0$.

1. Escribimos la ecuación en su forma estándar:
$$
y'' + \frac{x}{x^2+1}y' + \frac{1}{x^2+ 1}y = 0
$$
2. Los puntos singulares son donde los denominadores se hacen 0, es decir:
$$
x^2 + 1 = 0
$$
$$
x^2 = -1
$$
$$
x = \pm i
$$
3. En el plano complejo, la distancia desde $x_0$ hasta $x = i$ (o $x = -i$) es $1$.
4. Por lo tanto, el teorema nos garantiza que la serie que encontremos convergerá para $|x-0| < 1$, es decir $(-1, 1)$

