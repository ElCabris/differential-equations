# Solución de la EDO mediante el Método de Frobenius

## 1. Análisis de la Ecuación

Dada la ecuación diferencial:

$$4x^2y'' - 8x^2y' + (4x^2 + 1)y = 0$$

La llevamos a su **forma canónica** $y'' + P(x)y' + Q(x)y = 0$ dividiendo entre $4x^2$:

$$y'' - \frac{8x^2}{4x^2}y' + \frac{4x^2 + 1}{4x^2}y = 0$$

$$y'' - 2y' + \left(1 + \frac{1}{4x^2}\right)y = 0$$

### Clasificación del punto singular

Para $x_0 = 0$, observamos que $Q(x)$ no es analítica. Verificamos si es un **punto singular regular**:

- $xP(x) = x(-2) = -2x$
    
- $x^2Q(x) = x^2\left(1 + \frac{1}{4x^2}\right) = x^2 + \frac{1}{4}$
    

Ambas funciones son analíticas en $x = 0$, por lo tanto, $x_0 = 0$ es un punto singular regular y podemos aplicar el **Método de Frobenius**.

---

## 2. Aplicación del Método de Frobenius

Proponemos una solución de la forma:

$$y = \sum_{n =0}^{\infty} a_nx^{n + r}, \quad a_0 \neq 0$$

Sus derivadas son:

$$y' = \sum_{n = 0}^{\infty}a_n(n+r)x^{n+r-1}$$

$$y'' = \sum_{n = 0}^{\infty} a_n(n+r)(n + r - 1)x^{n + r - 2}$$

Sustituimos en la ecuación original $4x^2y'' - 8x^2y' + 4x^2y + y = 0$:

$$4\sum_{n =0}^{\infty} a_n(n+r)(n + r - 1)x^{n + r} - 8\sum_{n = 0}^{\infty}a_n(n+r)x^{n+r+1} + 4 \sum_{n =0}^{\infty} a_nx^{n+r+2} + \sum_{n =0}^{\infty} a_nx^{n + r} = 0$$

---

## 3. Ecuación Indicial

Para obtener la ecuación indicial, tomamos el coeficiente de la potencia más pequeña, que es $x^r$ (ocurre cuando $n=0$ en la primera y cuarta sumatoria):

$$a_0 [4r(r - 1) + 1] = 0$$

Como $a_0 \neq 0$:

$$4r^2 - 4r + 1 = 0 \implies (2r - 1)^2 = 0$$

Esto nos da una **raíz doble**:

$$r_1 = r_2 = \frac{1}{2}$$

---

## 4. Relación de Recurrencia

Sustituyendo $r = 1/2$ en la expresión general y agrupando términos para $x^{n+1/2}$:

1. **Para $n=1$ (término $x^{3/2}$):**
    
    $$a_1[4(1/2+1)(1/2) + 1] - 8(1/2)a_0 = 0 \implies 4a_1 - 4a_0 = 0 \implies a_1 = a_0$$
    
2. **Relación general ($n \ge 2$):**
    
    Igualando los coeficientes de $x^{n+r}$ tras re-indexar:
    
    $$a_n [4(n+r)(n+r-1) + 1] - 8(n+r-1)a_{n-1} + 4a_{n-2} = 0$$
    
    Con $r = 1/2$, el primer corchete simplifica a $4n^2$:
    
    $$4n^2 a_n - 8(n - 1/2) a_{n-1} + 4a_{n-2} = 0$$
    
    Dividiendo por 4:
    
    $$n^2 a_n - (2n - 1) a_{n-1} + a_{n-2} = 0$$
    

---

## 5. Cálculo de Coeficientes y Solución Final

Tomando $a_0 = 1$:

- $a_1 = 1$
    
- Para $n=2$: $4a_2 - 3(1) + 1 = 0 \implies a_2 = 1/2$
    
- Para $n=3$: $9a_3 - 5(1/2) + 1 = 0 \implies 9a_3 = 3/2 \implies a_3 = 1/6$
    

Se identifica el patrón $a_n = \frac{1}{n!}$.

### Primera Solución ($y_1$)

$$y_1(x) = x^{1/2} \sum_{n=0}^{\infty} \frac{x^n}{n!} = \sqrt{x} e^x$$

### Segunda Solución ($y_2$)

Al ser una raíz doble, la segunda solución independiente es de la forma:

$$y_2(x) = y_1(x) \ln(x) + \sum_{n=1}^{\infty} b_n x^{n+1/2}$$

Aplicando reducción de orden, obtenemos:

$$y_2(x) = \sqrt{x} e^x \ln(x)$$

### Solución General

$$y(x) = C_1 \sqrt{x} e^x + C_2 \sqrt{x} e^x \ln(x)$$