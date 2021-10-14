nbr = int(input("Enter un nombre "))

acc_one = 0
acc_two = 0

for i in range(1, nbr):
    if nbr % i == 0:
        acc_one = acc_one + i

for i in range(1, acc_one):
    if acc_one % i == 0:
        acc_two = acc_two + i

if nbr == acc_two:
    print("Le nombre amicaux de", nbr, "est:", acc_one)
else:
    print("Le nombre ne posséde pas de nombre amicaux")
