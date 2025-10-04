class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def get_nombre(self):
        return self.nombre
    
    def get_precio(self):
        return self.precio
    
    def set_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre
    
    def set_precio(self, nuevo_precio):
        self.precio = nuevo_precio
    
    def mostrar(self):
        print(f"Producto: {self.nombre} - ${self.precio}")

class Pedido:
    def __init__(self, numero, estado):
        self.numero = numero
        self.estado = estado
    
    def get_numero(self):
        return self.numero
    
    def get_estado(self):
        return self.estado
    
    def set_numero(self, nuevo_numero):
        self.numero = nuevo_numero
    
    def set_estado(self, nuevo_estado):
        self.estado = nuevo_estado
    
    def mostrar(self):
        print(f"Pedido #{self.numero} - {self.estado}")# Crear objetos
cafe = Producto("Café Latte", 15.50)
pedido = Pedido(101, "registrado")


print("GETTERS:")
print(cafe.get_nombre())    
print(cafe.get_precio())    
print(pedido.get_numero())  
print(pedido.get_estado())  


print("\nSETTERS:")
cafe.set_precio(18.00)
pedido.set_estado("preparado")


cafe.mostrar()     
pedido.mostrar()  