def app():
    #Creando un archivo
    archivo = open("archivo.txt", "w")

    #Generar numeros en archivos
    for i in range(0, 20):
        archivo.write("Esta es la linea " + str(i) + "\r\n")

    #Cerrando un archivo
    archivo.close()

app()