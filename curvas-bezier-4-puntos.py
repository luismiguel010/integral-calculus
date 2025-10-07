# Curvas de Bézier - 4 puntos de control (Curva Cúbica)

import numpy as np
import matplotlib.pyplot as plt

# Definir puntos de control con coordenadas explícitas
# P0 = (X0, Y0), P1 = (X1, Y1), P2 = (X2, Y2), P3 = (X3, Y3)
X0, Y0 = 0, 3    # Punto inicial
X1, Y1 = 1, 5    # Primer punto de control
X2, Y2 = 3, -1   # Segundo punto de control  
X3, Y3 = 4, 0    # Punto final

# Crear listas para almacenar las coordenadas de la curva
x_curve = []
y_curve = []

# Iterar sobre valores de t desde 0 hasta 1
t_values = np.linspace(0, 1, 100)

for t in t_values:
    # Fórmula de Bézier cúbica:
    # B(t) = (1-t)³P0 + 3(1-t)²tP1 + 3(1-t)t²P2 + t³P3
    
    # Calcular las coordenadas X e Y por separado
    x = (1-t)**3 * X0 + 3 * (1-t)**2 * t * X1 + 3 * (1-t) * t**2 * X2 + t**3 * X3
    y = (1-t)**3 * Y0 + 3 * (1-t)**2 * t * Y1 + 3 * (1-t) * t**2 * Y2 + t**3 * Y3
    
    # Agregar el punto a la curva
    x_curve.append(x)
    y_curve.append(y)

# Convertir a arrays de NumPy para el plotting
x_curve = np.array(x_curve)
y_curve = np.array(y_curve)

# Crear la gráfica
plt.figure(figsize=(10, 6))
plt.plot(x_curve, y_curve, 'b-', linewidth=2, label='Curva de Bézier')
plt.plot([X0, X1, X2, X3], [Y0, Y1, Y2, Y3], 'ro--', linewidth=1, markersize=8, label='Puntos de control')

# Agregar etiquetas a los puntos de control
plt.annotate('P0', (X0, Y0), xytext=(5, 5), textcoords='offset points')
plt.annotate('P1', (X1, Y1), xytext=(5, 5), textcoords='offset points')
plt.annotate('P2', (X2, Y2), xytext=(5, 5), textcoords='offset points')
plt.annotate('P3', (X3, Y3), xytext=(5, 5), textcoords='offset points')

plt.grid(True, alpha=0.3)
plt.legend()
plt.title('Curva de Bézier Cúbica - 4 Puntos de Control')
plt.xlabel('X')
plt.ylabel('Y')
plt.axis('equal')
plt.show()

# Mostrar algunos valores de ejemplo
print("Fórmula de Bézier cúbica:")
print("B(t) = (1-t)³P0 + 3(1-t)²tP1 + 3(1-t)t²P2 + t³P3")
print(f"\nPuntos de control:")
print(f"P0 = ({X0}, {Y0})")
print(f"P1 = ({X1}, {Y1})")
print(f"P2 = ({X2}, {Y2})")
print(f"P3 = ({X3}, {Y3})")
print(f"\nEjemplo: Para t = 0.5")
t_ejemplo = 0.5
x_ejemplo = (1-t_ejemplo)**3 * X0 + 3 * (1-t_ejemplo)**2 * t_ejemplo * X1 + 3 * (1-t_ejemplo) * t_ejemplo**2 * X2 + t_ejemplo**3 * X3
y_ejemplo = (1-t_ejemplo)**3 * Y0 + 3 * (1-t_ejemplo)**2 * t_ejemplo * Y1 + 3 * (1-t_ejemplo) * t_ejemplo**2 * Y2 + t_ejemplo**3 * Y3
print(f"B(0.5) = ({x_ejemplo:.2f}, {y_ejemplo:.2f})")