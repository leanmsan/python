class Restaurant:
    #Constructor
    def __init__(self, nombre, categoria, precio):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio #Default: Public / _ = Protected / __ - Private
    
    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}, Categoria {self.categoria}, Precio: {self.precio}")

    #Getters y Setters
    def get_precio(self):
        print(self.precio)
    
    def set_precio(self, precio):
        self.precio = precio

#Creando una clase hijo
class Hotel(Restaurant):
    def __init__(self, nombre, categoria, precio, pileta):
        super().__init__(nombre, categoria, precio)
        self.pileta = pileta

    #Metodo de la clase hotel
    def get_pileta(self):
        return self.pileta
    
    #Reescribiendo un metodo
    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}, Categoria {self.categoria}, Precio: {self.precio}, Pileta {self.pileta}")

hotel = Hotel("Hotel POO", "5 Estrellas", 250, "Si")
hotel.mostrar_informacion()

pileta = hotel.get_pileta()
print(pileta)