frutas = {'pera': 7, 'higo': 4, 'manzana': 5, 'platano': 3, 'durazno': 5, 'mango': 12, 'uva': 1}

print('----------Bienvenido----------\nPara empezar a agregar frutas a tu pedido ingresa el nombre de la fruta y la cantidad separado por una coma.\nSi quieres terminar de agregar pedidos coloca ingresa la palabra "Ok"')
pedido = {}
totalPedido = 0
contador = 0
while True:
  peticion = input('--->')
  
  if peticion.lower() != 'ok':
    try:
      precio = float(frutas[peticion.split(',')[0].lower()])
      cantidad = float(peticion.split(',')[1])
      fruta = peticion.split(',')[0]
      
      pedido[fruta] = f'{cantidad}, {cantidad * precio}'
      totalPedido += cantidad * precio
      print(f'${cantidad * precio}')
    except:
      print('No hay de la fruta que estás pidiendo.')
  else:
    contador += 1
    print(contador)
    print(f'Resúmen del Pedido {contador}:\n')
    for articulo in pedido:
      print(f'   Producto:  {articulo},  Cantidad:   {pedido[articulo].split(",")[0]},  Total:   ${pedido[articulo].split(",")[1]}\n')
    print(f'\nTotal del pedido: ${totalPedido}')
    pregunta = input('\n¿Quieres hacer otra venta?.(si/no).---> ')
    if pregunta.lower() == 'si':
      continue
    else:
        break


