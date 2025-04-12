class Persona:
    def __init__(self, nombre, edad, ciudad):
        self.nombre = nombre
        self.edad = int(edad)
        self.ciudad = ciudad
    
    def __str__(self):
        return f"Nombre:{self.nombre}  Edad:{self.edad}  Ciudad:{self.ciudad}"
    
    def es_mayor(self):
        if self.edad >= 18:
            print("Es mayor de edad")
        else:
            print("Es menor de edad")
Juan = Persona('Juan', '20', 'Bolivia')
Maria = Persona('Maria', '10', 'Argentina')
Marcelo = Persona('Marcelo', '29', 'Paraguay')
print(Juan)
print(Maria)
print(Marcelo)
Juan.es_mayor()
Maria.es_mayor()
Marcelo.es_mayor()