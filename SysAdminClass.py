from tkinter import *
from SysAdminWindow import *


class SysAdmin:
    def __init__(self):
        root = tk.Tk()
        postgres = Postgres()
        conn = postgres.returnConnect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
        print(users)
        table = Table(root, headings=(
        'ID', 'Логин', 'Пароль', 'Уровень привелегий',), rows=(users))
        table.pack()
        delbutton = tk.Button(root, text="Удалить пользователя", command=lambda: table.remove(conn, cursor), height=3,
                              width=20)
        delbutton.pack(side=tk.LEFT, padx=12, pady=20)
        addbutton = tk.Button(root, text="Добавить пользователя", command=lambda: table.createAddWin(conn, cursor),
                              height=3, width=20)
        addbutton.pack(side=tk.RIGHT, padx=12, pady=20)
        root.mainloop()