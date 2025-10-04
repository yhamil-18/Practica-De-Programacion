class Parada:
    def __init__(self, nombreP=None):
        
        self.nombreP = nombreP if nombreP else "Parada Central"
        self.admins = [""] * 10  
        self.autos = [["", "", ""] for _ in range(10)]  
        self.nroAdmins = 0
        self.nroAutos = 0

    def mostrar(self):
        print(f"Nombre Parada: {self.nombreP}")
        print("Administradores:")
        for i in range(self.nroAdmins):
            print(f"  - {self.admins[i]}")
        print("Autos:")
        for i in range(self.nroAutos):
            print(f"  - Modelo: {self.autos[i][0]}, Conductor: {self.autos[i][1]}, Placa: {self.autos[i][2]}")
        print("-" * 30)

    def adicionar_admin(self, admin):
        if self.nroAdmins < 10:
            self.admins[self.nroAdmins] = admin
            self.nroAdmins += 1
            print(f"Admin '{admin}' agregado")
        else:
            print("No hay espacio para más admins")
    
    def adicionar_auto(self, modelo, conductor, placa):
        if self.nroAutos < 10:
            self.autos[self.nroAutos][0] = modelo
            self.autos[self.nroAutos][1] = conductor
            self.autos[self.nroAutos][2] = placa
            self.nroAutos += 1
            print(f"Auto '{modelo}' agregado")
        else:
            print("No hay espacio para más autos")

parada1 = Parada()
parada1.adicionar_admin("Carlos") 
parada1.adicionar_auto("Toyota", "Juan", "ABC123")  


parada2 = Parada("Parada Norte")
parada2.adicionar_admin("Maria")
parada2.adicionar_auto("Honda", "Ana", "XYZ789")

print("PARADA 1:")
parada1.mostrar()

print("PARADA 2:")
parada2.mostrar()