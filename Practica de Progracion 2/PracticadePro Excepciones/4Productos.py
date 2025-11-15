class ProductoNoEncontradoException(Exception):
    pass

class StockInsuficienteException(Exception):
    pass

class Producto:
    def __init__(self, codigo, nombre, precio, stock):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

class Inventario:
    def __init__(self):
        self.productos = []
    
    def agregarProducto(self, p):
        for producto in self.productos:
            if producto.codigo == p.codigo:
                raise ValueError("Error: El código ya existe")
        
        if p.precio < 0 or p.stock < 0:
            raise ValueError("Error: Precio o stock no pueden ser negativos")
        
        self.productos.append(p)
    
    def buscarProducto(self, codigo):
        for producto in self.productos:
            if producto.codigo == codigo:
                return producto
        raise ProductoNoEncontradoException(f"Producto con código {codigo} no encontrado")
    
    def venderProducto(self, codigo, cantidad):
        producto = self.buscarProducto(codigo)
        
        if producto.stock < cantidad:
            raise StockInsuficienteException(f"Stock insuficiente. Disponible: {producto.stock}, Solicitado: {cantidad}")
        
        producto.stock -= cantidad


inventario = Inventario()
    
try:
    inventario.agregarProducto(Producto("001", "Laptop", 1000, 10))
    inventario.agregarProducto(Producto("002", "Mouse", 25, 50))
    print("Productos agregados correctamente")
except ValueError as e:
    print(e)
    
try:
    producto = inventario.buscarProducto("001")
    print(f"Producto encontrado: {producto.nombre}")
except ProductoNoEncontradoException as e:
    print(e)
    
try:
    inventario.venderProducto("001", 3)
    print("Venta realizada correctamente")
except (ProductoNoEncontradoException, StockInsuficienteException) as e:
    print(e)
    
try:
    inventario.venderProducto("001", 20)
except StockInsuficienteException as e:
    print(e)

try:
    inventario.buscarProducto("999")
except ProductoNoEncontradoException as e:
    print(e)