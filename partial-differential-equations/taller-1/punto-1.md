# Solución de la Ecuación Diferencial de Chebyshev

## 1. Planteamiento del Problema

Se busca resolver la siguiente ecuación diferencial ordinaria (EDO) alrededor del punto $x = 0$:

$$(1-x^2)y'' - xy' + p^2y = 0$$

donde $p$ es una constante real. Esta es la conocida **Ecuación de Chebyshev**.

### Análisis de Puntos Singulares

Dividiendo por el término principal $(1-x^2)$, obtenemos la forma estándar:

$$y'' - \frac{x}{1 - x^2}y' + \frac{p^2}{1 - x^2}y = 0$$

Definimos:

- $P(x) = -\frac{x}{1-x^2}$
    
- $Q(x) = \frac{p^2}{1-x^2}$
    

Evaluando en $x_0 = 0$:

- $P(0) = 0$
    
- $Q(0) = p^2$
    

Dado que $P(x)$ y $Q(x)$ son analíticas en $x_0 = 0$, este es un **punto ordinario**, lo que permite utilizar el método de series de potencia.

---

## 2. Intervalo de Convergencia

Las singularidades de la ecuación ocurren cuando el denominador es cero:

$$1 - x^2 = 0 \implies x = \pm 1$$

El radio de convergencia $R$ es la distancia desde $x_0 = 0$ hasta la singularidad más cercana. Por lo tanto, $R = 1$.

La serie converge al menos en el intervalo:

$$|x| < 1 \quad \text{o} \quad x \in (-1, 1)$$

---

## 3. Método de Series de Potencia

Asumimos una solución de la forma:

$$y = \sum_{n = 0}^{\infty} c_n x^n, \quad y' = \sum_{n = 1}^{\infty} n c_n x^{n-1}, \quad y'' = \sum_{n = 2}^{\infty} n(n-1)c_n x^{n-2}$$

Sustituyendo en la EDO original $(1-x^2)y'' - xy' + p^2y = 0$:

$$(1-x^2) \sum_{n=2}^{\infty} n(n-1)c_n x^{n-2} - x \sum_{n=1}^{\infty} n c_n x^{n-1} + p^2 \sum_{n=0}^{\infty} c_n x^n = 0$$

Distribuyendo los términos:

$$\sum_{n=2}^{\infty} n(n-1)c_n x^{n-2} - \sum_{n=2}^{\infty} n(n-1)c_n x^n - \sum_{n=1}^{\infty} n c_n x^n + \sum_{n=0}^{\infty} p^2 c_n x^n = 0$$

### Re-indexación y Agrupación

Para unificar los exponentes a $x^k$, re-indexamos el primer término haciendo $k = n-2 \implies n = k+2$:

$$\sum_{k=0}^{\infty} (k+2)(k+1)c_{k+2}x^k - \sum_{n=2}^{\infty} n(n-1)c_n x^n - \sum_{n=1}^{\infty} n c_n x^n + \sum_{n=0}^{\infty} p^2 c_n x^n = 0$$

Agrupando términos semejantes para una potencia genérica $x^n$:

$$(n+2)(n+1)c_{n+2} - \left[ n(n-1) + n - p^2 \right]c_n = 0$$

Simplificando el corchete: $n^2 - n + n - p^2 = n^2 - p^2$.

### Relación de Recurrencia

Para que la igualdad se cumpla, el coeficiente de cada potencia de $x^n$ debe ser cero:

$$c_{n+2} = \frac{n^2 - p^2}{(n+2)(n+1)}c_n, \quad n \ge 0$$

---

## 4. Obtención de Coeficientes

A partir de la recurrencia, obtenemos los términos para las dos soluciones independientes:

**Para la serie par (depende de $c_0$):**

- $n = 0: \quad c_2 = \frac{0^2 - p^2}{2 \cdot 1} c_0 = -\frac{p^2}{2!} c_0$
    
- $n = 2: \quad c_4 = \frac{2^2 - p^2}{4 \cdot 3} c_2 = \frac{-(p^2)(4 - p^2)}{4!} c_0$
    

**Para la serie impar (depende de $c_1$):**

- $n = 1: \quad c_3 = \frac{1^2 - p^2}{3 \cdot 2} c_1 = -\frac{(p^2 - 1)}{3!} c_1$
    
- $n = 3: \quad c_5 = \frac{3^2 - p^2}{5 \cdot 4} c_3 = \frac{-(p^2-1)(9-p^2)}{5!} c_1$
    

---

## 5. Solución General

La solución se expresa como la combinación lineal de dos funciones:

$$y(x) = C_1 y_1(x) + C_2 y_2(x)$$

Donde:

$$y_1(x) = 1 - \frac{p^2}{2!}x^2 + \frac{p^2(p^2 - 4)}{4!}x^4 - \dots$$

$$y_2(x) = x - \frac{p^2 - 1}{3!}x^3 + \frac{(p^2 - 1)(p^2 - 9)}{5!}x^5 - \dots$$

---

## 6. Polinomios de Chebyshev

Si $p = m$ (siendo $m$ un entero no negativo), una de las series se trunca al llegar al término donde $n^2 - p^2 = 0$, convirtiéndose en un polinomio de grado $m$.

### Ejemplos de Polinomios ($c_0=1, c_1=1$):

1. **Si $p = 0$:** La serie par se detiene en $c_0$.
    
    $$P_0(x) = 1$$
    
2. **Si $p = 1$:** La serie impar se detiene en $c_1 x$.
    
    $$P_1(x) = x$$
    
3. **Si $p = 2$:** $c_2 = \frac{0-4}{2} c_0 = -2c_0$.
    
    $$P_2(x) = 1 - 2x^2$$
    
4. **Si $p = 3$:** $c_3 = \frac{1-9}{6} c_1 = -\frac{4}{3} c_1$.
    
    $$P_3(x) = x - \frac{4}{3}x^3$$