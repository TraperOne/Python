def odleglosci(a, b, c, d):
    wynik = ((a - c) ** 2 + (b - d) ** 2) ** 0.5
    return wynik
w = odleglosci(2, 1, 6, 4)
print(w)
