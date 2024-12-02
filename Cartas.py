import Jugador

class CartaYugiOh:

  def __init__ (self, vida, nombre, descripcion, ataque, defensa):

    self.vida = int(vida)
    self.nombre = nombre
    self.descripcion = descripcion
    self.ataque = int(ataque)
    self.defensa = int(defensa)
    self.visibilidad = True

class CartaMonstruo(CartaYugiOh):
    def __init__(self, vida, nombre, descripcion, ataque, defensa, tipo_monstruo, tipo_atributo):
        super().__init__(vida, nombre, descripcion, ataque, defensa)
        self.tipo_monstruo = tipo_monstruo
        self.tipo_atributo = tipo_atributo
        self.pos_atk = False
        self.inventario = []
        
    def cambiarModo(self, modo):
        if modo == "ataque":
            self.pos_atk = True
        else:
            self.pos_atk = False

    def cambiarOrientacion(self):
        if self.visibilidad: 
            if self.pos_atk:
                self.pos_atk = False
            else:
                self.pos_atk = True
        else:
            print("No es posible cambiar de modo a esta carta")

    def declararBatalla(self, jugadorRecibe, jugadorAtaca, cartaRecibe):

        recibeCartasTrampa = []
        for carta in jugadorRecibe.tablero:
            if isinstance(carta, CartaTrampa):
                if self.tipo_atributo == carta.tipo_atributo:
                    recibeCartasTrampa.append(carta)

        if len(recibeCartasTrampa) > 0:
            jugadorRecibe.tablero.remove(recibeCartasTrampa[0])
            print(f"{jugadorRecibe.nombre} ha usado una carta trampa y ha anulado el ataque.")

        else:

            cartaRecibe.visibilidad = True

            if cartaRecibe.pos_atk:
                if cartaRecibe.ataque < self.ataque:
                    print(f"{cartaRecibe.nombre} de {jugadorRecibe.nombre} no ha soportado el ataque de {self.nombre}.")
                    print(f"{cartaRecibe.nombre} ha sido destruido.\n")
                    danoRecibido = self.ataque - cartaRecibe.ataque
                    jugadorRecibe.vida -= danoRecibido
                    jugadorRecibe.tablero.remove(cartaRecibe)

                elif cartaRecibe.ataque > self.ataque:
                    print(f"{cartaRecibe.nombre} está durísimo. No ha pasado nada.\n")

                else:
                    print("Ambas cartas han sido destruidas.")
                    if self in jugadorAtaca.tablero:
                        jugadorAtaca.tablero.remove(self)
                    if cartaRecibe in jugadorRecibe.tablero:
                        jugadorRecibe.tablero.remove(cartaRecibe)
            
            else: 
        
                if cartaRecibe.defensa < self.ataque:
                    print(f"{cartaRecibe.nombre} de {jugadorRecibe.nombre} no ha soportado el ataque de {self.nombre}.")
                    print(f"{cartaRecibe.nombre} ha sido destruido.\n")
                    jugadorRecibe.tablero.remove(cartaRecibe)
                    
                elif cartaRecibe.defensa > self.ataque:
                    danoRecibido = cartaRecibe.defensa - self.ataque
                    jugadorAtaca.vida -= danoRecibido
                    print(f"{cartaRecibe.nombre} está durísimo hermano. {jugadorAtaca.nombre} ha recibido {danoRecibido} puntos de daño.\n")
                
                else:
                    print("Ambas cartas han sido destruidas.")
                    jugadorAtaca.tablero.remove(self)
                    jugadorRecibe.tablero.remove(cartaRecibe)

    def declararBatallaDirecta(self, jugador):
        jugador.vida += self.ataque*-1
        print("El jugador " + jugador.nombre + " queda con " + str(jugador.vida) + " puntos de vida.")

    def __str__(self):
        if self.visibilidad:
            if self.pos_atk:
                return "MONSTER - " + self.nombre + " HP: "+ str(self.vida) + " Atk: " + str(self.ataque) + " Def: " + str(self.defensa) + " Tipo de Monstruo: " + self.tipo_monstruo + " Tipo de Atributo: " + self.tipo_atributo + " Modo de Ataque | Inventario: " + ", ".join([str(carta) for carta in self.inventario])
            else:
                return "MONSTER - " + self.nombre + " HP: " + str(self.vida)+ " Atk: " + str(self.ataque) + " Def: " + str(self.defensa) + " Tipo de Monstruo: " + self.tipo_monstruo + " Tipo de Atributo: " + self.tipo_atributo + " Modo de Defensa | Inventario: " + ", ".join([str(carta) for carta in self.inventario])
        else:
            return "Monstruo en Modo de Defensa"

class CartaMagia(CartaYugiOh):
    def __init__(self, nombre, descripcion, ataque, defensa, tipo_monstruo):
        super().__init__(1, nombre, descripcion, ataque, defensa)
        self.tipo_monstruo = tipo_monstruo
        self.owner = None
    
    def equiparCarta(self, owner):
        if isinstance(owner, CartaMonstruo) and (owner.tipo_monstruo == self.tipo_monstruo):
            owner.inventario.append(self)
            self.owner = owner
            print(f"{self.nombre} ahora está equipada en {owner.nombre}.")

        else:
            print(f"Las cartas elegidas no tienen el mismo tipo de monstruo. No se puede equipar.")

    def aumentarStats(self, owner):
        if isinstance(owner, CartaMonstruo):  
            if owner.tipo_monstruo == self.tipo_monstruo:
                owner.ataque += self.ataque
                owner.defensa += self.defensa
                print(f"{owner.nombre} ha recibido {self.ataque} puntos de ataque y {self.defensa} puntos de defensa.")
            else:
                print(f"Las cartas elegidas no tienen el mismo tipo de monstruo. No se puede aplicar el efecto.")
        else:
            print("El dueño de la carta no es un monstruo valido")

    def __str__(self):
        if self.owner is None:
            return "MAGIA - " + self.nombre + " Ataque: " + str(self.ataque) + " Defensa: " + str(self.defensa) + " Tipo de Monstruo: " + self.tipo_monstruo + " Equipado en: Nadie"
        return "MAGIA - " + self.nombre + " Ataque: " + str(self.ataque) + " Defensa: " + str(self.defensa) + " Tipo de Monstruo: " + self.tipo_monstruo + " Equipado en: " + self.owner.nombre

class CartaTrampa(CartaYugiOh):
    def __init__(self, nombre, descripcion, tipo_atributo):
        super().__init__(1, nombre, descripcion, 0, 0)
        self.tipo_atributo = tipo_atributo

    def validarJugada(self, Tablero):
        for elem in Tablero:
            if elem is CartaMonstruo & self.tipo_atributo == elem.tipo_atributo:
                return True
    
    def __str__(self):
        if self.visibilidad:
            return "TRAMPA - " + self.nombre + " Ataque: " + str(self.ataque) + " Defensa: " + str(self.defensa) + " Tipo de Atributo: " + self.tipo_atributo
        else:
            return "Carta boca abajo"