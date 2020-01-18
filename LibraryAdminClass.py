from tkinter import *
from LibraryAdminWidnow import *


class LibraryAdmin:
    def __init__(self):
        root = tk.Tk()
        postgres = Postgres()
        conn = postgres.returnConnect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM readers")
        readers = cursor.fetchall()
        print(readers)
        table = Table(root, headings=(
        'Читательский билет №', 'Фамилия', 'Имя', 'Отчество', 'Студ. билет', 'Срок окончания билета'), rows=(readers))
        table.pack()
        delbutton = tk.Button(root, text="Удалить читателя", command=lambda: table.remove(conn, cursor), height=3,
                              width=15)
        delbutton.pack(side=tk.LEFT, padx=12, pady=20)
        addbutton = tk.Button(root, text="Добавить читателя", command=lambda: table.createAddWin(conn, cursor),
                              height=3, width=15)
        addbutton.pack(side=tk.RIGHT, padx=12, pady=20)
        root.mainloop()