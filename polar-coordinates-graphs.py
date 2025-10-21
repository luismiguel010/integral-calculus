import numpy as np
import matplotlib.pyplot as plt

a = 2
theta = np.linspace(0, 2*np.pi, 4000)
r = 2*a*np.cos(theta)           # centro (a,0), radio a

ax = plt.subplot(111, projection='polar')
ax.plot(theta, r)
ax.set_title(rf"Círculo: $r = 2a\cos\theta$, a={a}")
plt.show()