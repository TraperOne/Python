ksiazka = []

while (True):
    print("d - Dodaj", "p - Pokaz", "q - Wyjscie")
    dec = input("Podaj co robimy? ")
    if dec == "d":
        i = input("Wpisz imie: ")
        n = input("Wpisz nazwisko: ")
        t = input("Wpisz telefon: ")
        ksiazka.append([i, n, t])
    if dec == "p":
        for xxx in ksiazka:
            print("%5s%12s%12s" % (xxx[0], xxx[1], xxx[2]))
    if dec == "q":
        break
