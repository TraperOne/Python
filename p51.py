dane = {0:"zero", 1:"jeden", 2:"dwa", 3:"trzy", 4:"cztery", 5:"piec", 6:"sześć", 7:"siedem", 8:"osiem", 9:"dziewięć"}

napis=input("Podaj liczbę: ")
ile=len(napis)

for i in range(0, ile):
    print(dane[int(napis[i])], end=" ")
