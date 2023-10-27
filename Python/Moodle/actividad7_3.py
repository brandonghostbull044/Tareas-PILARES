class Cuenta(object):
    def __init__(self, titular, cantidad = 100):
        self.__titular = titular
        self.__cantidad = cantidad
    
    @property
    def titular(self):
        return self.__titular
    
    @titular.setter
    def titular(self, titular):
        self.__titular = titular
    
    @property
    def cantidad(self):
        return self.__cantidad
    
    @cantidad.setter
    def cantidad(self, cantidad):
        self.__cantidad = cantidad
        
    def mostrar(self):
        return(f'Titular: {self.__titular}\nCantidad: {self.__cantidad}\n')
    
    def ingresar(self, cantidad):
        if cantidad > 0:
            self.__cantidad += cantidad
    
    def retirar(self, cantidad):
        if cantidad > 0:
            self.__cantidad -= cantidad
        else:
            print('Cantidad invalida')
                
class CuentaJoven(Cuenta):
    def __init__(self, titular, bonif, edad, cantidad = 100):
        super().__init__(titular, cantidad)
        self.__bonif = bonif
        self.__edad = edad
        
    @property
    def bonif(self):
        return self.__bonif
    
    @bonif.setter
    def bonif(self, bonif):
        self.__bonif = bonif
        
    @property
    def edad(self):
        return self.__edad
    
    @edad.setter
    def edad(self, edad):
        self.__edad = edad
    
        
    def titularValido(self):
        return self.__edad >= 18 and self.__edad < 25
    
    def retirar(self, cantidad):
        if cantidad > 0:
            if self.titularValido():
                self.cantidad -= cantidad
            else:
                print('Titular no valido')
        else:
            print('Cantidad invalida')
        
    
    def mostrar(self):
        return f'Cuenta Joven:\n  {super().mostrar()}  Bonificacion: {self.__bonif}%'
            


joven1 = CuentaJoven('Alan', 15, 18)
print('Construccion de instancia con cantidad vacía:')
print(joven1.mostrar())

joven2 = CuentaJoven('Beto', 22, 17, 1000)
print('\nConstruccion de instancia con datos completos: ')
print(joven2.mostrar())  

print('\nIngreso en cuenta: ')
joven1.ingresar(100)
print(joven1.mostrar())

print('\nRetiro en cuenta: ')
joven1.retirar(100)
print(joven1.mostrar())

print('\nNegacion de retiro a titular no valido: ')
joven2.retirar(250)
