n = int(input("Combien de chiffre voulez vous ? "))

somme = 0

for i in range(n):
    nombre = int(input("Donner un chiffre "))
    somme = somme + nombre*10**i

print(somme)
