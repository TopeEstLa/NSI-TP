n = int(input("Combien de note souhaiter vous ? "))

note_somme = 0
coef_somme = 0

for _ in range(n):
    note = float(input("Entrer une note (Entre 0 et 20) "))

    while note > 20 or note < 0:
        note = float(input("Entrer une note (Entre 0 et 20) "))

    coef = float(input("Entrer un coef "))

    coef_somme = coef_somme + coef

    note_somme = note_somme + note * coef


moyenne = note_somme / coef_somme

print(moyenne)