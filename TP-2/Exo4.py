nbr = int(input("Enter un nombre entier "))

premier = True

for i in range(2, nbr):
    if nbr % i == 0:
        premier = False

if premier:
    print("Le nombre est premier")
else:
    print("Le nombre n'est pas premier")

