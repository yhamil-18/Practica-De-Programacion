class Politico:
    def __init__(self, profesion, añosExp):
        self.profesion = profesion
        self.añosExp = añosExp

class Partido:
    def __init__(self, nombreP, rol):
        self.nombreP = nombreP
        self.rol = rol

class Presidente(Politico, Partido):
    def __init__(self, nombre, apellido, profesion="", añosExp=0, nombreP="", rol=""):
        Politico.__init__(self, profesion, añosExp)
        Partido.__init__(self, nombreP, rol)
        self.nombre = nombre
        self.apellido = apellido
    
    def mostrar(self):
        print(f"Presidente: {self.nombre} {self.apellido}")
        print(f"Profesión: {self.profesion}")
        print(f"Años experiencia: {self.añosExp}")
        print(f"Partido: {self.nombreP}")
        print(f"Rol: {self.rol}")
        print("-" * 30)


presidente1 = Presidente("Juan", "Pérez", "Abogado", 10, "Partido Azul", "Líder")
presidente1.mostrar()

presidente2 = Presidente("María", "García", "Economista", 15, "Partido Verde", "Fundador")

presidente2.mostrar()


presidente3 = Presidente("Carlos", "López", "Ingeniero", 8, "Partido Rojo", "Secretario")
presidentes = [presidente1, presidente2, presidente3]

def buscar_presidente(nombre_buscar):
    for pres in presidentes:
        if pres.nombre.lower() == nombre_buscar.lower():
            print(f"✓ ENCONTRADO: {pres.nombre} {pres.apellido}")
            print(f"  Partido: {pres.nombreP}")
            print(f"  Profesión: {pres.profesion}")
            return True
    print(f"✗ Presidente '{nombre_buscar}' no encontrado")
    return False

print("=== BUSCAR PRESIDENTES ===")
buscar_presidente("María")
buscar_presidente("Ana")
buscar_presidente("Carlos")