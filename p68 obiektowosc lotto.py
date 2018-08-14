from random import randint


class Lotto:
    def __init__(self):
        self.liczby = set()

    def losuj(self):
        while len(self.liczby) < 6:
            self.liczby.add(randint(0, 49))
        print(sorted(self.liczby))


ob = Lotto()
ob.losuj()
