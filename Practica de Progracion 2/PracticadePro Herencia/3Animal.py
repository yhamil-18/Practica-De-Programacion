class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def desplazarse(self):
        print(f"{self.nombre} se está desplazando...")

class Leon(Animal):
    def desplazarse(self):
        print(f"{self.nombre} está caminando poderosamente")

class Pinguino(Animal):
    def desplazarse(self):
        print(f"{self.nombre} está nadando en el agua fría")

class Canguro(Animal):
    def desplazarse(self):
        print(f"{self.nombre} está saltando con sus patas fuertes")

leon = Leon("Simba", 5)
pinguino = Pinguino("Pingu", 3)
canguro = Canguro("Kanga", 4)

leon.desplazarse()
pinguino.desplazarse()
canguro.desplazarse()