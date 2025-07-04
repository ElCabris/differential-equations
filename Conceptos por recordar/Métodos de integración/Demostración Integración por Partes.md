La fórmula de **integración por partes** surge directamente de la **regla del producto para derivadas**.

## Partir de la Regla del Producto
Sabemos que la derivada del producto de dos funciones $u(x) y v(x)$ es:
$$
\frac{d}{dx}[u(x)\cdot v(x)] = u'(x) \cdot v(x) + u(x) \cdot v'(x)
$$
## Integrar a Ambos lados
Si integramos ambos lados de la ecuación con respecto a $x$, obtenemos:
$$
\int \frac{d}{dx}[u(x)v(x)]dx = \int u'(x)v(x)dx + \int u(x)v'(x)dx
$$
- La integral de la derivada de $u(x)v(x)$ es simplemente $u(x)v(x)$ (por el Teorema Fundamental del Cálculo):
$$
u(x)v(x) = \int v(x)u'(x)dx + \int u(x)v'(x)dx
$$
## Reordenar los términos
Despejamos una de las integrales para obtener la fórmula de integración por partes:
$$
\int u(x)v'(x)dx = u(x)v(x) - \int v(x)u'(x)dx
$$

## Notación diferencial
Si hacemos:
- $u = u(x)$ (función a derivar)
- $dv = v'(x)dx$ (función a integrar)
entonces:
- $du = u'(x)dx$
- $v = \int dv$ (integral de $dv$)
Sustituyendo en la ecuación anterior, obtenemos la **fórmula clásica**:
$$
\int udv = uv - \int vdu
$$
