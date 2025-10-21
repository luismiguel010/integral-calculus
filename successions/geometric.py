a1 = 3
r = 2
n = 10
an = []

for i in range(1, n):
    an.append(a1 * r ** (i - 1))
    
print(an)