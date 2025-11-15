class Persona:
    def __init__(self, nombre, edad, email):
        self.nombre = nombre
        self.edad = edad
        self.email = email

class Facultad:
    def __init__(self, nombre):
        self.nombre = nombre

class Fraternidad:
    def __init__(self, nombre, encargado):
        self.nombre = nombre
        self.encargado = encargado
        self.miembros = []

class Bailarin(Persona):
    def __init__(self, nombre, edad, email, facultad, fraternidad):
        super().__init__(nombre, edad, email)
        self.facultad = facultad
        self.fraternidad = fraternidad
        self.verificar_duplicado()
        fraternidad.miembros.append(self)
        
    def verificar_duplicado(self):
        for miembro in self.fraternidad.miembros:
            if miembro.nombre == self.nombre:
                raise ValueError(f"{self.nombre} ya está en {self.fraternidad.nombre}")

facultad1 = Facultad("Ingeniería")
facultad2 = Facultad("Medicina")

encargado1 = Persona("Carlos Rodríguez", 25, "carlos@universidad.edu")
encargado2 = Persona("María González", 24, "maria@universidad.edu")

fraternidad1 = Fraternidad("Alpha Omega", encargado1)
fraternidad2 = Fraternidad("Beta Gamma", encargado2)

bailarines = [
    Bailarin("Ana López", 20, "ana@universidad.edu", facultad1, fraternidad1),
    Bailarin("Juan Pérez", 21, "juan@universidad.edu", facultad2, fraternidad2),
    Bailarin("Laura Martínez", 22, "laura@universidad.edu", facultad1, fraternidad1),
    Bailarin("Pedro Sánchez", 19, "pedro@universidad.edu", facultad2, fraternidad2),
    Bailarin("Sofía Ramírez", 20, "sofia@universidad.edu", facultad1, fraternidad1)
]

print("=== SISTEMA UNIVERSITARIO ===")
print("\n--- BAILARINES ---")
for bailarin in bailarines:
    print(f"{bailarin.nombre} ({bailarin.edad} años)")
    print(f"  Facultad: {bailarin.facultad.nombre}")
    print(f"  Fraternidad: {bailarin.fraternidad.nombre}")
    print(f"  Email: {bailarin.email}\n")

print("\n--- ENCARGADOS ---")
print(f"{fraternidad1.nombre}: {fraternidad1.encargado.nombre}")
print(f"{fraternidad2.nombre}: {fraternidad2.encargado.nombre}")

print("\n--- ESTADÍSTICAS ---")
print(f"Total bailarines: {len(bailarines)}")
print(f"Fraternidad {fraternidad1.nombre}: {len(fraternidad1.miembros)} miembros")
print(f"Fraternidad {fraternidad2.nombre}: {len(fraternidad2.miembros)} miembros")

print("\n--- VERIFICACIÓN DUPLICADOS ---")
try:
    Bailarin("Ana López", 20, "ana@universidad.edu", facultad1, fraternidad1)
except ValueError as e:
    print(f"❌ {e}")