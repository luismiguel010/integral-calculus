# Curvas de Bézier - 2 puntos de control (Curva Lineal)

import numpy as np
import matplotlib.pyplot as plt

# Definir puntos de control con coordenadas explícitas
# P0 = (X0, Y0), P1 = (X1, Y1)
X0, Y0 = 2, 2    # Punto inicial
X1, Y1 = 4, 4    # Punto final

# Crear listas para almacenar las coordenadas de la curva
x_curve = []
y_curve = []

# Iterar sobre valores de t desde 0 hasta 1
t_values = np.linspace(0, 1, 100)

for t in t_values:
    # Fórmula de Bézier lineal:
    # B(t) = (1-t)P0 + tP1
    
    # Calcular las coordenadas X e Y por separado
    x = (1-t) * X0 + t * X1
    y = (1-t) * Y0 + t * Y1
    
    # Agregar el punto a la curva
    x_curve.append(x)
    y_curve.append(y)

# Convertir a arrays de NumPy para el plotting
x_curve = np.array(x_curve)
y_curve = np.array(y_curve)

# Crear la gráfica
plt.figure(figsize=(10, 6))
plt.plot(x_curve, y_curve, 'b-', linewidth=2, label='Curva de Bézier Lineal')
plt.plot([X0, X1], [Y0, Y1], 'ro--', linewidth=1, markersize=8, label='Puntos de control')

# Agregar etiquetas a los puntos de control
plt.annotate('P0', (X0, Y0), xytext=(5, 5), textcoords='offset points')
plt.annotate('P1', (X1, Y1), xytext=(5, 5), textcoords='offset points')

plt.grid(True, alpha=0.3)
plt.legend()
plt.title('Curva de Bézier Lineal - 2 Puntos de Control')
plt.xlabel('X')
plt.ylabel('Y')
plt.axis('equal')
plt.show()

# Mostrar algunos valores de ejemplo
print("Fórmula de Bézier lineal:")
print("B(t) = (1-t)P0 + tP1")
print(f"\nPuntos de control:")
print(f"P0 = ({X0}, {Y0})")
print(f"P1 = ({X1}, {Y1})")
print(f"\nEjemplo: Para t = 0.5")
t_ejemplo = 0.5
x_ejemplo = (1-t_ejemplo) * X0 + t_ejemplo * X1
y_ejemplo = (1-t_ejemplo) * Y0 + t_ejemplo * Y1
print(f"B(0.5) = ({x_ejemplo:.2f}, {y_ejemplo:.2f})")
print(f"\nNota: Con 2 puntos de control, la curva de Bézier es simplemente una línea recta")
print(f"que va desde P0 hasta P1.")
