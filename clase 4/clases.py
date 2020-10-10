class Punto():
    #Un método que define como crear un punto:
    def  __init__(self, numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2

p = Punto(10.2,3.5)
print(p.numero1)
print(p.numero2)

class Vuelo():

    def __init__(self, numero, capacidad):
        self.numero = numero
        self.capacidad = capacidad
        self.pasajeros = []
    
    def agregar_pasajeros(self, nombre):
        if not self.asientos_disponibles():
            return False
        self.pasajeros.append(nombre)
        return True

    def asientos_disponibles(self):
        return self.capacidad - len(self.pasajeros)

vuelo147 = Vuelo(147, 2)


personas = ["Harry", "Ron", "Hermione"]

for una_persona in personas:
    if vuelo147.agregar_pasajeros(una_persona):
        print(f"Se agrego a {una_persona} al vuelo numero {vuelo147.numero}")
    else:
        print(f"No se pudo agregar a {una_persona} por limite de la capacidad")