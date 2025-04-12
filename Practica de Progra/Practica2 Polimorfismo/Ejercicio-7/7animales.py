class Perro:
    def __init__(self, nombre, edad, raza):
        self.nombre = nombre
        self.edad = edad
        self.raza = raza

    def hacerSonido(self):
        print(f"{self.nombre} dice: ¡Guau! ¡Guau!")

    def moverse(self):
        print(f"{self.nombre} corre rápidamente.")

class Gato:
    def __init__(self, nombre, color):
        self.nombre = nombre
        self.color = color

    def hacerSonido(self):
        print(f"{self.nombre} dice: ¡Miau! ¡Miau!")

    def moverse(self):
        print(f"{self.nombre} salta ágilmente.")

class Pajaro:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo

    def hacerSonido(self):
        print(f"{self.nombre} dice: ¡Pío! ¡Pío!")

    def moverse(self):
        print(f"{self.nombre} vuela por los aires.")

if __name__ == "__main__":
   
    perro = Perro("Rex", 3, "Pastor Alemán")
    gato = Gato("Luna", "Negro")
    pajaro = Pajaro("Piolín", "Canario")


    print("Sonido del Perro:")
    perro.hacerSonido()

    print("\nSonido del Gato:")
    gato.hacerSonido()

    print("\nSonido del Pájaro:")
    pajaro.hacerSonido()

    print("\nMovimiento del Perro:")
    perro.moverse()

    print("\nMovimiento del Gato:")
    gato.moverse()

    print("\nMovimiento del Pájaro:")
    pajaro.moverse()
