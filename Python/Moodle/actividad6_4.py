while True:
    respuesta = input('\nIntroduce un número y te devolveré su factorial o "Exit" para cerrar el programa: ')
    if respuesta.lower() != 'exit':
        try:
            num = int(respuesta)
            n = int(1)
            factorial = 1
            while n <= num:
                factorial = factorial * n
                n += 1
            print(f'\nFactorial: {factorial}')
        except:
            print('\nError: No introdujiste un numero')
    else:
        print('\nAdios;')
        break