id_carta = 0

class CartaYugiOh:
  def _init_ (self, vida, nombre, descripcion, ataque, defensa):
    id_carta += 1
    self.vida = int(vida)
    self.nombre = nombre
    self.descripcion = descripcion
    self.ataque = int(ataque)
    self.defensa = int(defensa)
    self.visibilidad = False

class CartaMonstruo(CartaYugiOh):
    def __init__(self, vida, nombre, descripcion, ataque, defensa, tipo_monstruo, tipo_atributo):
        super().__init__(id, vida, nombre, descripcion, ataque, defensa)
        self.tipo_monstruo = tipo_monstruo
        self.tipo_atributo = tipo_atributo
        self.pos_atk = False
        self.inventario = []
 
    def cartaViva(self):
        if self.vida == 0:
            return False
        else:
            return True
    
    def recibirAtaque(self, jugador, carta):
        realDamage = self.defensa - carta.ataque
        if realDamage <= 0:
            self.vida = 0
            jugador.vida += realDamage
        else:
            self.vida - carta.ataque
    
    def cambiarModo(self, modo):
        if modo == "ataque":
            self.pos_atk = True
        else:
            self.pos_atk = False

    def cambiarOrientacion(self):
        if self.pos_atk == False: 
            self.pos_atk = True
            self.visibilidad = True
        else:
            self.pos_atk = False
            self.visibilidad = False

    
    def __str__(self):
        return "MONSTER - " + self.nombre + "Ataque: " + str(self.ataque) + "Defensa: " + str(self.defensa) + "Tipo de Monstruo: " + self.tipo_monstruo + "Tipo de Atributo: " + self.tipo_atributo + "Equipado: " + self.inventario

class CartaMagia(CartaYugiOh):
    def __init__(self, nombre, descripcion, ataque, defensa, tipo_monstruo):
        super().__init__(id, 1, nombre, descripcion, ataque, defensa)
        self.tipo_monstruo = tipo_monstruo
        self.visibilidad = True
        self.owner = None
    
    def aumentarStats(self, owner):
        if owner.tipo == self.tipo_monstruo:
            owner.ataque += self.ataque
            owner.defensa += self.defensa
        else:
            print("Las cartas elegidas no tienen el mismo atributo")
    
    def __str__(self):
        return "MAGIA - " + self.nombre + "Ataque: " + str(self.ataque) + "Defensa: " + str(self.defensa) + "Tipo de Monstruo: " + self.tipo_monstruo + "Equipado en: " + self.owner.nombre

class CartaTrampa(CartaYugiOh):
    def __init__(self, nombre, descripcion, tipo_atributo):
        super().__init__(id, 1, nombre, descripcion, 0, 0)
        self.tipo_atributo = tipo_atributo

    def validarJugada(self, Tablero):
        for elem in Tablero:
            if elem is CartaMonstruo & self.tipo_atributo == elem.tipo_atributo:
                return True
    
    def __str__(self):
        return "TRAMPA - " + self.nombre + "Ataque: " + str(self.ataque) + "Defensa: " + str(self.defensa) + "Tipo de Atributo: " + self.tipo_atributo