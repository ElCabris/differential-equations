Las ecuaciones separables constituyen una de las clases más importantes y accesobles de ecuaciones diferenciales ordinarias de primer orden. Su nombre proviene del hecho de que se pueden reescribir separando las variables $x$ y $y$ en lados distintos de la ecuación, permitiendo así su integración directa.

## Definición
Una ecuación diferencial de primer orden se dice que **separable** si pueden expresarse de la forma:
$$
\frac{dy}{dx} = g(x)h(y)
$$
O, equivalentemente, puede escribirse como:
$$
\frac{1}{h(y)}dy = g(x)dx
$$
Es decir, se pueden separa las variables $x$ y $y$ en lados distintos de la ecuación.

## Método de resolución
Dada una ecuación separable:
$$
\frac{dy}{dx} = g(x)h(x)
$$
El procedimiento general consiste en los siguientes pasos:
### Paso 1: Separar las variables
$$
\frac{1}{h(y)}dy = g(x)dx
$$
### Paso 2: Integrar ambos lados
$$
\int \frac{1}{h(y)}dy = \int g(x)dx
$$
### Paso 3: Resolver la ecuación resultante (explícita o implícita)
Después de integrar, se obtiene una relación entre $x$ y $y$, ya sea de forma explícita ($y = y(x))$ o implícita.

## Ejemplo
Resuelva
$$
(1+x)dy -ydx = 0
$$
Dividir entre $(1 + x)y$, podemos escribir
$$
\frac{dy}{y} = \frac{dx}{1 + x}
$$
de donde tenemos que
$$
\int \frac{dy}{y} = \int \frac{dx}{1 + x}
$$
$$
\ln|y| = \ln|1 + x| + c_1
$$
$$ 
y = e^{\ln{|1+ x | + c_1}} = e^{\ln{|1+x}}\cdot e^{c_1}
$$
$$
= |1+x|e^{c_1} 
$$
$$
= \pm e^{c_1}(1 + x)
$$

