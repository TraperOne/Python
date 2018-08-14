lista = [1, -2]

l1 = lista[0]
l2 = lista[1]

if l1 >= 0 and l2 > 0:
    print("obie dodatnie")
elif l1 >= 0 and l2 < 0:
    print("jedna ujemna")
elif l1 < 0 and l2 > 0:
    print("jedna ujemna")
elif l1 < 0 and l2 < 0:
    print("obie ujemne")
