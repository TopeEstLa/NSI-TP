n = int(input("Entier supérieur à 2 "))

a = 0
b = 1

for _ in range(n-1):
    nbr = a + b
    a = b
    b = nbr

print(nbr)