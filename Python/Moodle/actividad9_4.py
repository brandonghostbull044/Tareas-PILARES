from functools import reduce 
texto = input('Ingresa una lista de números, separados por cómas uno de otro. ---> ')

def suma(a, b):
    return a + b

lista = []
for num in texto.split(','):
    lista.append(int(num))
    
print(f'El cuadrado de tus número es: {reduce(suma, lista)}')

