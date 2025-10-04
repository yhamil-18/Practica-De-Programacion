class Buzon:
    def __init__(self, numero):
        self.numero = numero
        self.cartas = [] 
    
    def agregar_carta(self, codigo, remitente, destinatario):
        self.cartas.append([codigo, remitente, destinatario])
    
    def mostrar(self):
        print(f"Buzón {self.numero}:")
        for carta in self.cartas:
            print(f"  {carta[0]} - De: {carta[1]} Para: {carta[2]}")

class Carta:
    def __init__(self, codigo, descripcion):
        self.codigo = codigo
        self.descripcion = descripcion

print("=== a) BUZONES ===")
b1 = Buzon("001")
b1.agregar_carta("C123", "Juan Álvarez", "Peter Chaves")
b1.agregar_carta("C456", "Pepe Mujica", "Wilmer Pérez")
b1.agregar_carta("C789", "Paty Vasques", "Pepe Mujica")

b2 = Buzon("002")
b2.agregar_carta("C111", "Maria Lopez", "Carlos Ruiz")
b2.agregar_carta("C222", "Ana Garcia", "Pedro Martinez")
b2.agregar_carta("C333", "Luis Torres", "Maria Lopez")

b3 = Buzon("003")
b3.agregar_carta("C444", "Wilmer Pérez", "Juan Álvarez")
b3.agregar_carta("C555", "Peter Chaves", "Paty Vasques")
b3.agregar_carta("C666", "Carlos Ruiz", "Pepe Mujica")

b1.mostrar()
b2.mostrar()
b3.mostrar()

print("\n=== b) CARTAS ===")
c1 = Carta("C123", "Querido amigo te escribo para decirte que ella no te ama...")
c2 = Carta("C456", "Hola Wilmer, el amor verdadero llegará cuando menos lo esperes.")
c3 = Carta("C789", "Pepe, necesito hablar contigo sobre trabajo.")

print(f"Carta {c1.codigo}: {c1.descripcion}")
print(f"Carta {c2.codigo}: {c2.descripcion}")
print(f"Carta {c3.codigo}: {c3.descripcion}")

print("\n=== c) CARTAS RECIBIDAS ===")
def contar_cartas(buzones, destinatario):
    total = 0
    for buzon in buzones:
        for carta in buzon.cartas:
            if carta[2] == destinatario:
                total += 1
    return total

print(f"Pepe Mujica recibió: {contar_cartas([b1, b2, b3], 'Pepe Mujica')} cartas")

print("\n=== d) ELIMINAR CARTA ===")
for buzon in [b1, b2, b3]:
    for carta in buzon.cartas:
        if carta[0] == "C456":
            buzon.cartas.remove(carta)
            print("Carta C456 eliminada")

b1.mostrar()

print("\n=== e) QUIÉN ENVIÓ Y RECIBIÓ ===")
todos_remitentes = []
todos_destinatarios = []

for buzon in [b1, b2, b3]:
    for carta in buzon.cartas:
        todos_remitentes.append(carta[1])
        todos_destinatarios.append(carta[2])

for persona in set(todos_remitentes):
    if persona in todos_destinatarios:
        print(f"{persona} envió y recibió cartas")

print("\n=== f) y g) BUSCAR 'amor' ===")
cartas_desc = [c1, c2, c3]
for carta in cartas_desc:
    if "amor" in carta.descripcion.lower():

        for buzon in [b1, b2, b3]:
            for c in buzon.cartas:
                if c[0] == carta.codigo:
                    print(f"Carta {carta.codigo}:")
                    print(f"  De: {c[1]}")
                    print(f"  Para: {c[2]}")
                    print(f"  Texto: {carta.descripcion}")