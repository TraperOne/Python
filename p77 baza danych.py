import pymysql

class Pracownicy:
    def __init__(self):
        self.conn = pymysql.connect('localhost', 'root', 'alfa147', 'testpython')
        self.c = self.conn.cursor()
        print("połączenie ustanowione!")
        self.logowanie()

    def insert(self):
        imie = input("Imie = ")
        nazwisko = input("Nazwisko = ")
        rokUrodzenia = input("Rok urodzenia (YYYY) = ")
        pensja = input("Pensja = ")
        pesel = input("PSEL = ")
        dataZatrudnienia = input("Data zatrudnienia (YYYY-MM-DD = ")

        self.c.execute("INSERT INTO pracownicy(imie, nazwisko, rokUrodzenia, pensja, pesel, dataZatrudnienia) VALUES (%s,%s,%s,%s,%s,%s)", (imie, nazwisko, rokUrodzenia, pensja, pesel, dataZatrudnienia))
        czynapewno = input("Czy na pewno dodać nowe dane? T/N ")
        if (czynapewno == "t"):
            self.conn.commit()
            print("Pomyślnie dodano")
        else:
            self.conn.rollback()
            print("Anulowano operację")

    def select(self):
        self.c.execute("SELECT * FROM pracownicy")
        Result = self.c.fetchall()
        print("%10s|%20s|%20s|%20s|%20s|%20s" % ("Imię", "Nazwisko", "Rok urodzenia", "Pensjia", "PESEL", "Data urodzenia"))
        for row in Result:
            print("%10s|%20s|%20s|%20s|%20s|%20s" % (row[1], row[2], row[3], row[4], row[5], row[6]))

    def update(self):
        self.select()
        pesel = input("Podaj PESEL osoby, którą zamierzasz edytować = ")
        column = input("Którą kolumnę chcesz edytować? ")
        value = input("Podaj nową wartość = ")

        sql = ("UPDATE pracownicy SET {}=%s WHERE pesel=%s").format(column)
        self.c.execute(sql, (value, pesel))
        czynapewno = input("Czy na pewno chcesz zmienić dane? T/N ")
        if (czynapewno == "t"):
            self.conn.commit()
            print("Pomyślnie dodano")
        else:
            self.conn.rollback()
            print("Anulowano operację")

    def delet(self):
        self.select()
        pesel1 = input("Podaj PESEL osoby, którą chcesz usunąć = ")
        self.c.execute("DELETE FROM pracownicy WHERE pesel=%s", pesel1)
        czynapewno1 = input("Czy na pewno chcesz usunąć dane? T/N ")
        if czynapewno1 == "t":
            self.conn.commit()
            print("Pomyślnie usunięto")
        else:
            self.conn.rollback()
            print("Anulowano operację")

    def logowanie(self):
        login = input("podaj login: ")
        haslo = input("podaj hasło: ")
        self.c = self.conn.cursor()
        self.c.execute("SELECT * FROM logowanie where login=%s and haslo=%s", (login, haslo))
        LogRes = self.c.fetchall()
        if (len(LogRes) == 1):
            print("zalogowano")
            self.menu()
        else:
            print("błędne hasło")


    def menu(self):
        while(True):
            dec = input("i -dodaj, s -pokaz, d -usun, u -aktualizacja, q -zakoncz\nCo chcesz zrobić: ")
            if (dec == "i"):
                self.insert()
            elif (dec == "s"):
                self.select()
            elif (dec == "u"):
                self.update()
            elif (dec == "d"):
                self.delet()
            elif (dec == "q"):
                break

ob = Pracownicy()