class Bloque:
    def __init__(self):
        pass

    def accion(self):
        pass

    def colocar(self, orientacion):
        pass

    def romper(self):
        pass


class BloqueCofre(Bloque):
    def __init__(self, capacidad, resistencia, tipo):
        self.capacidad = capacidad
        self.resistencia = resistencia
        self.tipo = tipo

    def accion(self):
        print(f"El {self.tipo} se abre, mostrando su contenido.")

    def colocar(self, orientacion):
        print(f"Colocando el {self.tipo} en posición: {orientacion}.")

    def romper(self):
        print(f"El {self.tipo} ha sido roto. Los objetos dentro se caen.")
        

class BloqueTnt(Bloque):
    def __init__(self, tipo, daño):
        self.tipo = tipo
        self.daño = daño

    def accion(self):
        print(f"¡El {self.tipo} está a punto de explotar!")

    def colocar(self, orientacion):
        print(f"Colocando el {self.tipo} en posición: {orientacion}.")

    def romper(self):
        print(f"¡El {self.tipo} ha explotado! Causando {self.daño} puntos de daño.")


class BloqueHorno(Bloque):
    def __init__(self, color, capacidadComida):
        self.color = color
        self.capacidadComida = capacidadComida

    def accion(self):
        print(f"El {self.color} horno está cocinando la comida.")

    def colocar(self, orientacion):
        print(f"Colocando el {self.color} horno en posición: {orientacion}.")

    def romper(self):
        print(f"El {self.color} horno ha sido roto. Los alimentos dentro se han caído.")


if __name__ == "__main__":

    cofre1 = BloqueCofre(30, 50, "Cofre de Madera")
    cofre2 = BloqueCofre(50, 80, "Cofre de Hierro")

    tnt1 = BloqueTnt("TNT", 100)
    tnt2 = BloqueTnt("TNT de Agua", 50)

    horno1 = BloqueHorno("Rojo", 20)
    horno2 = BloqueHorno("Azul", 30)

    print("Acción del Cofre 1:")
    cofre1.accion()
    print("\nAcción del Cofre 2:")
    cofre2.accion()

    print("\nAcción del TNT 1:")
    tnt1.accion()
    print("\nAcción del TNT 2:")
    tnt2.accion()

    print("\nAcción del Horno 1:")
    horno1.accion()
    print("\nAcción del Horno 2:")
    horno2.accion()

    print("\nColocar el Cofre 1:")
    cofre1.colocar("suelo")
    print("\nColocar el Cofre 2:")
    cofre2.colocar("pared")

    print("\nColocar el TNT 1:")
    tnt1.colocar("suelo")
    print("\nColocar el TNT 2:")
    tnt2.colocar("pared")

    print("\nColocar el Horno 1:")
    horno1.colocar("suelo")
    print("\nColocar el Horno 2:")
    horno2.colocar("pared")

    print("\nRomper el Cofre 1:")
    cofre1.romper()
    print("\nRomper el Cofre 2:")
    cofre2.romper()

    print("\nRomper el TNT 1:")
    tnt1.romper()
    print("\nRomper el TNT 2:")
    tnt2.romper()

    print("\nRomper el Horno 1:")
    horno1.romper()
    print("\nRomper el Horno 2:")
    horno2.romper()
