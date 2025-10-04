public class Videojuego {
    String nombre;
    String plataforma;
    int cantidadJugadores;
    
    public Videojuego() {
        this.nombre = "";
        this.plataforma = "";
        this.cantidadJugadores = 0;
    }
    
    public Videojuego(String nombre) {
        this.nombre = nombre;
        this.plataforma = "Multiplataforma";
        this.cantidadJugadores = 1;
    }
    
    public Videojuego(String nombre, String plataforma, int jugadores) {
        this.nombre = nombre;
        this.plataforma = plataforma;
        this.cantidadJugadores = jugadores;
    }
    
    public void agregarJugadores() {
        this.cantidadJugadores++;
        System.out.println("Se agregó 1 jugador");
    }
    
    public void agregarJugadores(int cantidad) {
        this.cantidadJugadores += cantidad;
        System.out.println("Se agregaron " + cantidad + " jugadores");
    }
    
    public void mostrar() {
        System.out.println(nombre + " - " + plataforma + " - " + cantidadJugadores + " jugadores");
    }
    
    public static void main(String[] args) {
        Videojuego v1 = new Videojuego("FIFA", "PlayStation", 2);
        Videojuego v2 = new Videojuego("Mario Kart", "Nintendo", 4);
        
        Videojuego v3 = new Videojuego();
        Videojuego v4 = new Videojuego("Minecraft");
        
        v1.agregarJugadores();      
        v2.agregarJugadores(3);    
        
        v1.mostrar();
        v2.mostrar();
        v3.mostrar();
        v4.mostrar();
    }
}