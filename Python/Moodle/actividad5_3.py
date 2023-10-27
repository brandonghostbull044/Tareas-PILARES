cantidad = float(input('Ingresa una cantidad: '))
porcentaje = int(input('Ingresa el porcentaje de interes: '))
if porcentaje > 30:
    print(f'El total es: {cantidad + (cantidad * (float("0" + "." + str(porcentaje))))}')
else:
    print(f'El total es: {cantidad}')

