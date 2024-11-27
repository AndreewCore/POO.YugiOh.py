import Utilitaria

class Jugador:
    
    def __init__(self, nombre, deck):
        self.vida = 4000
        self.nombre = nombre
        self.deck = Utilitaria.crearMano(deck)
        self.mano = self.deck[:5]
        self.tableroMonstruo = []
        self.tableroMagiaTrampa = []
    
    def robarCarta(self):
        if len(self.deck) > 0:
            carta = self.deck.pop(0)
            self.mano.append(carta)
            print(f"{self.nombre} ha robado una carta: {carta}")
        else:
            print(f"El deck de {self.nombre} está vacío. No puede robar más cartas.")
