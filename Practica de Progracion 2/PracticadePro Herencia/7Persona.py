class Persona:
    def __init__(self, nombre, paterno, materno, edad):
        self.nombre = nombre
        self.paterno = paterno
        self.materno = materno
        self.edad = edad
    
    def mostrar(self):
        print(f"Nombre: {self.nombre} {self.paterno} {self.materno}")
        print(f"Edad: {self.edad}")

class Docente(Persona):
    def __init__(self, nombre, paterno, materno, edad, sueldo, regProfesional):
        super().__init__(nombre, paterno, materno, edad)
        self.sueldo = sueldo
        self.regProfesional = regProfesional
    
    def mostrar(self):
        super().mostrar()
        print(f"Sueldo: {self.sueldo}")
        print(f"Registro: {self.regProfesional}")

class Estudiante(Persona):
    def __init__(self, nombre, paterno, materno, edad, ru, matricula):
        super().__init__(nombre, paterno, materno, edad)
        self.ru = ru
        self.matricula = matricula
    
    def mostrar(self):
        super().mostrar()
        print(f"RU: {self.ru}")
        print(f"Matrícula: {self.matricula}")
    
    def modificarEdad(self, nueva_edad):
        self.edad = nueva_edad
        print(f"Edad cambiada a: {nueva_edad}")

estudiante1 = Estudiante("Ana", "García", "López", 20, "123456", "2023001")
estudiante2 = Estudiante("Carlos", "Martínez", "Pérez", 22, "123457", "2023002")
docente1 = Docente("María", "Rodríguez", "Silva", 35, 5000, "PROF123")

print("=== DATOS ===")
estudiante1.mostrar()
print()
estudiante2.mostrar()
print()
docente1.mostrar()

def promedio_edad(estudiantes):
    total = sum(est.edad for est in estudiantes)
    return total / len(estudiantes)

print(f"\nPromedio de edad estudiantes: {promedio_edad([estudiante1, estudiante2])}")

print("\n=== MODIFICAR EDAD ===")
estudiante1.modificarEdad(21)

print("\n=== COMPARAR EDADES ===")
print(f"¿Estudiante1 misma edad que docente? {estudiante1.edad == docente1.edad}")
print(f"¿Estudiante2 misma edad que docente? {estudiante2.edad == docente1.edad}")
