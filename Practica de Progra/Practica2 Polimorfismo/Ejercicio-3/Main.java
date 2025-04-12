public class Main {
    public static void main(String[] args) {
    
        Cocinero c1 = new Cocinero("Juan", 3000, 10, 15.5f);
        Mesero m1 = new Mesero("Maria", 2500, 5, 10.0f, 200.0f);
        Mesero m2 = new Mesero("Carlos", 2400, 8, 10.0f, 150.0f);
        Administrativo a1 = new Administrativo("Ana", 3500.5f, "Gerente");
        Administrativo a2 = new Administrativo("Luis", 2800.0f, "Contador");
    
        c1.mostrarSueldo();
        m1.mostrarSueldo();
        m2.mostrarSueldo();
        a1.mostrarSueldo();
        a2.mostrarSueldo();
        System.out.println("empleados que tienen un  sueldo mes = 2500:");

        c1.sueldoTotal(2500);
        m1.sueldoTotal(2500);
        m2.sueldoTotal(2500);
        a1.sueldoTotal(2500);
        a2.sueldoTotal(2500);
    }
}