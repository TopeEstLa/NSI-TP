n = int(input("Entrer un nombre entier : "))

nbr = 0

for i in range(n+1):
    nbr = nbr + i

print(nbr)

print(n*(n+1) // 2)