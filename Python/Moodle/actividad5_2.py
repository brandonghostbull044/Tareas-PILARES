
while True:
    numero = input('\nIntroduce un número y te diré si está en el rango o "Exit" para salir: ')
    try:
        float(numero)
        if float(numero) > 0 and float(numero) < 8:
            print('\nEstá dentro del rango.')
        else:
            print('Está fuera del rango.')
    except:
        if numero.lower() != 'exit':
            print('Error: No introdujiste un número.')
        else:
            print('\nAdios.')
            break