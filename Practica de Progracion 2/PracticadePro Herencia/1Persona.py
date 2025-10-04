class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)
        self.carrera = carrera

class Docente(Persona):
    def __init__(self, nombre, edad, especialidad):
        super().__init__(nombre, edad)
        self.especialidad = especialidad

class Curso:
    def __init__(self, nombre, codigo):
        self.nombre = nombre
        self.codigo = codigo
        self.docente = None
        self.estudiantes = []

estudiante1 = Estudiante("Ana", 20, "Ingeniería")
estudiante2 = Estudiante("Carlos", 22, "Medicina")
docente1 = Docente("Dr. Pérez", 45, "Matemáticas")

curso1 = Curso("Matemáticas", "MAT101")
curso1.docente = docente1
curso1.estudiantes = [estudiante1, estudiante2]


print(f"Curso: {curso1.nombre}")
print(f"Docente: {curso1.docente.nombre}")
print("Estudiantes:")
for est in curso1.estudiantes:
    print(f"- {est.nombre}")