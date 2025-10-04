class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

class Empleado:
    def __init__(self, sueldo, antiguedad):
        self.sueldo = sueldo
        self.antiguedad = antiguedad

class Policia:
    def __init__(self, grado, departamento):
        self.grado = grado
        self.departamento = departamento

class JefePolicia(Persona, Empleado, Policia):
    def __init__(self, nombre, edad, sueldo, antiguedad, grado, departamento):
        Persona.__init__(self, nombre, edad)
        Empleado.__init__(self, sueldo, antiguedad)
        Policia.__init__(self, grado, departamento)
    
    def mostrar(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Sueldo: ${self.sueldo}")
        print(f"Antigüedad: {self.antiguedad} años")
        print(f"Grado: {self.grado}")
        print(f"Departamento: {self.departamento}")
        print("-" * 25)

jefe1 = JefePolicia("Carlos Rojas", 45, 5000, 20, "Coronel", "Narcóticos")
jefe2 = JefePolicia("Ana Mendoza", 38, 5500, 15, "Coronel", "Homicidios")

print("=== DATOS JEFES DE POLICÍA ===")
jefe1.mostrar()
jefe2.mostrar()

print("=== COMPARACIÓN DE SUELDOS ===")
if jefe1.sueldo > jefe2.sueldo:
    print(f"Mayor sueldo: {jefe1.nombre} - ${jefe1.sueldo}")
elif jefe2.sueldo > jefe1.sueldo:
    print(f"Mayor sueldo: {jefe2.nombre} - ${jefe2.sueldo}")
else:
    print(f"Ambos tienen el mismo sueldo: ${jefe1.sueldo}")

print("\n=== COMPARACIÓN DE GRADOS ===")
if jefe1.grado == jefe2.grado:
    print(f"✓ Ambos tienen el mismo grado: {jefe1.grado}")
else:
    print(f"✗ Tienen grados diferentes: {jefe1.grado} vs {jefe2.grado}")