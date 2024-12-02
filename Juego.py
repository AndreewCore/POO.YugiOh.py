import random as rd
import Cartas
import Jugador

class Juego:
    def __init__(self, jugador, consola):
       self.jugador = jugador
       self.consola = consola

    @staticmethod
    def faseTomarCarta(jugador):
        input("Presione Enter para robar una carta.")
        jugador.robarCarta()
        print("\n")

    @staticmethod
    def fasePrincipal(jugador):
        t_monstruos_jugador = []
        t_magicas_trampas_jugador = []
        t_magicas = []
        for carta in jugador.tablero:
          if isinstance(carta, Cartas.CartaMonstruo):
              t_monstruos_jugador.append(carta)
          elif isinstance(carta, (Cartas.CartaMagia, Cartas.CartaTrampa)):
              t_magicas_trampas_jugador.append(carta)
        for carta in jugador.tablero:
            if isinstance(carta, Cartas.CartaMagia):
                t_magicas.append(carta)
        
        if len(jugador.tablero) <6:
            jugador.imprimirMano()
            if len(t_monstruos_jugador) == 3:
                eleccion = input("Seleccionar numero de la carta No Monstruo que quieres jugar: ")
            
                while not eleccion.isdigit() or (int(eleccion)-1) not in range(0, len(jugador.mano)) or isinstance(jugador.mano[(int(eleccion)-1)], Cartas.CartaMonstruo):
                    eleccion = input("No pudimos acceder a esa carta. Selecciona número de la carta No Monstruo que quieres jugar: ")
                
                eleccion = int(eleccion) - 1
                cartaJugada = jugador.mano.pop(eleccion)
                if isinstance(cartaJugada, Cartas.CartaMagia):
                    equiparCarta = input("¿Quieres equipar esta carta a un monstruo? Sí(S) No(N).")
                
                    while equiparCarta not in ["s", "n", "S", "N"]:
                        print("Selección inválida, debes elegir 'S' para cambiar una o 'N' para continuar.")
                        equiparCarta = input("¿Quieres equipar esta carta? Sí(S) No(N).")
                
                    equiparCarta=equiparCarta.lower()
                
                    if equiparCarta == "s":
                        jugador.imprimirTablero()
                        elegirCarta = input("Seleccionar el numero de la carta Monstruo que equipará la carta: ")
                                    
                        while not elegirCarta.isdigit() or (int(elegirCarta)-1) not in range(0, 3):
                            elegirCarta = input("No pudimos acceder a esa carta. Selecciona numero de la carta que equipará la carta: ")
                    
                        elegirCarta = int(elegirCarta) -1

                        cartaJugada.equiparCarta(t_monstruos_jugador[elegirCarta])
                        cartaJugada.aumentarStats(t_monstruos_jugador[elegirCarta])
                else:
                    cartaJugada.visibilidad = False
                                        
            elif len(t_magicas_trampas_jugador) == 3:
                eleccion = input("Seleccionar numero de la carta Monstruo que quieres jugar: ")
            
                while not eleccion.isdigit() or (int(eleccion)-1) not in range(0, len(jugador.mano)) or isinstance(jugador.mano[(int(eleccion)-1)], (Cartas.CartaMagia, Cartas.CartaTrampa)):
                    eleccion = input("No pudimos acceder a esa carta. Selecciona número de la carta Monstruo que quieres jugar: ")
                
                eleccion = int(eleccion) - 1
                cartaJugada = jugador.mano.pop(eleccion)

                tipoCarta = input("¿Quieres poner la carta en Ataque(A) o Defensa(D)?. ")
                
                while tipoCarta not in ["a","d", "A", "D"]:
                    print("Selección inválida, debes elegir 'A' para ataque o 'D' para defensa.")
                    tipoCarta = input("¿Quieres poner la carta en Ataque(A) o Defensa(D)?. ")
                
                tipoCarta = tipoCarta.lower()

                if tipoCarta == "a": 
                    cartaJugada.pos_atk = True
                    cartaJugada.visibilidad = True
                else:
                    cartaJugada.pos_atk = False
                    cartaJugada.visibilidad = False
                
                t_monstruos_jugador.append(cartaJugada)

            else:
                eleccion = input("Seleccionar numero de la carta que quieres jugar: ")
            
                while not eleccion.isdigit() or (int(eleccion)-1) not in range(0, len(jugador.mano)):
                    eleccion = input("No pudimos acceder a esa carta. Selecciona número de la carta que quieres jugar: ")
                
                eleccion = int(eleccion) - 1      
                cartaJugada = jugador.mano.pop(eleccion)

                if isinstance(cartaJugada, Cartas.CartaMonstruo):
                    tipoCarta = input("¿Quieres poner la carta en Ataque(A) o Defensa(D)?. ")
                
                    while tipoCarta not in ["a","d", "A", "D"]:
                        print("Selección inválida, debes elegir 'A' para ataque o 'D' para defensa.")
                        tipoCarta = input("¿Quieres poner la carta en Ataque(A) o Defensa(D)?. ")
                    
                    tipoCarta = tipoCarta.lower()

                    if tipoCarta == "a": 
                        cartaJugada.pos_atk = True
                        cartaJugada.visibilidad = True
                    else:
                        cartaJugada.pos_atk = False
                        cartaJugada.visibilidad = False

                    t_monstruos_jugador.append(cartaJugada)

                elif isinstance(cartaJugada, Cartas.CartaMagia):
                    equiparCarta = input("¿Quieres equipar esta carta a un monstruo? Sí(S) No(N).")
                
                    while equiparCarta not in ["s", "n", "S", "N"]:
                        print("Selección inválida, debes elegir 'S' para cambiar una o 'N' para continuar.")
                        equiparCarta = input("¿Quieres equipar esta carta? Sí(S) No(N).")
                
                    equiparCarta=equiparCarta.lower()
                
                    if equiparCarta == "s":
                        jugador.imprimirTablero()
                        elegirCarta = input("Seleccionar el numero de la carta Monstruo que equipará la carta: ")
                                    
                        while not elegirCarta.isdigit() or (int(elegirCarta)-1) not in range(0, len(t_monstruos_jugador)):
                            elegirCarta = input("No pudimos acceder a esa carta. Selecciona numero de la carta que equipará la carta: ")
                    
                        elegirCarta = int(elegirCarta) -1

                        cartaJugada.equiparCarta(t_monstruos_jugador[elegirCarta])
                        cartaJugada.aumentarStats(t_monstruos_jugador[elegirCarta])
                else:
                    cartaJugada.visibilidad = False
                    
            jugador.tablero.append(cartaJugada)
            print(f"{cartaJugada.nombre} ha sido añadida al tablero.")

        else:
            print(f"Tablero Lleno, no puedes jugar cartas")

        if len(t_monstruos_jugador)>0:

            cambiarOrientacion = input("Quieres cambiar la posición de una carta monstruo de tu tablero? Sí(S) No(N). ")

            while cambiarOrientacion not in ["s", "n", "S", "N"]:
            
                print("Selección inválida, debes elegir 'S' para cambiar una o 'N' para continuar.")
                cambiarOrientacion = input("Quieres cambiar la posición de una carta monstruo de tu tablero?? Sí(S) No(N). ")
        
            if cambiarOrientacion.lower() == "s":

                jugador.imprimirTablero()
                eleccion = input("Seleccionar numero de la carta que quieres cambiar: ")
        
                while not eleccion.isdigit() or (int(eleccion)-1) not in range(0, len(t_monstruos_jugador)):
                    if (int(eleccion)-1) in range(4,6):
                        print("No se puede cambiar el modo de una carta Magia o Trampa")
                    eleccion = input("No pudimos acceder a esa carta. Selecciona numero de la carta monstruo que quieres cambiar: ")

                eleccion = int(eleccion) -1
                t_monstruos_jugador[eleccion].cambiarOrientacion()
    
        if len(t_magicas) > 0:
            equiparCarta = input("¿Quieres equipar una carta mágica a un monstruo? Sí(S) No(N).")
                
            while equiparCarta not in ["s", "n", "S", "N"]:
                print("Selección inválida, debes elegir 'S' para cambiar una o 'N' para continuar.")
                equiparCarta = input("¿Quieres equipar esta carta? Sí(S) No(N).")

            equiparCarta=equiparCarta.lower()
                
            if equiparCarta == "s":
                cartaMagica = input("Elige la carta mágica que quieras equipar: ")

                while not cartaMagica.isdigit() or (int(cartaMagica)-1) not in range(0, len(jugador.tablero)) or not isinstance(jugador.tablero[int(cartaMagica)-1], Cartas.CartaMagia):
                    print("Por favor, elige una carta mágica válida.")
                    cartaMagica = input("Elige la carta mágica que quieras equipar: ")
                
                cartaMagica = int(cartaMagica)-1

                jugador.imprimirTablero()
                elegirCarta = input("Seleccionar el numero de la carta Monstruo que equipará la carta: ")
                                    
                while not elegirCarta.isdigit() or (int(elegirCarta)-1) not in range(0, len(jugador.tablero) or not isinstance((jugador.tablero[int(elegirCarta)-1], Cartas.CartaMonstruo))):
                    elegirCarta = input("No pudimos acceder a esa carta. Selecciona numero de la carta que equipará la carta: ")
                    
                elegirCarta = int(elegirCarta) -1

                jugador.tablero[cartaMagica].equiparCarta(jugador.tablero[elegirCarta])
                jugador.tablero[cartaJugada].aumentarStats(jugador.tablero[elegirCarta])


        jugador.imprimirTablero()
    
    @staticmethod
    def faseBatalla(jugador1, jugador2):
    # Inicialización de listas para clasificar las cartas del tablero de jugador1
        t_monstruos_jugador = []
        t_magicas_trampas_jugador = []
        for carta in jugador1.tablero:
            if isinstance(carta, Cartas.CartaMonstruo):
                t_monstruos_jugador.append(carta)
            elif isinstance(carta, (Cartas.CartaMagia, Cartas.CartaTrampa)):
                t_magicas_trampas_jugador.append(carta)

        # Inicialización de listas para clasificar las cartas del tablero de jugador2 (máquina)
        t_monstruos_maquina = []
        t_magicas_trampas_maquina = []
        for carta in jugador2.tablero:
            if isinstance(carta, Cartas.CartaMonstruo) and not carta.pos_atk:
                t_monstruos_maquina.append(carta)
            elif isinstance(carta, (Cartas.CartaMagia, Cartas.CartaTrampa)):
                t_magicas_trampas_maquina.append(carta)

        print("="*120)
        print("Fase de Batalla: Puedes batallar.")

        # Caso: El oponente no tiene monstruos en su tablero
        if not t_monstruos_maquina:  # Lista vacía significa que no hay monstruos
            if len([c for c in t_monstruos_jugador if c.pos_atk]) > 0:
                print("Fase de Batalla: El rival no tiene monstruos en modo defensa. Puedes declarar batalla directa.")
                jugador1.imprimirTablero()

                cartaAtacante = input("Selecciona la carta de monstruo en modo ataque para atacar (número): ")
                while not (
                    cartaAtacante.isdigit() 
                    and 0 <= (int(cartaAtacante) - 1) < len(t_monstruos_jugador)
                    and t_monstruos_jugador[int(cartaAtacante) - 1].pos_atk
                ):
                    print("Selecciona un número correspondiente a una carta monstruo en modo ataque válida.")
                    cartaAtacante = input("Selecciona la carta de monstruo en modo ataque para atacar (número): ")
                
                cartaAtacante = int(cartaAtacante) - 1
                cartaAtacante = t_monstruos_jugador[cartaAtacante]
                print(f"Atacando directamente a {jugador2.nombre}...")
                cartaAtacante.declararBatallaDirecta(jugador2)
            else:
                print("No tienes monstruos en modo ataque. No puedes atacar.") 

        # Caso: El oponente tiene monstruos en su tablero
        elif t_monstruos_maquina:  # Hay monstruos en el tablero del oponente
            if len([c for c in t_monstruos_jugador if c.pos_atk]) > 0:
                print("Fase de Batalla: El rival tiene monstruos. No puedes hacer batalla directa.")
                jugador1.imprimirTablero()

                cartaAtacante = input("Selecciona la carta de monstruo en modo ataque para atacar (número): ")
                while not (
                    cartaAtacante.isdigit() 
                    and 0 <= (int(cartaAtacante) - 1) < len(t_monstruos_jugador)
                    and t_monstruos_jugador[int(cartaAtacante) - 1].pos_atk
                ):
                    print("Selecciona un número correspondiente a una carta monstruo en modo ataque válida.")
                    cartaAtacante = input("Selecciona la carta de monstruo en modo ataque para atacar (número): ")

                cartaAtacante = int(cartaAtacante) - 1
                cartaAtacante = t_monstruos_jugador[cartaAtacante]

                print(f"Tablero de {jugador2.nombre}:")
                jugador2.imprimirTablero()

                cartaDefensora = input("Selecciona la carta de monstruo a la que vas a atacar (número): ")
                while not (
                    cartaDefensora.isdigit() 
                    and 0 <= (int(cartaDefensora) - 1) < len(t_monstruos_maquina)
                ):
                    print("Ingresa un número válido.")
                    cartaDefensora = input("Selecciona la carta de monstruo a la que vas a atacar (número): ")
                
                cartaDefensora = int(cartaDefensora) - 1
                cartaDefensora = t_monstruos_maquina[cartaDefensora]

                cartaAtacante.declararBatalla(jugador2, jugador1, cartaDefensora)
            else:
                print("No tienes monstruos en modo ataque. No puedes atacar.") 
