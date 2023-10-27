respuesta = str(input('Introduce "Init" para iniciar el programa: '))
if respuesta.lower() == 'init':
    meses = ('Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre')
    while True:
        peticion = int(input('Introduce un número: '))
        if peticion <= len(meses) and peticion > 0:
            print(f'El mes {peticion} es: {meses[(peticion -1)]}')
        elif peticion > len(meses) or peticion < 0:
            print('\nNumero incorrecto')
        else:
            print('\nPrograma terminado;')
            break