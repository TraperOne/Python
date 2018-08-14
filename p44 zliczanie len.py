print("podaj trzy liczby, a powiem Ci ile jest różnych")
x = input("podaj 1 liczbę: ")
y = input("podaj 2 liczbę: ")
z = input("podaj 3 liczbę: ")

xyz = set([x, y, z])
liczba = len(xyz)
print(liczba)