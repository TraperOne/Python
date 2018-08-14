licznik = 10
wartosc = 25
while (licznik <= wartosc):
    licznik += 1
    print("Jestem w pętli " + str(licznik))

a = 4
while (a):
    a -= 1
    print(a)
else:
    print("KONIEC")

lista = [1, 2, 3, 4, 5]
ile = len(lista)
licz = 0
for ax in lista:
    licz += ax
srednia = licz / ile
print(srednia)
