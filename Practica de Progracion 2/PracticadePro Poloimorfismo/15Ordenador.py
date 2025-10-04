class Ordenador:
    def __init__(self, serial, numero, ram, procesador, estado=True):
        self.serial = serial
        self.numero = numero
        self.ram = ram
        self.procesador = procesador
        self.estado = estado

class Laboratorio:
    def __init__(self, nombre):
        self.nombre = nombre
        self.ordenadores = []
    
    def agregar_ordenador(self, ordenador):
        self.ordenadores.append(ordenador)
    
    def quitar_ordenador(self, serial):
        for ordenador in self.ordenadores:
            if ordenador.serial == serial:
                self.ordenadores.remove(ordenador)
                return ordenador
        return None

print("=== a) LABORATORIOS Y ORDENADORES ===")
lab1 = Laboratorio("Lasin 1")
lab2 = Laboratorio("Lasin 2")


lab1.agregar_ordenador(Ordenador("SER001", 1, 16, "Intel i7", True))
lab1.agregar_ordenador(Ordenador("SER002", 2, 8, "Intel i5", True))
lab1.agregar_ordenador(Ordenador("SER003", 3, 4, "AMD Ryzen", False))
lab1.agregar_ordenador(Ordenador("SER004", 4, 32, "Intel i9", True))

lab2.agregar_ordenador(Ordenador("SER005", 5, 8, "AMD Ryzen", True))
lab2.agregar_ordenador(Ordenador("SER006", 6, 16, "Intel i7", False))


print("\n=== b) INFORMACIÓN ===")


print("--- Ordenadores ACTIVOS Lasin 1 ---")
for o in lab1.ordenadores:
    if o.estado:
        print(f"Serial: {o.serial}, RAM: {o.ram}GB")

print("--- Ordenadores INACTIVOS Lasin 1 ---")
for o in lab1.ordenadores:
    if not o.estado:
        print(f"Serial: {o.serial}, RAM: {o.ram}GB")


print("--- Todos Los Ordenadores Lasin 1 ---")
for o in lab1.ordenadores:
    print(f"Serial: {o.serial}, RAM: {o.ram}GB")


print("--- Ordenadores con RAM > 8GB ---")
for lab in [lab1, lab2]:
    for o in lab.ordenadores:
        if o.ram > 8:
            print(f"{lab.nombre}: {o.serial} - {o.ram}GB")


print("\n=== c) TRASLADO ===")
print("ANTES:")
print(f"Lasin 1: {len(lab1.ordenadores)} ordenadores")
print(f"Lasin 2: {len(lab2.ordenadores)} ordenadores")


ordenador1 = lab1.quitar_ordenador("SER001")
ordenador2 = lab1.quitar_ordenador("SER002")

if ordenador1:
    lab2.agregar_ordenador(ordenador1)
    print("✓ SER001 trasladado")
if ordenador2:
    lab2.agregar_ordenador(ordenador2)
    print("✓ SER002 trasladado")

print("\nDESPUÉS:")
print(f"Lasin 1: {len(lab1.ordenadores)} ordenadores")
print(f"Lasin 2: {len(lab2.ordenadores)} ordenadores")