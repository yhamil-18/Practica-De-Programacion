public class Bus {
    private int total_asientos;
    private int pasajeros;
    private double dinero;
    private double precio;

    public Bus(int total_asientos) {
        this.total_asientos = total_asientos;
        this.pasajeros = 0;
        this.dinero = 0;
        this.precio = 1.50;
    }

    public void subirPasajero(int cantidad) {
        if (this.pasajeros + cantidad <= this.total_asientos) {
            this.pasajeros += cantidad;
            System.out.println("Subieron " + cantidad + " pasajeros");
        } else {
            System.out.println("No caben más pasajeros");
        }
    }

    public void Cobrar() {
        double total = this.pasajeros * this.precio;
        this.dinero += total;
        System.out.println("Se cobró " + total + " bs por " + this.pasajeros + " pasajeros");
    }

    public int AsientosDisponibles() {
        int disponibles = this.total_asientos - this.pasajeros;
        System.out.println("Asientos disponibles: " + disponibles);
        return disponibles;
    }
    
    public static void main(String[] args) {
        Bus bus1 = new Bus(40);  
        bus1.subirPasajero(30);
        bus1.AsientosDisponibles();
        bus1.Cobrar();  

        System.out.println("//////////////////////////");  

        Bus bus2 = new Bus(50);  
        bus2.subirPasajero(55);  
        bus2.AsientosDisponibles();
        bus2.Cobrar();
    }
}