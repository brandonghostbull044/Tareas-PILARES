#1
import random
respuesta = str(input('Introduce "Init" para iniciar el programa: '))
lista = []
if respuesta.lower() == 'init':
    while len(lista) < 10:
        agregado = random.randint(0, 10)
        if agregado not in lista:
            lista.append(agregado)
            print(f' \nNúmero {len(lista)}: {agregado}\nCuadrado: {agregado**2}\nCubo: {agregado**3}\n')