a1 = 1
a2 = 1
n = 10
an = [a1, a2]

for i in range(2, n):
    an.append(an[i - 1] + an[i - 2])
    
print(an)