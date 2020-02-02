import tkinter as tk
import tkinter.ttk as ttk
from _sqlite3 import *
from tkinter import messagebox as mb
import datetime
from time import *
from Postgres import *
from tkinter import *


# def return_collection(collection):
#     client = MongoClient()
#     db = client['MongoLibrary']
#     collections = db[collection]
#     massiv = list()
#     for item in collections.find():
#         item.pop('_id')
#         massiv.append(item.values())
#     return massiv
#
# def return_booksOfReader(id_reader):
#     books = db.readers.find_one({"id": id_reader}, {"books": 1, "_id": 0})
#     massiv = list()
#     for book in books.values():
#         for item in book:
#             massiv.append(item.values())
#     return tuple(massiv)
#
#
# def return_bookOfReader(id_reader,id_book):
#     books = db.readers.find_one({"id": id_reader}, {"books": 1, "_id": 0})
#     massiv = list()
#     for book in books.values():
#         for item in book:
#             if item['id'] == id_book:
#                 massiv.append(item.values())
#     return tuple(massiv)
#
#
# def bookOnHandsOfReader(id_reader,id_book):
#     books = db.readers.find_one({"id": id_reader}, {"books": 1, "_id": 0})
#     for book in books.values():
#         for item in book:
#             if item['id'] == id_book:
#                 return True
#     return False

# def readerClear(id_reader):
#     books = db.readers.find_one({"id": id_reader}, {"books": 1, "_id": 0})
#     if not books['books']:
#         return True
#     return False
#
# def isReaderViolator(id_reader):
#     violation = db.readers.find_one({"id": id_reader}, {"violator": 1, "_id": 0})
#     if violation['violator']:
#         return True
#     return False



def SQLiteMain():
    root = tk.Tk()
    global SQLiteconn, SQLitecursor
    SQLiteconn = connect("/home/archi144/PycharmProjects/library.issues/source/db.sqlite3")
    SQLitecursor = SQLiteconn.cursor()
    SQLitecursor.execute("""SELECT webapp_book.id, webapp_book.title, webapp_book.author, webapp_book.link, webapp_book.amount
                   FROM webapp_book""")
    massiv = SQLitecursor.fetchall()
    postgres = Postgres()
    Postgresconn = postgres.returnConnect()
    Postgrescursor = Postgresconn.cursor()
    Postgrescursor.execute("SELECT * FROM readers")
    readers = Postgrescursor.fetchall()
    table = Table(root, headings=(
    'Читательский билет №', 'Фамилия', 'Имя', 'Отчество', 'Студ. билет', 'Срок окончания билета','Нарушитель'), rows=(readers))
    table.pack()
    addbutton = tk.Button(root, text="Выдать читателю книгу", command=lambda: table.createBooksWin(),
                                      height=3, width=20)
    addbutton.pack(side=tk.RIGHT, padx=12, pady=20)
    returnbookbutton= tk.Button(root, text="Принять книги читателя", command=lambda: table.createReaderBooksShowWin(),
                                      height=3, width=20)
    returnbookbutton.pack(side=tk.LEFT, padx=12, pady=20)
    root.mainloop()





class Table(tk.Frame):
    def __init__(self, parent=None, headings=tuple(), rows=tuple()):
        super().__init__(parent)
        self.table = ttk.Treeview(self, show="headings", height = 12, selectmode="browse")
        self.table["columns"] = headings
        self.table["displaycolumns"] = headings

        self.loginEntry = None
        self.passwordEntry = None
        self.roleEntry = None



        for head in headings:
            self.table.heading(head, text=head, anchor=tk.CENTER)
            self.table.column(head, anchor=tk.CENTER)

        for row in rows:
            self.table.insert('', tk.END, values=tuple(row))

        scrolltable = tk.Scrollbar(self, command=self.table.yview)
        self.table.configure(yscrollcommand=scrolltable.set)
        scrolltable.pack(side=tk.RIGHT, fill=tk.Y)
        self.table.pack(expand=tk.YES, fill=tk.BOTH)

    def remove(self,connect,cursor):
        item = self.table.selection()
        massiv = self.table.item(item)['values']
        massiv[-1] = str(massiv[-1])
        print(massiv)
        cursor.execute("DELETE FROM users WHERE (id=%s AND login=%s AND password=%s AND role=%s)",
                       (massiv))
        connect.commit()
        self.table.delete(item)

    def createAddWin(self, connect, cursor):
        self.window = tk.Toplevel(self)
        self.window.geometry("500x350")
        addbutton = tk.Button(self.window, text="Добавить читателя", command=self.addUser, height=3,
                              width=15)
        addbutton.pack(side=tk.BOTTOM, padx=12, pady=20)

        loginLabel = tk.Label(self.window, text="Логин*", font="16pt")
        loginLabel.place(x=10, y=50)
        loginEntry = tk.Entry(self.window, font="16pt", fg="black", width=30)
        loginEntry.place(x=120, y=50)
        self.loginEntry = loginEntry

        passwordLabel = tk.Label(self.window, text="Пароль*", font="16pt")
        passwordLabel.place(x=10, y=100)
        passwordEntry = tk.Entry(self.window, font="16pt", fg="black", width=30)
        passwordEntry.place(x=120, y=100)
        self.passwordEntry = passwordEntry

        roleLabel = tk.Label(self.window, text="Роль", font="16pt")
        roleLabel.place(x=10, y=150)
        roleEntry = ttk.Combobox(self.window, font="16pt", width=30,values=['Системный администратор','Администратор библиотеки','Бибиотекарь'])
        roleEntry.place(x=120, y=150)
        self.roleEntry = roleEntry

    def createReaderBooksShowWin(self):
        self.ReaderBooksWin = tk.Toplevel(self)

        postgres = Postgres()
        item = self.table.selection()
        massiv = self.table.item(item)['values']
        self.ReaderBooksWin.title(f"№{massiv[0]} {massiv[1]} {massiv[2]}")
        id = massiv[0]
        print(massiv)
        postgres.cursor.execute(f"""SELECT * FROM django_reader_books""")
        books = postgres.cursor.fetchall()

        print(books)
        self.readerBooksTable = Table(self.ReaderBooksWin, headings=(
            'ID','Название книги', 'Автор','Дата возврата книги', 'Тип книги',),
                                rows=(books))
        returnBookButton = tk.Button(self.ReaderBooksWin, text="Принять книгу", command=self.returnBook, height=3,
                                  width=15)
        returnBookButton.pack(side=tk.BOTTOM, padx=12, pady=20)
        self.readerBooksTable.pack()

    def createBooksWin(self):
        self.BooksWin = tk.Toplevel(self)
        postgres = Postgres()
        books = postgres.returnAllBooks()
        print(books)
        item = self.table.selection()
        massiv = self.table.item(item)['values']
        self.BooksWin.title(f"№{massiv[0]} {massiv[1]} {massiv[2]}")
        SQLiteconn = connect("/home/archi144/PycharmProjects/library.issues/source/db.sqlite3")
        SQLitecursor = SQLiteconn.cursor()
        SQLitecursor.execute("""SELECT webapp_book.id, webapp_book.title, webapp_book.author, 
                                    webapp_book.amount, webapp_book.link, webapp_book.type
                           FROM webapp_book""")
        books = SQLitecursor.fetchall()
        self.BooksTable = Table(self.BooksWin, headings=(
            'ID', 'Название книги', 'Автор', 'Количество', 'Ссылка', 'Тип',),
                      rows=(books))
        self.BooksTable.pack()
        givBookButton = tk.Button(self.BooksWin, text="Выдать книгу", command=self.givBook, height=3,
                              width=15)
        givBookButton.pack(side=tk.BOTTOM, padx=12, pady=20)


    def update(self):
        postgres = Postgres()
        conn = postgres.returnConnect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
        self.table.delete(*self.table.get_children())
        for row in users:
            self.table.insert('', tk.END, values=tuple(row))

    def updateBooksWin(self):
        postgres = Postgres()
        SQLiteconn = connect("/home/archi144/PycharmProjects/library.issues/source/db.sqlite3")
        SQLitecursor = SQLiteconn.cursor()
        SQLitecursor.execute("""SELECT webapp_book.id, webapp_book.title, webapp_book.author, 
                                            webapp_book.amount, webapp_book.link, webapp_book.type
                                   FROM webapp_book""")
        books = SQLitecursor.fetchall()
        print(books)
        self.BooksTable.table.delete(*self.BooksTable.table.get_children())
        for row in books:
            self.BooksTable.table.insert('', tk.END, values=tuple(row))

    def updateReaderBooksShowWin(self):
        postgres = Postgres()
        item = self.table.selection()
        massiv = self.table.item(item)['values']
        id_reader = massiv[0]
        books = postgres.returnReaderBooks(id_reader)
        self.readerBooksTable.table.delete(*self.readerBooksTable.table.get_children())
        for row in books:
            self.readerBooksTable.table.insert('', tk.END, values=tuple(row))

    def returnBook(self):
        postgres = Postgres()
        item = self.readerBooksTable.table.selection()
        massivofbooks = self.readerBooksTable.table.item(item)['values']
        id_book = massivofbooks[0]
        datereturn = massivofbooks[3]
        item = self.table.selection()
        massiv = self.table.item(item)['values']
        id_reader = massiv[0]
        postgres.returnPaperBook(id_reader,id_book,datereturn)
        self.updateReaderBooksShowWin()

    def givBook(self):
        postgres = Postgres()
        item = self.BooksTable.table.selection()
        massivofbooks = self.BooksTable.table.item(item)['values']
        id_book = massivofbooks[0]
        item = self.table.selection()
        massiv = self.table.item(item)['values']
        id_reader = massiv[0]
        date = datetime.today() + timedelta(days=14)
        if postgres.bookOnHand(id_reader,id_book):
            mb.showerror(parent=self, message="Эта книга уже есть у пользователя")
        else:
            if massivofbooks[-1] == 'Печатная':
                postgres.cursor.execute(
                    "INSERT INTO django_reader_books(id, name, author, date_return, type, reader_id) VALUES (%s, %s, %s, %s, %s, %s)",
                    (massivofbooks[0], massivofbooks[1], massivofbooks[2], date, massivofbooks[-1], id_reader))
                postgres.connect.commit()
                SQLitecursor.execute(f"""UPDATE webapp_book SET amount=amount-1 WHERE id={id_book}""")
                SQLiteconn.commit()
               # postgres.givPaperBook(id_reader,id_book)
            else:
                pass
               # postgres.givElectroBook(id_reader,id_book)
        self.updateBooksWin()

