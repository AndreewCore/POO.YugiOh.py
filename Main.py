import Cartas
import random as rd
import Juego
import Jugador
import Utilitaria

deckConsola = Utilitaria.crearDeck()
deckJugador = Utilitaria.crearDeck()

manoConsola = Utilitaria.crearMano(deckConsola)
manoJugador =  Utilitaria.crearMano(deckJugador)

nombreJugador = input("Ingrese su nombre: ")
player = Jugador(nombreJugador, manoJugador)
consola = Jugador("consola", manoConsola)

tableroMonstruoConsola = []
tableroMagiaTrampaConsola = []

tableroMonstruoJugador = []
tableroMagiaTrampaJugador = []

