import matplotlib.pyplot as plt
import numpy as np

# Definición del campo direccional: dy/dx = 0.2xy
def f(x, y):
    return 0.2 * x * y

# Crear malla más densa en rango [-5, 5]
x = np.linspace(-5, 5, 30)
y = np.linspace(-5, 5, 30)
X, Y = np.meshgrid(x, y)

# Componentes del campo: dx siempre 1, dy = f(x,y)
U = np.ones_like(X)
V = f(X, Y)

# Normalizar para visualización
norm = np.sqrt(U**2 + V**2)
U /= norm
V /= norm

# Configurar la figura
plt.figure(figsize=(10, 8))
plt.quiver(X, Y, U, V, 
           angles='xy', 
           scale_units='xy', 
           scale=None,  # escala automática
           color='blue', 
           width=0.004, 
           alpha=0.8)

# Solución general: y = C * e^{0.1x^2}
def solucion(x, C):
    return C * np.exp(0.1 * x**2)

# Dibujar curvas solución para diferentes constantes C
x_vals = np.linspace(-5, 5, 400)
C_values = [-5, -2, -1, 0, 1, 2, 5]
for C in C_values:
    y_vals = solucion(x_vals, C)
    plt.plot(x_vals, y_vals, 'r-', linewidth=1.5, label=f'C={C}')

# Estética del gráfico
plt.title(r'Campo Direccional y Curvas Solución para $\frac{dy}{dx} = 0.2xy$', fontsize=16)
plt.xlabel('x', fontsize=14)
plt.ylabel('y', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.4)
plt.axhline(0, color='black', linewidth=0.7)
plt.axvline(0, color='black', linewidth=0.7)
plt.xlim(-5, 5)
plt.ylim(-5, 5)
plt.legend(loc='upper left', fontsize=10)
plt.tight_layout()
plt.show()
