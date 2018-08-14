def srednia(x, y, z):       # trzy argumenty
    wynik=(x+y+z)/3
    return wynik
w= srednia(5, 3, 5)
print(w)
v = srednia(20, 50, 100)
print(v)

def potega(p, w):           # dwa argumenty
    co=(p**w)
    return co
k = potega(2, 3)
print(k)
l = potega(4, 3)
print(l)

def hellow (imie):          # jeden argument
    print("Cześć "+imie)
hellow ("Emil")

def test():
    return ("COCA", "COLA") # wielo parametrowe
A, B = test()
print(A, B)

def test(a, b=5):           # wartość domyślna
    print(a, b)
test(10)

def suma(*arg):
    s=0
    for x in arg:
        s+=x
    return s
z=suma(1,2,3,4,5,6)
print(z)

def sum2(lista):
    sum = 0
    for i in lista:
        sum += i
    return (sum)
print(sum2([2,5,6,3]))