class Restaurant:
    #Constructor
    def __init__(self, nombre, categoria, precio):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
    
    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}, Categoria {self.categoria}, Precio: {self.precio}")

#Instanciando una clase
restaurant = Restaurant("Locos por la Pizza", "Pizzeria", 50)

#Mostrando la informacion del restaurant
restaurant.mostrar_informacion()
