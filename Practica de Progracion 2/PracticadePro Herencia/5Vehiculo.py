class Vehiculo:
    def __init__(self, conductor, placa, id):
        self.conductor = conductor
        self.placa = placa
        self.id = id
    
    def mostrar(self):
        print(f"Placa: {self.placa}, Conductor: {self.conductor}")
    
    def cambiar_conductor(self, nuevo_conductor):
        self.conductor = nuevo_conductor
        print(f"Conductor cambiado a: {nuevo_conductor}")

class Bus(Vehiculo):
    def __init__(self, conductor, placa, id, capacidad, sindicato):
        super().__init__(conductor, placa, id)
        self.capacidad = capacidad
        self.sindicato = sindicato

class Auto(Vehiculo):
    def __init__(self, conductor, placa, id, caballosFuerza, descapotable):
        super().__init__(conductor, placa, id)
        self.caballosFuerza = caballosFuerza
        self.descapotable = descapotable

class Moto(Vehiculo):
    def __init__(self, conductor, placa, id, cilindrada, casco):
        super().__init__(conductor, placa, id)
        self.cilindrada = cilindrada
        self.casco = casco

bus1 = Bus("Juan Pérez", "ABC123", 1, 50, "Sindicato A")
auto1 = Auto("María García", "XYZ789", 2, 150, True)
moto1 = Moto("Carlos López", "DEF456", 3, 250, True)

print("=== VEHÍCULOS ===")
bus1.mostrar()
auto1.mostrar()
moto1.mostrar()

print("\n=== CAMBIANDO CONDUCTOR ===")
bus1.cambiar_conductor("Pedro Martínez")
bus1.mostrar()