cadena = 'Soy una cadena string'

#Las funciones son bloques de código que pueden ser invocados
#Los métodos son bloques de código que viven dentro de una clase. Los métodos requieren de paréntesis al terminar. Un métdodo requiere de un objeto
#En Python el punto indica que va a acceder a todo lo que contiene la clase 

#Esta función nos sirve para imprimir los métododos que podemos usar en la variable que especifiquemos
print(dir(cadena))
print(cadena.upper())
print(cadena.lower())
print(cadena.title())

print(len(cadena))
print(cadena.replace('a', 'b'))
print(cadena.split(' '))