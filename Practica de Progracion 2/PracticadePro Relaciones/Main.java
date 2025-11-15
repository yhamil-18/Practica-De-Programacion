import java.util.ArrayList;
import java.util.List;

// Clase Departamento Ejecicio 2

class Departamento {
    private String nombre;
    private String area;
    private List<Empleado> empleados;
    
    public Departamento(String nombre, String area) {
        this.nombre = nombre;
        this.area = area;
        this.empleados = new ArrayList<>();
    }
    
    public void agregarEmpleado(Empleado empleado) {
        this.empleados.add(empleado);
    }
    
    public void mostrarEmpleados() {
        System.out.println("\n--- Empleados del Departamento " + this.nombre + " ---");
        if (this.empleados.isEmpty()) {
            System.out.println("No hay empleados en este departamento.");
        } else {
            for (Empleado empleado : this.empleados) {
                empleado.mostrarInfo();
            }
        }
    }
    
    public void cambiarSalario(double porcentaje) {
        for (Empleado empleado : this.empleados) {
            double nuevoSueldo = empleado.getSueldo() * (1 + porcentaje / 100);
            empleado.setSueldo(nuevoSueldo);
        }
        System.out.printf("Salarios cambiados en %.1f%% para el departamento %s\n", 
                         porcentaje, this.nombre);
    }
    
    public void moverEmpleados(Departamento otroDepartamento) {
        otroDepartamento.empleados.addAll(this.empleados);
        System.out.printf("Se movieron %d empleados de %s a %s\n", 
                         this.empleados.size(), this.nombre, otroDepartamento.nombre);
        this.empleados.clear();
    }
    
    public String getNombre() { return nombre; }
    public String getArea() { return area; }
    public List<Empleado> getEmpleados() { return empleados; }
}

class Empleado {
    private String nombre;
    private String cargo;
    private double sueldo;
    
    public Empleado(String nombre, String cargo, double sueldo) {
        this.nombre = nombre;
        this.cargo = cargo;
        this.sueldo = sueldo;
    }
    
    public void mostrarInfo() {
        System.out.printf("Nombre: %s, Cargo: %s, Sueldo: $%,.2f\n", 
                         nombre, cargo, sueldo);
    }
    

    public String getNombre() { return nombre; }
    public String getCargo() { return cargo; }
    public double getSueldo() { return sueldo; }
    public void setSueldo(double sueldo) { this.sueldo = sueldo; }
}

public class Main {
    public static void main(String[] args) {
        Departamento departamento1 = new Departamento("Ventas", "Comercial");
        Departamento departamento2 = new Departamento("Recursos Humanos", "Administrativo");

        Empleado[] empleadosDep1 = {
            new Empleado("Ana García", "Gerente de Ventas", 50000),
            new Empleado("Carlos López", "Ejecutivo de Ventas", 35000),
            new Empleado("María Rodríguez", "Asistente de Ventas", 30000),
            new Empleado("Pedro Martínez", "Analista Comercial", 40000),
            new Empleado("Laura Sánchez", "Coordinadora", 32000)
        };
        
        for (Empleado empleado : empleadosDep1) {
            departamento1.agregarEmpleado(empleado);
        }
        
        System.out.println("=== ESTADO INICIAL ===");
        departamento1.mostrarEmpleados();
        departamento2.mostrarEmpleados();

        departamento1.cambiarSalario(10);
        System.out.println("\n=== VERIFICACIÓN DE EMPLEADOS ===");
        boolean empleadosEnAmbos = false;
        for (Empleado empleado : departamento1.getEmpleados()) {
            if (departamento2.getEmpleados().contains(empleado)) {
                empleadosEnAmbos = true;
                System.out.println("El empleado " + empleado.getNombre() + " está en ambos departamentos");
                break;
            }
        }
        
        if (!empleadosEnAmbos) {
            System.out.println("No hay empleados del departamento 1 en el departamento 2");
        }
        
        System.out.println("\n=== MOVIENDO EMPLEADOS ===");
        departamento1.moverEmpleados(departamento2);
        
        System.out.println("\n=== ESTADO FINAL ===");
        departamento1.mostrarEmpleados();
        departamento2.mostrarEmpleados();
    }
}