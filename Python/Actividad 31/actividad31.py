monto = float(input('Ingresa el monto: '))
if monto < 500:
    print(f'Cobra: ${monto}')
elif monto >= 500 and monto <= 1000:
    print(f'Cobra: ${monto * .95}')
elif monto > 1000 and monto <= 7000:
    print(f'Cobra: ${monto * .89}')
elif monto > 7000 and monto <= 15000:
    print(f'Cobra: ${monto * .82}')
else:
    print(f'Cobra: ${monto * .75}')
    