def tutki_huonetta():
    print("\n--- TYÖHUONE ---")
    print("Olet Edvard Kiven työhuoneessa.")
    print("Huoneessa on suuri kirjoituspöytä, kirjahylly ja vanha kello.")
    print("Pöydällä näyttää olevan jotain mielenkiintoista...")

def nayta_inventaario():
    print("\n--- INVENTAARIO ---")

    if len(inventaario) == 0:
        print("Inventaario on tyhjä.")
    else:
        print("Sinulla on:")
        for esine in inventaario:
            print(f"- {esine}")

def nayta_epaillyt():
    print("\n--- EPÄILLYT ---")
    print("1. Elisa Kivi - Edvardin vaimo")
    print("2. James Kivi - Edvardin veli")
    print("3. Sofia Niemi - Edvardin sihteeri")
    print("4. Viktor Salonen - Edvardin liikekumppani")

def lisaa_esine():
    print("\n--- ESINEEN KERÄÄMINEN ---")

    esine = input("Minkä esineen haluat kerätä? ")

    if esine == "":
        print("Et kirjoittanut esineen nimeä.")
    else:
        inventaario.append(esine)
        print(f"{esine} lisättiin inventaarioon.")

def nayta_ohjeet():
    print("\n--- OHJEET ---")
    print("Tutki kartanoa ja etsi vihjeitä.")
    print("Kerää hyödyllisiä esineitä.")
    print("Tutki epäiltyjä ja heidän kertomuksiaan.")
    print("Ratkaise arvoituksia ja selvitä murhaajan henkilöllisyys.")
    print("Lopulta sinun täytyy löytää oven koodi.")

print("================================")
print("       MURHA KARTANOSSA")
print("================================")

nimi = input("Mikä sinun nimesi on? ")

while True:
    try:
        ika = int(input("Kuinka vanha olet? "))
        break
    except ValueError:
        print("Anna ikä numerona.")

if ika < 12:
    print("\nOlet liian nuori pelaamaan tätä peliä.")
    print("Pelin ikäraja on 12 vuotta.")
else:
    print(f"\nTervetuloa, {nimi}!")
    print("Olet saapunut vanhaan Kiven kartanoon.")
    print("Edvard Kivi on kuollut.")
    print("Sinun tehtäväsi on selvittää, mitä tapahtui.")

    inventaario = []

    while True:

        print("\n================================")
        print("          PÄÄVALIKKO")
        print("================================")
        print("1. Tutki huonetta")
        print("2. Kerää esine")
        print("3. Katso inventaario")
        print("4. Tutki epäiltyjä")
        print("5. Ohjeet")
        print("6. Lopeta")
        print("================================")

        komento = input("Valitse toiminto: ")

        if komento == "1":
            tutki_huonetta()

        elif komento == "2":
            lisaa_esine()

        elif komento == "3":
            nayta_inventaario()

        elif komento == "4":
            nayta_epaillyt()

        elif komento == "5":
            nayta_ohjeet()

        elif komento == "6" or komento.lower() == "lopeta":
            print("\nPeli lopetetaan.")
            print(f"Kiitos pelaamisesta, {nimi}!")
            break

        else:
            print("\nTuntematon komento.")
            print("Valitse jokin valikon vaihtoehdoista.")