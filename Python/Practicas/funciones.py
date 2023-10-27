print("""------Bienvenido-------
      ¿En qué te puedo ayudar
      a) Calcuar el area de unm circulo
      b) Calcular el volumen de un cilindro""")

def calc_area_circle():
        import math

        while True:
            radio = input('Ingresa el radio del circulo: ')
            try:
                radio = float(radio)
                print(math.pi * (radio**2))
            except:
                if radio.lower() == 'exit':
                    break
                else:
                    print('Error: No  introdujiste un numero')
funciones = {
        'a': calc_area_circle,
        'b': 2
    }

while True:
    eleccion = input('---> ')
    funciones[eleccion]
