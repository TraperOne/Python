for x in range(0, 10):
    if (x == 5):
        continue
    print(x)



liczby = [2, 1, 4, -1, -2]
for x in liczby:
    if x < 0:
        continue
    print("Pierwiastkiem liczby %1i jest %5.2f" % (x, x**3))


for x in range(0, 10):
    if (x == 5):
        break
    print(x)