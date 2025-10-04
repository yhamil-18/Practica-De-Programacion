public class Producto {
    private String nombre;
    private double precio;
    private int stock;
    

    public Producto(String nombre, double precio, int stock) {
        this.nombre = nombre;
        this.precio = precio;
        this.stock = stock;
    }

    public void vender(int cantidad) {
        this.stock -= cantidad;
        System.out.println("Vendidos " + cantidad + " unidades de " + this.nombre + ". Stock restante: " + this.stock);
    }
    

    public void reabastecer(int cantidad) {
        this.stock += cantidad;
        System.out.println("Reabastecidos " + cantidad + " unidades de " + this.nombre + ". Stock actual: " + this.stock);
    }
    

    public static void main(String[] args) {
        Producto prod1 = new Producto("Camiseta", 20.0, 100);
        prod1.vender(5);
        prod1.reabastecer(10);
        
        Producto prod2 = new Producto("Pantalón", 40.0, 50);
        prod2.vender(3);
        prod2.reabastecer(5);
    }
}