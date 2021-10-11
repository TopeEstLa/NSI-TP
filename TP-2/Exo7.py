nbr_mask = int(input("Combien de masques souhaiter vous acheter ? "))

price = 0

for i in range(1, nbr_mask+1):
    if i <= 20:
        price = price + 0.20
    elif i <= 30:
        price = price + 0.15
    else:
        price = price + 0.10

print(price)
