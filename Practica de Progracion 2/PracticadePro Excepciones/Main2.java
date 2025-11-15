// Ejercicio 2 Calculadora con Excepciones

class NumeroInvalidoException extends Exception {
    public NumeroInvalidoException(String mensaje) {
        super(mensaje);
    }
}

class Calculadora {
    
    public static int sumar(int a, int b) {
        return a + b;
    }
    
    public static int restar(int a, int b) {
        return a - b;
    }
    
    public static int multiplicar(int a, int b) {
        return a * b;
    }
    
    public static double dividir(int a, int b) throws ArithmeticException {
        if (b == 0) {
            throw new ArithmeticException("Error: No se puede dividir por cero");
        }
        return (double) a / b;
    }
    
    public static int convertirAEntero(String texto) throws NumeroInvalidoException {
        try {
            return Integer.parseInt(texto);
        } catch (NumberFormatException e) {
            throw new NumeroInvalidoException("Error: '" + texto + "' no es un número válido");
        }
    }
}

public class Main2 {
    public static void main(String[] args) {
        System.out.println("Operaciones normales:");
        System.out.println("5 + 3 = " + Calculadora.sumar(5, 3));
        System.out.println("10 - 4 = " + Calculadora.restar(10, 4));
        System.out.println("6 * 7 = " + Calculadora.multiplicar(6, 7));
        
        try {
            System.out.println("15 / 3 = " + Calculadora.dividir(15, 3));
        } catch (ArithmeticException e) {
            System.out.println(e.getMessage());
        }
        
        System.out.println("\nPruebas con errores:");
        
        try {
            Calculadora.dividir(10, 0);
        } catch (ArithmeticException e) {
            System.out.println(e.getMessage());
        }
        
        try {
            Calculadora.convertirAEntero("abc");
        } catch (NumeroInvalidoException e) {
            System.out.println(e.getMessage());
        }
        
        try {
            int numero = Calculadora.convertirAEntero("123");
            System.out.println("Número convertido: " + numero);
        } catch (NumeroInvalidoException e) {
            System.out.println(e.getMessage());
        }
    }
}