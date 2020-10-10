class Empleado():
    num_empleado = 0
    porcentaje_aumento = 1.04
    def __init__(self, nombre, apellido, sueldo):
        self.nombre = nombre
        self.apellido = apellido
        self.sueldo = sueldo
        self.email = nombre + '.' + apellido + '@miempresa.com'
        Empleado.num_empleado += 1

    def nombre_completo(self):
        return '{} {}'.format(self.nombre, self.apellido)
    
    def aplicar_aumento(self):
        self.sueldo = int(self.sueldo * self.porcentaje_aumento)
    

class Desarrollador(Empleado):
    porcentaje_aumento = 1.10
    def __init__(self, nombre, apellido, sueldo, lenguaje):
        super().__init__(nombre, apellido, sueldo)
        self.lenguaje = lenguaje

empleado1 = Desarrollador("Harry", "Potter", 999, "Python")
empleado1.aplicar_aumento()
print(empleado1.lenguaje)
empleado2 = Empleado("Ron", "Weasley", 999)
empleado2.aplicar_aumento()
print(empleado2.sueldo)


