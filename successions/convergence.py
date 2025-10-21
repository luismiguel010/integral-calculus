import matplotlib.pyplot as plt

n = range(1, 100)
a_n = [(3*i + 1)/(2*i + 4) for i in n]
plt.plot(n, a_n, marker='o')
plt.axhline(y=1.5, color='r', linestyle='--')
plt.title("Convergencia de la sucesión a_n = (3n + 1)/(2n + 4)")
plt.xlabel("n")
plt.ylabel("a_n")
plt.show()