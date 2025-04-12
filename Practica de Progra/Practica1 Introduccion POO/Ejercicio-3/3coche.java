class Coche {
    public String marca;
    public String modelo;
    public int velocidad;

    public Coche(String marca, String modelo) {
        this.marca = marca;
        this.modelo = modelo;
        velocidad = 0;
    }

    public void acelerar() {
        velocidad = velocidad + 10;
        System.out.println("la marca "+marca + " con " + modelo + " acelero y su velocidad es ahora : " + velocidad);
    }

    public void frenar() {
        if (velocidad <= 5) {
            velocidad = 0;
        } else {
            velocidad = velocidad - 5;
        }
        System.out.println(" la marca "+marca+ " con modelo " + modelo + " freno y su velocidad es ahora : " + velocidad);
    }
}


class Main {
    public static void main(String[] args) {

        Coche coche1 = new Coche("Toyota", "Corolla");
        Coche coche2 = new Coche("Honda", "Civic");
        

        System.out.println("Velocidad inicial de " + coche1.marca + " " + coche1.modelo + ": " + coche1.velocidad);
        System.out.println("Velocidad inicial de " + coche2.marca + " " + coche2.modelo + ": " + coche2.velocidad);
        

        coche1.acelerar();
        coche2.acelerar();
        
        coche1.frenar();
        coche2.frenar();
    }
}