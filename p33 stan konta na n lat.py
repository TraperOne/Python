k=float(input("Podaj kwotę konta \n"))
r=float(input("Podaj stope procentową [%] \n"))
l=float(input("Podaj ilość lat \n"))

v=round((k*(1+(r/100))**l), 2)
print("Twój stan konta to:", str(v))


