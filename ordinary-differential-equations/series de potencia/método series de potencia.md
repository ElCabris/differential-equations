Este método se utiliza para resolver ecuaciones diferenciales ordinarias, especialmente cuando las soluciones no se pueden expresar con funciones elementales.

## Condiciones para aplicar el método
No todas las ecuaciones diferrenciales pueden resolverse con cualquier serie de potencia. La clave está en el punto alrededor del cual desarrollamos la solución.

- **Punto ordinario**: Un punto $x_0$ se llama **ordinario** si las funciones que multiplican a $y$, $y'$, $y''$ en una ecuación diferencial lineal de segundo orden (de la forma $P(x)y'' + Q(x)y' + R(x)y = 0$) son analíticas en  $x_0$. Esto signfica que pueden representarse como una seire e potencia alrededor de $x_0$. Si el punto no es ordinario, se llama **singular**.
- **Aplicabilidad**: Si el punto de expansión $x_0$ es un punto ordinario. Si lo es, podemos garantizar la existencia de una solución en forma de serie de potencias.
- **Forma de la Serie**: Asumimos que la solución $y(x)$ se puede escribir como una serie de potencia centrada en el punto ordinario $x_0$
$$ 
y(x) = \sum_{n = 0}^{\infty} c_n(x-x_0)^n
$$

Aquí, $c_n$ con los coeficientes que debemos determinar.


## Paso a paso para aplicar el método
Una vez que has verificado que trabajas alrededor de un punto ordinario, sigue estos pasos. El ejempló se hará resolviendo la ecuación $y' = y$.

### Asumir una solución en forma de serie de potencias
Supón que la solución tiene la forma de una serie centrada en el punto ordinario. Si el problema no especifica el punto, generalente se toma $x_0 = 0$ por simplicidad.
$$
y' = y
$$
$$
y' - y = 0
$$
$$
y = \sum_{ n =0}^{\infty} c_nx^n = c_0 + c_1x + c_2x^2 + c_3x^3 + \cdots
$$

### Derivar series término a término
Calcula las derivasdas necesarias de $y$. Es crucial ajustar correctamente el índice de la sumatoria para que la serie comience con un término no nulo.
$$
y' =  \sum_{n = 1}^{\infty} nc_nx^{n - 1}  = c_1 + 2c_2x +3xc_3x^2 + \cdots
$$
Sustituir las series en la ecuación diferencial
$$
\sum_{n = 1}^{\infty} nc_nx^{n -1} - \sum_{n = 0}^{\infty} c_nx^n = 0 = 0  = 0  = 0 
$$

### Re-indexar las sumas para igualar las potencias
Par poder combinar sumatorias en una sola, necesitamos que todas tengan la mis apotencia de $x$ y que sis índice comienecn en el mismo número. Esto se logar modificando los índices de la sumatorias.

para el primer término hacemos:
$$
k = n - 1
$$
$$
n = k + 1
$$
$$
\sum_{n = 1}^{\infty} nc_nx^{n-1} = \sum_{k = 0}^{\infty} (k+1)c_{k + 1}x^{k}
$$
como $k$ es un índice mudo, lo podemos renombrar como $n$ nuevamente
$$
\sum_{n = 0}(n + 1)c_{n + 1}x^n - \sum_{n = 0}^{\infty} c_nx^n = 0
$$
### Combinar las series y plantear la relación de recurrencia
Combinamos la series en una sola:
$$
\sum_{n = 0}^{\infty} [(n + 1)c_{n + 1} - c_n]x^n  =  0
$$
Esto nos lleva a la relación de recurrencia, que es la fórmula que relaciona una coeficiente con los anteriores:
$$
(n+1)c_{n+1} - c_n
$$
$$
c_{n+1} = \frac{c_n}{n + 1}
$$
### Calcular los coeficientes usando la relación de recurrencia
La relación de recurrencia nos permite expresar todos los coeficientes en función de los primeros.

- Aplicamos la relación para los primeros valores en $n$:
	- Para $n = 0$:  $c_1 = \frac{c_0}{1}  = c_0$ 
	- Para $n  = 1: $c_2 = \frac{c_1}{2} = \frac{c_0}{2}$
	- Para $n=2$: $c_3 = \frac{c_2}{3} = \frac{c_0}{2 \cdot 3} = \frac{c_0}{3!}$
	- Para $n=3$: $c_4 = \frac{c_3}{4} = \frac{c_0}{4 \cdot 3!} = \frac{c_0}{4!}$
- Observamos el patrón claro $c_n = \frac{c_0}{n!}$.
### Escribir la solución final
Susituimos los coeficientse encontrados de vuelta en al serie original para obtener la solución.
- La solución para nuestro ejemplo es:
$$
y = \sum_{n =0}^{\infty} c_nx^n = \sum_{n = 0}^{\infty} \frac{c_0}{n!}x^n = c_0\sum_{n = 0}^{\infty} \frac{x^n}{n!}
$$
dado que
$$
\sum_{n =0}^{\infty} \frac{x^n}{n!} = e^x \rightarrow y = c_0e^x
$$