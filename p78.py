po=int(input("Podaj podstawe: "))
wy=int(input("Podaj wykładnik: "))
wynik=1
for i in range(wy):
    wynik = wynik*po
print(wynik)