#declaracion de una lista
meses = ["Enero", "Febrero", "Marzo"];

print(meses[0])

lenguajes = ["Python", "Java", "C++"];

print(lenguajes)

lenguajes.sort()

print(lenguajes)

aprendiento = f"Estoy aprendiendo {lenguajes[2]}"

print(aprendiento)

#Modificando un arreglo 
lenguajes[1] = "JavaScript"

print(lenguajes)

#Agregando elementos
lenguajes.append("R")
print(lenguajes)

#eliminar un elemento
del lenguajes[3]
print(lenguajes)

#eliminar el ultimo elemento
lenguajes.pop()
print(lenguajes)

#otra forma de eliminar un elemento
lenguajes.pop(0)
print(lenguajes)

#eliminar por nombre
lenguajes.remove("JavaScript")
print(lenguajes)