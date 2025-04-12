class Estudiante:
    def __init__(self, nombre, nota_1, nota_2):
        self.nombre = nombre
        self.nota_1 = nota_1
        self.nota_2 = nota_2
    
    def calcular_promedio(self):
        return (self.nota_1 + self.nota_2) / 2
    
    def verificar(self):
        if self.calcular_promedio() >= 6:
            print("el esudiante aprobo")
        else :
            print("el estudiante reprobo")

Estudiante1 = Estudiante("Juan", 3, 5)
Estudiante2 = Estudiante("Marcos", 10, 9)
Estudiante3 = Estudiante("Angela", 9, 8)
print(f"{Estudiante1.nombre} = {Estudiante1.calcular_promedio()}")
print(f"{Estudiante2.nombre} = {Estudiante2.calcular_promedio()}")
print(f"{Estudiante3.nombre} = {Estudiante3.calcular_promedio()}")

Estudiante1.verificar()
Estudiante2.verificar()
Estudiante3.verificar()