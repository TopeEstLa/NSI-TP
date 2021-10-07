n = int(input("Entrer un nombre entier : "))

k = int(input("Entrer un nombre de chiffre : "))

for _ in range(k):
    nombre = n % 10
    n = n // 10
    print(nombre)