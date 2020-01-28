import psycopg2
from tkinter import *
from tkinter import messagebox as mb
from SysAdminClass import *
from LibraryAdminClass import *
from LibraryWorkerClass import *
import MongoDB
import SQLite
SYSADMIN = "Системный администратор"
LIBADMIN = "Администратор библиотеки"
LIBWORKER = "Библиотекарь"

root = Tk()
root.title("Университетская библиотека")
root.geometry("400x300")


def validate():
    f = open('config', 'r')
    text = f.readlines()
    db = text[0].split('=')
    db = db[1].strip()
    if db == "MongoLibrary":
        mongo = MongoDB.MongoMain()
    elif db == "Library":
        libraryworker = LibraryWorker()
    elif db == "IntegrationLibrary":
        sqlite = SQLite.SQLiteMain()
    else:
        mb.showerror(parent=root, message=f"Базы данных {db} не существует")
    #admin = SysAdmin()
    # library = LibraryAdmin()
   # login = loginTxt.get()
   # password = passwordTxt.get()
   # cursor.execute("SELECT * FROM users WHERE password = \'{}\' AND login = \'{}\'".format(password,login))
   # result = cursor.fetchall()
   # print(result)
   # if not result:
   #     answer = mb.showerror(parent = root, message = "Логин или пароль введены неверно :( ")
   # elif result[0][3] == SYSADMIN:
   #     sy = sysAd.SysAdminPanel(cursor,conn)
   # elif result[0][3] == LIBADMIN:
   #   libAdmin = libAd.LibAdminPanel(cursor,conn)





loginLabel = Label(text="Логин", font="16pt").place(x=50, y=60)
loginTxt = StringVar()
loginEntry = Entry(textvariable=loginTxt, font="16pt", fg="black").place(x=140, y=60)


passwordLabel = Label(text="Пароль", font="16pt").place(x=50, y=120)
passwordTxt = StringVar()
passwordEntry = Entry(textvariable = passwordTxt,font="16pt", fg="black", show="*").place(x=140, y=120)
loginButton = Button(text="Войти", fg="black", command=validate).place(x=150, y=200, height=50, width=150)
root.mainloop()


def printa():
    print("a")