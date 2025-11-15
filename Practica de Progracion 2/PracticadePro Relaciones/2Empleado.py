class Departamento:
    def __init__(self, nombre, area):
        self.nombre = nombre
        self.area = area
        self.empleados = []
    
    def agregarEmpleado(self, empleado):
        self.empleados.append(empleado)
    
    def mostrarEmpleados(self):
        print(f"\n--- Empleados del Departamento {self.nombre} ---")
        if not self.empleados:
            print("No hay empleados en este departamento.")
        else:
            for empleado in self.empleados:
                empleado.mostrarInfo()
    
    def cambiarSalario(self, porcentaje):
        for empleado in self.empleados:
            empleado.sueldo *= (1 + porcentaje / 100)
        print(f"Salarios cambiados en {porcentaje}% para el departamento {self.nombre}")
    
    def moverEmpleados(self, otro_departamento):
        otro_departamento.empleados.extend(self.empleados)
        print(f"Se movieron {len(self.empleados)} empleados de {self.nombre} a {otro_departamento.nombre}")
        self.empleados.clear()

class Empleado:
    def __init__(self, nombre, cargo, sueldo):
        self.nombre = nombre
        self.cargo = cargo
        self.sueldo = sueldo
    
    def mostrarInfo(self):
        print(f"Nombre: {self.nombre}, Cargo: {self.cargo}, Sueldo: ${self.sueldo:,.2f}")

departamento1 = Departamento("Ventas", "Comercial")
departamento2 = Departamento("Recursos Humanos", "Administrativo")

empleados_dep1 = [
    Empleado("Ana García", "Gerente de Ventas", 50000),
    Empleado("Carlos López", "Ejecutivo de Ventas", 35000),
    Empleado("María Rodríguez", "Asistente de Ventas", 30000),
    Empleado("Pedro Martínez", "Analista Comercial", 40000),
    Empleado("Laura Sánchez", "Coordinadora", 32000)
]

for empleado in empleados_dep1:
    departamento1.agregarEmpleado(empleado)

departamento1.mostrarEmpleados()
departamento2.mostrarEmpleados()

departamento1.cambiarSalario(10)  

empleados_en_ambos = False
for empleado in departamento1.empleados:
    if empleado in departamento2.empleados:
        empleados_en_ambos = True
        print(f"El empleado {empleado.nombre} está en ambos departamentos")
        break

if not empleados_en_ambos:
    print("No hay empleados del departamento 1 en el departamento 2")

print("\n=== MOVIENDO EMPLEADOS ===")
departamento1.moverEmpleados(departamento2)

print("\n=== ESTADO FINAL ===")
departamento1.mostrarEmpleados()
departamento2.mostrarEmpleados()