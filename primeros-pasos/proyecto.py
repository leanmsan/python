import os 

CARPETA = "Contactos/" #Constante
EXTENSION = ".txt" #Extension de archivos

#Clase Contactos
class Contacto:
    def __init__(self, Nombre, Telefono, Categoria):
        self.Nombre = Nombre
        self.Teleforno = Telefono
        self.Categoria = Categoria
#Fin clase Contacto

#Main
def app():
    #Revisa si la carpeta existe
    crear_directorio()
    #Muestra el menu
    menu()
    #Ingreso de opcion
    preguntar = True
    while preguntar:
        opcion = input("Seleccione una opcion: \r\n")
        opcion = int(opcion)

        if opcion == 1:
            agregar_contacto()
            preguntar = False
        elif opcion == 2:
            editar_contacto()
            preguntar = False
        elif opcion == 3:
            print("Lista de contactos")
            preguntar = False
        elif opcion == 4:
            print("Buscar contacto")
            preguntar = False
        elif opcion == 5:
            print("Borrar contacto")
            preguntar = False
        elif opcion == 6:
            print("Cerrando...")
            preguntar = False
        else :
            print("Opcion no valida, intente nuevamente")
#Fin Main

#Verifica si existe un contacto
def existe_contacto(nombre):
    return os.path.isfile(CARPETA + nombre + EXTENSION)
#Fin existe_contacto

#Crea un contacto 
def agregar_contacto():
    print("Ingrese los datos del contacto")
    #Ingreso de los campos
    nombre_contacto = input("Nombre del contacto: \r\n")
    #Validando si existe el contacto
    existe = existe_contacto(nombre_contacto)
    if not existe:
        telefono_contacto = input("Numero de telefono: \r\n")
        categoria_contacto = input("Categoria de contacto: \r\n")

        #Instanciando la clase contacto
        contacto = Contacto(nombre_contacto, telefono_contacto, categoria_contacto)

        #Escribiendo en el archivo
        with open(CARPETA + nombre_contacto + EXTENSION, "w") as archivo:
            archivo.write("Nombre:" + nombre_contacto + "\r\n")
            archivo.write("Telefono:" + telefono_contacto + "\r\n")
            archivo.write("Categoria:" + categoria_contacto + "\r\n")
        #Mensaje de registro exitoso
        print("\r\n Contacto agregado correctamente \r\n")
        app()
    else:
        print("\r\n Ya existe un contacto con el mismo nombre")
        print(" Intente nuevamente \r\n")
        agregar_contacto()
#Fin agregar_contacto

#Editar un contacto
def editar_contacto():
    print("Ingrese el nombre del contacto")
    nombre_anterior = input("Nombre del contacto que desea editar: \r\n")
    #Validando si existe el contacto
    existe = existe_contacto(nombre_anterior)
    if existe:
        nombre_contacto = input("Nuevo nombre del contacto: \r\n")
        telefono_contacto = input("Nuevo numero de telefono: \r\n")
        categoria_contacto = input("Nueva categoria de contacto: \r\n")
        contacto = Contacto(nombre_contacto, telefono_contacto, categoria_contacto)
        with open(CARPETA + nombre_anterior + EXTENSION, "w") as archivo:
            archivo.write("Nombre:" + nombre_contacto + "\r\n")
            archivo.write("Telefono:" + telefono_contacto + "\r\n")
            archivo.write("Categoria:" + categoria_contacto + "\r\n")
        os.rename(CARPETA + nombre_anterior + EXTENSION, CARPETA + nombre_contacto + EXTENSION)
    else: 
        print("Ese contacto no existe")
#Fin editar_contacto

#Revisa y crea la carpeta
def crear_directorio():
    if not os.path.exists(CARPETA):
        os.makedirs(CARPETA) #Crea la carpeta
#Fin crear_directorio

#Menu de opciones
def menu():
    print("Menú")
    print(" 1- Agregar contacto \r\n 2- Editar contacto \r\n 3- Ver lista de contactos \r\n 4- Buscar contacto \r\n 5- Borrar contacto \r\n 6- Salir")
#Fin menu

app()