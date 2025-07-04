Ejemplo con
$$
\frac{dy}{dx} = y^{2} - 4
$$
## Paso 1: Resolver EDO por Separación de variables
La ecuación diferencial ordinaria (EDO) dada es:
$$
\frac{dy}{dx} = y^{2} - 4
$$
**Método separación de variables**
1. Separamos $y$ y $x$.
$$
\frac{dy}{y^{2} - 4} = dx
$$
2. Integramos ambos lados:
$$
\int \frac{dy}{y^{2} - 4} = \int dx
$$
La integral del lado izquierdo se resuelve por [[Fracciones parciales]]
$$
\frac{1}{y^{2} - 4} = \frac{\frac{1}{4}}{y - 2} - \frac{\frac{1}{4}}{y + 2}
$$
Por lo tanto:
$$
\frac{1}{4}\ln|y - 2| - \frac{1}{4}\ln|y + 2| = x + C
$$
3. Simplificamos la expresión:
$$
\ln\left|\frac{y - 2}{y + 2}\right| = 4x + C_1 (\text{donde }C_ 1 = 4C)
$$
Aplicamos potencias a ambos lados:
$$
\left|\frac{y - 2}{y + 2}\right| = e^{4x + C_1} = C_2e^{4x} (\text{con }C_2 = e^{C_1} > 0)
$$
Eliminamos el valor absoluto (notando que $C_2$ puede absorber el signo $\pm$ ):
$$
\frac{y - 2}{y + 2} = C_3 e^{4x} (\text{donde }C_3 \neq 0)
$$
4. Despejamos $y$:
$$
y - 2 = C_3e^{4x}(y + 2)
$$
$$
y - C_3e^{4x}y = 2C_3e^{4x} + 2
$$
$$
y(1 - C_3e^{4x}) = 2(C_3e^{4x} + 1)
$$
$$
y = \frac{2(C_3e^{4x}+ 1)}{1 - C_3e^{4x}}
$$
Podemos redefinir $C = -C_3$ para simplificar:
$$
y = \frac{2(-Ce^{4x} + 1)}{1 + Ce^{4x}} = \frac{2(1-Ce^{4x})}{1 + Ce^{4x}}
$$
**Solución general explícita:**
$$
y(x) = \frac{2 - 2Ce^{4x}}{1 + Ce^{4x}}
$$
## Paso 2: Identificar la Solución Perdida
Durante el proceso de separación de variables, **Dividimos ambos lados por $y^{2} - 4$**, lo que implica que $y^{2} - 4 \neq 0$.
Pero $y^{2} - 4 = 0$ tiene soluciones constantes.
$$
y = 2, y = -2
$$

**Verificación:**
$$
\frac{d}{dy}\left(\frac{2 - 2Ce^{4x}}{1 + Ce^{4x}}\right) = 
$$
- Si $y = 2$:
$$
\frac{dy}{dx} = 0 = (2)^{2} - 4 = 0 (\text{es solución})
$$
- Si  $y = -2$
$$
\frac{dy}{dx} = 0 = (-2)^{2} - 4 = 0 (\text{es solución})
$$
