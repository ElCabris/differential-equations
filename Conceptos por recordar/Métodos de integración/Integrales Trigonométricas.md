Las integrales trigonométricas involucran combinaciones de funciones como $\sin x$, $\cos x$, $\tan x$, etc. Su resolución depende del tipo de expresión en el integrando.

## Integrales de la forma $\int \sin^{n}{x} \cos^{m}{x}dx$
Dependiendo de los exponentes $n$ y $m$, se aplican distintas estrategias:

### Algún exponente es impar
- **Si $n$ es impar** (potencia impar de $\sin{x}$): Usamos la identidad $\sin^{2}{x} = 1 - \cos^{2}{x}$ y hacemos sustitución $u = \cos x$.
$$
\int \sin^{3}{x}\cos^{2}{x}dx = \int \sin^{2}\cos^{2}\cdot\sin{x}dx = \int (1 - \cos^{2}{x})\cos^{2}{x}\sin{x}dx
$$
Hacemos $u = \cos x$, $du = -\sin{x}dx$:
$$
= - \int (1 - u²)u^{2}du = \int (u^4 - u^2)du = \frac{u^{5}}{5} - \frac{u^{3}}{3} + C
$$
Sustituyendo $u = \cos x$:
$$
= \frac{\cos^{5}{x}}{5} - \frac{\cos^{3}{x}}{3} + C
$$
- Si $m$ es impar (potencia impar de $\cos x$): Usamos $\cos^{2}x = 1 - \sin^{2}{x}$ y sustitución $u = \sin x$.
$$
\int \sin^{2}{x}\cos^{3}{x}dx = \int \sin^{2}{x}(1-\sin^{2}{x})\cos{x}dx
$$
Con $u = \sin{x}$, $du = \cos{x}dx$:
$$
= \int u^{2}(1 - u^2)du = \frac{u^{3}}{3} - \frac{u^{5}}{5} + C = \frac{\sin^{3}{x}}{3} - \frac{\sin^{5}{x}}{5} + C
$$
### Ambos exponentes son pares
Usamos [[Identidades de ángulo doble]] para reducir potencias:
$$
\int \sin^{2}{x}\cos^{2}{x}dx = \int \left(\frac{1 - \cos {2x}}{2}\right)\left(\frac{1 + \cos {2x}}{2}\right)dx = \frac{1}{4}\int (1 - \cos^{2}{2x})dx
$$
Aplicamos nuevamente $\cos^{2}{2x} = \frac{1 + \cos{4x}}{2}$:
$$
= \frac{1}{4}\int \left(1 - \frac{1 + \cos{4x}}{2}\right)dx = \frac{1}{8}\int (1 - \cos {4x})dx = \frac{x}{8} - \frac{\sin{4x}}{32} + C
$$
## Integrales con $\tan x$ y $\sec x$.
### $\int \tan^{n}{x}\sec^{m}{x}dx$
- **Si $m$ es par (potencia par de $\sec x$):** Usamos $\sec^{2}{x} = 1 + \tan^{2}{x}$ y sustitución $u = \tan{x}$.
$$
\int \tan^{2}{x}\sec^{4}{x}dx = \int \tan^{2}{x}(1 + \tan^{2}{x})\sec^{2}xdx
$$
Con $u = \tan{x}$, $du = \sec^{2}{x}dx$:
$$
= \int u^{2}(1 + u^{2})du = \frac{u^{3}}{3}+\frac{u^{5}}{5} + C = \frac{\tan^{3}{x}}{3} + \frac{\tan^{5}{x}}{5} + C
$$
- **Si $n$ es impar (potencia impar de $\tan{x}$)**: Usamos $\tan^{2}{x} = \sec^{2}{x} - 1$ y sustitución $u = \sec{x}$
$$
\int\tan^{3}{x}\sec{x}dx = \int(\sec^{2}{x} - 1)\sec{x}\tan{x}dx
$$
Con $u = \sec{x}$, $du = \sec{x}\tan{x}dx$:
$$
= \int(u^{2}- 1)du = \frac{u^{3}}{3} -u + C = \frac{\sec^{3}{x}}{3} - \sec{x} + C
$$
## Integrales con Productos de Senos y Cosenos
Para integrales del tipo $\int \sin {ax} \cos {bx}dx$, usamos **identidades de productos a sumas:**
$$
\sin{A}\cos{B} = \frac{1}{2}[\sin(A + B) + \sin(A - B)]
$$
$$
\int \sin{3x}\cos{2x}dx
$$
## Integrales Racionales Trigonométricas (Sustitución Universal)
Si el integrando es una función racional de $\sin{x}$ y $\cos{x}$, usamos la **sustitución universal**.
$$
t = \tan{\frac{1}{2}}, \sin{x} = \frac{2t}{1 + t^2}, \cos{x} = \frac{1 - t^2}{1 + t^2}, dx = \frac{2}{1 + t^2}dt
$$
$$
\int \frac{1}{1 + \sin{x}}dx
$$

