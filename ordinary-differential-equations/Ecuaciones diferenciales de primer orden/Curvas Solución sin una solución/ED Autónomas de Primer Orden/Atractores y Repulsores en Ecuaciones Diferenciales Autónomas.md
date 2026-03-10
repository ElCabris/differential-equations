En el análisis cualitativo de [[ED Autónomas de primer orden]], los puntos críticos juegan un papel central. Estos puntos dividen el eje $y$ en regiones y determinan la dirección del cambio de las soluciones. Sin embargo, no todos los puntos críticos se comportan igual. Algunos **atraen** soluciones cercanas; otros, por el contrario, las **repelen**.
Esto nos lleva a los conceptos de **atractor** y **repulsor**.

## Puntos de equilibrio
Recordemos que en una ecuación diferencial autónoma de primer orden
$$
\frac{dy}{dx} = f(y)
$$
un **punto crítico** es un valor $y = y_c$ tal que:
$$
f(y_c) = 0
$$
En dicho punto, la solución $y(x) = y_c$ es constante, pues $dy/dx = 0$. Esto define una **solución de equilibrio**. La naturaleza de este equilibrio puede clasificarse analizando cómo se comportan las soluciones cercanas.

## Atractor
Un punto crítico $y = y_c$ es un **atractor** (también llamado **equilibrio estable**) si:
- Las soluciones que **comienzan cerca** de $y_c$ tienden a acercarse a $y_c$ cuando $x \rightarrow \infty$.
Geométricamente, esto ocurre si:
- $f(y) > 0$ cuando $y < y_c$, y
- $f(y) < 0$ cuando $y > y_c$
Esto significa que:
- Desde la izquierda, las soluciones **suben hacia** $y_c$.
- Desde la derecha, **bajan hacia** $y_c$.
La dirección de las flechas en el diagrama de fases **converge hacia el punto crítico**.

## Repulsor
Un punto crítico $y = y_c$ es un **repulsor** (o equilibrio inestable) si:
- Las soluciones que comienzan cerca de $y_c$ **se alejan** de él cuando $x \rightarrow \infty$.
Esto ocurre si:
- $f(y) < 0$ cuando $y < y_c$, y
- $f(y) > 0$ cuando $y > y_c$
Aquí las soluciones bajan desde la izquierda y suben desde la derecha, alejándose del punto crítico.
Las flechas del diagrama de fases divergen desde el punto.


## Equilibrio semiestable
Existe una tercer posibilidad: un **punto semiestable**.
Este es un equilibrio donde las soluciones se acercan por un lado y se alejan por el otro:
- Por ejemplo: $f(y) > 0$ a un lado, $f(y) = 0$ en el punto, y $f(y) > 0$ 0 o $f(y) < 0$ del toro lado.
En este caso, una solución puede tender hacia el punto si parte de un lado, pero alejarse si parte del otro.
