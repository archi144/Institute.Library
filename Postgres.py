import psycopg2
from datetime import *

class Postgres:
    def __init__(self):
        f = open('config', 'r')
        text = f.readlines()
        db = text[0].split('=')
        db = db[1].strip()
        user = text[1].split('=')
        user = user[1].strip()
        password = text[2].split('=')
        password = password[1].strip()
        host = text[3].split('=')
        host = host[1].strip()
        f.close()
        self.connect = psycopg2.connect(dbname="Library", user=user, password=password, host=host)
        self.cursor = self.connect.cursor()

    def returnConnect(self):
        return self.connect

    def addReader(self,name,surname,patronymic,studbilet):
        date = datetime.today() + timedelta(days=365)
        self.cursor.execute("INSERT INTO readers (name, surname, patronymic, studbilet, biletexpiredin) VALUES (%s, %s, %s, %s, %s)",
                                                 (name, surname, patronymic, studbilet, date))
        self.connect.commit()

    def addUser(self,login,password,role):
        self.cursor.execute(
            "INSERT INTO users (login, password, role) VALUES (%s, %s, %s)",
            (login, password, role))
        self.connect.commit()

    def returnAllBooks(self):
        self.cursor.execute(
            """SELECT books."id","name","author","countofvolumes","link","type" FROM books
            FULL OUTER JOIN paperbook p on books.id = p.id_book
            FULL OUTER JOIN electronicbook e on books.id = e.id_book
            ORDER BY books.id
            """
        )
        return self.cursor.fetchall()

    def returnReaderBooks(self,id_reader):
        self.cursor.execute(
            f"""SELECT books."id",books."name","author","datereturn","type"
                from books INNER JOIN readers_books rb on books.id = rb.id_book
                inner join readers r on r.id = rb.id_reader
                WHERE r.id={id_reader}
            """
        )
        return self.cursor.fetchall()

    def givPaperBook(self,id_reader,id_book):
        date = datetime.today() + timedelta(days=14)
        print(date)
        self.cursor.execute(
            f"""UPDATE paperbook SET countofvolumes=countofvolumes-1 WHERE id_book={id_book};""")
        self.cursor.execute(
            "INSERT INTO readers_books(id_reader,id_book,datereturn) VALUES(%s, %s, %s)",(id_reader,id_book,date))
        self.connect.commit()

    def givElectroBook(self,id_reader,id_book):
        date = datetime.today() + timedelta(days=14)
        print(date)
        self.cursor.execute(
            "INSERT INTO readers_books(id_reader,id_book,datereturn) VALUES(%s, %s, %s)", (id_reader, id_book, date))
        self.connect.commit()

    def returnPaperBook(self,id_reader,id_book,datereturn):
        self.cursor.execute(
            f"""UPDATE paperbook SET countofvolumes=countofvolumes+1 WHERE id_book={id_book};""")
        self.cursor.execute(
        "DELETE FROM readers_books WHERE id_reader=%s AND id_book=%s AND datereturn=%s", (id_reader, id_book, datereturn))
        self.connect.commit()

    def bookOnHand(self,id_reader,id_book):
        self.cursor.execute(
            f"""SELECT * FROM readers_books WHERE id_book={id_book} AND id_reader={id_reader};""")
        result = self.cursor.fetchall()
        if result:
            return True
        else:
            return False