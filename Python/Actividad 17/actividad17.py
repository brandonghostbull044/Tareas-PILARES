#a
texto = input('Ingresa el log: ')
print(f'El corre electrónico de tu log es: "{texto.split(" ")[1]}"')

#b
print(f'La hora de recepción es: "{texto.split(" ")[-3]}"')

#c
print(f'EL dominio del correo es: "{texto.split(" ")[1].split("@")[1]}"')

#d
print(f'El año de recepción es: "{texto.split(" ")[-1]}"')

#e
print(f'El mes de recepción es: "{texto.split(" ")[-6]}"')