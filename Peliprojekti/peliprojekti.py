nimi = input("Anna nimi: ")
ika = int(input("Anna ikä: "))
print("\n" + nimi)
print(ika)

if ika <12:
    print("Olet alaikäinen")
else:
    print(f"Tervetuloa {nimi}!")

    while True:
        print("\n" +"Päävalikko")
        print("- Ohje")
        print("- Aloita")
        print("- Liiku")
        print("- Lopeta")

        komento = input ("\nAnna komento:")

        if komento == "Ohje":
            print("Katso ohjeet painamalla i")
        elif komento == "Aloita":
            print("Aloita peli painamalla space")
        elif komento == "Liiku":
            print("Liiku eteenpäin nuolilla")
        elif komento == "Lopeta":
            print("Peli lopetetaan")
            break
        else:
            print("Annoit tuntemattoman komennon")