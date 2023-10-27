import random
aciertos = 0
total = 0
print('---------BIenvenido---------\nSe imprimirá en pantallla una multiplicación aleatoria y tendrás que escribir la respuesta. Si quieres terminar el programa escribe "Finish" y se imprimirá en pantalla en número de aciertos que tuviste.\n')
multiplicador = 0
while True:
    peticion = input('¿De cuantos dígitos quieres que sean los números a multiplicar? --> ')
    try:
        float(peticion)
        if float(peticion) > 0.0:
            while len(str(multiplicador)) != (int(peticion) + 1):
                multiplicador += 1
        else:
            print('Ingresa un número válido')
            continue
        break          
    except:
        print('Error de escritura')

multiplicador -= 1
print('\nEmpecemos.\n')   
while True:
    num1 = random.randrange(1, multiplicador + 1)
    num2 = random.randrange(1, multiplicador + 1)
    solucion = num1 * num2
    print(f'\n{num1}x{num2}')
    respuesta = input('--> ')
    try:
        respuesta = int(respuesta)
        if respuesta == solucion:
            print('Correcto')
            aciertos += 1
        else:
            print('Incorrecto')
        total += 1
    except:
        if respuesta.lower() == 'finish':
            print(f'\nObtuviste: {aciertos} aciertos de {total}\nAdios')
            break
        else:
            print('\nError de escritura.')