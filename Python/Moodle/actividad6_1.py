print('---------------->Bienvenido<----------------\n--->Elije la opcion que deseas:\n---> a) Comer pizza\n---> b) Comer pozole\n---> c) Comer camarones\n---> d) Comer comida china\nO escribe "Exit" para salir del programa.')
while True:
    peticion = input('¿Qué deseas?---> ').lower()
    respuestas = {'a': '\nPara comer pizza te recomiendo que vayas a:\n    1) Little Caesars\n    2) La pizzería que está en la base.\n ¿A cual quieres ir?: ', 'b': '\nPara comer pozole te recomiendo que vayas a:\n    1) Los Dorados en Boulevares\n    2) La casa de Toño.\n ¿A cual quieres ir?: ', 'c': '\nPara comer camarones te recomiendo que vayas a:\n    1) El Chairel\n    2) Fhishers.\n ¿A cual quieres ir?: ', 'd': '\nPara comer comida china te recomiendo que vayas a:\n    1) La terraza.\n    2) Sakana Roll.\n ¿A cual quieres ir?: '}
    ubicaciones = {'a1': 'Aquí tienes la ubicación: https://maps.app.goo.gl/bJu6FMvzzyDCCEWv7', 'a2': 'Aquí tienes la ubicación: https://maps.app.goo.gl/Y5Tb6AMyUWQgGGveA', 'b1': 'Aquí tienes la ubicación: https://maps.app.goo.gl/MwV7EcDfe8vG3XcU8', 'b2': 'Aquí tienes la ubicación: https://maps.app.goo.gl/aZmAZShRYtozdnfG6', 'c1': 'Aquí tienes la ubicación: https://maps.app.goo.gl/EGy5JLR7261imiyp9', 'c2': 'Aquí tienes la ubicación: https://maps.app.goo.gl/5aqutAKFJnUsSU847', 'd1': 'Aquí tienes la ubicación: https://maps.app.goo.gl/TKD2phxiEbqo6J296', 'd2': 'Aquí tienes la ubicación: https://maps.app.goo.gl/HN61bn8LUrmq1hjRA'}
    if peticion.lower() != 'exit':
        try:
            print(f'{respuestas[peticion]}')
            while True:
                try:
                    peticion2 = input('---> ')
                    print(ubicaciones[str(peticion + peticion2)])
                    break
                except:
                    print('La opción que seleccionaste no existe')
        except:
            print('La opción que seleccionaste no existe')
    else:
        print('\nAdios.\n')
        break