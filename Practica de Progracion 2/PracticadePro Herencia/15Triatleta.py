class Nadador:
    def __init__(self, estiloNatacion):
        self.estiloNatacion = estiloNatacion
    
    def nadar(self):
        print(f"Nadando estilo {self.estiloNatacion}")

class Ciclista:
    def __init__(self, tipoBicicleta):
        self.tipoBicicleta = tipoBicicleta
    
    def pedalear(self):
        print(f"Pedaleando en bicicleta tipo {self.tipoBicicleta}")

class Corredor:
    def __init__(self, distanciaPreferida):
        self.distanciaPreferida = distanciaPreferida
    
    def correr(self):
        print(f"Corriendo una distancia de {self.distanciaPreferida} km")

class Triatleta(Nadador, Ciclista, Corredor):
    def __init__(self, estiloNatacion, tipoBicicleta, distanciaPreferida, nombre):
        Nadador.__init__(self, estiloNatacion)
        Ciclista.__init__(self, tipoBicicleta)
        Corredor.__init__(self, distanciaPreferida)
        self.nombre = nombre
    
    def mostrar_info(self):
        print(f"\nTriatleta: {self.nombre}")
        print(f"Estilo natación: {self.estiloNatacion}")
        print(f"Tipo bicicleta: {self.tipoBicicleta}")
        print(f"Distancia preferida: {self.distanciaPreferida} km")

triatleta1 = Triatleta("Crol", "Carretera", 10, "Ana García")

triatleta1.mostrar_info()

print("\n=== ACCIONES DEL TRIATLETA ===")
triatleta1.nadar()
triatleta1.pedalear()
triatleta1.correr()