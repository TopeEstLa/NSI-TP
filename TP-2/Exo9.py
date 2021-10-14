yA = int(input("y de A "))
xA = int(input("x de A "))

yB = int(input("y de B "))
xB = int(input("x de B "))

yC = int(input("y de C "))
xC = int(input("x de C "))

if xA == xB and xB == xC:
    print("Les trois point sont alignés")
elif xA == xB and xB != xC:
    print("Les trois point ne sont pas alignés")
elif (yC - yB) / (xC - xB) == (yB - yA) / (xB - xA):
    print("Les trois point sont alignés")
else:
    print("Les trois point ne sont pas alignés")