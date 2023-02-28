#Declarando el diccionario
playlist = {} #Diccionario vacio
playlist["Canciones"] = [] #Lista vacia de canciones

#Funcion principal
def app():
    agregar_playlist = True
    while agregar_playlist:
        nombre_playlist = input("Ingrese el nombre de la playlist \r\n")

        if nombre_playlist:
            playlist["nombre"] = nombre_playlist
            agregar_playlist = False
            print(playlist)
            agregar_canciones()

#Funcion para agregar canciones
def agregar_canciones():
    agregar_cancion = True
    while agregar_cancion:
        #Preguntando que cancion quiere ingresar
        nombre_playlist = playlist["nombre"]
        pregunta = f"\r\nAgrega canciones a {nombre_playlist}: \r\n"
        pregunta += "Escribe 'X' para dejar de agregar canciones \r\n"
        
        cancion = input(pregunta)
        if cancion == "X":
            agregar_cancion = False
            mostrar_resumen()
        else :
            playlist["Canciones"].append(cancion)
            print(playlist)

#Funcion que muestra un resumen de la playlist
def mostrar_resumen():
    nombre_playlist = playlist["nombre"]
    print(f"Playlist: {nombre_playlist}\r\n")
    print("Canciones:")
    for cancion in playlist["Canciones"]:
        print(cancion)

#Ejecucion de la funcion principal
app()