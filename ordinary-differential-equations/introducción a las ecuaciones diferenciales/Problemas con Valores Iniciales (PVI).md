Un **problema con valores iniciales (PVI)** es una **ecuación diferencial (EDO)** junto con condiciones adicionales que especifican el valor de la solución (y posiblemente sus derivadas) en un punto dado.

## Estructura general
Para una EDO de **orden $n$** (que incolucra derivadas hasta $y^n$):
EDO
$$
y^{(n)} = f(x, y, y', \cdots , y^{(n-1)})
$$
Condiciones inciales
$$
y(x_0) = y_0, y'(x_0) = y_ 1, \cdots, y^{(n - 1)}(x_0) = y_{n-1}
$$
- $x_0$: Punto donde se especifican las condiciones
- $y_0, y_1, \cdots, y_{n - 1}$

## Objetivo
Encontrar una función $y(x)$ que:
1. Satisfaga la EDO en un intervalo $I$ que contiene a $x_0$.
2. Cumpla con todas las condiciones iniciales dadas.


## Ejemplo clásico: PVI de Primer Orden

**EDO + Condición inicial**
$$
\frac{dy}{dx} = 2x
$$
$$
y(0) = 1$$

**Solución:**
1. Resolver la EDO
$$
\frac{dy}{dx} = 2x \rightarrow y(x) = x^2+ C
$$
2. Aplicar la condición inicial $y(0) = 1$
$$
1 = 0^2 + C \rightarrow C = 1
$$
3. Solución única
$$
y(x) = x^2 + 1
$$