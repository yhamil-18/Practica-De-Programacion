class Bus:
    def __init__(self, total_asientos):
        self.total_asientos = total_asientos  
        self.pasajeros = 0
        self.dinero = 0
        self.precio = 1.50
        
    def subirPasajero(self, cantidad):
        if self.pasajeros + cantidad <= self.total_asientos:
            self.pasajeros += cantidad
            print(f"Subieron {cantidad} pasajeros")
        else:
            print("No caben más pasajeros")
        
    def Cobrar(self): 
        total = self.pasajeros * self.precio
        self.dinero += total
        print(f"Se cobró {total} bs por {self.pasajeros} pasajeros")
    
    def AsientosDisponibles(self):
        disponibles = self.total_asientos - self.pasajeros
        print(f"Asientos disponibles: {disponibles}")
        return disponibles

bus1 = Bus(40)  
bus1.subirPasajero(30)
bus1.AsientosDisponibles()
bus1.Cobrar()  

print("//////////////////////////")  

bus2 = Bus(50)  
bus2.subirPasajero(55)  
bus2.AsientosDisponibles()
bus2.Cobrar()  