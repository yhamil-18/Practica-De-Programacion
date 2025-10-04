class Pasajero:
    def __init__(self, nombre="", edad=0, genero="", nroHabitacion=0, costoPasaje=0):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.nroHabitacion = nroHabitacion
        self.costoPasaje = costoPasaje
    
    def __pos__(self):
        print(f"Leyendo datos de {self.nombre}")
        return self
    
    def __neg__(self):
        print(f"Pasajero: {self.nombre}, Hab: {self.nroHabitacion}, Costo: ${self.costoPasaje}")
        return self

class Crucero:
    def __init__(self, nombre="", paisOrigen="", paisDestino="", nroPasajeros=0):
        self.nombre = nombre
        self.paisOrigen = paisOrigen
        self.paisDestino = paisDestino
        self.nroPasajeros = nroPasajeros
        self.pasajeros = []
    
    def __pos__(self):
        print(f"Leyendo datos del crucero {self.nombre}")
        return self
    
    def __neg__(self):
        print(f"Crucero: {self.nombre}, Pasajeros: {self.nroPasajeros}")
        return self
    
    def __eq__(self, otro):
        total1 = sum(p.costoPasaje for p in self.pasajeros)
        total2 = sum(p.costoPasaje for p in otro.pasajeros)
        return total1 == total2
    
    def __add__(self, otro):

        return self.nroPasajeros == otro.nroPasajeros
    
    def __sub__(self, otro):
        hombres = sum(1 for p in self.pasajeros if p.genero.upper() == 'M')
        mujeres = sum(1 for p in self.pasajeros if p.genero.upper() == 'F')
        return hombres, mujeres

crucero1 = Crucero("Caribe Paradise", "USA", "Bahamas", 3)
crucero2 = Crucero("Mediterranean", "España", "Italia", 2)

p1 = Pasajero("Juan Vargas", 35, "M", 502, 500)
p2 = Pasajero("Martina Vasques", 28, "F", 603, 1000)
p3 = Pasajero("Wilmer Montero", 42, "M", 401, 925)
p4 = Pasajero("Ana García", 29, "F", 305, 750)
p5 = Pasajero("Carlos López", 45, "M", 208, 850)

crucero1.pasajeros = [p1, p2, p3]
crucero2.pasajeros = [p4, p5]


print("=== DATOS ===")
-crucero1
-crucero2
for p in [p1, p2, p3, p4, p5]:
    -p


print(f"\nMisma suma de costos: {crucero1 == crucero2}")

print(f"Misma cantidad pasajeros: {crucero1 + crucero2}")

hombres, mujeres = crucero1 - crucero2
print(f"Hombres: {hombres}, Mujeres: {mujeres}")