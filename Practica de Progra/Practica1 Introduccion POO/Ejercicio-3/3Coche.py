class Coche:
    def __init__(self, marca, modelo, velocidad):
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad
    def acelerar(self):
        self.velocidad += 10
        print(f"{self.marca} {self.modelo} acelero a {self.velocidad}km/h")
        
    def frenar(self):
        self.velocidad -=5
        print(f"{self.marca} {self.modelo} disminuyo a {self.velocidad}km/h")
            
    def mostra_velocidad(self):
        return f"la velocidad actual de {self.marca} {self.modelo} es: {self.velocidad}km/h"
    
Coche1 = Coche("Toyota", "Corrolla", 1)
Coche2 = Coche("Nissan", "Caldina", 30)
Coche1.acelerar()
Coche2.acelerar()
Coche2.acelerar()
Coche1.frenar()
Coche2.frenar()

print(Coche1.mostra_velocidad())
print(Coche2.mostra_velocidad())