from tkinter import *
from time import *
from tkinter import messagebox as mb
from tkinter import ttk as ttk
import random
class LibWorkerPanel:
    def __init__(self,cursor,connect):
        self.LibWrkWin = Tk()
        self.cursor = cursor
        self.connect = connect
        self.LibWrkWin.title("Панель библиотекаря")
        self.LibWrkWin.geometry("700x365")
        surNameLabel = Label(self.LibWrkWin,text="Фамилия читателя*", font="16pt")
        surNameLabel.grid(row=0, column=0, pady=8)
        self.surNameEntry = Entry(self.LibWrkWin,font="16pt",fg= "black")
        self.surNameEntry.grid(row = 0, column = 2, pady = 8)
        nameLabel = Label(self.LibWrkWin, text="Имя читателя*", font="16pt")
        nameLabel.grid(row = 2, column = 0, pady = 8)
        self.nameEntry = Entry(self.LibWrkWin, font="16pt", fg="black")
        self.nameEntry.grid(row=2, column=2, pady=8)
        readerBiletLabel = Label(self.LibWrkWin, text="Номер читательского билета*", font="16pt")
        readerBiletLabel.grid(row = 4, column = 0, pady = 8)
        self.readerBiletEntry = Entry(self.LibWrkWin, font="16pt", fg="black")
        self.readerBiletEntry.grid(row=4, column=2, pady=8)
        nameOfBook = Label(self.LibWrkWin, text="Название книги*", font="16pt")
        nameOfBook.grid(row = 6, column = 0, pady = 8)
        self.nameOfBookEntry = Entry(self.LibWrkWin, font="16pt", fg="black")
        self.nameOfBookEntry.grid(row = 6, column = 2, pady = 8)
        authorLabel = Label(self.LibWrkWin, text="Автор книги*", font="16pt")
        authorLabel.grid(row = 8, column = 0, pady = 8)
        self.authorEntry = Entry(self.LibWrkWin, font="16pt", fg="black")
        self.authorEntry.grid(row=8, column=2, pady=8)
        typeofbookLabel = Label(self.LibWrkWin, text="Тип книги*", font="16pt")
        typeofbookLabel.grid(row=10, column=0, pady=8)
        self.listboxTypesofbook = Listbox(self.LibWrkWin, height=2, width=26, selectmode=EXTENDED)
        list = ["Печатная", "Электронная"]
        for i in list:
            self.listboxTypesofbook.insert(END, i)
        self.listboxTypesofbook.grid(row=10, column=2, pady=8)
        addButton = Button(self.LibWrkWin,text="Выдать книгу", font="16pt",command = self.add)
        addButton.grid (row = 12, column = 2, pady = 36)
        showUsersButton = Button(self.LibWrkWin,text="Читатели", font="16pt",command = self.showUsers)
        showUsersButton.grid(row=12, column=1, pady=36)
        self.removeButton = Button(self.LibWrkWin,text="Принять книгу", font="16pt",command = self.remove)
        self.removeButton.grid(row=12, column=0, pady=36, padx = 36)
        infoLabel = Label(self.LibWrkWin,text="Поля, отмеченные * обязательны к заполнению")
        infoLabel.grid(row = 13, column = 0, pady=0)
        self.LibWrkWin.mainloop()

    def showUsers(self):
        self.cursor.execute("SELECT * FROM readers")
        result=self.cursor.fetchall()
        showUsrWin = Toplevel(self.LibWrkWin)
        tree = ttk.Treeview(showUsrWin,column = ("№ Читательского билета","Фамилия","Имя","Адрес","Номер и серия паспорта"))
        tree.heading("№ Читательского билета",text="awd",anchor = W)
        tree.pack()

        showUsrWin.mainloop()

    def add(self):
        surname = self.surNameEntry.get()
        name = self.nameEntry.get()
        readerBilet = self.readerBiletEntry.get()
        nameOfBook = self.nameOfBookEntry.get()
        authorOfBook = self.authorEntry.get()
        shouldShowErr = FALSE
        message = "Пожалуйста, введите"
        if (not surname):
            message += " фамилию"
            shouldShowErr = TRUE
        if (not name):
            message += " имя"
            shouldShowErr = TRUE
        if (not readerBilet):
            message += " номер читательского билета"
            shouldShowErr = TRUE
        if (not nameOfBook):
            message += " название книги"
            shouldShowErr = TRUE
        if (not authorOfBook):
            message += " автора книги"
            shouldShowErr = TRUE
        try:
            posLB = self.listboxTypesofbook.curselection()
            role = self.listboxTypesofbook.get(posLB)
        except:
            message += " тип книги"
        if shouldShowErr:
            answer = mb.showerror(parent=self.LibWrkWin, message=message)
        else:
            self.cursor.execute("SELECT * FROM readers  WHERE (surname=%s AND name=%s AND id =%s)",
                (passport,passport))
            phone = self.cursor.fetchone()
            if phone:
                answer = mb.showerror(parent=self.LibWrkWin, message="Читатель с таким паспортом уже зарегистрирован")
            else:
                self.cursor.execute("INSERT INTO readers (id, surname, name, patronymic, adress, passport) VALUES (%s, %s, %s, %s, %s, %s)",
                            (id, surname, name, patronymic, adress, passport))
                self.connect.commit()
                answer = mb.showinfo(parent=self.LibWrkWin,
                             message=f"Читатель успешно занесен в базу данных. Номер его читательского билета {id}")

    def remove(self):
        surname = self.surNameEntry.get()
        name = self.nameEntry.get()
        passport = self.passportEntry.get()
        shouldShowErr = FALSE
        message = "Пожалуйста, введите"
        if (not surname):
            message += " фамилию"
            shouldShowErr = TRUE
        if (not name):
            message += " имя"
            shouldShowErr = TRUE
        if (not passport):
            message += " номер телефона"
            shouldShowErr = TRUE
        if shouldShowErr:
            answer = mb.showerror(parent=self.LibWrkWin, message=message)
        else:
            self.cursor.execute("SELECT * FROM readers  WHERE (name=%s AND surname=%s AND passport=%s)",
                (name,surname,passport))
            user = self.cursor.fetchone()
            if user:
                self.cursor.execute("DELETE FROM readers WHERE (name=%s AND surname=%s AND passport=%s)",
                                    (name,surname,passport))
                self.connect.commit()
                answer = mb.showinfo(parent=self.LibWrkWin, message=f"Читатель №{user[0]} успешно удален из базы")
            else:
                answer = mb.showerror(parent=self.LibWrkWin, message="Такого читателя в базе данных нет, пожалуйста, проверьте введенные данные и попробуйте снова")