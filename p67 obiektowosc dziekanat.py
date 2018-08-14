class Dziekanat:
    def __init__(self):
        self.lista_st = []

    def menu(self):
        while (True):
            dec = input("d -dodaj, p -pokaz studentow, u -usun, q -zakoncz \n")
            if dec == "d":
                i = input("Wpisz imie: ")
                n = input("Wpisz nazwisko: ")
                t = input("Wpisz nr_indeksu: ")
                self.dodajStudenta(i, n, t)
            if dec == "p":
                self.pokazStudentow()
            if dec == "u":
                t = input("Wpisz nr_indeksu do usuniecia: ")
                self.usunStudenta(t)
            if dec == "q":
                break

    def dodajStudenta(self, i, n, t):
        self.lista_st.append([i, n, t])

    def pokazStudentow(self):
        for xxx in self.lista_st:
            print("%5s%12s%12s" % (xxx[0], xxx[1], xxx[2]))

    def usunStudenta(self, t):
        for index, wartosc in enumerate(self.lista_st):
            if wartosc[2] == t:
                self.lista_st.pop(index)

ob = Dziekanat()
ob.menu()