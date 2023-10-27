valor = float(input('Ingresa un valor: '))
if valor >= 0 and valor <= 100:
    if valor < 50:
        print('El valor está dentro del rango 0 a 100 y es menor a 50')
    else:
        print('El valor está dentro del rango 0 a 100 y es mayor o igual a 50')
else:
    print('El valor no está dentro del rango')