#Creando un diccionario

cancion = {
    "Artista" : "Beethoven", #llave y valor 
    "Cancion" : "9th Symphony"
}

#Imprimiendo un diccionario
print(cancion)

#Acceder a un elemento del diccionario
print(cancion["Artista"])

#Mezclando con un string 
print(f"Estoy escuchando {cancion['Artista']}")

#Agregar nuevos elementos 
cancion["cancion"] = "5th Symphony"
print(cancion)

#Eliminando un valor 
del cancion["cancion"]
print(cancion)

