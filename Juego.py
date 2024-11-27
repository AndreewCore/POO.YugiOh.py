import random as rd
import Cartas

class Juego:
    def __init__(self, jugador, consola):
       self.jugador = jugador
       self.consola = consola
       self.turno = rd.choice([jugador,consola])

    def mostrarEstado(self):
        print(f"Turno actual: {self.turno.nombre}")
        print(f"Deck Jugador: {len(self.jugador.deck)} cartas restantes")
        print(f"Deck Máquina: {len(self.consola.deck)} cartas restantes")
    

    def fasePrincipal(self, jugador):
        
        print(f"Turno de {self.jugador.nombre}.")
        print("_"*160)
        print("Cartas en mano:")
        for i in range(len(self.jugador.mano)):
            carta=self.jugador.mano[i]
            print(f"{i + 1}. {carta}")
        print("_"*160)

        eleccion = int(input("Seleccionar numero de la carta que quieres jugar: ")) -1
        
        while eleccion not in range(0, len(jugador.mano)):
                eleccion = int(input("No pudimos acceder a esa carta. Selecciona numero de la carta que quieres jugar: ")) -1
               
        cartaJugada = self.jugador.mano.pop(eleccion)

        if isinstance(cartaJugada, Cartas.CartaMonstruo):

            jugador.tableroMonstruo.append(cartaJugada)
            
            tipoCarta = input("¿Quieres poner la carta en Ataque(A) o Defensa(D)?. ")
            
            while tipoCarta not in ["a","d", "A", "D"]:
                print("Selección inválida, debes elegir 'A' para ataque o 'D' para defensa.")
                tipoCarta = input("¿Quieres poner la carta en Ataque(A) o Defensa(D)?. ")
            
            if tipoCarta == "a": 
                cartaJugada.pos_atk = True
                cartaJugada.visibilidad = True
            else:
                cartaJugada.pos_atk = False
                cartaJugada.visibilidad = False
        
        elif isinstance(cartaJugada, Cartas.CartaMagia):

            jugador.tableroMagiaTrampa.append(cartaJugada)

            equiparCarta = input("¿Quieres equipar esta carta? Sí(S) No(N).")
            
            while equiparCarta not in ["s", "n", "S", "N"]:
                print("Selección inválida, debes elegir 'S' para cambiar una o 'N' para continuar.")
                equiparCarta = input("¿Quieres equipar esta carta? Sí(S) No(N).")
            
            equiparCarta.lower()
            if equiparCarta == "s":

                elegirCarta = input("Seleccionar numero de la carta Monstruo que equipará la carta: ")
                
                while elegirCarta not in range(0, len(jugador.tableroMonstruo)):
                    elegirCarta = int(input("No pudimos acceder a esa carta. Selecciona numero de la carta que equipará la carta: ")) -1
                
                jugador.tableroMonstruo(elegirCarta).inventario.append.cartaJugada

        else:

            jugador.tableroMagiaTrampa.append(cartaJugada)

        cambiarOrientacion = input("Quieres cambiar la orientación de una carta? Sí(S) No(N). ")

        while cambiarOrientacion not in ["s", "n", "S", "N"]:
            
            print("Selección inválida, debes elegir 'S' para cambiar una o 'N' para continuar.")
            cambiarOrientacion = input("Quieres cambiar la orientación de una carta? Sí(S) No(N). ")
        
        eleccion = int(input("Seleccionar numero de la carta que quieres jugar: ")) -1
        
        while eleccion not in range(0, len(jugador.tableroMonstruo)):
                eleccion = int(input("No pudimos acceder a esa carta. Selecciona numero de la carta que quieres jugar: ")) -1
        
        
            
                

        print(f"Has jugado: {cartaJugada}. Posicion: {"Ataque" if cartaJugada.pos_atk else "Defensa"}")     
        print("_"*160)
        print("Cartas en tablero :")
        for i, carta in enumerate( self.tableroJ):
            estado="Boca Arriba" if carta.visibilidad else "Boca Abajo"
            posicion= "Ataque" if getattr(carta, "pos_atk",False) else "Defensa"
            print(f"{i + 1}. {carta.nombre} ({estado}, {posicion})")
        cambiarPos=input("¿Quieres cambiar la posición de alguna carta? (S/N): ").strip().lower()
        if cambiarPos=="s":
            seleccion = int(input("Selecciona el número de carta que quieres cambiar: ")) - 1
            if 0 <= seleccion < len(self.tableroJ):
                cartaSeleccionada=self.tableroJ[seleccion]
                if isinstance(cartaSeleccionada, Cartas.CartaMonstruo) and cartaSeleccionada.visibilidad:
                    cartaSeleccionada.pos_atk= not cartaSeleccionada.pos_atk
                    nuevaPos= "Ataque" if cartaSeleccionada.pos_atk else "Defensa"
                    print(f"La carta {cartaSeleccionada.nombre} ahora está en posición {nuevaPos}.")
                else:
                    print("Solo puedes cambiar la posición de cartas monstruo que estén boca arriba.")
            else:
                print("Seleccion Invalida xdxd")