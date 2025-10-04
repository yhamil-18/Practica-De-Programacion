class Videojuego:
    def __init__(self, nombre="", plataforma="", jugadores=0):
        self.nombre = nombre
        self.plataforma = plataforma
        self.cantidad_jugadores = jugadores
    
    def agregarJugadores(self, cantidad=1):
        if cantidad == 1:
            self.cantidad_jugadores += 1
            print(f"Se agregó 1 jugador")
        else:
            self.cantidad_jugadores += cantidad
            print(f"Se agregaron {cantidad} jugadores")
    
    def mostrar(self):
        print(f"{self.nombre} - {self.plataforma} - {self.cantidad_jugadores} jugadores")

v1 = Videojuego("FIFA", "PlayStation", 2)
v2 = Videojuego("Mario Kart", "Nintendo", 4)

v3 = Videojuego()  
v4 = Videojuego("Minecraft")  

v1.agregarJugadores()  
v2.agregarJugadores(3)  

v1.mostrar()
v2.mostrar()
v3.mostrar()
v4.mostrar()