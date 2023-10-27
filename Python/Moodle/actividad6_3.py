pago = 10
mes = 1
pagos = []
while mes < 21:
    print(f'Pago número: {mes}: ${pago}')
    pagos.append(pago)
    mes += 1
    pago = pago * 2
    
print(f'\nTotal a pagar: ${sum(pagos)}')
