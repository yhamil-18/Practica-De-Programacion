class Empleado:
    def __init__(self, nombre, puesto, salario):
        self.nombre = nombre
        self.puesto = puesto
        self.salario = salario
    
    def __str__(self):
        return f"{self.nombre} - {self.puesto} - ${self.salario}"

class Empresa:
    def __init__(self, nombre):
        self.nombre = nombre
        self.empleados = []
    
    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)
    
    def mostrar_informacion(self):
        print(f"Empresa: {self.nombre}")
        print("Empleados:")
        for empleado in self.empleados:
            print(f"  - {empleado}")
        print()
    
    def buscar_empleado(self, nombre):
        for empleado in self.empleados:
            if empleado.nombre.lower() == nombre.lower():
                return empleado
        return None

    def eliminar_empleado(self, nombre):
        for i, empleado in enumerate(self.empleados):
            if empleado.nombre.lower() == nombre.lower():
                return self.empleados.pop(i)
        return None
    
    def promedio_salarial(self):
        if not self.empleados:
            return 0
        total = sum(empleado.salario for empleado in self.empleados)
        return total / len(self.empleados)
    
    def empleados_salario_mayor(self, salario_minimo):
        return [empleado for empleado in self.empleados if empleado.salario > salario_minimo]
empresa = Empresa("Tech Solutions")

empresa.agregar_empleado(Empleado("Ana García", "Desarrollador", 50000))
empresa.agregar_empleado(Empleado("Luis Martínez", "Gerente", 75000))
empresa.agregar_empleado(Empleado("Carlos Rodríguez", "Analista", 45000))
empresa.agregar_empleado(Empleado("María López", "Desarrollador", 52000))
empresa.mostrar_informacion()

empleado_buscado = empresa.buscar_empleado("Ana García")
if empleado_buscado:
    print(f"Empleado encontrado: {empleado_buscado}")
else:
    print("Empleado no encontrado")
print()

eliminado = empresa.eliminar_empleado("Carlos Rodríguez")
if eliminado:
    print(f"Empleado eliminado: {eliminado}")
else:
    print("Empleado no encontrado para eliminar")
print()

empresa.mostrar_informacion()

promedio = empresa.promedio_salarial()
print(f"Promedio salarial: ${promedio:.2f}")

salario_minimo = 48000
empleados_altos_salarios = empresa.empleados_salario_mayor(salario_minimo)
print(f"\nEmpleados con salario mayor a ${salario_minimo}:")
for empleado in empleados_altos_salarios:
    print(f"  - {empleado}")