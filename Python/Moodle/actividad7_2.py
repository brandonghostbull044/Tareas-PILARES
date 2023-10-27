class Cuenta:
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
    
cuenta1 = Cuenta('Alberto')
print('Construccion de instancia con cantidad vacía:')
print(cuenta1.mostrar())


cuenta2 = Cuenta('Brandon', 2000)
print('\nConstruccion de instancia con datos completos: ')
print(cuenta2.mostrar())  

print('\nIngreso en cuenta: ')
cuenta1.ingresar(100)
print(cuenta1.mostrar())

print('\nRetiro en cuenta, quedando en numeros negativos: ')
cuenta1.retirar(250)
print(cuenta1.mostrar())