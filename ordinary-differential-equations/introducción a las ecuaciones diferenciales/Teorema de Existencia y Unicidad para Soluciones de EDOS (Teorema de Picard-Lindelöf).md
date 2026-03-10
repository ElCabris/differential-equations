Este teorema garantiza bajo qué condiciones una ecuación diferencial ordinaria (EDO) con un valor inicial tiene **una y solo una solución**. Es fundamental para asegurar que un problema modelado con EDOs está bien planteado.

## Enunciado del teorema
Considera el **problema de valor inicial (PVI)** de primer orden:
$$
\frac{dy}{dx} = f(x, y)
$$
$$
y(x_0) = y_0
$$
donded $f(x, y)$ está definida en una región rectangular $R$ que contien al punto $(x_0, y_0)$ 

### Condiciones del teorema

#### Continuidad de $f(x, y)$
- $f(x, y)$ debe ser continua en $R$.
- Esto garantiza que almenos existe una solución local.
#### Lipschitz respecto a $y$ (o continuidad de $\frac{\partial f}{\partial y}$)
- $f(x, y)$ debe ser Lipschitz **continua** en $y$ (o, más fácil $\frac{\partial f}{\partial y}$ debe existir y ser continua en $R$).
- Esto garantiza que la solución es **única**.
Si ambas condiciones se cumplen, entonces:
Existe una solución çunica $y(x)$ definida en algún intevervao $|x - x_0| < h$ (donde $h >0$)