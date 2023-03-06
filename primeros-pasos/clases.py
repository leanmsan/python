class Restaurant:
    def agregar_restaurant(self, nombre):
        self.nombre = nombre

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")

#Instanciando una clase
restaurant = Restaurant()

#Agregando un restaurant
restaurant.agregar_restaurant("Locos por la Pizza")

#Mostrando la informacion del restaurant
restaurant.mostrar_informacion()

#Otra forma de mostrar la informacion
print(f"Nombre: {restaurant.nombre}")