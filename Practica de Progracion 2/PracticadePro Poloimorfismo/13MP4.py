class MP4:
    def __init__(self, marca, capacidad):
        self.marca = marca
        self.capacidad = capacidad
        self.canciones = []
        self.videos = []
    
    def espacio(self):
        usado = sum(c[2] for c in self.canciones)/1024/1024 + sum(v[2] for v in self.videos)/1024
        return self.capacidad - usado
    
    def borrar(self, tipo, nombre=None, artista=None):
        if tipo == "cancion":
            if nombre and artista:
                self.canciones = [c for c in self.canciones if not (c[0]==nombre and c[1]==artista)]
            elif nombre:
                self.canciones = [c for c in self.canciones if c[0]!=nombre]
            elif artista:
                self.canciones = [c for c in self.canciones if c[1]!=artista]
    
    def __add__(self, cancion):
        if cancion[:2] not in [c[:2] for c in self.canciones] and self.espacio() > 0:
            self.canciones.append(cancion)
        return self
    
    def __sub__(self, video):
        if video[0] not in [v[0] for v in self.videos] and self.espacio() > 0:
            self.videos.append(video)
        return self
    
    def mostrar(self):
        print(f"{self.marca}: {self.espacio():.2f}GB libres")


mp = MP4("Sony", 1.0)
mp.canciones = [["Back To Black", "Amy", 100], ["Lost", "LP", 150]]
mp.videos = [["Heathens", "21P", 50], ["Harmonica", "KSHMR", 70]]

mp.mostrar()
mp.borrar("cancion", nombre="Lost")
mp + ["Nueva", "Artista", 200]
mp - ["Video Nuevo", "Director", 30]
mp.mostrar()