cesta = {}
totaln = 0
while True:
    articulo = input('Ingresa un articulo o "listo" para terminar; ')
    if articulo.lower() != 'listo':
        precio = float(input('Ingresa el precio: '))
        cantidad = float(input('Ingresa la cantidad: '))
        totaln = totaln + (precio * cantidad)
        cesta[articulo] = str(f'{precio}, {cantidad}')
    else:
        if totaln > 0:
            print('Articulos:')
            for n in cesta:
                print(f'   {n} - {cesta[n].split(",")[0]} cantidad: {cesta[n].split(",")[1]} ')
            print(f'Total: {totaln}')
            break
        else:
            print('No tienes nada en la cesta')
            break
       
   