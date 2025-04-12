class Universidad:
    def __init__(self, nombre):
        self.nombre = nombre
        self.oficinas = []
        self.aulas = []
        self.laboratorios = []

    def agregar_oficina(self, oficina):
        self.oficinas.append(oficina)

    def agregar_aula(self, aula):
        self.aulas.append(aula)

    def agregar_laboratorio(self, laboratorio):
        self.laboratorios.append(laboratorio)

    def mostrar_ambientes(self):
        print(f"\n=== Universidad: {self.nombre} ===")
        print("\n--- Oficinas ---")
        for oficina in self.oficinas:
            oficina.mostrar()
            oficina.cantidad_muebles()
            print()

        print("--- Aulas ---")
        for aula in self.aulas:
            aula.mostrar()
            aula.cantidad_muebles()
            print()

        print("--- Laboratorios ---")
        for lab in self.laboratorios:
            lab.mostrar()
            lab.cantidad_muebles()
            print()

    def resumen(self):
        print(f"\nResumen de ambientes en la universidad {self.nombre}:")
        print(f"Total de oficinas: {len(self.oficinas)}")
        print(f"Total de aulas: {len(self.aulas)}")
        print(f"Total de laboratorios: {len(self.laboratorios)}")



class Oficina:
    def __init__(self, nombre, ubicacion, nro_sillas, nro_escritorios, nro_estanterias):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.nro_sillas = nro_sillas
        self.nro_escritorios = nro_escritorios
        self.nro_estanterias = nro_estanterias

    def mostrar(self):
        print("=== Oficina ===")
        print(f"Nombre: {self.nombre}")
        print(f"Ubicación: {self.ubicacion}")
        print(f"Sillas: {self.nro_sillas}, Escritorios: {self.nro_escritorios}, Estanterías: {self.nro_estanterias}")

    def cantidad_muebles(self, *args):
        if len(args) == 0:
            total = self.nro_sillas + self.nro_escritorios + self.nro_estanterias
            print(f"Muebles totales: {total}")
        else:
            print(f"Muebles indicados (sumados): {sum(args)}")


class Aula:
    def __init__(self, nombre, capacidad, nro_pupitres):
        self.nombre = nombre
        self.capacidad = capacidad
        self.nro_pupitres = nro_pupitres

    def mostrar(self):
        print("=== Aula ===")
        print(f"Nombre: {self.nombre}")
        print(f"Capacidad: {self.capacidad}")
        print(f"Número de pupitres: {self.nro_pupitres}")

    def cantidad_muebles(self, *args):
        if len(args) == 0:
            print(f"Muebles totales: {self.nro_pupitres}")
        else:
            print(f"Muebles indicados (sumados): {sum(args)}")


class Laboratorio:
    def __init__(self, nombre, capacidad, nro_mesas, nro_sillas):
        self.nombre = nombre
        self.capacidad = capacidad
        self.nro_mesas = nro_mesas
        self.nro_sillas = nro_sillas

    def mostrar(self):
        print("=== Laboratorio ===")
        print(f"Nombre: {self.nombre}")
        print(f"Capacidad: {self.capacidad}")
        print(f"Mesas: {self.nro_mesas}, Sillas: {self.nro_sillas}")

    def cantidad_muebles(self, *args):
        if len(args) == 0:
            total = self.nro_mesas + self.nro_sillas
            print(f"Muebles totales: {total}")
        else:
            print(f"Muebles indicados (sumados): {sum(args)}")

if __name__ == "__main__":

    uni = Universidad("Universidad Nacional de Ejemplo")


    oficina1 = Oficina("Oficina de Decanato", "Edificio A", 4, 2, 1)
    oficina2 = Oficina("Oficina de Finanzas", "Edificio B", 6, 3, 2)

    aula1 = Aula("Aula 101", 40, 40)
    aula2 = Aula("Aula 202", 30, 30)

    laboratorio1 = Laboratorio("Lab de Informática", 25, 10, 25)


    uni.agregar_oficina(oficina1)
    uni.agregar_oficina(oficina2)

    uni.agregar_aula(aula1)
    uni.agregar_aula(aula2)

    uni.agregar_laboratorio(laboratorio1)


    uni.mostrar_ambientes()
    uni.resumen()
