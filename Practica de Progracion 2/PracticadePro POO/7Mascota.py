class Mascota:
    def __init__(self, nombre, tipo, energia):
        self.nombre = nombre
        self.tipo = tipo
        self.energia = energia
    
    def alimentar(self):
        self.max = 100
        self.aum = self.energia + 20
        return self.aum

    def jugar(self):
        self.min = 0
        self.dis = self.energia - 15
        return self.dis
    
m1 = Mascota("Firulais", "Perro", 80)
m2 = Mascota("Michi", "Gato", 50)

m1.alimentar()
print(f"la energia de {m1.nombre} es {m1.aum}")
m1.jugar()
print(f"la energia de {m1.nombre} es {m1.dis}")

m2.alimentar()
print(f"la energia de {m2.nombre} es {m2.aum}")
m2.jugar()
print(f"la energia de {m2.nombre} es {m2.dis}")