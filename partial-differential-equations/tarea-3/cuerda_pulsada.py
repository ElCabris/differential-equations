"""
============================================================
  ECUACION DE ONDA 1D — CUERDA PULSADA EN EL CENTRO
  Solucion por Separacion de Variables y Series de Fourier
============================================================

Problema:
    u_tt = c^2 * u_xx,   0 < x < L,  t > 0

    CF:  u(0,t) = 0,  u(L,t) = 0       (extremos fijos)
    CI1: u(x,0) = f(x)                  (forma triangular)
    CI2: u_t(x,0) = 0                   (velocidad inicial nula)

Solucion analitica:
    u(x,t) = sum_{n=1,3,5,...} B_n * cos(n*pi*c/L * t) * sin(n*pi/L * x)

    Coeficientes:
    B_n = (8h / n^2*pi^2) * sin(n*pi/2)

    - B_n = 0 para n par (simetria del pulso en x=L/2)
    - Decaen como 1/n^2 (convergencia sin fenomeno de Gibbs)
"""

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.gridspec import GridSpec
import time

# ──────────────────────────────────────────────────────────────────────────────
#  SECCION 1: PARAMETROS DEL PROBLEMA
#  Modificar aqui para cambiar cualquier parametro fisico o numerico
# ──────────────────────────────────────────────────────────────────────────────

# Parametros fisicos
L     = 1.0        # Longitud de la cuerda [m]
h     = 0.5        # Altura del pulso triangular [m]
c     = 1.0        # Velocidad de propagacion [m/s]  (c = sqrt(T/rho))

# Parametros numericos
N     = 100        # Numero de terminos en la serie de Fourier
Nx    = 600        # Puntos espaciales de evaluacion
Nt    = 500        # Numero de frames de la animacion
T_max = 2.0*L/c   # Duracion de la animacion [s] = 2 periodos fundamentales

# ──────────────────────────────────────────────────────────────────────────────
#  SECCION 2: GRILLAS DE EVALUACION
# ──────────────────────────────────────────────────────────────────────────────

x     = np.linspace(0, L, Nx)          # Vector espacial: Nx puntos en [0,L]
t_vec = np.linspace(0, T_max, Nt)      # Vector temporal: Nt instantes en [0,T_max]

# ──────────────────────────────────────────────────────────────────────────────
#  SECCION 3: CONDICION INICIAL — FORMA TRIANGULAR
#
#  f(x) = (2h/L)*x          si 0 <= x <= L/2
#  f(x) = (2h/L)*(L-x)      si L/2 < x <= L
#
#  Esta es la cuerda de guitarra pulsada exactamente en el centro.
# ──────────────────────────────────────────────────────────────────────────────

def condicion_inicial(x, L, h):
    """
    Calcula la forma triangular f(x) en todos los puntos del array x.
    np.where aplica la condicion elemento a elemento (vectorizado).
    """
    return np.where(x <= L/2,
                    (2*h/L) * x,           # Rama izquierda: sube hasta L/2
                    (2*h/L) * (L - x))     # Rama derecha: baja desde L/2

# ──────────────────────────────────────────────────────────────────────────────
#  SECCION 4: COEFICIENTES DE FOURIER
#
#  B_n = (8h / n^2*pi^2) * sin(n*pi/2)
#
#  Derivacion:
#  - Se calcula la integral B_n = (2/L) * integral_0^L f(x)*sin(n*pi*x/L) dx
#  - Dividiendo en [0, L/2] y [L/2, L], integrando por partes en cada tramo
#  - El cambio de variable x -> L-x en el segundo tramo muestra que
#    I_2 = (-1)^{n+1} * I_1
#  - Para n par: I_1 + I_2 = 0  =>  B_n = 0
#  - Para n impar: cos(n*pi/2) = 0  =>  B_n = 8h/(n^2*pi^2)*sin(n*pi/2)
# ──────────────────────────────────────────────────────────────────────────────

def coeficiente_Bn(n, h):
    """
    Calcula el coeficiente B_n de la serie de Fourier.
    Para n par: sin(n*pi/2) = 0, por lo que B_n = 0.
    Para n impar: sin(n*pi/2) = +1 o -1 alternadamente.
    """
    return (8.0 * h / (n**2 * np.pi**2)) * np.sin(n * np.pi / 2.0)

# ──────────────────────────────────────────────────────────────────────────────
#  SECCION 5: SOLUCION ANALITICA POR SERIE TRUNCADA
#
#  u_N(x,t) = sum_{n=1}^{N} B_n * cos(n*pi*c/L * t) * sin(n*pi/L * x)
#
#  Implementacion:
#  - Para cada n de 1 a N, se calcula B_n.
#  - Si |B_n| < umbral, se salta el termino (modos pares: B_n = 0 exacto).
#  - Se acumula la contribucion vectorizada sobre todos los puntos x.
# ──────────────────────────────────────────────────────────────────────────────

def solucion_serie(x, t, N, L, h, c):
    """
    Evalua la serie de Fourier truncada a N terminos en un instante t.

    Parametros:
        x     : array de puntos espaciales (shape: Nx)
        t     : instante de tiempo (escalar)
        N     : numero de terminos en la suma
        L, h, c: parametros del problema

    Retorna:
        u     : array de desplazamientos (shape: Nx)
    """
    u = np.zeros_like(x, dtype=float)

    for n in range(1, N + 1):
        Bn = coeficiente_Bn(n, h)

        # Optimizacion: saltamos modos con coeficiente nulo (n par)
        if abs(Bn) < 1e-15:
            continue

        omega_n = n * np.pi * c / L    # Frecuencia angular del modo n
        k_n     = n * np.pi / L        # Numero de onda del modo n

        # Parte temporal: cos(omega_n * t)   [escalar]
        parte_temporal = np.cos(omega_n * t)

        # Parte espacial: sin(k_n * x)       [array de shape Nx]
        parte_espacial = np.sin(k_n * x)

        # Contribucion del modo n
        u += Bn * parte_temporal * parte_espacial

    return u

# ──────────────────────────────────────────────────────────────────────────────
#  SECCION 6: ESTUDIO DE CONVERGENCIA
#
#  Se evalua el error maximo |f(x) - u_N(x,0)| para distintos valores de N.
#  En t=0, cos(omega_n * 0) = 1, entonces u_N(x,0) = sum B_n*sin(n*pi*x/L).
#  El error mide que tan bien la serie reproduce la CI triangular.
# ──────────────────────────────────────────────────────────────────────────────

print("=" * 60)
print("  ESTUDIO DE CONVERGENCIA")
print("=" * 60)
print(f"  L = {L} m,  h = {h} m,  c = {c} m/s")
print("-" * 60)
print(f"  {'N':>6}  |  {'Error L-inf':>14}  |  {'Error relativo':>14}  |  {'Tiempo (ms)':>12}")
print("-" * 60)

f_exacta = condicion_inicial(x, L, h)
N_vals_convergencia = [1, 3, 5, 10, 20, 33, 50, 100, 200]

errores = {}
for N_test in N_vals_convergencia:
    t_inicio = time.time()
    u0 = solucion_serie(x, 0.0, N_test, L, h, c)
    t_fin = time.time()
    error_abs = np.max(np.abs(u0 - f_exacta))
    error_rel = error_abs / h * 100
    tiempo_ms = (t_fin - t_inicio) * 1000
    errores[N_test] = error_abs
    print(f"  {N_test:>6}  |  {error_abs:>14.6f}  |  {error_rel:>13.3f}%  |  {tiempo_ms:>10.2f}")

print("-" * 60)

# Encontrar N optimo automaticamente (error relativo < 1%)
N_optimo = None
for N_test in range(1, 500, 2):    # Solo impares (modos activos)
    u0 = solucion_serie(x, 0.0, N_test, L, h, c)
    er = np.max(np.abs(u0 - f_exacta)) / h * 100
    if er < 1.0:
        N_optimo = N_test
        break
print(f"\n  N optimo para error relativo < 1%:  N = {N_optimo}")
print()

# ──────────────────────────────────────────────────────────────────────────────
#  SECCION 7: FIGURA DE CONVERGENCIA (6 paneles)
#
#  Muestra como mejora la aproximacion de la CI al aumentar N.
#  La linea discontinua negra es la funcion exacta.
# ──────────────────────────────────────────────────────────────────────────────

fig_conv, axes_c = plt.subplots(2, 3, figsize=(15, 8), sharey=True)
fig_conv.suptitle(
    "Convergencia de la serie de Fourier — Cuerda pulsada en el centro",
    fontsize=14, fontweight='bold', color='#1a237e', y=1.01
)

N_paneles = [1, 3, 10, 20, 33, 100]
colores_paneles = ['#e53935', '#f57c00', '#2e7d32', '#1565c0', '#6a1b9a', '#00838f']

for ax, Np, col in zip(axes_c.flat, N_paneles, colores_paneles):
    u0 = solucion_serie(x, 0.0, Np, L, h, c)
    error = np.max(np.abs(u0 - f_exacta))

    ax.plot(x, f_exacta, 'k--', lw=1.8, alpha=0.6, label='Exacta $f(x)$', zorder=3)
    ax.plot(x, u0, color=col, lw=2.2,
            label=f'$u_{{N={Np}}}(x,0)$', zorder=4)
    ax.fill_between(x, f_exacta, u0, alpha=0.15, color='red',
                    label=f'Error = {error:.4f}')

    ax.set_title(f'$N = {Np}$ terminos   (error = {error:.4f})',
                 fontsize=11, color='#1a237e')
    ax.set_xlabel('$x$ [m]', fontsize=10)
    ax.set_ylabel('$u(x, 0)$', fontsize=10)
    ax.set_xlim(0, L)
    ax.set_ylim(-0.05, h * 1.15)
    ax.grid(True, alpha=0.3)
    ax.legend(fontsize=8, loc='upper right')
    ax.set_facecolor('#fafafa')

plt.tight_layout()
plt.savefig('/mnt/user-data/outputs/tarea_convergencia.png',
            dpi=150, bbox_inches='tight')
plt.close()
print("  Figura de convergencia guardada: tarea_convergencia.png")

# ──────────────────────────────────────────────────────────────────────────────
#  SECCION 8: COEFICIENTES B_n
#
#  Muestra la magnitud de los coeficientes para n = 1..50.
#  Los modos pares tienen B_n = 0 exacto.
#  Los modos impares decaen como 1/n^2.
# ──────────────────────────────────────────────────────────────────────────────

n_todos = np.arange(1, 51)
Bn_todos = np.array([coeficiente_Bn(n, h) for n in n_todos])

fig_Bn, (ax1_b, ax2_b) = plt.subplots(1, 2, figsize=(14, 5))
fig_Bn.suptitle(r'Coeficientes de Fourier: $B_n = \frac{8h}{n^2\pi^2}\sin\!\left(\frac{n\pi}{2}\right)$',
                fontsize=13, fontweight='bold', color='#1a237e')

# Panel izquierdo: barras
impares_mask = (n_todos % 2 == 1)
pares_mask   = (n_todos % 2 == 0)

ax1_b.bar(n_todos[impares_mask], Bn_todos[impares_mask],
          color='#1565c0', alpha=0.85, width=0.7,
          label='$n$ impar (activo)')
ax1_b.bar(n_todos[pares_mask], Bn_todos[pares_mask],
          color='#e53935', alpha=0.5, width=0.7,
          label='$n$ par ($B_n = 0$)')
ax1_b.axhline(0, color='gray', lw=0.8)
ax1_b.set_xlabel('$n$', fontsize=12)
ax1_b.set_ylabel('$B_n$', fontsize=12)
ax1_b.set_title('Coeficientes (escala lineal)', fontsize=11)
ax1_b.legend(fontsize=10)
ax1_b.grid(True, alpha=0.3)

# Panel derecho: decaimiento en escala log-log (solo impares)
n_imp = n_todos[impares_mask]
Bn_imp_abs = np.abs(Bn_todos[impares_mask])
referencia = Bn_imp_abs[0] / n_imp**2 * 1**2   # Referencia 1/n^2

ax2_b.loglog(n_imp, Bn_imp_abs, 'o-', color='#1565c0', lw=2,
             ms=6, label='$|B_n|$ calculado')
ax2_b.loglog(n_imp, referencia, 'r--', lw=1.5, label=r'$\propto 1/n^2$')
ax2_b.set_xlabel('$n$ (solo impares)', fontsize=12)
ax2_b.set_ylabel('$|B_n|$', fontsize=12)
ax2_b.set_title('Decaimiento (escala log-log)', fontsize=11)
ax2_b.legend(fontsize=10)
ax2_b.grid(True, which='both', alpha=0.3)

plt.tight_layout()
plt.savefig('/mnt/user-data/outputs/tarea_coeficientes_Bn.png',
            dpi=150, bbox_inches='tight')
plt.close()
print("  Figura de coeficientes guardada: tarea_coeficientes_Bn.png")

# ──────────────────────────────────────────────────────────────────────────────
#  SECCION 9: SNAPSHOTS EN DISTINTOS INSTANTES
#
#  Se muestran 8 perfiles de la cuerda en tiempos distribuidos
#  uniformemente entre 0 y T_max = 2L/c (dos periodos fundamentales).
#
#  Interpretacion:
#  - t=0: forma triangular inicial
#  - t~L/(2c): el pulso se ha dividido en dos que se alejan
#  - t=L/c: primer rebote (los dos pulsos llegan a los extremos)
#  - t=2L/c: la cuerda regresa exactamente a la forma inicial (periodicidad)
# ──────────────────────────────────────────────────────────────────────────────

T_periodo = 2.0 * L / c    # Periodo fundamental de la cuerda

t_snaps = [
    0.0,
    T_periodo / 8,
    T_periodo / 4,
    3 * T_periodo / 8,
    T_periodo / 2,
    5 * T_periodo / 8,
    3 * T_periodo / 4,
    T_periodo
]

fig_snap, axes_s = plt.subplots(2, 4, figsize=(17, 7), sharey=True)
fig_snap.suptitle(
    f'Evolucion temporal de la cuerda pulsada  (N = {N} modos)',
    fontsize=14, fontweight='bold', color='#1a237e'
)

cmap_snap = plt.cm.plasma
colores_s = cmap_snap(np.linspace(0.1, 0.9, len(t_snaps)))

for ax_s, t_s, col_s in zip(axes_s.flat, t_snaps, colores_s):
    u_s = solucion_serie(x, t_s, N, L, h, c)
    ax_s.plot(x, u_s, color=col_s, lw=2.2, zorder=4)
    ax_s.fill_between(x, u_s, 0, alpha=0.2, color=col_s)
    ax_s.plot(x, condicion_inicial(x, L, h), 'k--', lw=0.8,
              alpha=0.3, zorder=2)   # Forma inicial de referencia
    ax_s.axhline(0, color='gray', lw=0.7, ls='--', zorder=1)
    ax_s.axvline(L/2, color='gray', lw=0.5, ls=':', alpha=0.6, zorder=1)
    ax_s.set_title(
        f't = {t_s:.3f} s  ({t_s/T_periodo:.3f} T)',
        fontsize=10, color='#1a237e'
    )
    ax_s.set_xlabel('$x$ [m]', fontsize=9)
    ax_s.set_ylabel('$u(x,t)$', fontsize=9)
    ax_s.set_xlim(0, L)
    ax_s.set_ylim(-h * 1.15, h * 1.15)
    ax_s.grid(True, alpha=0.25)
    ax_s.set_facecolor('#fafafa')

plt.tight_layout()
plt.savefig('/mnt/user-data/outputs/tarea_snapshots.png',
            dpi=150, bbox_inches='tight')
plt.close()
print("  Snapshots guardados: tarea_snapshots.png")

# ──────────────────────────────────────────────────────────────────────────────
#  SECCION 10: MAPA ESPACIO-TIEMPO  u(x, t)
#
#  Imagen 2D donde el eje horizontal es x y el vertical es t.
#  Los patrones diagonales son las ondas viajando a velocidad +c y -c.
#  Se observa la periodicidad temporal: el patron se repite cada T = 2L/c.
# ──────────────────────────────────────────────────────────────────────────────

print("\n  Calculando mapa espacio-tiempo... ", end='', flush=True)
t_mapa = time.time()

U_mat = np.zeros((Nt, Nx))
for i, t_i in enumerate(t_vec):
    U_mat[i, :] = solucion_serie(x, t_i, N, L, h, c)

print(f"listo ({time.time()-t_mapa:.1f} s)")

fig_mapa, ax_m = plt.subplots(figsize=(12, 6))
im = ax_m.pcolormesh(x, t_vec, U_mat,
                      cmap='RdBu_r', shading='auto',
                      vmin=-h, vmax=h)
cbar = fig_mapa.colorbar(im, ax=ax_m, pad=0.02)
cbar.set_label('$u(x, t)$  [m]', fontsize=12)

# Lineas de referencia: frentes de onda desde x=L/2 a t=0
t_plot = np.linspace(0, T_max, 200)
ax_m.plot(L/2 + c*t_plot, t_plot, 'w--', lw=1.2, alpha=0.7,
          label='Frente derecho (+c)')
ax_m.plot(L/2 - c*t_plot, t_plot, 'w:',  lw=1.2, alpha=0.7,
          label='Frente izquierdo (-c)')
ax_m.set_xlim(0, L)
ax_m.set_ylim(0, T_max)
ax_m.set_xlabel('$x$  [m]', fontsize=12)
ax_m.set_ylabel('$t$  [s]', fontsize=12)
ax_m.set_title(
    f'Mapa espacio-tiempo  $u(x,t)$  (N = {N} modos)',
    fontsize=13, fontweight='bold', color='#1a237e'
)
ax_m.legend(fontsize=9, loc='upper right')
plt.tight_layout()
plt.savefig('/mnt/user-data/outputs/tarea_mapa_espacio_tiempo.png',
            dpi=150, bbox_inches='tight')
plt.close()
print("  Mapa espacio-tiempo guardado: tarea_mapa_espacio_tiempo.png")

# ──────────────────────────────────────────────────────────────────────────────
#  SECCION 11: ANIMACION PRINCIPAL
#
#  Muestra la cuerda vibrando en tiempo real.
#  - Linea cyan: perfil actual u(x,t)
#  - Linea discontinua gris: forma inicial de referencia
#  - Punto naranja: posicion del centro x = L/2
#  - El color de la linea cambia segun la amplitud en el centro
#  - Titulo dinamico muestra el tiempo actual
# ──────────────────────────────────────────────────────────────────────────────

print("\n  Generando animacion GIF... ", end='', flush=True)
t_anim_inicio = time.time()

fig_anim, ax_a = plt.subplots(figsize=(12, 5))
fig_anim.patch.set_facecolor('#0d1117')
ax_a.set_facecolor('#0d1117')

# Ejes y etiquetas
ax_a.set_xlim(0, L)
ax_a.set_ylim(-h * 1.2, h * 1.2)
ax_a.set_xlabel('$x$  [m]', color='white', fontsize=13)
ax_a.set_ylabel('$u(x, t)$  [m]', color='white', fontsize=13)
ax_a.tick_params(colors='white', labelsize=10)
for spine in ax_a.spines.values():
    spine.set_edgecolor('#555')

# Lineas de referencia fijas
ax_a.axhline(0,   color='#333', lw=0.8, ls='--', zorder=1)
ax_a.axvline(L/2, color='#333', lw=0.6, ls=':', alpha=0.6, zorder=1)

# Forma inicial en gris translucido (referencia visual)
ax_a.fill_between(x, condicion_inicial(x, L, h), 0,
                  alpha=0.07, color='white', zorder=1)

# Linea animada principal
linea_cuerda, = ax_a.plot([], [], color='#00e5ff', lw=2.5, zorder=5)

# Punto en el centro de la cuerda
punto_centro, = ax_a.plot([], [], 'o', color='#ff6d00',
                           ms=8, zorder=6, label='$x = L/2$')

# Indicador de energia: barra lateral
barra_energia = ax_a.barh(-h*1.1, 0, height=0.05*h,
                            left=0, color='#76ff03', alpha=0.8, zorder=6)

# Texto de informacion fija
info = (f'L = {L} m   |   h = {h} m   |   c = {c} m/s   '
        f'|   N = {N} modos   |   T = {T_periodo:.2f} s')
ax_a.text(L/2, -h*1.13, info, ha='center', va='center',
          color='#aaa', fontsize=8.5, zorder=6)

titulo_anim = ax_a.set_title('', color='white', fontsize=13, pad=12)

def init_anim():
    """Inicializa los objetos animados."""
    linea_cuerda.set_data([], [])
    punto_centro.set_data([], [])
    titulo_anim.set_text('')
    return linea_cuerda, punto_centro, titulo_anim

def actualizar_frame(frame):
    """
    Actualiza la animacion para el frame dado.
    Se llama Nt veces, una por cada instante t = t_vec[frame].
    """
    t_actual = t_vec[frame]

    # Calcular el perfil de la cuerda en este instante
    u_actual = solucion_serie(x, t_actual, N, L, h, c)

    # Actualizar la linea de la cuerda
    linea_cuerda.set_data(x, u_actual)

    # Calcular la posicion del centro
    u_centro = solucion_serie(np.array([L/2]), t_actual, N, L, h, c)[0]
    punto_centro.set_data([L/2], [u_centro])

    # Cambiar color de la linea segun amplitud en el centro
    frac = abs(u_centro) / (h + 1e-10)
    r_col = int(min(frac * 2, 1.0) * 255)
    g_col = int((1 - frac * 0.7) * 229)
    linea_cuerda.set_color(f'#{r_col:02x}{g_col:02x}ff')

    # Actualizar titulo
    titulo_anim.set_text(
        f'Cuerda de guitarra pulsada   '
        f't = {t_actual:.3f} s = {t_actual/T_periodo:.3f} T   '
        f'N = {N} modos'
    )

    return linea_cuerda, punto_centro, titulo_anim

anim = animation.FuncAnimation(
    fig_anim,
    actualizar_frame,
    init_func=init_anim,
    frames=Nt,
    interval=35,      # milisegundos entre frames (~28 fps)
    blit=True
)

# Guardar como GIF animado
escritor_gif = animation.PillowWriter(fps=28)
anim.save('/mnt/user-data/outputs/tarea_animacion.gif',
          writer=escritor_gif, dpi=100)
plt.close()
print(f"listo ({time.time()-t_anim_inicio:.1f} s)")
print("  Animacion guardada: tarea_animacion.gif")

# ──────────────────────────────────────────────────────────────────────────────
#  SECCION 12: RESUMEN FINAL
# ──────────────────────────────────────────────────────────────────────────────

print()
print("=" * 60)
print("  RESUMEN")
print("=" * 60)
print(f"  Parametros fisicos:")
print(f"    L = {L} m,  h = {h} m,  c = {c} m/s")
print(f"    Periodo fundamental T = {T_periodo:.4f} s")
print(f"    Frecuencia fundamental f_1 = {c/(2*L):.4f} Hz")
print()
print(f"  Serie de Fourier:")
print(f"    Solo modos impares contribuyen (B_n=0 para n par)")
print(f"    Coeficientes decaen como 1/n^2")
print(f"    N optimo (error < 1%): N = {N_optimo}")
print(f"    N usado en la animacion: N = {N}")
print()
print(f"  Archivos generados:")
print(f"    - tarea_animacion.gif")
print(f"    - tarea_convergencia.png")
print(f"    - tarea_coeficientes_Bn.png")
print(f"    - tarea_snapshots.png")
print(f"    - tarea_mapa_espacio_tiempo.png")
print("=" * 60)
