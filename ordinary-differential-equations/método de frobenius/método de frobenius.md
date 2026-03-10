el método de frobenius es una técnica para resolver ecuaciones diferenciales lineales de segundo orden cerca de un punto donde el método de series de potencias ordinarias  no funciona, pero aún existe cierto tipo de regularidad

Se usa para ecuaciones de la forma:
$$
y'' + P(x)y'+ Q(x)y = 0
$$

## Cuándo se usa el método de Frobenius?
Primero se analiza el punto $x_0$ 

### Punto ordinario
Si $P(x)$ y $Q(x)$ son analíticas en $x_0$.
Entoncers se usa serie de potneicas normal:
$$
y = \sum_{n = 0}^{\infty} a_n(x - x_ 0)^n
$$

y NO hace falta frobenius

### Punto singular
Si $P(x)$ o $Q(x)$ no son analiticas en $x_0$
Pero puede ser de dos tipos:

#### Punto singular regular (aquí se usa Frobenius)
Si cumple que:
$$
(x - x_0)P(x)
$$
y
$$
(x-x_0)^2Q(x)
$$
son analíticas en $x_0$.

Si esto ocurre, se puede aplicar frobenius

#### Punto singular irregular
Si las condiciones anteriores no se cumplen, el método no sirve.

## Idea del método de Frobenius
En vez de asumir una serie normal, se propone una solución más general:
$$
y = \sum_{n = 0}^{\infty} a_n(x - x_0)^{n + r}
$$

donde:
- $r$ no se conoce
- debe determinarse
Esta potencia extra permite manejar singularidades

---
## Pasos del método de Frobenius

### Suponer la solución
$$
y = \sum_{n = 0}^{\infty} a_nx^{n + r}
$$

(si el punto es $x_0 = 0$).

### Derivar
Primera derivada:
$$ 
y' = \sum_{n = 0}^{\infty} a_n (n + r)x^{n + r - 1}
$$
Segunda derivada:
$$
y'' = \sum_{n =0}^{\infty} a_n(n + r)(n+r-1)x^{n + r -2}
$$
### Sustituimos en la ecuación diferencial
Se reemplaza $y, y', y''$.

Eso produce una serie infinita.

### Igualar potencias 
Se reorganizan todas las sumas para que queden en potencias de $x^{n + r}$

#### Ecuación indicial
El término de menor potencia produce una ecuación para $r$
$$
f(r) =0
$$
Esta es la ecuación indicial.
Sus soluciones son:
$$
r_1,r_2
$$

---
### Encontrar recurrencia
Para $n\geq 1$ se obtiene una relación:
$$
a_n = f(a_{n-1}, a_{n-2}, \cdots)
$$
que permite calcular todos los coeficientes

---
### Qué pasa con las raíces de la ecuación indicial
Depende de $r_1$ y $r_2$

### Raíces distintas y no difieren en entero
$$
r_1 - r_2 \notin \mathbb{Z}
$$
Se obtienen dos soluciones independientes.
### Raíces distintas que difieren en entero
Puede aparecen un **logaritmo** en la segunda solución

### Raíces iguales
La segunda solución tiene forma
$$
y_2 = y_2\ln{x} + \text{serie}
$$

