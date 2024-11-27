import Cartas
import random as random

class Utilitaria:

  @staticmethod
  def crearDeck():
    deck = []
    f = open("Cartas Monstruo".txt, "r")
    while (len(deck) < 20):
      for linea in f:
        vida, nombre, descripcion, ataque, defensa, tipo_monstruo, tipo_atributo = linea.strip().split(',')
        carta = Cartas.CartaMonstruo(id, int(vida), nombre, descripcion, int(ataque), int(defensa), tipo_monstruo, tipo_atributo)
        deck.append(carta)
    
    while (len(deck) < 25):
      f = open("CartasMagia".txt, "r")
      for linea in f:
        valor = random.randint(0,10)
        if valor < 2:
          f.readline()
        nombre, descripcion, ataque, defensa, tipo_monstruo = linea.strip().split(',')
        carta = Cartas.CartaMagia(id, nombre, descripcion, int(ataque), int(defensa), tipo_monstruo)
        deck.append(carta)
    
    while (len(deck) < 30):
      f = open("CartasTrampa".txt, "r")
      for linea in f:
        valor = random.randint(0,10)
        if valor < 2:
          f.readline()
        nombre, descripcion, tipo_atributo = linea.strip().split(',')
        carta = Cartas.CartaMagia(id, nombre, descripcion, tipo_atributo)
        deck.append(carta)
    
    return random.shuffle(deck)