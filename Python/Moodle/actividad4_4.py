respuesta = str(input('Introduce "Init" para iniciar el programa: '))
if respuesta.lower() == 'init':
    alumnos = {}
    while True:
        respuesta2 = input('Introduce el nombre de un alumno o "Exit" para salir: ')
        
        if respuesta2.lower() != 'exit' and respuesta2 not in alumnos:
            calificaciones = input('Introduce sus calificaciones separadas por comas una de otra: ')
            calstring = calificaciones.split(',')
            calnums = []
            contador = 0
            for cal in calstring:
                num = float(calstring[contador].strip())
                calnums.append(num)
                contador += 1
            alumnos[respuesta2] = calnums
        elif respuesta2.lower() != 'exit' and respuesta2 in alumnos:
            print('El alumno ya existe en la lista.')
        else:
            break
    print(f'\nLista de alumnos: ')
    for alumno in alumnos:
        print(f'\n   {alumno}\n     Promedio: {round(sum(alumnos[alumno]) / len(alumnos[alumno]), 2)}')