class Animal {
    String nombre;
    int edad;
    
    public Animal(String n, int e) {
        nombre = n;
        edad = e;
    }
    
    void desplazarse() {
        System.out.println(nombre + " se está desplazando...");
    }
}

class Leon extends Animal {
    public Leon(String n, int e) {
        super(n, e);
    }
    
    void desplazarse() {
        System.out.println(nombre + " está caminando poderosamente");
    }
}

class Pinguino extends Animal {
    public Pinguino(String n, int e) {
        super(n, e);
    }
    
    void desplazarse() {
        System.out.println(nombre + " está nadando en el agua fría");
    }
}

class Canguro extends Animal {
    public Canguro(String n, int e) {
        super(n, e);
    }
    
    void desplazarse() {
        System.out.println(nombre + " está saltando con sus patas fuertes");
    }
}

public class Main {
    public static void main(String[] args) {
        Leon leon = new Leon("Simba", 5);
        Pinguino pinguino = new Pinguino("Pingu", 3);
        Canguro canguro = new Canguro("Kanga", 4);
        
        leon.desplazarse();
        pinguino.desplazarse();
        canguro.desplazarse();
    }
}