texto = input('Ingresa una lista de números, separados por cómas uno de otro. ---> ')
def suma(x):
    return x*x
    
lista = []
for num in texto.split(','):
    lista.append(int(num))
print(f'Aquí tienes los cuadrados de tu lista {list(map(suma, lista))}')