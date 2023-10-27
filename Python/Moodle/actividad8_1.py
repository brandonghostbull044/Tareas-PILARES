class Diccionario:
    def __init__(self, cantidad):
        self.cantidad = cantidad
    
    def crearDiccionario(self, cantidad):
        diccionario = {}
        if cantidad > 1:
            contador = 1
            while contador <= cantidad:
                diccionario[contador] = contador**2
                contador += 1
        else:
            diccionario[1] = 1
        return diccionario

while True:
    peticion = input('\nIngresa un número entero o "Exit" para salir: ')
    try:
        peticion = int(peticion)
        print(Diccionario.crearDiccionario(peticion, peticion))
    except:
        if peticion.lower() != 'exit':
            print('\nIntroduce un número correcto')
        else:
            print('\nAdios.')
            break