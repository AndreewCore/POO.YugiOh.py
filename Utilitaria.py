import Cartas
import random

class Utilitaria:

  @staticmethod
  def crearDeck():
    deck = []

    deckMonstruo = []
    f = open("CartasMonstruo.txt", "r")
    for linea in f:
      vida, nombre, descripcion, ataque, defensa, tipo_monstruo, tipo_atributo = linea.strip().split(',')
      carta = Cartas.CartaMonstruo(int(vida), nombre, descripcion, int(ataque), int(defensa), tipo_monstruo, tipo_atributo)
      deckMonstruo.append(carta)
    f.close()

    deckMagia = []
    f = open("CartasMagia.txt", "r")
    for linea in f:
      nombre, descripcion, ataque, defensa, tipo_monstruo = linea.strip().split(',')
      carta = Cartas.CartaMagia(nombre, descripcion, int(ataque), int(defensa), tipo_monstruo)
      deckMagia.append(carta)
    f.close()

    deckTrampa = []
    f = open("CartasTrampa.txt", "r")
    for linea in f:
      nombre, descripcion, tipo_atributo = linea.strip().split(',')
      carta = Cartas.CartaTrampa(nombre, descripcion, tipo_atributo)
      deckTrampa.append(carta)
    f.close()
    
    random.shuffle(deckMonstruo)
    random.shuffle(deckMagia)
    random.shuffle(deckTrampa)
    
    deck = deckMonstruo[:20] + deckMagia[:5] + deckTrampa[:5]
    random.shuffle(deck)

    return deck