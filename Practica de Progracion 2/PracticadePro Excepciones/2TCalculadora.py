class NumeroInvalidoException(Exception):
    pass

class Calculadora:
    
    @staticmethod
    def sumar(a, b):
        return a + b
    
    @staticmethod
    def restar(a, b):
        return a - b
    
    @staticmethod
    def multiplicar(a, b):
        return a * b
    
    @staticmethod
    def dividir(a, b):
        if b == 0:
            raise ArithmeticError("Error: No se puede dividir por cero")
        return a / b
    
    @staticmethod
    def convertir_a_entero(texto):
        try:
            return int(texto)
        except ValueError:
            raise NumeroInvalidoException(f"Error: '{texto}' no es un número válido")

if __name__ == "__main__":
    print("Operaciones normales:")
    print(f"5 + 3 = {Calculadora.sumar(5, 3)}")
    print(f"10 - 4 = {Calculadora.restar(10, 4)}")
    print(f"6 * 7 = {Calculadora.multiplicar(6, 7)}")
    print(f"15 / 3 = {Calculadora.dividir(15, 3)}")
    
    print("\nPruebas con errores:")
    
    try:
        Calculadora.dividir(10, 0)
    except ArithmeticError as e:
        print(e)
    
    try:
        Calculadora.convertir_a_entero("abc")
    except NumeroInvalidoException as e:
        print(e)
    
    try:
        numero = Calculadora.convertir_a_entero("123")
        print(f"Número convertido: {numero}")
    except NumeroInvalidoException as e:
        print(e)