import pymysql

class DataBase:
    def __init__(self):
        self.connection = pymysql.connect(host = "localhost", user = "root", password = "leanmsanroot", db = "prueba_python")
        self.cursor = self.connection.cursor()

    def select_user(self, id):
        sql = "select id, username, email from users WHERE id = {}".format(id)

        try:
            self.cursor.execute(sql)
            user = self.cursor.fetchone()
            print("Id:", user[0])
            print("Username:", user[1])
            print("Email:", user[2])
        except Exception as e:
            print(e)

    def select_all_users(self):
        sql = "select id, username, email from users"

        try:
            self.cursor.execute(sql)
            user = self.cursor.fetchall()

            for usr in user:
                print("Id:", usr[0])
                print("Username:", usr[1])
                print("Email:", usr[2])
                print("---------------------------------")
        except Exception as e:
            print(e)
    
    def update_username(self, id, username):
        sql = "UPDATE users SET username = '{}' WHERE id = {}".format(username, id)

        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            print(e)

    def close(self):
        self.connection.close()
#Fin class DataBase

def app():
    database = DataBase()

    database.select_user(1)
    database.update_username(1, "Leandro")
    database.select_user(1)
    print("-----------------------------------------------")
    database.select_all_users()
    print("-----------------------------------------------")
#Fin app

app()