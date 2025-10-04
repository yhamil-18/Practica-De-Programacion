public class Matriz {
    private double[][] matriz;
    
    public Matriz() {
        this.matriz = new double[][]{{1, 0}, {0, 1}};
    }
    
    public Matriz(double[][] datos) {
        this.matriz = datos;
    }
    
    public Matriz sumar(Matriz otra) {
        double[][] resultado = new double[matriz.length][matriz[0].length];
        for (int i = 0; i < matriz.length; i++) {
            for (int j = 0; j < matriz[0].length; j++) {
                resultado[i][j] = matriz[i][j] + otra.matriz[i][j];
            }
        }
        return new Matriz(resultado);
    }
    
    public boolean igual(Matriz otra) {
        if (matriz.length != otra.matriz.length) return false;
        for (int i = 0; i < matriz.length; i++) {
            for (int j = 0; j < matriz[0].length; j++) {
                if (matriz[i][j] != otra.matriz[i][j]) {
                    return false;
                }
            }
        }
        return true;
    }
    
    public void mostrar() {
        for (int i = 0; i < matriz.length; i++) {
            for (int j = 0; j < matriz[0].length; j++) {
                System.out.print(matriz[i][j] + " ");
            }
            System.out.println();
        }
    }
    
    public static void main(String[] args) {
        Matriz m1 = new Matriz();
        System.out.println("Matriz identidad:");
        m1.mostrar();
        
        Matriz m2 = new Matriz(new double[][]{{1, 2}, {3, 4}});
        System.out.println("\nMatriz personalizada:");
        m2.mostrar();
        
        Matriz m3 = m2.sumar(m2);
        System.out.println("\nSuma m2 + m2:");
        m3.mostrar();
        
        System.out.println("\n¿m1 es igual a m2? " + m1.igual(m2));
    }
}