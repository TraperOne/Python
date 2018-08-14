class Pracownicy:
    def __init__(self):
        self.listaPracownik = []

    def dodajPracownika(self, i, n, k="staż", p=1000):
        self.listaPracownik.append([i, n, k, p])

    def pokazPracownika(self):
        for i, xxx in enumerate(self.listaPracownik):
            print("%5i%5s%12s%12s%12s" % (i, xxx[0], xxx[1], xxx[2], xxx[3]))

    def zmianaPracownika(self, z):
        p = input("Jaka pensja: ")
        self.listaPracownik[z][2] = "etat"
        self.listaPracownik[z][3] = p

    def usunPracownika(self, d):
        self.listaPracownik.pop(d)

class Firma(Pracownicy):
    def __init__(self, nazwaFirmy):
        self.nazwaFirmy = nazwaFirmy
        super().__init__()

    def menu(self):
        while (True):
            dec = input("d -dodaj, p -pokaz, u -usun, z -zmiana kontaktu, q -koniec \n")
            if dec == "d":
                k = input("Kogo dodajesz: s -starzysta, e -etatowiec \n")
                if k == "s":
                    i = input("Wpisz imie pracownika: ")
                    n = input("Wpisz nazwisko pracownika: ")
                    self.dodajPracownika(i, n)
                else:
                    i = input("Wpisz imie pracownika: ")
                    n = input("Wpisz nazwisko pracownika: ")
                    p = input("Podaj wysokość pensji: ")
                    self.dodajPracownika(i, n, "etat", p)
            if dec == "p":
                self.pokazPracownika()
            if dec == "u":
                self.pokazPracownika()
                d = input("Wpisz nr id do usuniecia: ")
                self.usunPracownika(int(d))
            if dec == "z":
                self.pokazPracownika()
                z = input("Wpisz nr id do zmiany: ")
                self.zmianaPracownika(int(z))
            if dec == "q":
                break

ob = Firma("NOW NAME")
ob.menu()