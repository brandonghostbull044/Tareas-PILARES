#2
respuesta = str(input('Introduce "Init" para iniciar el programa: '))
if respuesta.lower() == 'init':
    lista = []
    while len(lista) < 5:
        if len(lista) <= 0:
            cadena = input('Introduce una cadena de texto; ')
            lista.append(cadena)
        else:
            cadena = input('Introduce otra cadena de texto; ')
            lista.append(cadena)
    print(f'\nAquí tienes tu lista invertida: ')
    for n in reversed(lista):
        print(n)