## Ecuaciones Diferenciales Lineales
Una ED es lineal si puede escribirse como una combinación lineal de la función incógnita y sus derivadas. Es decir, no hay productos, potencias ni funciones no linales de la variable dependiente o sus derivadas.

### Formula general de una ED lineal de orden $n$.
$$
a_n(x)\frac{d^ny}{dx^n} + a_{n - 1}(x)\frac{d^{n - 1}y}{dx^{n - 1}} + \cdots a_1(x)\frac{dy}{dx} + a_0y = g(x)
$$
#### Caracteristicas
- Cadat término es de primer grado en $y$ y sus derivadas.
- No hay términos como $y^2, \sin{y}, e^y, y \cdot y'$, etc.
- Los coeficientes $a_i(x)$ pueden ser funciones de $x$ (pero no de $y$).

## Ecuaciones diferenciales no lineales
Una ED es **no lineal** si **no cumple** las condiciones de linealidad. Esto ocurre cuando:

- Hay **potencias distintas de 1** en yy o sus derivadas (ej: y2,(y′)3y2,(y′)3).
- Hay **funciones no lineales** aplicadas a yy (ej: sin⁡(y),ey,ln⁡(y)sin(y),ey,ln(y)).
- Hay **productos entre yy y sus derivadas** (ej: y⋅y′y⋅y′).