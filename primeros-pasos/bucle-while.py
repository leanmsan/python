pregunta = "Dime un numero y te dire si es par o no \r\n"

# concatenar dos string
pregunta += "(Escribe cerrar para salir) \r\n"

preguntar = True

#bucle while
while preguntar:
    numero = input(pregunta)
    if numero == "cerrar":
        preguntar = False
    else :
        numero = int(numero)
        if numero % 2 == 0:
            print(f"El numero {numero} es par")
        else:
            print(f"El numero {numero} no es par")
