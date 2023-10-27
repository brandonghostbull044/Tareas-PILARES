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
    def __init__(self, nombre, confirmacion = '', ahorcado = -1, encontradas = [], formacion = '', secreta = '', relacion = ''):
        self.__nombre = nombre
        self.__ahorcado = ahorcado
        self.__secreta = secreta
        self.__encontradas = encontradas
        self.__relacion = relacion
        self.__formacion = formacion
        self.__confirmacion = confirmacion
        
    @property
    def ahorcado(self):
        return self.__ahorcado
    
    @ahorcado.setter
    def ahorcado(self, ahorcado):
        self.__ahorcado = ahorcado
        
    @property
    def secreta(self):
        return self.__secreta
    
    @property
    def encontradas(self):
        return self.__encontradas
    
    @encontradas.setter
    def encontradas(self, encontradas):
        self.__encontradas = encontradas
    
    @property
    def formacion(self):
        return self.__formacion
    
    @formacion.setter
    def formacion(self, formacion):
        self.__formacion = formacion
    
    @property
    def confirmacion(self):
        return self.__confirmacion
    
    @confirmacion.setter
    def confirmacion(self, confirmacion):
        self.__confirmacion = confirmacion
        
        
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
                    
            form = form.replace('', ' ')
            self.__formacion = form.strip().capitalize()
            self.__encontradas.append(entrada.lower())
            self.__confirmacion = 'Correcto.'
        elif entrada.lower() in self.__encontradas:
            self.__confirmacion = 'Palabra ya encontrada.'
        else:
            self.__ahorcado += 1
            self.__confirmacion = 'Incorrecto'
    
    def obtenAhorcado(self):
        return self.__ahorcado
    
    def obtenerSecreta(self):
        return self.__secreta

    def obtenerFormacion(self):
        return self.__formacion.replace(' ', '').lower()

    def obtenerNombre(self):
        return self.__nombre
    
    def impresion(self):
        print(f'\n\n{self.__confirmacion}\n\n{AHORCADO[self.__ahorcado]}\n\n------>Palabra relacionada con: "{self.__relacion}"<------\n\n\n               {self.__formacion}\n\n')
        

while True:
    name = input('Ingresa tu nombre para iniciar el juego o "Exit" para salir del juego: ')
    if name.lower() != 'exit':
        jugador = Juego(name)
        jugador.definir()
        jugador.impresion()
        while True:
            ahorcado = jugador.obtenAhorcado()
            secreta = jugador.obtenerSecreta()
            formacion = jugador.obtenerFormacion()
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
    