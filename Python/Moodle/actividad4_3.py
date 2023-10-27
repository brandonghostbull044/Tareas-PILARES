respuesta = str(input('Introduce "Init" para iniciar el programa: '))
if respuesta.lower() == 'init':
    calificaciones = input('Introduce tus calificacione, separas por comas una de otra: ')
    contador = 0
    print(f'Tus calificaciones son:')
    calnums = []
    while contador < 5:
        print(f'Calificación {contador + 1}: {calificaciones.split(",")[contador].strip()}')
        calnums.append(float(calificaciones.split(",")[contador].strip()))
        contador += 1
        
    calnums.sort()
    print(f'Promedio: {sum(calnums) / len(calnums)}\nNota mayor: {calnums[-1]}\nNota menor: {calnums[0]}')