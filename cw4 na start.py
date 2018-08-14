def tabliczka(x, y):
    for w in range(1, x+1):
        for w1 in range(1, y+1):
            print("%4i" % (w * w1), end=" ")
        print("\n")

tabliczka(5, 5)
