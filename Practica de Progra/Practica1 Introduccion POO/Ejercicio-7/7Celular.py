class Celular:
    def __init__(self ):
        self.espacio_total = 1024  
        self.max_apps = 20
        self.bateria = 100  
        self.aplicaciones = []  

    def espacio_disponible(self):
        usado = sum(app['tamano'] for app in self.aplicaciones)
        return self.espacio_total - usado

    def instalar_app(self, nombre, tamano):
        if len(self.aplicaciones) >= self.max_apps:
            print("No se pueden instalar más de 20 aplicaciones.")
            return
        if self.espacio_disponible() < tamano:
            print("No hay suficiente espacio para instalar la aplicación.")
            return
        self.aplicaciones.append({"nombre": nombre, "tamano": tamano})
        print(f"Aplicación '{nombre}' instalada con éxito.")

    def usar_app(self, nombre, minutos):
        if self.bateria <= 0:
            print("Celular apagado.")
            return

        app = next((a for a in self.aplicaciones if a["nombre"] == nombre), None)
        if not app:
            print(f"La aplicación '{nombre}' no está instalada.")
            return

        tamano = app["tamano"]
        uso_por_10min = 1  

        if tamano > 250:
            uso_por_10min = 5
        elif tamano > 100:
            uso_por_10min = 2

        consumo = (minutos // 10) * uso_por_10min

        if self.bateria <= consumo:
            self.bateria = 0
            print("La batería se ha agotado. Celular apagado.")
        else:
            self.bateria -= consumo
            print(f"Usaste '{nombre}' por {minutos} minutos. Batería restante: {self.bateria}%")

    def mostrar_bateria(self):
        if self.bateria <= 0:
            print("Celular apagado.")
        else:
            print(f"Batería restante: {self.bateria}%")


mi_celular = Celular()
mi_celular.instalar_app("Clash Royale", 210)
mi_celular.instalar_app("Spotify", 260)
mi_celular.usar_app("Clash Royale", 200)  
mi_celular.usar_app("Spotify", 150)   
mi_celular.mostrar_bateria()
