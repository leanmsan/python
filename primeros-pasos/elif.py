#Ejemplo con elif
ocupacion = "Desempleado"

if ocupacion == "Estudiante" :
    print("tienes un descuento del 50%")
elif ocupacion == "Jubilado" :
    print("Tienes un descuento del 75%")
elif ocupacion == "Desempleado" :
    print("Tienes un 10% de descuento")
else :
    print("Debes pagar el 100%")
