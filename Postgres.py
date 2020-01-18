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
        self.connect = psycopg2.connect(dbname=db, user=user, password=password, host=host)
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

