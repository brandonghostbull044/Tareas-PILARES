texto = input('Ingresa una lista de números, separados por cómas uno de otro. ---> ')
def esMayor(x):
    return x > 5

lista = []
for num in texto.split(','):
    lista.append(int(num))
print(f'La cantidad de números mayores en tu lista es: {len(list(filter(esMayor, lista)))}')