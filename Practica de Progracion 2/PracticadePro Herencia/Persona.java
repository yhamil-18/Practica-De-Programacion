class Persona {
    String nombre;
    int edad;
    
    public Persona(String nombre, int edad) {
        this.nombre = nombre;
        this.edad = edad;
    }
}

class Estudiante extends Persona {
    String carrera;
    
    public Estudiante(String nombre, int edad, String carrera) {
        super(nombre, edad);
        this.carrera = carrera;
    }
}

class Docente extends Persona {
    String especialidad;
    
    public Docente(String nombre, int edad, String especialidad) {
        super(nombre, edad);
        this.especialidad = especialidad;
    }
}

class Curso {
    String nombre;
    String codigo;
    Docente docente;
    Estudiante[] estudiantes;
    
    public Curso(String nombre, String codigo) {
        this.nombre = nombre;
        this.codigo = codigo;
        this.docente = null;
        this.estudiantes = new Estudiante[0];
    }
}


public class Main {
    public static void main(String[] args) {
        Estudiante estudiante1 = new Estudiante("Ana", 20, "Ingeniería");
        Estudiante estudiante2 = new Estudiante("Carlos", 22, "Medicina");
        Docente docente1 = new Docente("Dr. Pérez", 45, "Matemáticas");
        
        Curso curso1 = new Curso("Matemáticas", "MAT101");
        curso1.docente = docente1;
        curso1.estudiantes = new Estudiante[]{estudiante1, estudiante2};
        
        System.out.println("Curso: " + curso1.nombre);
        System.out.println("Docente: " + curso1.docente.nombre);
        System.out.println("Estudiantes:");
        for (Estudiante est : curso1.estudiantes) {
            System.out.println("- " + est.nombre);
        }
    }
}