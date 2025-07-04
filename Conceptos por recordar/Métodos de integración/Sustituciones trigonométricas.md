La **sustitución trigonométrica** es un métod de integración útil para integrales que contienn expresiones con raíces cuadradas de las formas:
- $\sqrt{a^{2} - x^{2}}$
- $\sqrt{a^{2} +  x^{2}}$
- $\sqrt{x^{2} - a^{2}}$
Estas expresiones sugieren una relación con el **Teoremá de Pitágoras**, lo que permite asociarlas a triángulos rectángulos y simplificarlas usando identidades trigonométricas.

## Casos principales y Sustituciones
Cada caso tiene una sustitución especifica basada en identidades trigonométricas

### Caso 1: $\sqrt{a^{2} - x^{2}}$
- **Sustitución:**
$$
x = a \sin{\theta} \Rightarrow dx = a \cos{\theta}d\theta
$$
- **Identidad usada:**
$$
1 - \sin^{2}{x} = \cos^{2}{\theta}
$$
- **Simplificación:**
$$
\sqrt{a^{2} - x^{2}} = \sqrt{a^{2} - a^{2}\sin{\theta}} = a \cos{\theta}
$$
- **Ejemplo:**
$$
\int \frac{dx}{\sqrt{9 - x^{2}}}
$$
### Caso 2: $\sqrt{a^{2} + x^{2}}$
- **Sustitución:**
$$
x = a \tan{\theta} \Rightarrow dx=a \sec^{2}{\theta}d\theta
$$
- **Identidad usada:**
$$
1 + \tan^{2}{\theta} = \sec{\theta}
$$
- **Simplificación:**
$$
\sqrt{a^{2} + x^{2}} = \sqrt{a^{2} + a^{2}\tan{\theta}} = a \sec{\theta}
$$
- **Ejemplo:**
$$
\int \frac{dx}{x^{2}\sqrt{x^{2} + 4}}
$$
### Caso 3: $\sqrt{x^{2} - a^{2}}$
- **Sustitución:**
$$
x = a\sec{\theta} \Rightarrow dx = a\sec{\theta}\tan{\theta}d\theta
$$
- **Identidad usada:**
$$
\sec^{2}{\theta} - 1 = \tan^{2}{\theta}
$$
- **Simplificación:**
$$
\sqrt{x^{2} - a^{2}} = \sqrt{a^{2}\sec^{2}{\theta} - a^{2}} = a\tan{\theta}
$$
