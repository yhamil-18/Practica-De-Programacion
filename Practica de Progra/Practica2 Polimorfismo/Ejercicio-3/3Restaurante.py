from abc import ABC, abstractmethod

class Empleado(ABC):
    def __init__(self, nombre, sueldo_mes):
        self.nombre = nombre
        self.sueldo_mes = sueldo_mes

    @abstractmethod
    def sueldo_total(self):
        pass

    def mostrar_si_sueldo_es(self, x):
        if self.sueldo_mes == x:
            print(f"{self.__class__.__name__} - Nombre: {self.nombre}, SueldoMes: {self.sueldo_mes}")


class Cocinero(Empleado):
    def __init__(self, nombre, sueldo_mes, horas_extras, sueldo_hora):
        super().__init__(nombre, sueldo_mes)
        self.horas_extras = horas_extras
        self.sueldo_hora = sueldo_hora

    def sueldo_total(self):
        return self.sueldo_mes + (self.horas_extras * self.sueldo_hora)

    def __str__(self):
        return f"Cocinero: {self.nombre} - Sueldo Total: {self.sueldo_total():.2f}"


class Mesero(Empleado):
    def __init__(self, nombre, sueldo_mes, horas_extras, sueldo_hora, propina):
        super().__init__(nombre, sueldo_mes)
        self.horas_extras = horas_extras
        self.sueldo_hora = sueldo_hora
        self.propina = propina

    def sueldo_total(self):
        return self.sueldo_mes + (self.horas_extras * self.sueldo_hora) + self.propina

    def __str__(self):
        return f"Mesero: {self.nombre} - Sueldo Total: {self.sueldo_total():.2f}"


class Administrativo(Empleado):
    def __init__(self, nombre, sueldo_mes, cargo):
        super().__init__(nombre, sueldo_mes)
        self.cargo = cargo

    def sueldo_total(self):
        return self.sueldo_mes  

    def __str__(self):
        return f"Administrativo: {self.nombre}, Cargo: {self.cargo} - Sueldo Total: {self.sueldo_total():.2f}"

# Crear objetos
cocinero = Cocinero("Luis", 1200, 10, 5.5)
mesero1 = Mesero("Ana", 900, 8, 4.0, 100.0)
mesero2 = Mesero("Carlos", 950, 6, 4.5, 80.0)
admin1 = Administrativo("Laura", 1100.0, "Gerente")
admin2 = Administrativo("Mario", 1100.0, "Contador")


empleados = [cocinero, mesero1, mesero2, admin1, admin2]


for emp in empleados:
    print(emp)


print("\nEmpleados con sueldo base igual a 1100.0:\n")
for emp in empleados:
    emp.mostrar_si_sueldo_es(1100.0)
