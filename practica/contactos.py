#imports
import pymysql
#Fin imports

#class DataBase
class DataBase:
    #Constructor
    def __init__(self):
        self.connection = pymysql.connect(host = 'localhost', user = 'root', password = 'leanmsanroot', db = 'contactos')
        self.cursor = self.connection.cursor()
    #Fin constructor

    #Insert
    def insert(self, nombre, ntelefono, email):
        sql = "insert into contacto(nombre, ntelefono, email) values('{}', {} , '{}');".format(nombre, ntelefono, email)
        try: 
            self.cursor.execute(sql)
            self.connection.commit()
            return True
        except Exception as e:
            print(e)
            return False
    #Fin insert

    #Select all
    def select_all(self):
        sql = "select nombre, ntelefono, email from contacto;"
        try:
            self.cursor.execute(sql)
            contactos = self.cursor.fetchall()
            for contacto in contactos:
                print("------------------------------------------")
                print("Nombre:", contacto[0])
                print("Teléfono:", contacto[1])
                print("Email:", contacto[2])
                print("------------------------------------------")
        except Exception as e:
            print(e)
    #Fin select_all

    #Select nombre
    def select_search(self):
        sql = "select nombre from contacto;"
        try:
            self.cursor.execute(sql)
            contactos = self.cursor.fetchone()
            return contactos
        except Exception as e:
            print(e)

    #cerrar conexión
    def close(self):
        self.connection.close()
    #Fin close
#Fin class DataBase

#Instanciando la base de datos 
db = DataBase();

#class Contacto
class Contacto:
    #Constructor
    def __init__(self, Nombre, Telefono, Email):
        self.Nombre = Nombre
        self.Telefono = Telefono
        self.Email = Email
    #Fin Constructor
#Fin class Contacto

#App
def app():
    #Muestra el menú de opciones
    menu()
    #Ingreso de opciones
    preguntar = True
    while preguntar:
        opcion = input("Seleccione una opción \n")
        opcion = int(opcion)

        if opcion == 1:
            agregar_contacto()
            preguntar = False
        elif opcion == 2:
            editar_contacto()
            preguntar = False
        elif opcion == 3:
            mostrar_contactos()
            preguntar = False
        elif opcion == 4:
            buscar_contacto()
            preguntar = False
        elif opcion == 5:
            eliminar_contacto()
            preguntar = False
        elif opcion == 6:
            print("Cerrando...")
            preguntar = False
        else:
            print("Opción no válida, intente nuevamente")
#Fin app

#Menú
def menu():
    print("Menú")
    print(" 1- Agregar contacto \r\n 2- Editar contacto \n 3- Ver lista de contactos \n 4- Buscar contacto \n 5- Borrar contacto \n 6- Salir")
#Fin menú

#Agregar contacto
def agregar_contacto():
    print("Ingrese los datos del contacto")
    #Ingreso de los campos
    nombre_contacto = input("Nombre del contacto: \n")
    telefono_contacto = input("Número de teléfono: \n")
    email_contacto = input("Email del contacto: \n")
    contacto = Contacto(nombre_contacto, telefono_contacto, email_contacto)
    #Realiza el insert en la base de datos, si la función retorna true, se imprime el mensaje de exito, de lo contrario, vuelve a ejecutar esta función
    if db.insert(nombre_contacto, telefono_contacto, email_contacto):
        print("\n Contacto agregado correctamente \n")
        app()
    else:
        print("\n Se produció un error, por favor vuelva a intentar \n") 
        agregar_contacto()
#Fin agregar_contacto

#Editar contacto
def editar_contacto():
    print("Editar contacto")
    app()
#Fin editar_contacto

#Listar contactos
def mostrar_contactos():
    print("Lista de Contactos")
    db.select_all()
    print(db.select_all())
    app()
#Fin mostrar_contactos

#Buscar contactos
def buscar_contacto():
    cont = db.select_search()
    print(cont)
    app()
#FIn editar

#Eliminar contacto
def eliminar_contacto():
    print("Eliminar contacto")
    app()
#Fin eliminar_contacto

#Ejecución
app()
db.close()
#Fin Ejecución