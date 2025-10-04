class Administrativo:
    def __init__(self, cargo, sueldoHora):
        self.cargo = cargo
        self.sueldoHora = sueldoHora
    
    def SueldoTotal(self, horas=160):  
        return self.sueldoHora * horas

class Chef:
    def __init__(self, tipo, sueldoHora, horaExtra=0):
        self.tipo = tipo
        self.sueldoHora = sueldoHora
        self.horaExtra = horaExtra
    
    def SueldoTotal(self, horas=160):
        return (self.sueldoHora * horas) + (self.sueldoHora * 1.5 * self.horaExtra)

class Mesero:
    def __init__(self, sueldoHora, horaExtra=0, propina=0):
        self.sueldoHora = sueldoHora
        self.horaExtra = horaExtra
        self.propina = propina
    
    def SueldoTotal(self, horas=160):
        return (self.sueldoHora * horas) + (self.sueldoHora * 1.5 * self.horaExtra) + self.propina

chef1 = Chef("Pastelero", 25, 10)
mesero1 = Mesero(15, 8, 200)
mesero2 = Mesero(12, 12, 350)
admin1 = Administrativo("Gerente", 30)
admin2 = Administrativo("Contador", 20)

empleados = [chef1, mesero1, mesero2, admin1, admin2]

print("=== SUELDOS TOTALES ===")
for emp in empleados:
    sueldo = emp.SueldoTotal()
    tipo = type(emp).__name__
    print(f"{tipo}: ${sueldo:.2f}")

def buscar_sueldo(X):
    print(f"\n=== EMPLEADOS CON SUELDO ${X} ===")
    encontrados = False
    for emp in empleados:
        if emp.SueldoTotal() == X:
            tipo = type(emp).__name__
            print(f"{tipo} - ${emp.SueldoTotal():.2f}")
            encontrados = True
    if not encontrados:
        print("No hay empleados con ese sueldo")

buscar_sueldo(4800)  
buscar_sueldo(1000)  