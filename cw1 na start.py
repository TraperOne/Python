a=int(input("Podaj liczbę całkowitą: "))
b=float(input("Podaj liczbę rzeczywistą: "))
c=bool(int(input("Podaj wartość logiczną: ")))
d=str(input("Podaj wartość tekstową: "))

x=b*10
x=x**a
x=x*c

print(("Podano napis \"" + d + '" oraz obliczono ' + str(x) + "\n") * 10)