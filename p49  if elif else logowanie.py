konta = {"admin": "admin00", "user": "user00", "emil": "emil00"}

login = input("podaj login: ")
haslo = input("podaj hasło: ")

if login == "admin" and haslo == konta[login]:
    print("witaj adminie")
elif haslo == konta[login]:
    print("witaj użytkowniku")
else:
    print("błędne hasło")
