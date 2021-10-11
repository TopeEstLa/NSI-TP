nbr_one = int(input("Entrer un premier nombre entier "))
nbr_two = int(input("Enter un deuxième nombre entier "))

if nbr_one > nbr_two:
    print("Le premier nombre (", nbr_one, ") est plus grand que le deuxième.")
elif nbr_two > nbr_one:
    print("Le deuxième nombre (", nbr_two, ") est plus grand que le premier.")
else:
    print("les deux nombre sont égaux")
