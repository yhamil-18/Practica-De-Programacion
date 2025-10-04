class Persona:
    def __init__(self, nombre, paterno,materno, edad, ci):
        self.nombre = nombre
        self.paterno = paterno
        self.materno = materno
        self.edad = edad 
        self.ci = ci
    
    def mostrarDatos(self):
        print(f"Nombre: {self.nombre} {self.paterno} {self.materno}, Edad: {self.edad}, CI: {self.ci}")
        
    def mayorDeEdad(self):
        if self.edad > 18:
            print("es mayor de edad")
        else:
            print("Es menor de edad")
    
    def modificarEdad(self, nuevo):
        self.edad = nuevo
        print(f"su nueva edad es {self.edad}")
        
p1 = Persona("Juan", "Lopez", "Perez", 17, 1231241)
p1.mostrarDatos()
p1.mayorDeEdad()
p1.modificarEdad(19)
p1.mayorDeEdad()
p2 = Persona("Pepe", "Perez", "Catillo", 19, 31242142)
p2.mostrarDatos()
p2.mayorDeEdad()
p2.modificarEdad(17)
p2.mayorDeEdad()

if p1.paterno == p2.paterno:
    print("son iguales")
else:
    print("son diferentes")