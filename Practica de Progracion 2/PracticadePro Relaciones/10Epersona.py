class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

class Speaker(Persona):
    def __init__(self, nombre, apellido, edad, especialidad):
        super().__init__(nombre, apellido, edad)
        self.especialidad = especialidad

class Participante(Persona):
    def __init__(self, nombre, apellido, edad, noTicket):
        super().__init__(nombre, apellido, edad)
        self.noTicket = noTicket

class Charla:
    def __init__(self, lugar, nombreCharla, speaker):
        self.lugar = lugar
        self.nombreCharla = nombreCharla
        self.S = speaker
        self.np = 0
        self.P = [None] * 50

class Evento:
    def __init__(self, nombre):
        self.nombre = nombre
        self.nc = 0
        self.C = [None] * 50
    
    def edad_promedio_participantes(self):
        total_edad = 0
        total_participantes = 0
        
        for charla in self.C:
            if charla:
                for participante in charla.P:
                    if participante:
                        total_edad += participante.edad
                        total_participantes += 1
        
        return total_edad / total_participantes if total_participantes > 0 else 0

    def buscar_persona(self, nombre, apellido):
        for charla in self.C:
            if charla:
                if charla.S and charla.S.nombre == nombre and charla.S.apellido == apellido:
                    return f"Encontrado como Speaker en: {charla.nombreCharla}"
                for participante in charla.P:
                    if participante and participante.nombre == nombre and participante.apellido == apellido:
                        return f"Encontrado como Participante en: {charla.nombreCharla}"
        
        return "No encontrado"
    def eliminar_charlas_speaker(self, nombre, apellido):
        for i in range(len(self.C)):
            if self.C[i] and self.C[i].S and self.C[i].S.nombre == nombre and self.C[i].S.apellido == apellido:
                self.C[i] = None
                self.nc -= 1
    def ordenar_charlas_participantes(self):
        charlas_activas = [charla for charla in self.C if charla]
        charlas_activas.sort(key=lambda x: x.np, reverse=True)
        self.C = [None] * 50
        for i, charla in enumerate(charlas_activas):
            self.C[i] = charla

speaker1 = Speaker("Juan", "Pérez", 35, "Tecnología")
speaker2 = Speaker("María", "Gómez", 28, "Ciencia")

participante1 = Participante("Ana", "López", 25, 1001)
participante2 = Participante("Carlos", "Ruiz", 30, 1002)

charla1 = Charla("Auditorio A", "Inteligencia Artificial", speaker1)
charla1.P[0] = participante1
charla1.np = 1

charla2 = Charla("Sala B", "Machine Learning", speaker1)
charla2.P[0] = participante2
charla2.np = 1

charla3 = Charla("Sala C", "Ciencia de Datos", speaker2)
charla3.np = 0

evento = Evento("Tech Conference 2024")
evento.C[0] = charla1
evento.C[1] = charla2
evento.C[2] = charla3
evento.nc = 3

print(f"a) Edad promedio: {evento.edad_promedio_participantes()}")
print(f"b) Buscar Ana López: {evento.buscar_persona('Ana', 'López')}")
print(f"c) Charlas antes de eliminar: {evento.nc}")
evento.eliminar_charlas_speaker("Juan", "Pérez")
print(f"   Charlas después de eliminar: {evento.nc}")