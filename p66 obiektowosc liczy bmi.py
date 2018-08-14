class Zawodnik:
    def __init__(self, imie0, wzrost0, waga0):
        self.imie = imie0
        self.wzrost = wzrost0
        self.waga = waga0

    def obliczBMI(self):
        bmi = round(self.waga / (self.wzrost * self.wzrost), 2)
        return bmi

zan = Zawodnik("Zenek", 1.7, 62)
print(zan.obliczBMI())

zol = Zawodnik("Robert", 1.8, 68)
print(zol.obliczBMI())
