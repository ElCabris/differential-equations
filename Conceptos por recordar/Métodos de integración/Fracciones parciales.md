El método de fracciones parciales se usa para integrar funciones racionales (fracciones donde el numerados y denominador son polinomios). La idea es descomponer una fracción compleja en fracciones más simples que sean fáciles de integrar.

## ¿Cuándo Usar Fracciones Parciales?
Se aplica cuando:
- El grado del numerador es **menor** que el del denominador (si no, primero se divide con el algoritmo de la división).
- El denominador puede **factorizarse** en polinomios más simples (lineales o cuadráticos irreducibles).

## Pasos para Aplicar el Método

### Paso 1: Factorizar el Denominador
Descomponer el denominador $Q(x)$ en factores:
- **Lineales**
- **Cuadráticos irreducibles**
### Paso 2: Forma General de la Descomposición
Dependiendo de los factores del denominador, la descomposición tiene distintas formas:
#### Caso 1: Factores Lineales Distintos
Para cada factor (x - a), se escribe una fracción parcial con constante $A$:
$$
\frac{P(x)}{(x - a)(x - b)} = \frac{A}{x - a} + \frac{B}{x - b}
$$
**Ejemplo:**
$$
\frac{3x + 5}{(x -1)(x + 2)} = \frac{A}{x - 1} + \frac{B}{x + 2}
$$
#### Caso 2: Factores Lineales Repetidos
Si  $(x - a)^{n}$ aparece, se incluyen términos para cada potencia:
$$
\frac{P(x)}{(x - a)^{3}} = \frac{A}{x - a} + \frac{B}{(x - a)^{2}} + \frac{C}{(x - a)^{3}}
$$
**Ejemplo**:
$$
\frac{2x}{(x - 3)^{2}} = \frac{A}{x - 3} + \frac{B}{(x - 3)^{2}}
$$
#### Caso 3: Factores Cuadráticos Irreducibles
Para $(x^{2} + bx + c)$, se usa un numerador lineal $Ax + B$:
$$
\frac{P(x)}{(x^{2} + 1)(x - 2)} = \frac{Ax + B}{x^{2} + 1} + \frac{C}{x - 2}
$$

### Paso 3 Determinar las Constantes ($A, B, C, \cdots$)
Multiplicamos ambos lados por el denominador común y resolvemos el sistema de ecuaciones
**Ejemplo caso 1**
$$
\frac{3x + 5}{(x - 1)(x + 2)} = \frac{A}{x - 1} + \frac{B}{x + 2}
$$
1. Multiplicamos por $(x - 1)(x + 2)$:
$$
3x + 5 = A(x + 2) + B(x - 1)
$$
2. Sustituimos valores estratégicos para $x$.
	1. Si $x = 1: 3(1) + 5 = A(3) \Rightarrow A = \frac{5}{8}$
	2. Si $x = -2: 3(-2) + 5 = B(-3) \Rightarrow B = \frac{1}{3}$
3. Resultado:
$$
\frac{3x + 5}{(x - 1)(x + 2)} = \frac{\frac{8}{3}}{x - 1} + \frac{\frac{1}{3}}{x + 2}
$$
### Integrar cada fracción parcial
Ahora, integramos término a término
$$
\int \frac{3x + 5}{(x - 1)(x +2)}dx
$$
