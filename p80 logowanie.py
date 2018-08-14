import pymysql

class logowanie:
    def __init__(self):
        self.conn = pymysql.connect('localhost', 'root', 'alfa147', 'logowanie')
        self.c = self.conn.cursor()
        print("połączenie ustanowione!")
        self.logowanie()

    def logowanie(self):
        login = input("podaj login: ")
        haslo = input("podaj hasło: ")
        self.c = self.conn.cursor()
        self.c.execute("SELECT * FROM logowanie where login=%s and haslo=%s", (login, haslo))
        LogRes = self.c.fetchall()
        if (len(LogRes) == 1):
            if (LogRes [0][5] == str(1)):
                self.menu()
            elif (LogRes[0][5] == str(2)):
                self.menu_user()
            print("zalogowano")
        else:
            print("błędne hasło")

    def pokaz(self):
        self.c.execute("SELECT * FROM logowanie")
        Result = self.c.fetchall()
        print("%20s|%20s|%20s|%20s|%20s" % (
        "Imię", "Nazwisko", "Login", "Hasło", "Uprawnienia"))
        for row in Result:
            print("%20s|%20s|%20s|%20s|%20s" % (row[1], row[2], row[3], row[4], row[5]))

    def dodaj(self):
        imie = input("Imie = ")
        nazwisko = input("Nazwisko = ")
        login = input("Login = ")
        haslo = input("Hasło = ")
        uprawnienia = input("Uprawnienia = ")

        self.c.execute(
            "INSERT INTO logowanie(imie, nazwisko, login, haslo, uprawnienia) VALUES (%s,%s,%s,%s,%s)",
            (imie, nazwisko, login, haslo, uprawnienia))
        czynapewno = input("Czy na pewno dodać nowego uzytkownika? T/N ")
        if (czynapewno == "t"):
            self.conn.commit()
            print("Pomyślnie dodano")
        else:
            self.conn.rollback()
            print("Anulowano operację")

    def zmien(self):
        self.pokaz()
        login = input("Podaj login osoby, którą zamierzasz edytować = ")
        column = input("Którą kolumnę chcesz edytować? ")
        value = input("Podaj nową wartość = ")

        sql = ("UPDATE logowanie SET {}=%s WHERE login=%s").format(column)
        self.c.execute(sql, (value, login))
        czynapewno = input("Czy na pewno chcesz zmienić dane? T/N ")
        if (czynapewno == "t"):
            self.conn.commit()
            print("Pomyślnie dodano")
        else:
            self.conn.rollback()
            print("Anulowano operację")

    def usun(self):
        self.pokaz()
        login1 = input("Podaj login osoby, którą chcesz usunąć = ")
        self.c.execute("DELETE FROM logowanie WHERE login=%s", login1)
        czynapewno1 = input("Czy na pewno chcesz usunąć dane? T/N ")
        if czynapewno1 == "t":
            self.conn.commit()
            print("Pomyślnie usunięto")
        else:
            self.conn.rollback()
            print("Anulowano operację")

    def menu(self):
        while (True):
            dec = input("p -pokaz, d -dodaj, u -usun, z -zmień uprawnienia, q -wyjście\nCo chcesz zrobić: ")
            if (dec == "p"):
                self.pokaz()
            elif (dec == "d"):
                self.dodaj()
            elif (dec == "u"):
                self.usun()
            elif (dec == "z"):
                self.zmien()
            elif (dec == "q"):
                break

    def menu_user(self):
        while (True):
            dec = input("p -pokaz, q -wyjście\nCo chcesz zrobić: ")
            if (dec == "p"):
                self.pokaz()
            elif (dec == "q"):
                break
ob = logowanie()