texto = input('Ingresa un texto: ')
#1
print(len(f'La longitud de tu texto es {texto}'))

#2
print(f'La primera letra de tu texto es: "{texto[0]}" y la última letra es: "{texto[-1]}"')

#3
print(f'Aquí tienes un substring de tu texto del índice 2 al 4: "{texto[2:5]}"')

#4
print(f'Aquí tienes tu texto sin espacios "{texto.replace(" ", "")}"')

#5
texto2 = input('Ingresa un texto en minúsculas y lo convertiré a mayúsculas: ')
print(f'Aquí está tu texto en minúsculas. "{texto2.upper()}"')

#6
texto3 = input('Ingresa un texto en mayúsculas y lo convertiré a minúsculas: ')
print(f'Aquí está tu texto en minúsculas. "{texto3.lower()}"')

#7
texto4 = input('Ingresa un texto que contengas letras "a" y le quitaré las letras "a": ')
print(texto4.replace('a', ''))

#8
text5 = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
#a
puntos = text5.split('.')
print(f'El dominio de tu correo es: "{puntos[1][9:]}.{puntos[2]}.{puntos[3][:2]}"')
#b
print(f'Tu correo completo es: "{puntos[0].split(" ")[1]}.{puntos[1]}.{puntos[2]}.{puntos[3][:2]}"')
#c
print(f'El año es: "{puntos[-1].split(" ")[-1]}"')