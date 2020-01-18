from tkinter import *
from LibraryWorkerWindow import *


class LibraryWorker:
    def __init__(self):
        root = tk.Tk()
        postgres = Postgres()
        conn = postgres.returnConnect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM readers")
        readers = cursor.fetchall()
        print(readers)
        table = Table(root, headings=(
        'Читательский билет №', 'Фамилия', 'Имя', 'Отчество', 'Студ. билет', 'Срок окончания билета','Нарушитель'), rows=(readers))
        table.pack()
        delbutton = tk.Button(root, text="Удалить пользователя", command=lambda: table.remove(conn, cursor), height=3,
                              width=20)
        delbutton.pack(side=tk.LEFT, padx=12, pady=20)
        addbutton = tk.Button(root, text="Выдать пользователю книгу", command=lambda: table.createBooksWin(),
                              height=3, width=20)
        addbutton.pack(side=tk.RIGHT, padx=12, pady=20)
        showreaderbooksbuttion = tk.Button(root, text="Посмотреть книги читателя", command=lambda: table.createReaderBooksShowWin(),
                              height=3, width=20)
        showreaderbooksbuttion.pack(side=tk.RIGHT, padx=12, pady=20)

        root.mainloop()