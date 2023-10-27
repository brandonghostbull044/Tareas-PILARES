class Persona:
    def __init__(self, nombre = 'Fulanito', edad = 17, dni = 'AEQ234'):
        self.__nombre = nombre
        self.__edad = edad
        self.__dni = dni
    
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre
        
    @property
    def edad(self):
        return self.__edad
    
    @edad.setter
    def edad(self, edad):
        self.__edad = edad
    
    @property
    def dni(self):
        return self.__dni
    
    @dni.setter
    def dni(self, dni):
        self.__dni = dni
        
    def mostrar(self):
        return(f'Nombre: {self.__nombre}\nEdad: {self.__edad}\nDNI: {self.__dni}')
    
    def esMayorDeEdad(self):
        return(self.__edad >= 18)
    
persona1 = Persona()
print('Construccion de instancia vacía:')
print(persona1.mostrar())
print(persona1.esMayorDeEdad())

persona2 = Persona('Brandon', 22, 'ASDAW123')
print('\nConstruccion de instancia con datos: ')
print(persona2.mostrar())  
print(persona2.esMayorDeEdad())    

persona1.edad = 22
persona1.dni = 'JGTYHJ12'
print('\nModificacion de "edad" i "DNI" de la primera instancia')
print(persona1.mostrar())
print(persona1.esMayorDeEdad())