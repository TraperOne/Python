lista = [["a", "b", "c", "d", "e", "f"], [1, 2, 3, 4, 5, 6]]
print(lista[0][1])  # wypisze z pierwszej listy drugi element, czyli b

lista = lista * 2  # powielenie listy razy 2
lista *=3 # inny zapis powielenia listy

print(len(lista))  # długość listy

lista = lista [0:5]  # skracanie listy

lista[0:2] = ["jeden", "dwa"] # zamiana wartości w podanej liście

lista.pop(1) # usuwa określony element

print(lista)