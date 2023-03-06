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

#Creando una clase hijo
class Hotel(Restaurant):
    def __init__(self, nombre, categoria, precio):
        super().__init__(nombre, categoria, precio)

hotel = Hotel("Hotel POO", "5 Estrellas", 250)
hotel.mostrar_informacion()