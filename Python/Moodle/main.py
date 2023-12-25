import random
from Palabras import palabras
from Palabras import relaciones
from ahorcado_diagramas import AHORCADO

#Creamos la clase juego, que contendrá los métodos
class Juego():
    #Creamos el constructor del objeto
    def __init__(self):
        self.__ahorcado = int
        self.__secreta = str
        self.__encontradas = list
        self.__relacion = str
        self.__formacion = str
        self.__confirmacion = str
        
    #Primer método: El cual asignará valores iniciales a los atributos del objeto
    def definir(self):
        self.__ahorcado = 0
        self.__secreta = random.choice(palabras).lower()
        self.__relacion = relaciones[palabras.index(self.__secreta.capitalize())].split()[random.randrange(3)]
        self.__formacion = ' _ ' * len(self.__secreta)
        self.__confirmacion = ''
        self.__encontradas = []
    
    #Segundo método: El cual es la jugada.
    def jugada(self, entrada):
        #Creamos un filtro para asegurarnos de que la letra introducida por el usuario se encuentra en la palabra secreta y que no se encuentre en las letras ya encontradas
        if entrada.lower() in self.__secreta and entrada.lower() not in self.__encontradas:
            #Creamos un contador que servirá de index para las letras de la formación de la palabra secreta
            contador = -1
            #Variable que nos ayuda a quitarle los espacios a la formación de la palabra.
            form = self.__formacion.replace(' ', '').lower()
            #Iteración a la palabra secreta
            for i in self.__secreta:
                #Aumento de 1 al contador
                contador += 1
                #Filtro que nos permite saber si la entrada del usuario es igual al carácter iterado
                if entrada == i:
                    #Listamos la variable
                    l = list(form)
                    #Reemplazamos el guión bajo de la formación de palabra por la palabra iterada
                    l[contador] = i
                    #Asignamos la nueva formación a la variable
                    form = "".join(l)
            #Cambiamos el valor del atributo formación del usuario con la nueva formación creada, y le agregamos los espacios y mayúsculas a la primera letra. 
            self.__formacion = form.replace('', ' ').strip().capitalize()
            #Cambiamos el valor del atributo encontradas, agregandole la letra encontrada
            self.__encontradas.append(entrada.lower())
            #Cambiamos el valor del atributo confirmación para que se imprima y sepa el usuario que acertó la palabra
            self.__confirmacion = 'Correcto.'
        #Otro camino en el filtro que nos dice que la palabra que ingresó el usuario ya la ha encontrado
        elif entrada.lower() in self.__encontradas:
            #Cambiamos el valor del atributo para que se imprima y sepa el usuario que la palabra ingresada ya ha sido encontrada
            self.__confirmacion = 'Palabra ya encontrada.'
        #Si no se cumpĺe ninguna condición (La palabra ingresada es incorrecta)
        else:
            #Cambiamos el valor del atributo agorcado que nos sirve de index para el diagrama del ahorcado
            self.__ahorcado += 1
            #Cambiamos el valor del atributo confirmación para que se imprima y sepa el usuario que no acertó la palabra
            self.__confirmacion = 'Incorrecto.'
    
    #Tercer método: Que nos devuelve el valor de los datos del objeto (index de ahorcado, palabra secreta y la formación de palabra)
    def obtenDatos(self):
        return str(f'{self.__ahorcado}, {self.__secreta}, {self.__formacion.replace(" ", "").lower()}')
    
    #Cuarto método: El cual crea la impresión de pantalla, conformada por la cofirmación, el diagrama del ahorcado, la palabra relacionada con la secreta y la formación de palabra.
    def impresion(self):
        print(f'\n\n{self.__confirmacion}\n\n{AHORCADO[self.__ahorcado]}\n\n------>Palabra relacionada con: "{self.__relacion}"<------\n\n\n               {self.__formacion}\n\n')

#Iniciamos el flujo del juego con un ciclo while   
while True:
    #Pedimos al usuario su nombre o que ingrese "Exit" para terminar el juego
    name = input('Ingresa tu nombre para iniciar el juego o "Exit" para salir del juego: ')
    #Filtro para saber que usuario no ingresó "Exit"
    if name.lower() != 'exit':
        #Creamos el objeto
        jugador = Juego()
        #Iniciamos el método definir
        jugador.definir()
        #Iniciamos el método impresión
        jugador.impresion()
        #Iniciamos otro ciclo
        while True:
            #Creamos tres variables con los valores de los datos del objeto, obtenidos mediante el método obtenDatos
            ahorcado = int(jugador.obtenDatos().split(',')[0])
            secreta = jugador.obtenDatos().split(',')[1]
            formacion = jugador.obtenDatos().split(',')[2]
            #Filtro para saber que index de ahorcado es menor al 6 que es número máximo de errores permitidos y que la palabra secreta no sea igual a formación
            if ahorcado < 6 and secreta != formacion:
                #Pedimos al usuario una palabra
                palabra = input('---> ').replace(' ', '')
                #Iniciamos el método jugada
                jugador.jugada(palabra)
                #iniciamos el método impresion
                jugador.impresion()
            #Filtro para saber si la palabra secreta es igual a la formación, lo que quiere decir que el usuario ha ganado
            elif ahorcado < 6 and secreta == formacion:
                #Imprimimos las felicitaciones al usuario
                print(f"""               ¡Felicidades {name}!
────────────────────────────────
───────────────██████████───────
──────────────████████████──────
──────────────██────────██──────
──────────────██▄▄▄▄▄▄▄▄▄█──────
──────────────██▀███─███▀█──────
█─────────────▀█────────█▀──────
██──────────────────█───────────
─█──────────────██──────────────
█▄────────────████─██──████
─▄███████████████──██──██████ ──
────█████████████──██──█████████
─────────────████──██─█████──███
──────────────███──██─█████──███
──────────────███─────█████████
──────────────██─────████████▀
────────────────██████████
────────────────██████████
─────────────────████████
──────────────────██████████▄▄
────────────────────█████████▀
─────────────────────████──███
────────────────────▄████▄──██
────────────────────██████───▀
────────────────────▀▄▄▄▄▀
                      """)
                break
            #Si no se cumple ninguna condición (el usuario superó el número de errores)
            else:
                #Imprimimos el mensaje de que el usuario ha perdido
                print(f"""               Lo lamento {name}, has perdido.
                      
                      
                      
                        ──────────────────────────────────
                        ─────────▄██████████████████▄─────
                        ────────██▀░░░░░░░░░░░░░░░░▀██▄───
                        ───────█▌░░▄░░░░░░░▀▄▄▀░░░░░░▀█───
                        ──────█▌░░░▀███▄░░▀▄▄▄▄▀░░░░░░▀█──
                        ─────█▌░░░░█▀──▀▄░░░░░░░░░▄▄█▀░▐█─
                        ────█▌░░░░░█─────█░▄▄▄░░▄▀▀▀▀▄░░▐█
                        ───█▌░░░░░░█──█──█░░░░░█─────█░░░█
                        ──█▌░░░░░░░░▀▄▄▄▀░░░░░░█──█──█░░░█
                        ─█▌░░░░░░░░░░░░░░▄░░▄░░░▀▄▄▄▀░░░░█
                        █▌░░░░▄▀▀▄░░░░░▀▀░░░░▀▀░░░░░░░░░░█
                        █░░░░░▀▄░░░░░░░▄▀░▀▄░░░░░▄▀▀▄░░░░█
                        █░▐░░░░░▀▀▀▀▀▀▀░░░░░▀▀▄▄▄▄▄▄▀░░▌░█
                        █░░▌▄░░░░░░▄█▀▀█▀▀█▀▄░░░░░░░▄░▐░░█
                        █░░▌█▀█▀▀█▀─█──█──█──█▀▀█▀▀██░▐░░█
                        █░▐░█▄█▄▄█▄▄█▄▄█▄▄█▄▄█▄▄█▄██░░▐░░█
                        █░░░███████████████████████░░░░▌░█
                        █░░░█▄─█──█──█──█──█──█──█▀░░░░░░█
                        █░░░░▀██▄▄█▄▄█▄▄█▄▄█▄▄█▄█▀░░░░░░▐█
                        █▌░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄█▀
                        ─█▄░░░░░░░░░░░░░░░░░░░░░░░░░░░▄█──
                        ──█▄░░░░░░░▀▄▄▄▄▄▄▄▀░░░░░░░░░▄█───
                        ───██▄░░░░░░░░░░░░░░░░░░░░░▄██────
                        ────▀██▄░░░░░░░░░░░░░░░░░▄██▀─────
                        ──────▀███████████████████▀───────
                        
                        
                        """)
                #Se rompre el ciclo anidado
                break
    #Si no se cumple la condición (el usuario ingreso "EXit")
    else:
        #Imprimimos la despedida
        print('\n\nAdios.\n\n')
        #Se rompe el ciclo principal
        break