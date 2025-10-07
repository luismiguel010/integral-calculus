import numpy as np

def punto_medio(f, a, b, n):
  h = (b-a)/n
  x = np.linspace(a, b, n+1)
  c = (x[:-1] + x[1:])/2
  return h * np.sum(f(c))

def trapecio(f, a, b, n):
  h = (b-a)/n
  x = np.linspace(a, b, n+1)
  return (h/2) * (f(a) + 2*np.sum(f(x[1:-1])) + f(b))

def simpson(f, a, b, n):
  if n % 2 == 1 : n += 1
  h = (b-a)/n
  x = np.linspace(a, b, n+1)
  return (h/3) *(f(a) + 4*np.sum(f(x[1:-1:2])) + 2*np.sum(f(x[2:-2:2])) + f(b))


# ejemplo con x^2 en el intervalo [0, 2]
f = lambda x: x**2
resultado = simpson(f, 0, 2, 4)
print(resultado)