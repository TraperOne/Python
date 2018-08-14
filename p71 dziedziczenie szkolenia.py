class Produkt:
    def __init__(self, nazwa0, cena0):
        self.nazwa = nazwa0
        self.cena = cena0

class Oprogramowanie(Produkt):
    def __init__(self, nazwa0, cena0, jezyk0, system0):
        super().__init__(nazwa0, cena0)
        self.jezyk = jezyk0
        self.system = system0

class Szkolenia(Oprogramowanie):
    def __init__(self, nazwa0, cena0, jezyk0, system0, termin0):
        super().__init__(nazwa0, cena0, jezyk0, system0)
        self.termin = termin0

    def wyswietl(self):
        print(self.nazwa, self.cena, self.jezyk, self.system, self.termin)


obj = Szkolenia("kurs", 10000, "python", "pro", 3)
obj.wyswietl()