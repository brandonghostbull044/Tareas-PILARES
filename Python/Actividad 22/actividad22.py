sueldo = float(input('Ingresa tu sueldo: '))
if sueldo < 1000:
    print(f'Tu nuevo sueldo es: ${sueldo * 1.15}')
else:
    print(f'Tu nuevo sueldo es: ${sueldo * 1.12}')