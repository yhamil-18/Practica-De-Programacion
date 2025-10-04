class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        
    def vender(self, cantidad):
        self.stock -= cantidad
        print(f"Vendidos {cantidad} unidades de {self.nombre}. Stock restante: {self.stock}")
        
    def reabastecer(self, cantidad):
        self.stock += cantidad
        print(f"Reabastecidos {cantidad} unidades de {self.nombre}. Stock actual: {self.stock}")

prod1 = Producto("Camiseta", 20.0, 100)
prod1.vender(5)
prod1.reabastecer(10)
prod2 = Producto("Pantalón", 40.0, 50)
prod2.vender(3)
prod2.reabastecer(5)