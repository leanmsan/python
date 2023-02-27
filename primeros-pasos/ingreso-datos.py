#Ingreso de datos
nombre = input("dime tu nombre: \r\n") #\r\n es el salto de linea
print(f"Hola {nombre}")

#Ingreso de numeros 
edad = input("dime tu edad: \r\n")

#Convertir edad de string a int
edad = int(edad)

if edad >= 18:
    print("Ya puedes manejar")

#Mezclando con operadores
numero = input("Dime un numero y te dire si es par o no \r\n")
numero = int(numero)

if numero % 2 == 0 :
    print(f"El numero {numero} es par")
else :
    print(f"El numero {numero} no es par")
