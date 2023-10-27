while True:
    numero = input('\nIntroduce un número y te diré si es positivo, negativo o nulo o "Exit" para salir: ')
    try:
        float(numero)
        if float(numero) > 0:
            print('\nPositivo.')
        elif float(numero) < 0:
            print('\nNegativo.')
        else:
            print('\nNulo.')
    except:
        if numero.lower() != 'exit':
            print('\nError: No introdujiste un número.')
        else:
            print('\nAdios.')
            break