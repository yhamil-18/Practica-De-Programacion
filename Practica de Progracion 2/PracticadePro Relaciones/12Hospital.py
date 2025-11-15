class Doctor:
    def __init__(self, nombre, especialidad):
        self.nombre = nombre
        self.especialidad = especialidad
    
    def __str__(self):
        return f"Dr. {self.nombre} - {self.especialidad}"

class Hospital:
    def __init__(self, nombre):
        self.nombre = nombre
        self.doctores = []
    
    def asignar_doctor(self, doctor):
        self.doctores.append(doctor)
    
    def mostrar_doctores(self):
        print(f"Doctores del {self.nombre}:")
        for doctor in self.doctores:
            print(f"  - {doctor}")
        print()

doctor1 = Doctor("Juan Pérez", "Cardiología")
doctor2 = Doctor("María García", "Pediatría")
doctor3 = Doctor("Carlos López", "Cirugía")

hospital1 = Hospital("Hospital Central")
hospital2 = Hospital("Hospital del Norte")

hospital1.asignar_doctor(doctor1)
hospital1.asignar_doctor(doctor2)

hospital2.asignar_doctor(doctor2)  
hospital2.asignar_doctor(doctor3)
hospital1.mostrar_doctores()
hospital2.mostrar_doctores()