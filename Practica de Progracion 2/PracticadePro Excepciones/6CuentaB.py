class FondosInsuficientesException(Exception):
    pass

class MontoInvalidoException(Exception):
    pass

class CuentaBancaria:
    def __init__(self, numeroCuenta, titular, saldo):
        self.numeroCuenta = numeroCuenta
        self.titular = titular
        self.saldo = saldo
    
    def depositar(self, monto):
        if monto <= 0:
            raise MontoInvalidoException("El monto debe ser positivo")
        self.saldo += monto
    
    def retirar(self, monto):
        if monto > self.saldo:
            raise FondosInsuficientesException("Fondos insuficientes")
        self.saldo -= monto
    
    def mostrarInfo(self):
        print(f"Cuenta: {self.numeroCuenta}, Titular: {self.titular}, Saldo: ${self.saldo:.2f}")

cuenta = CuentaBancaria("12345", "Juan Pérez", 1000)
cuenta.mostrarInfo()

try:
    cuenta.depositar(500)
    print("Depósito exitoso")
    cuenta.mostrarInfo()
except MontoInvalidoException as e:
    print(f"Error en depósito: {e}")

try:
    cuenta.depositar(-100)
except MontoInvalidoException as e:
    print(f"Error en depósito: {e}")

try:
    cuenta.retirar(300)
    print("Retiro exitoso")
    cuenta.mostrarInfo()
except FondosInsuficientesException as e:
    print(f"Error en retiro: {e}")

try:
    cuenta.retirar(2000)
except FondosInsuficientesException as e:
    print(f"Error en retiro: {e}")