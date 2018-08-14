def dodaj():
    i = input("Wpisz imie: ")
    n = input("Wpisz nazwisko: ")
    g = int(input("Wpisz nr grupy: "))

    plik = open("dane.txt", "a")
    plik.write("%10s,%10s,%10i\n" % (i, n, g))
    plik.close()

def pokaz():
    plik = open("dane.txt", "r")
    for line in plik:
        dane = (line.strip().split(','))  #split czyści białe znaki
        print("%2s %10s %10s" % (dane[0], dane[1], dane[2]))
    plik.close()

def usun():
    nazwisko = input("Wpisz nazwisko do usuniecia: ")
    plik = open("dane.txt", "r")
    zm = ""
    znaleziono = False
    for t in plik:
        dane = (t.split(','))
        if dane[1] != nazwisko:
            zm += t
        else:
            znaleziono = True
    if znaleziono == False:
        print("Nie ma takiego studenta")
    plik.close()
    plik = open("dane.txt", "w")
    plik.write(zm)
    plik.close()

while (True):
    dec = input("d -dodaj, p -pokaz studentow, u -usun, q -zakoncz\nCo chcesz zrobić: ")
    if dec == "d":
        dodaj()
    if dec == "p":
        pokaz()
    if dec == "u":
        usun()
    if dec == "q":
        break
