class Ropa:
    def __init__(self, tipo, material):
        self.tipo = tipo
        self.material = material
    
    def mostrarInfo(self):
        return f"Tipo: {self.tipo}, Material: {self.material}"

class Ropero:
    CAPACIDAD_MAXIMA = 20
    
    def __init__(self, material):
        self.material = material
        self.ropas = []
        self.nroRopas = 0
    
    def agregarRopa(self, ropa):
        if self.nroRopas < self.CAPACIDAD_MAXIMA:
            self.ropas.append(ropa)
            self.nroRopas += 1
            print(f"Prenda agregada: {ropa.mostrarInfo()}")
            return True
        else:
            print("¡El ropero está lleno! No se puede agregar más prendas.")
            return False
    
    def eliminarRopa(self, material=None, tipo=None):
        if material is None and tipo is None:
            print("Debe especificar material o tipo para eliminar")
            return 0
        
        ropas_eliminadas = []
        ropas_restantes = []
        
        for ropa in self.ropas:
            if (material and ropa.material == material) or (tipo and ropa.tipo == tipo):
                ropas_eliminadas.append(ropa)
            else:
                ropas_restantes.append(ropa)
        
        self.ropas = ropas_restantes
        self.nroRopas = len(self.ropas)
        
        print(f"Se eliminaron {len(ropas_eliminadas)} prendas:")
        for ropa in ropas_eliminadas:
            print(f"  - {ropa.mostrarInfo()}")
        
        return len(ropas_eliminadas)
    
    def mostrarRopas(self):
        print(f"\n--- Ropero de {self.material} ---")
        print(f"Total de prendas: {self.nroRopas}/{self.CAPACIDAD_MAXIMA}")
        if self.nroRopas == 0:
            print("El ropero está vacío")
        else:
            for i, ropa in enumerate(self.ropas, 1):
                print(f"{i}. {ropa.mostrarInfo()}")
    
    def mostrarRopasPorMaterial(self, material):
        print(f"\n--- Prendas de material: {material} ---")
        encontradas = [ropa for ropa in self.ropas if ropa.material == material]
        
        if not encontradas:
            print(f"No se encontraron prendas de material {material}")
        else:
            for i, ropa in enumerate(encontradas, 1):
                print(f"{i}. {ropa.mostrarInfo()}")
        return encontradas
    
    def mostrarRopasPorTipo(self, tipo):
        print(f"\n--- Prendas de tipo: {tipo} ---")
        encontradas = [ropa for ropa in self.ropas if ropa.tipo == tipo]
        
        if not encontradas:
            print(f"No se encontraron prendas de tipo {tipo}")
        else:
            for i, ropa in enumerate(encontradas, 1):
                print(f"{i}. {ropa.mostrarInfo()}")
        return encontradas

ropero = Ropero("Madera")

print("=== AGREGANDO PRENDAS AL ROPERO ===")
prendas = [
    Ropa("Camisa", "Algodón"),
    Ropa("Pantalón", "Jean"),
    Ropa("Camisa", "Seda"),
    Ropa("Vestido", "Algodón"),
    Ropa("Chaqueta", "Cuero"),
    Ropa("Pantalón", "Algodón"),
    Ropa("Blusa", "Seda"),
    Ropa("Falda", "Jean")
]

for prenda in prendas:
    ropero.agregarRopa(prenda)

ropero.mostrarRopas()

print("\n=== MOSTRANDO PRENDAS POR MATERIAL Y TIPO ===")
ropero.mostrarRopasPorMaterial("Algodón")
ropero.mostrarRopasPorTipo("Camisa")

print("\n=== ELIMINANDO PRENDAS ===")
print("Eliminando prendas de material 'Jean':")
ropero.eliminarRopa(material="Jean")

print("\nEliminando prendas de tipo 'Camisa':")
ropero.eliminarRopa(tipo="Camisa")

ropero.mostrarRopas()

print("\n=== ESTADO FINAL ===")
ropero.mostrarRopasPorMaterial("Algodón")
ropero.mostrarRopasPorMaterial("Seda")