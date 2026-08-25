import random
tahkot = int(input("Anna tahkot: "))

def noppa(tahkot):
    luku = random.randint(1, tahkot)
    return luku

while True:
    silmaluku = noppa(tahkot)
    print(silmaluku)

    if silmaluku == tahkot:
        break