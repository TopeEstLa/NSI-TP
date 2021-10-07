n = int(input("Combien de chiffre voulez vous ? "))

somme = 0

for _ in range(n):
    nombre = int(input("Donner un chiffre "))
    somme = somme * 10 + nombre

print(somme)