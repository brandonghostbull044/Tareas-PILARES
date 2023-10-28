import random
AHORCADO = ['''
      +---+
      |   |
          |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========''']

palabras = ['Aficionado', 'Gente', 'Software', 'Presionar', 'Disponible', 'Comer', 'Pensar', 'Infectar', 'Vestir', 'Optico', 'Iracundo', 'Aprovechar', 'Rastrillo', 'Terremoto', 'Francotirador', 'Transporte', 'Niñera', 'Sufrir', 'Forzar', 'Efímera', 'Telaraña', 'Dependiente', 'Amargo', 'Solicitar', 'Amoroso']

relaciones = ['Fan Amateur Entusiasta', 'Poblacion Pueblo Hombre', 'Informatica Computadora Codigo', 'Forzar Apretar Exigir', 'Libre Accesible Posible', 'Ingerir Pan Cuchara', 'Concebir Creer Considerar', 'Cortada Inyeccion Hongo', 'Ponerse Calzar Usar', 'Lente Prisma Oculista', 'Colera Rabia Enojo', 'Beneficiarse Basarse Recurrir', 'Bello Facial Barba', 'Sismo Tectonico Temblor', 'Bala Asesino Punteria', 'Tren Burro Mercancia', 'Bebe Cuidar Nana', 'Padecer Soportar Innecesario', 'Obligar Impulsar Romper', 'Fugaz Temporal Transitorio', 'Araña Red Tejido', 'Filial Vincilado Subsidiario', 'Agrio Acido Resentido', 'Pedir Disponer Recurrir', 'Cariño Encanto Romatico']

class Juego():
    def __init__(self):
        self.__ahorcado = int
        self.__secreta = str
        self.__encontradas = list
        self.__relacion = str
        self.__formacion = str
        self.__confirmacion = str
        
    def definir(self):
        self.__ahorcado = 0
        self.__secreta = random.choice(palabras).lower()
        self.__relacion = relaciones[palabras.index(self.__secreta.capitalize())].split()[random.randrange(3)]
        self.__formacion = ' _ ' * len(self.__secreta)
        self.__confirmacion = ''
        self.__encontradas = []
    
    def jugada(self, entrada):
        if entrada.lower() in self.__secreta and entrada.lower() not in self.__encontradas:
            contador = -1
            form = self.__formacion.replace(' ', '').lower()
            for i in self.__secreta:
                contador += 1
                if entrada == i:
                    l = list(form)
                    l[contador] = i
                    form = "".join(l)
            self.__formacion = form.replace('', ' ').strip().capitalize()
            self.__encontradas.append(entrada.lower())
            self.__confirmacion = 'Correcto.'
        elif entrada.lower() in self.__encontradas:
            self.__confirmacion = 'Palabra ya encontrada.'
        else:
            self.__ahorcado += 1
            self.__confirmacion = 'Incorrecto.'
    
    def obtenDatos(self):
        return str(f'{self.__ahorcado}, {self.__secreta}, {self.__formacion.replace(" ", "").lower()}')
    
    def impresion(self):
        print(f'\n\n{self.__confirmacion}\n\n{AHORCADO[self.__ahorcado]}\n\n------>Palabra relacionada con: "{self.__relacion}"<------\n\n\n               {self.__formacion}\n\n')
    
while True:
    name = input('Ingresa tu nombre para iniciar el juego o "Exit" para salir del juego: ')
    if name.lower() != 'exit':
        jugador = Juego()
        jugador.definir()
        jugador.impresion()
        while True:
            ahorcado = int(jugador.obtenDatos().split(',')[0])
            secreta = jugador.obtenDatos().split(',')[1]
            formacion = jugador.obtenDatos().split(',')[2]
            if ahorcado < 6 and secreta != formacion:
                palabra = input('---> ').replace(' ', '')
                jugador.jugada(palabra)
                jugador.impresion()
            elif ahorcado < 6 and secreta == formacion:
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
            else:
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
                break
    else:
        print('\n\nAdios.\n\n')
        break