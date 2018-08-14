a=float(input("Ile kupujesz chebów: "))
b=float(input("Ile kupujesz soków: "))
c=float(input("Ile kupujesz pączków: "))

x=2.99*a
y=3.99*b
z=1.50*c
w=x+y+z
print("Twoje zamowienie to:")
print("1. Chlebów - "+str(a)+" szt. - razem "+str(x)+" zł")
print("2. Soków - "+str(b)+" szt. - razem "+str(y)+" zł")
print("3. Pączków - "+str(c)+" szt. - razem "+str(z)+" zł")
print("Razem: "+str(w)+" zł")