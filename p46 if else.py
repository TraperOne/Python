lista=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
l=int(input("Podaj liczbę 0-9: "))
if l in lista:
    print("cyfra w przedziale")
else:
    print("liczba poza przedziałem")

a=int(input("Podaj liczbę 0-9: "))
if a > 0:
    if a < 10:
        print("cyfra w przedziale")
    else:
        print("liczba poza przedziałem")
