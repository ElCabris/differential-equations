Resolver la siguiente EDO al rededor de $x = 0$
$$
(1-x^2)y'' - xy' + p^2y =0
$$

donde $p$ es una constante

Estamos frente la ecuación de Chebyshe!!

$$
y'' - \frac{x}{1 - x^2}y' + \frac{p^2}{1 - x^2}y  = 0
$$
$$
P(x)= -\frac{x}{1-x^2}
$$
$$
Q(x) = \frac{p^2}{1-x^2}
$$
evaluando en $x_0 = 0$
$$
P(x_0) = - \frac{0}{1 - 0} = 0
$$
$$
Q(x_0) = \frac{p^2}{1 - 0} = p^2
$$

entonces $P$ y $Q$ son analíticas en $x_0 =0$, se puede utilizar el método de series de potencia.

utilizando el teorema de la existencia, vamos a determinar en que intervalo la serie que vamos a encontrar converge:

primero vamos a encontrar la singularidad más cercana, esto ocurre en:
$$
1 - x^2 = 0
$$
$$
-x^2 = -1
$$
$$
x^2= 1
$$
$$
x = \pm 1 
$$
entonces la serie converge al menos en el intervalo:
$$
|x| < R
$$
y $R$ es la distancia en el plano complejo de $x_0$ a la singularidad más cercana, que es $x = \pm 1$, entonces:
$$
|x| < 1
$$
entonces el intervalo es donde al menos converge la serie es:
$$
(-1, 1)
$$

ahora si, vamos con la solución:
$$
y = \sum_{n = 0}^{\infty} c_nx^n
$$
$$
y' =\sum_{n = 1}^{\infty} nc_nx^{n -1}
$$
$$
y'' = \sum_{n = 2}^{\infty} n(n - 1)c_nx^{n - 2}
$$
reemplazamos en la ecuación:
$$
\sum_{n = 2}^{\infty} n(n - 1)c_nx^{n - 2} - x\sum_{n = 1}^{\infty} nc_nx^{n -1} + p^2  \sum_{n = 0}^{\infty} c_nx^n = 0
$$

$$
\sum_{n = 2}^{\infty} n(n - 1)c_nx^{n - 2} - \sum_{n = 1}^{\infty} nc_nx^{n} + p^2  \sum_{n = 0}^{\infty} c_nx^n = 0
$$

ahora vamos a re-indexar el primer término, sea $k = n - 2$ entonces $n = k + 2$.

$$
\sum_{k =0}^{\infty} (k +2)(k +1)c_{k + 2}x^{k}
$$
volvemos a $n$
$$
\sum_{n =0}^{\infty} (n +2)(n + 1)c_{n + 2}x^{n}
$$
reemplazadon nuevamente en la ecuación:
$$
\sum_{n =0}^{\infty} (n +2)(n + 1)c_{n + 2}x^{n} - \sum_{n = 1}^{\infty} nc_nx^{n} + p^2  \sum_{n = 0}^{\infty} c_nx^n = 0
$$
todas las potencias de $x$ están con el mismo exponente pero falta igualar las sumas, para esto vamos a sacar un término del primer y último término.

para  $n =0$, el primer término queda
$$
(2)(1)c_{2}
$$
para el tercer término:
$$
c_0
$$

entonces queda para  $n = 0$
$$
2c_2 + c_0 = 0
$$
reemplazando en la ecuación:
$$
2c_2\sum_{n =1}^{\infty} (n +2)(n + 1)c_{n + 2}x^{n} - \sum_{n = 1}^{\infty} nc_nx^{n} + p^2  c_0\sum_{n = 1}^{\infty} c_nx^n = 0
$$
$$
\sum_{n = 1}^{\infty}\left[(n+2 )(n+1)c_{n + 2} - nc_n + p^2c_n\right]x^n = 0
$$
$$
\sum_{n = 1}^{\infty}\left[(n+2 )(n+1)c_{n + 2} + (p^2 - n)c_n\right]x^n = 0
$$

las condiciones para que esta suma sea $0$ para todo $x$ en $(-1, 1)$, el coeficiente dentro del corchete debe ser cero para cada $n\ge1$:
$$
(n+2)(n+1)c_{n+2} + (p^2 - n)c_n = 0, n \ge 1
$$

despejamos:
$$
c_{n+2} = - \frac{p^2 - n}{(n+2)(n+1)} 
$$
$$
c_{n+2} = \frac{n - p^2}{(n+2)(n+1)}c_n, n \ge 1
$$
ahora vamos por nuestros coeficientes:

para $n = 1$
$$
c_{3} = \frac{1 - p^2}{3 \times 2}c_{1} = \frac{1-p^2}{6}c_1
$$
para $n=2$
$$
c_4= \frac{1-p^2}{4 \times 3} c_2 = \frac{1 - p^2}{12}c_2
$$
para $n = 3$
$$
c_5 = \frac{1 - p^2}{5 \times 4}c_3 = \frac{1 - p^2}{5 \times 4} \cdot \frac{1 - p^2}{3\times 2}c_1 = \frac{(1 - p^2)^2}{5!}c_1
$$
para $n = 4$
$$
c_6 = \frac{1-p^2}{6 \times 5}c_4 = \frac{1-p^2}{6 \times 5} \cdot \frac{1 - p^2}{4 \times 3}= \frac{(1-p²)^2}{6\times5\times4\times3}c_2
$$