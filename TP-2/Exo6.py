years = int(input("Enter une année "))

if years % 4 == 0 and years % 100 != 0:
    print("L'année est bissextile")
else:
    print("L'année est pas bissextile")
