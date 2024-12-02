import Utilitaria
import Cartas
import random

class Jugador:
    
    def __init__(self, nombre):
        self.vida = 4000
        self.nombre = nombre
        self.deck = Utilitaria.Utilitaria.crearDeck()
        self.mano = self.deck[:5]
        self.deck = self.deck[5:]
        self.tablero = []
    
    def jugarCarta(self, int):
        contadorMonstruos = 0
        contadorMagia = 0
        contadorTrampa = 0
        for c in self.tablero:
            if isinstance(c, Cartas.CartaMonstruo):
                contadorMonstruos +=1
            if isinstance(c, Cartas.CartaMagia):
                contadorMagia +=1
            else:
                contadorTrampa +=1
        
        if contadorMonstruos < 3 and isinstance(c, Cartas.CartaMonstruo):
            carta = self.mano.pop(int)
            self.tablero.append(carta)
        if ((contadorMagia + contadorTrampa) < 3) and (isinstance(c, Cartas.CartaMagia) or isinstance(c, Cartas.CartaTrampa)):
            carta = self.mano.pop(int)
            self.tablero.append(carta)
        else:
            print("No es posible hacer esta jugada. Tablero lleno.")

    def robarCarta(self):
        if len(self.deck) > 0:
            carta = self.deck.pop(0)
            self.mano.append(carta)
            print(f"{self.nombre} ha robado una carta: {carta}")
        else:
            print(f"El deck de {self.nombre} está vacío. No puede robar más cartas.")

    def estaDerrotado(self):
        if self.vida < 0:
            print(self.nombre + " ha sido derrotado y ha perdido.")
            return True
        return False


    def imprimirMano(self):
        print("-"*50 + " Mano de " + self.nombre + "-"*50)
        i = 0
        for carta in self.mano:
            i += 1
            print(str(i), carta)
    
    def imprimirTablero(self):
        t_monstruos_jugador = []
        t_magicas_trampas_jugador = []
        for carta in self.tablero:
          if isinstance(carta, Cartas.CartaMonstruo):
              t_monstruos_jugador.append(carta)
          elif isinstance(carta, (Cartas.CartaMagia, Cartas.CartaTrampa)):
              t_magicas_trampas_jugador.append(carta)
        
        t_monstruos_jugador += ["(Espacio Vacio)"] * (3 - len(t_monstruos_jugador))
        t_magicas_trampas_jugador += ["(Espacio Vacio)"] * (3 - len(t_magicas_trampas_jugador))

        print("\nTablero de ", self.nombre," - Puntos de Vida:", self.vida)
        print("Monstruos:   \t", "\n\t\t ".join([f"[{str(carta)}]" for carta in t_monstruos_jugador]))
        print("Magia/Trampa:\t", "\n\t\t ".join([f"[{str(carta)}]" for carta in t_magicas_trampas_jugador]),"\n")                         

class Bot(Jugador):
    def __init__(self,nombre="Botsito"):
        self.vida = 4000
        self.nombre = nombre
        self.deck = Utilitaria.Utilitaria.crearDeck()
        self.mano = self.deck[:5]
        self.deck = self.deck[5:]
        self.tablero = []
        
    def robarCarta(self):
        if len(self.deck) > 0:
            carta = self.deck.pop(0)
            self.mano.append(carta)
            print(f"{self.nombre} ha robado una carta.")
        else:
            print(f"El deck de {self.nombre} está vacío. No puede robar más cartas.")


    @staticmethod
    def seleccionarObjetivo(tableroEnemigo):
        cartasEnemigas = []
        for carta in tableroEnemigo:
            if isinstance(carta, Cartas.CartaMonstruo):
                cartasEnemigas.append(carta)

        # Si no hay cartas enemigas, retorna None
        if not cartasEnemigas:
            return None

        dañoAtaque = []
        dañoDefensa = []
        for carta in cartasEnemigas:
            if carta.pos_atk:
                dañoAtaque.append(carta.ataque)
                dañoDefensa.append(0)
            else:
                dañoAtaque.append(0)
                dañoDefensa.append(carta.defensa)

        # Encontrar el mínimo ataque y defensa (si existen)
        debilAtaque = min((x for x in dañoAtaque if x > 0), default=None)
        debilDefensa = min((x for x in dañoDefensa if x > 0), default=None)

        # Determinar el objetivo más débil
        if debilAtaque is not None and (debilDefensa is None or debilAtaque <= debilDefensa):
            return cartasEnemigas[dañoAtaque.index(debilAtaque)]
        elif debilDefensa is not None:
            return cartasEnemigas[dañoDefensa.index(debilDefensa)]
        else:
            return None


    def jugarManoBot(self):
        
        contadorMonstruos = 0
        contadorMagia = 0
        contadorTrampa = 0
        verifMonstruos = []
        
        for c in self.tablero:
            if isinstance(c, Cartas.CartaMonstruo):
                contadorMonstruos +=1
                verifMonstruos.append(c)

            if isinstance(c, Cartas.CartaMagia):
                contadorMagia +=1
            else:
                contadorTrampa +=1
        
        cartasJugables = []
        for c in self.mano:
            if isinstance(c, Cartas.CartaMonstruo):
                cartasJugables.append(c)
        
        if len(cartasJugables) > 0:
            cartaJugar = random.choice(cartasJugables)
            cartaIndex = self.mano.index(cartaJugar)
        else:
            cartaIndex = random.randint(0,len(self.mano))

        if contadorMonstruos < 3 and isinstance(self.mano[cartaIndex], Cartas.CartaMonstruo):
            
            carta = self.mano.pop(cartaIndex)
            carta.pos_atk = True
            carta.visibilidad = True

            verifDefensa = []
            for carta in self.tablero:
                if not carta.pos_atk:
                    verifDefensa.append(carta)

            if len(verifDefensa) == 0:
                carta.pos_atk = False
                carta.visibilidad = False

            self.tablero.append(carta)

        elif ((contadorMagia + contadorTrampa) < 3) and (isinstance(self.mano[cartaIndex], Cartas.CartaMagia) or isinstance(self.mano[cartaIndex], Cartas.CartaTrampa)):
            carta = self.mano.pop(cartaIndex)
            self.tablero.append(carta)
            if isinstance(carta,Cartas.CartaTrampa):
                carta.visibilidad = False
        
    def declararBatallaBot(self, jugadorOponente):
        
        if not any(isinstance(carta, Cartas.CartaMonstruo) for carta in jugadorOponente.tablero):

            if [c for c in self.tablero if isinstance(c, Cartas.CartaMonstruo) and c.pos_atk]:
                print(f"{self.nombre} ataca directamente a {jugadorOponente.nombre}.")
                
                cartasMonstruo = []
                for carta in self.tablero:
                    if isinstance(carta, Cartas.CartaMonstruo) and carta.visibilidad:
                        cartasMonstruo.append(carta)

                carta = random.choice(cartasMonstruo)        
                carta.declararBatallaDirecta(jugadorOponente)
                carta.pos_atk = True

            else:

                print(f"{self.nombre} no tiene monstruos en modo de ataque. No puede realizar ataques.")   

        else:

            if [c for c in self.tablero if isinstance(c, Cartas.CartaMonstruo) and c.pos_atk]:

                print(f"{self.nombre} declara batalla contra {jugadorOponente.nombre}.")
                cartasMonstruo = []
                
                for cartaAtacante in self.tablero:
                    if isinstance(cartaAtacante, Cartas.CartaMonstruo):
                        cartasMonstruo.append(cartaAtacante)
                
                carta1 = random.choice(cartasMonstruo)
                carta2 = Bot.seleccionarObjetivo(jugadorOponente.tablero)

                cartasTrampa = []
                for carta in jugadorOponente.tablero:
                    if isinstance(carta, Cartas.CartaTrampa) and cartaAtacante.tipo_atributo == carta.tipo_atributo:
                        cartasTrampa.append(carta)

                if len(cartasTrampa) > 0:
                    
                    validacion = input(f"¿Quieres usar {cartasTrampa[0].nombre} para evitar el ataque? Sí(S) No(N). ")
                    while validacion not in ["s", "n", "S", "N"]:
                    
                        print("Selección inválida, debes elegir 'S' para cambiar una o 'N' para continuar.")
                        validacion = input(f"¿Quieres usar {carta2} para evitar el ataque? Sí(S) No(N). ")
                
                    if validacion.lower() == "s":
                        jugadorOponente.tablero.remove[cartasTrampa[0]]
                        print(f"{jugadorOponente.nombre} ha usado una carta trampa y ha anulado el ataque.")
                    else:
                        #carta1.declararBatalla(jugadorOponente, self, carta2)
                        carta2.visibilidad = True

                        if carta2.pos_atk:
                            if carta2.ataque < self.ataque:
                                print(f"{carta2.nombre} de {jugadorOponente.nombre} no ha soportado el ataque.")
                                print(f"{carta2.nombre} ha sido destruido.\n")
                                danoRecibido = self.ataque - carta2.ataque
                                jugadorOponente.vida -= danoRecibido
                                jugadorOponente.tablero.remove(carta2)

                            elif carta2.ataque > self.ataque:
                                print(f"{carta2.nombre} está durísimo. No ha pasado nada.\n")

                            else:
                                print("Ambas cartas han sido destruidas.")
                                if self in self.tablero:
                                    self.tablero.remove(self)
                                if carta2 in jugadorOponente.tablero:
                                    jugadorOponente.tablero.remove(carta2)
                        
                        else: 
                    
                            if carta2.defensa < self.ataque:
                                print(f"{carta2.nombre} de {jugadorOponente.nombre} no ha soportado el ataque.")
                                print(f"{carta2.nombre} ha sido destruido.\n")
                                jugadorOponente.tablero.remove(carta2)
                                
                            elif carta2.defensa > self.ataque:
                                danoRecibido = carta2.defensa - self.ataque
                                self.vida -= danoRecibido
                                print(f"{carta2.nombre} está durísimo hermano. {jugadorOponente.nombre} ha recibido {danoRecibido} puntos de daño.\n")
                                print(f"{jugadorOponente.nombre} queda con {jugadorOponente.vida} puntos de vida.\n")
                            
                            else:
                                print("Ambas cartas han sido destruidas.")
                                self.tablero.remove(self)
                                jugadorOponente.tablero.remove(carta2)

                else:                       
                    print(f"{self.nombre} ataca con {carta1.nombre} a {carta2.nommbre} de {jugadorOponente.nombre}")
                    carta1.declararBatalla(jugadorOponente, self, carta2)

            else:

                print(f"{self.nombre} no tiene monstruos en modo de ataque. No puede realizar ataques.")           