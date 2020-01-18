import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox as mb
from Postgres import *
import psycopg2

class Table(tk.Frame):
    def __init__(self, parent=None, headings=tuple(), rows=tuple()):
        super().__init__(parent)
        self.table = ttk.Treeview(self, show="headings", height = 12, selectmode="browse")
        self.table["columns"] = headings
        self.table["displaycolumns"] = headings

        self.nameEntry = None
        self.surnameEntry = None
        self.patronymicEntry = None
        self.studbiletEntry = None


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
        massiv[4] = str(massiv[4])
        print(massiv)
        cursor.execute("DELETE FROM readers WHERE (id=%s AND surname=%s AND name=%s OR patronymic=%s AND studbilet=%s AND biletexpiredin=%s)",
                       (massiv))
        connect.commit()
        self.table.delete(item)

    def createAddWin(self, connect, cursor):
        self.window = tk.Toplevel(self)
        self.window.geometry("500x350")
        addbutton = tk.Button(self.window, text="Добавить читателя", command = self.addReader, height=3,
                              width=15)
        addbutton.pack(side=tk.BOTTOM, padx=12, pady=20)

        nameLabel = tk.Label(self.window, text="Имя*", font="16pt")
        nameLabel.place(x=10,y=50)
        nameEntry = tk.Entry(self.window, font="16pt", fg="black",width = 30)
        nameEntry.place(x=120,y=50)
        self.nameEntry = nameEntry

        surnameLabel = tk.Label(self.window, text="Фамилия*", font="16pt")
        surnameLabel.place(x=10,y=100)
        surnameEntry = tk.Entry(self.window, font="16pt", fg="black",width = 30)
        surnameEntry.place(x=120,y=100)
        self.surnameEntry = surnameEntry

        patronymicLabel = tk.Label(self.window, text="Отчество", font="16pt")
        patronymicLabel.place(x=10,y=150)
        patronymicEntry = tk.Entry(self.window, font="16pt", fg="black",width = 30)
        patronymicEntry.place(x=120,y=150)
        self.patronymicEntry = patronymicEntry

        studbiletLabel = tk.Label(self.window, text="Студ. билет*", font="16pt")
        studbiletLabel.place(x=10, y=200)
        studbiletEntry = tk.Entry(self.window, font="16pt", fg="black", width=30)
        studbiletEntry.place(x=120, y=200)
        self.studbiletEntry = studbiletEntry

    def update(self):
        postgres = Postgres()
        conn = postgres.returnConnect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM readers")
        readers = cursor.fetchall()
        self.table.delete(*self.table.get_children())
        for row in readers:
            self.table.insert('', tk.END, values=tuple(row))


    def addReader(self):
        postgres = Postgres()
        name = self.nameEntry.get()
        surname = self.surnameEntry.get()
        patronymic = self.patronymicEntry.get()
        studbilet = self.studbiletEntry.get()
        badInput = False
        errorMessage = "Пожалуйста, введите"
        if not name:
            errorMessage+= " имя"
            badInput = True
        if not surname:
            errorMessage+= " фамилию"
            badInput = True
        if not studbilet:
            errorMessage+= " студенческий билет"
            badInput = True
        if badInput:
            answer = mb.showerror(parent=self.window,message=errorMessage)
        else:
            postgres.addReader(name,surname,patronymic,studbilet)
            self.update()