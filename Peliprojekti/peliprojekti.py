esine_lista = []
rahat = 100

def ohje():
    print("Katso ohjeet painamalla i")

def liiku():
    print("Liiku eteenpäin nuolilla")

def lisaa_esine():
    esine = input("Minkä esineen haluat lisätä? ")
    esine_lista.append(esine)
    print(f"{esine} lisättiin esineisiin.")

def inventaario():
    print("Esineet:")
    for esine in esine_lista:
        print("-", esine)

def tilastot():
    print("Pelaajan tilastot:")
    print(f"Nimi: {nimi}")
    print(f"Ikä: {ika}")
    print(f"Esineitä: {len(esine_lista)}")
    print("Esineet:")

    for esine in esine_lista:
        print("-", esine)

    print(f"Rahatilanne: {rahat} euroa")

def rahatilanne():
    print(f"Sinulla on {rahat} euroa.")

nimi = input("Anna nimi: ").capitalize()
ika = int(input("Anna ikä: "))

print("\n" + nimi)
print(ika)

if ika < 12:
    print("Olet alaikäinen")
else:
    print(f"Tervetuloa {nimi}!")

    while True:
        print("\nPäävalikko")
        print("- Ohje")
        print("- Liiku")
        print("- Esine")
        print("- Inventaario")
        print("- Tilastot")
        print("- Rahatilanne")
        print("- Lopeta")

        komento = input("\nAnna komento: ").lower()

        if komento == "ohje":
            ohje()
        elif komento == "liiku":
            liiku()
        elif komento == "esine":
            lisaa_esine()
        elif komento == "inventaario":
            inventaario()
        elif komento == "tilastot":
            tilastot()
        elif komento == "rahatilanne":
            rahatilanne()
        elif komento == "lopeta":
            print("Peli lopetetaan")
            break
        else:
            print("Annoit tuntemattoman komennon")