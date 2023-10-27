class Diccionario:
    def __init__(self, texto):
        self.texto = texto
    
    def crearDiccionario(self, texto):
        diccionario = {}
        for car in texto:
            if car in diccionario:
                diccionario[car] = int(diccionario[car]) + 1
            else:
                diccionario[car] = 1
        return diccionario

while True:
    peticion = input('\nIngresa un texto o "Exit" para salir: ')
    if peticion.lower() != 'exit':
        dic = Diccionario(peticion)
        print(dic.crearDiccionario(peticion))
    else:
        print('\nAdios.')
        break