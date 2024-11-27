from Cartas import *

def mostrar_info(carta):

    if not carta.visibilidad:
        return f"[{carta.nombre} (Boca Abajo)]"
    
    if isinstance(carta, CartaMonstruo):
        posicion = "ATK" if carta.posicion else "DEF"
        return f"[{carta.nombre} ATK:{carta.ataque} DEF:{carta.defensa} Posición: {posicion} Tipo de Monstruo: {carta.tipo_monstruo} Tipo de Atributo: {carta.tipo_atributo}]"
    
    elif isinstance(carta, CartaMagia):
        return f"[{carta.nombre} Tipo Mágica Vinculada a: {carta.owner.nombre if carta.owner else 'Ninguno'} Tipo Monstruo: {carta.tipo_monstruo}]"
    
    elif isinstance(carta, CartaTrampa):
        return f"[{carta.nombre} Tipo de Atributo: {carta.tipo_atributo}]"

def completar_espacios(tablero):
    while len(tablero) < 3:
        tablero.append("(Vacio)")
    return tablero

# Función para mostrar el tablero
def tablero(t_monstruos_maquina, t_magicas_trampas_maquina, t_monstruos_jugador, t_magicas_jugador, vida_maquina, vida_jugador):
    t_monstruos_maquina = completar_espacios(t_monstruos_maquina)
    t_magicas_trampas_maquina = completar_espacios(t_magicas_trampas_maquina)
    t_monstruos_jugador = completar_espacios(t_monstruos_jugador)
    t_magicas_jugador = completar_espacios(t_magicas_jugador)

    print("TABLERO DE YU-GI-OH!\n")
    
    print("Jugador 2 (Máquina) - Puntos de Vida:", vida_maquina)
    print("Magia/Trampa: ", "  ".join([mostrar_info(carta) for carta in t_magicas_trampas_maquina]))
    print("Monstruos:    ", "  ".join([mostrar_info(carta) for carta in t_monstruos_maquina]))
    print("-" * 50)
    
    print("Jugador 1 - Puntos de Vida:", vida_jugador)
    print("Monstruos:    ", "  ".join([mostrar_info(carta) for carta in t_monstruos_jugador]))
    print("Magia/Trampa: ", "  ".join([mostrar_info(carta) for carta in t_magicas_jugador]))
