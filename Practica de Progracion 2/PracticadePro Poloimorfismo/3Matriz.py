class Matriz:
    def __init__(self, datos=None):
        if datos is None:
            self.matriz = [[1.0 if i == j else 0.0 for j in range(10)] for i in range(10)]
        else:
            self.matriz = datos
    
    def sumar(self, otra):
        resultado = []
        for i in range(len(self.matriz)):
            fila = []
            for j in range(len(self.matriz[0])):
                fila.append(self.matriz[i][j] + otra.matriz[i][j])
            resultado.append(fila)
        return Matriz(resultado)
    
    def restar(self, otra):
        resultado = []
        for i in range(len(self.matriz)):
            fila = []
            for j in range(len(self.matriz[0])):
                fila.append(self.matriz[i][j] - otra.matriz[i][j])
            resultado.append(fila)
        return Matriz(resultado)
    
    def igual(self, otra):
        return self.matriz == otra.matriz
    
    def mostrar(self):
        for fila in self.matriz:
            print(fila)

m1 = Matriz()
print("Matriz identidad:")
m1.mostrar()

datos = [[1.0, 2.0], [3.0, 4.0]]
m2 = Matriz(datos)
print("\nMatriz personalizada:")
m2.mostrar()

m3 = m2.sumar(m2)
print("\nSuma m2 + m2:")
m3.mostrar()

print(f"\n¿m1 es igual a m2? {m1.igual(m2)}")