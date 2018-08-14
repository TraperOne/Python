lista = ["a", "b", "c", "d", "e", "f"]
lista2 = lista # kopiowanie listy, ale to pewne zagrożenie
lista2[2] = "x"  # zamienia w obu listach, nie tylko w lista2
print(lista, lista2)


print("e" in lista)
print("cx" in lista)
print("g" not in lista)