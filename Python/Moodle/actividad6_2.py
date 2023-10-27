while True:
    peticion = input('¿Cuántos números primos quieres?. ---> ')
    try:
        1 / int(peticion)
        aprovacion = True
    except:
        if peticion.lower() != 'exit':
            print('Error: No introjiste un número correcto.')
            aprovacion = False
        else:
            print('\nAdios.\n')
            break
    if aprovacion:
        peticion = int(peticion)
        if peticion > int(1):
            contador = 0
            contador2 = 3
            contador3 = 2
            print(2)
            while contador < (peticion - 1):
                lista = list(range(1, contador2))
                for n in lista:
                    num = int(n)
                    operacion = int(contador2) % num
                    if operacion == 0:
                        continue
                    else:
                        contador3 += 1
                if contador3 == contador2:
                    contador += 1
                    print(contador2)
                contador2 += 1
                contador3 = 2
        else:
            print(2)