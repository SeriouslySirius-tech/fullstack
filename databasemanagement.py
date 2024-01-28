import pymysql
import os

pas=os.getenv("db_pswd")

class DBManager:
    def __init__(self):
        self.conn = pymysql.connect(host="localhost", user="root", password=pas, database="flashfleet")
        self.cursor = self.conn.cursor()

    def say_hello(self):
        print("Hello There")
    def add_user(self, name, uname, pswd):
        try:
            self.cursor.execute(f'INSERT INTO flashfleet.users VALUES ("{name}", "{uname}", "{pswd}")')
        except Exception:
            return "Cannot add as username already exists"
        self.conn.commit()
    def show_users(self):
        self.cursor.execute("SELECT * from users")
        print(self.cursor.fetchall())

