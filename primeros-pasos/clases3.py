class Restaurant:
    #Constructor
    def __init__(self, nombre, categoria, precio):
        self.nombre = nombre
        self.categoria = categoria
        self.__precio = precio #Default: Public / _ = Protected / __ - Private
    
    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}, Categoria {self.categoria}, Precio: {self.__precio}")

    #Getters y Setters
    def get_precio(self):
        print(self.__precio)
    
    def set_precio(self, precio):
        self.__precio = precio


#Instanciando una clase
restaurant = Restaurant("Locos por la Pizza", "Pizzeria", 50)

#Mostrando la informacion del restaurant
restaurant.mostrar_informacion()

restaurant.get_precio()

restaurant.set_precio(250)

restaurant.get_precio()