s = int(input("Qu'elle somme souhaiter vous déposée sur le livret : "))

t = float(input("Qu'elle le taux d'intérêts annuel (en %) : "))

n = int(input("Sur combien d'année voulez vous : "))

for i in range(n+1):
    gain = s*t / 100
    print("vous à gagner", gain, "€ d'intérêts (", i, ")")
    s = s + gain

print("Vous avez maintenant", s, "€ sur votre livret en", n ,"ans")