# Curvas de Bezier

import numpy as np
import matplotlib.pyplot as plt

P0, P1, P2, P3 = np.array([0,3]), np.array([1,5]), np.array([3,-1]), np.array([4,0])
t = np.linspace(0,1,100)
B = ((1-t)[:,None])**3 * P0 + 3 * ((1-t)[:,None])**2 * (t[:,None]) * P1 + 3 * ((1-t)[:,None]) * (t[:,None])**2 * P2 + (t[:,None])**3 * P3

plt.plot(B[:,0], B[:,1], 'b-', label='Curva Bézier')
plt.plot(*zip(P0,P1,P2,P3), 'ro--', label='Puntos de control')
plt.legend(); plt.show()