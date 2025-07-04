 Una de las caracterísitcas más importntes y distintivas de las [[ED Autónomas de primer orden]] es su **invariancia respecto a traslaciones horizontales**. Esta propiedad, conocida como la propiedad de traslación, simplifica notablemente el análisis de sus soluciones.

## Enunciado de la propiedad de traslación
Si $y(x)$ es una solución de una ecuación diferencial autónoma, entonces la función trasladada horizontalmente
$$
y_h(x) = y(x + h)
$$
también es solución de la misma ecuación, para cualquier constante $h \in \mathbb{R}$ 

## Demostración
Supongamos que $y(x)$ satisface:
$$
\frac{dy}{dx} = f(y)
$$
Definimos una nueva función $y_h = y(x + h)$. Entonces, su derivada es:
$$
\frac{dy_h}{dx} = \frac{d}{dx}\left[y(x + h)\right] = \frac{dy}{dx} (x + h)
$$
Como $y(x)$ satisface la ecuación $dy/dx = f(y)$ , entonces:
$$
\frac{dy}{dx}(x + h) = f(y(x+ h)) = f(y_h)
$$
Por lo tanto:
$$
\frac{dy_h}{dx} = f(y_h)
$$
Es decir, **la función trasladada $y_h(x)$ también es solución**.