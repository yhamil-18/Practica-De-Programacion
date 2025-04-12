class Computadora:
    def __init__(self, procesador, memoria, disco_duro, tarjeta_grafica):
        self.procesador = procesador
        self.memoria = memoria
        self.disco_duro = disco_duro
        self.tarjeta_grafica = tarjeta_grafica
        self.encendida = False
        
    def mostrar_componentes(self):
        print("La Computadora tiene estos componentes")
        print(f"Procesador: {self.procesador}")
        print(f"Memoria Ram: {self.memoria}")
        print(f"Disco duro: {self.disco_duro}")
        print(f"Tarjeta grafica: {self.tarjeta_grafica}")
        
    def encender(self):
        if not self.encendida:
            self.encendida = True
            print("La computadora se ha encendido.")
        else:
            print("La computadora ya está encendida.")

    def apagar(self):
        if self.encendida:
            self.encendida = False
            print("La computadora se ha apagado.")
        else:
            print("La computadora ya está apagada.")
            
    def mostrar_estado(self):
        estado = "encendida" if self.encendida else "apagada"
        print(f"La computadora está {estado}.")

mi_pc = Computadora(
    procesador="Intel Core i10",
    memoria="64GB",
    disco_duro="1TB SSD",
    tarjeta_grafica="NVIDIA GTX 1660"
)

mi_pc.mostrar_componentes()
mi_pc.mostrar_estado()
mi_pc.encender()
mi_pc.mostrar_estado()
mi_pc.apagar()
mi_pc.mostrar_estado()