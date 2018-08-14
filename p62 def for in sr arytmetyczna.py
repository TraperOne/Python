def srednia(liczby):
    sum = 0
    for i in liczby:
        sum += i / len(liczby)
    return (sum)
print(srednia([5, 2, 9, 12]))
