class ProductoNoEncontradoException extends Exception {
    public ProductoNoEncontradoException(String mensaje) {
        super(mensaje);
    }
}

class StockInsuficienteException extends Exception {
    public StockInsuficienteException(String mensaje) {
        super(mensaje);
    }
}

class Producto {
    String codigo;
    String nombre;
    double precio;
    int stock;
    
    public Producto(String codigo, String nombre, double precio, int stock) {
        this.codigo = codigo;
        this.nombre = nombre;
        this.precio = precio;
        this.stock = stock;
    }
}

class Inventario {
    private java.util.ArrayList<Producto> productos;
    
    public Inventario() {
        productos = new java.util.ArrayList<>();
    }
    
    public void agregarProducto(Producto p) throws IllegalArgumentException {
        for (Producto producto : productos) {
            if (producto.codigo.equals(p.codigo)) {
                throw new IllegalArgumentException("Error: El código ya existe");
            }
        }
        
        if (p.precio < 0 || p.stock < 0) {
            throw new IllegalArgumentException("Error: Precio o stock no pueden ser negativos");
        }
        
        productos.add(p);
    }
    
    public Producto buscarProducto(String codigo) throws ProductoNoEncontradoException {
        for (Producto producto : productos) {
            if (producto.codigo.equals(codigo)) {
                return producto;
            }
        }
        throw new ProductoNoEncontradoException("Producto con código " + codigo + " no encontrado");
    }
    
    public void venderProducto(String codigo, int cantidad) throws ProductoNoEncontradoException, StockInsuficienteException {
        Producto producto = buscarProducto(codigo);
        
        if (producto.stock < cantidad) {
            throw new StockInsuficienteException("Stock insuficiente. Disponible: " + producto.stock + ", Solicitado: " + cantidad);
        }
        
        producto.stock -= cantidad;
    }
}

public class Main4 {
    public static void main(String[] args) {
        Inventario inventario = new Inventario();
        
        try {
            inventario.agregarProducto(new Producto("001", "Laptop", 1000, 10));
            inventario.agregarProducto(new Producto("002", "Mouse", 25, 50));
            System.out.println("Productos agregados correctamente");
        } catch (IllegalArgumentException e) {
            System.out.println(e.getMessage());
        }
        
        try {
            Producto producto = inventario.buscarProducto("001");
            System.out.println("Producto encontrado: " + producto.nombre);
        } catch (ProductoNoEncontradoException e) {
            System.out.println(e.getMessage());
        }
        
        try {
            inventario.venderProducto("001", 3);
            System.out.println("Venta realizada correctamente");
        } catch (ProductoNoEncontradoException | StockInsuficienteException e) {
            System.out.println(e.getMessage());
        }
        
        try {
            inventario.venderProducto("001", 20);
        } catch (ProductoNoEncontradoException | StockInsuficienteException e) {
            System.out.println(e.getMessage());
        }
        
        try {
            inventario.buscarProducto("999");
        } catch (ProductoNoEncontradoException e) {
            System.out.println(e.getMessage());
        }
    }
}