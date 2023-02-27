#Iniciando un diccionario vacio 
jugador = {}
print(jugador)

#Se une un jugador
jugador["Nombre"] = "Juan"
jugador["Puntaje"] = 0
print(jugador)

#Incrementando el puntaje
jugador["Puntaje"] = 100
print(jugador)

#Acceder a un valor
print(jugador.get("Puntaje"))

#Iterar en el diccionario
for llave, valor in jugador.items() :
    print(llave, valor)

#Eliminar elemento 
del jugador["Nombre"]
del jugador["Puntaje"]
print(jugador)
