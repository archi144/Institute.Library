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
        addbutton = tk.Button(self.window, text="Добавить читателя", command=self.addReader, height=3,
                              width=15)
        addbutton.pack(side=tk.BOTTOM, padx=12, pady=20)

        loginLabel = tk.Label(self.window, text="Имя*", font="16pt")
        loginLabel.place(x=10, y=50)
        loginEntry = tk.Entry(self.window, font="16pt", fg="black", width=30)
        loginEntry.place(x=120, y=50)
        self.loginEntry = loginEntry

        passwordLabel = tk.Label(self.window, text="Фамилия*", font="16pt")
        passwordLabel.place(x=10, y=100)
        passwordEntry = tk.Entry(self.window, font="16pt", fg="black", width=30)
        passwordEntry.place(x=120, y=100)
        self.passwordEntry = passwordEntry

        roleLabel = tk.Label(self.window, text="Роль", font="16pt")
        roleLabel.place(x=10, y=150)
        roleEntry = ttk.Combobox(self.window, font="16pt", width=30,values=['Системный администратор','Администратор библиотеки','Бибиотекарь'])
        roleEntry.place(x=120, y=150)
        self.roleEntry = roleEntry


    def update(self):
        postgres = Postgres()
        conn = postgres.returnConnect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM readers")
        readers = cursor.fetchall()
        self.table.delete(*self.table.get_children())
        for row in readers:
            self.table.insert('', tk.END, values=tuple(row))


    def addUser(self):
        postgres = Postgres()
        login = self.loginEntry.get()
        password = self.passwordEntry.get()
        role = self.roleEntry.get()
        badInput = False
        errorMessage = "Пожалуйста, введите"
        if not login:
            errorMessage+= " логин"
            badInput = True
        if not password:
            errorMessage+= " пароль"
            badInput = True
        if not role:
            errorMessage+= " роль"
            badInput = True
        if badInput:
            answer = mb.showerror(parent=self.window,message=errorMessage)
        else:
            postgres.addReader(login,password,role)
            self.update()