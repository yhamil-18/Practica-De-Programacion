class Celular:
    def __init__(self, nroTel, dueño, espacio, ram, nroApp):
        self.nroTel = nroTel
        self.dueño = dueño
        self.espacio = espacio
        self.ram = ram
        self.nroApp = nroApp
        
    def __pos__(self):
        """Aumenta en 10 el nroApp"""
        self.nroApp += 10
        return self
    
    def __neg__(self):
        """Disminuye el espacio en 5 GB"""
        self.espacio -= 5
        return self
    
    def mostrar_datos(self):
        print(f"Número: {self.nroTel}")
        print(f"Dueño: {self.dueño}")
        print(f"Espacio: {self.espacio} GB")
        print(f"RAM: {self.ram} GB")
        print(f"Apps: {self.nroApp}")
        print("-" * 20)

mi_celular = Celular("123456789", "Juan", 128, 8, 15)

print("ANTES DE OPERADORES:")
mi_celular.mostrar_datos()
+mi_celular
-mi_celular
print("DESPUÉS DE OPERADORES:")
mi_celular.mostrar_datos()