import Juego
import Jugador
import Cartas
import random as rd

sorteo = rd.choice([0, 1])  
turno = 1  

# Inicialización del jugador y el bot
nombreJugador = input("Ingrese su nombre: ")
player = Jugador.Jugador(nombreJugador)
bot = Jugador.Bot("Botsito")

# Comienza el juego
while player.vida > 0 and bot.vida > 0:
    print(f"\n{"="*30} Turno {turno} {"="*30}")

    if sorteo == 0:
        print(f"\nTurno del jugador {player.nombre}:") 
     
        print("\nFase de tomar carta:")
        Juego.Juego.faseTomarCarta(player) 
   
        print("\nFase principal:")
        Juego.Juego.fasePrincipal(player)
        
        # Fase de batalla
        if turno > 2:  
            print("\nFase de batalla del jugador:")
            bot.jugarManoBot()
            Juego.Juego.faseBatalla(player, bot) 
            print(f"\nVida del jugador {player.nombre}: {player.vida}\n") 
            print(f"\nVida del jugador {bot.nombre}: {bot.vida}\n") 
        
        sorteo = 1
    else:
        print(f"\nTurno del bot {bot.nombre}:\n")
       
        bot.robarCarta()
     
        bot.jugarManoBot()
        if turno ==1 and isinstance(bot.tablero[0],Cartas.CartaMonstruo):
            bot.tablero[0].visibilidad = False
            bot.tablero[0].pos_atk = False
        bot.imprimirTablero()
        
        if turno > 2: 
            bot.declararBatallaBot(player)

        sorteo = 0 
    
    turno += 1

# Resultado final
if player.vida <= 0 and bot.vida <= 0:
    print("¡Es un empate!")
elif player.vida <= 0:
    print(f"¡{bot.nombre} gana la partida!")
else:
    print(f"¡{player.nombre} gana la partida!")

