class Videojuego:
    def __init__(self, nombre: str, plataforma: str, cantidadJugadores: int = 0):
        self.nombre = nombre
        self.plataforma = plataforma
        self.cantidadJugadores = cantidadJugadores
        
    @classmethod
    def desde_nombre(cls, nombre: str):
        return cls(nombre, "Plataforma desconocida")
    
    @classmethod
    def desde_nombre_jugadores(cls, nombre: str, cantidadJugadores: int):
        return cls(nombre, "Plataforma desconocida", cantidadJugadores)
    

    def mostrar(self):
        print(f"Nombre: {self.nombre}")
        print(f"Plataforma: {self.plataforma}")
        print(f"Número de jugadores: {self.cantidadJugadores}")

    def agregarJugadores(self, cantidad: int = 1):
        self.cantidadJugadores += cantidad
        print(f"Jugadores actualizados: {self.cantidadJugadores}")
        


videojuego1 = Videojuego("Clash Royale", "Steam", 20)
videojuego2 = Videojuego("Vice City", "EA", 1)
videojuego3 = Videojuego("Among Us", "MediaFire", 10)


videojuego1_alt = Videojuego.desde_nombre("Clash Royale")
videojuego2_alt = Videojuego.desde_nombre("Vice City")
videojuego3_alt = Videojuego.desde_nombre("Among Us")

videojuego1_jugadores = Videojuego.desde_nombre_jugadores("Clash Royale", 20)
videojuego2_jugadores = Videojuego.desde_nombre_jugadores("Vice City", 1)
videojuego3_jugadores = Videojuego.desde_nombre_jugadores("Among Us", 10)

videojuego1.mostrar()
videojuego2.mostrar()
videojuego3.mostrar()

videojuego1_alt.mostrar()
videojuego2_alt.mostrar()
videojuego3_alt.mostrar()

videojuego1_jugadores.mostrar()
videojuego2_jugadores.mostrar()
videojuego3_jugadores.mostrar()


videojuego1.agregarJugadores()
videojuego2.agregarJugadores(1)
