cote_one = int(input("Longueur du premier côtés "))
cote_two = int(input("Longueur du deuxième côtés "))
cote_three = int(input("Longueur du troisième côtés "))

if cote_one > cote_two and cote_one > cote_two:
    cote_big = cote_one
    cote_other_one = cote_two
    cote_other_two = cote_three
elif cote_two > cote_one and cote_two > cote_three:
    cote_big = cote_two
    cote_other_one = cote_one
    cote_other_two = cote_three
elif cote_three > cote_one and cote_three > cote_two:
    cote_big = cote_three
    cote_other_one = cote_one
    cote_other_two = cote_two
else:
    cote_big = 2
    cote_other_one = 1
    cote_other_two = 1
    print("Il ne seras pas rectangle !")

if cote_one == cote_two == cote_three:
    print("Le triangle est équilatéral")
elif cote_one == cote_two or cote_one == cote_three or cote_two == cote_three:
    print("Le triangle est isocèle")
elif cote_other_one ** 2 + cote_other_two ** 2 == cote_big ** 2:
    print("Le triangle est réctangle")
else:
    print("Le triangle est quelconque")

