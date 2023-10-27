class Empleado:
    def __init__(self, nombre, edad, expediente, sueldo):
        self.nombre = nombre
        self.__edad = edad
        self.expediente = expediente
        self.sueldo = sueldo
    
    def calcularSueldo(self, descuento, bono):
        return (self.sueldo - descuento) * bono
    

empleado1 = Empleado('Jorge', 45, '345', 8000)

print(empleado1.calcularSueldo(1000, 2))
