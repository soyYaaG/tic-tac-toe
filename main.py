import os
import random

board_espacio = [' ' for x in range(9)]

def main():
    limpiar()
    bienvenido()
    board(board_espacio)
    while True:
        posicion = int(input("Por favor selecciona la posición entre 1 y 9 para insertar tu jugada (X): "))
        posicion = posicion - 1
        # validar si la posición es valida
        if posicion >= 0 and posicion < 9:
            limpiar()
            # validar si la posición esta libre
            if not(espacio_libre(posicion)):
                print(f'\t\tLa posición {posicion + 1} esta en uso')
                print()
            else:
                insertar_letra(posicion, 'X')

                if es_ganador(board_espacio, 'X'):
                    bienvenido()
                    board(board_espacio)
                    print()
                    print('\t\t¡¡¡Eres el ganador!!!')
                    break
                elif board_llena():
                    bienvenido()
                    board(board_espacio)
                    print()
                    print('\t\t¡¡¡Juego terminado!!!')
                    break

                # hacer movimiento de la maquina
                posicion_maquina = movimiento_computador()
                insertar_letra(posicion_maquina, 'O')
                # validar si la maquina es la ganadora
                if es_ganador(board_espacio, 'O'):
                    bienvenido()
                    board(board_espacio)
                    print()
                    print('\t\t¡¡¡La maquina ha ganado!!!')
                    break
                
        else:
            print('¡Upss! Por favor intenta con número del 1 al 9')

        bienvenido()
        board(board_espacio)

def board(board_espacio):
    for i in range(3):
        print('\t\t\t   |   |   ')
        print(f"\t\t\t {board_espacio[i*3]} | {board_espacio[i*3+1]} | {board_espacio[i*3+2]} ")
        print('\t\t\t   |   |   ')
        if (i+1) % 3 != 0: 
            print('\t\t\t------------')

def limpiar():
    """Limpiar la consola"""
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def bienvenido():
    print('\t\t________________________')
    print('\t\t J U E G O  T R I Q U I ')
    print('\t\t________________________')
    print("\t\t  Tigo - Data Analytics ")
    print()

def espacio_libre(posicion):
    """Validar si es el espacio en la posción esta disponible.

    Args:
        posicion (int): posición que se quiere validar en la lista

    Returns:
        bool
    """
    return board_espacio[posicion] == ' '

def insertar_letra(posicion:int, letra:str):
    """Función para insertar la letra en el tablero.

    Args:
        posicion (int): posición que se quiere validar en la lista.
        letra (str): caracter a insertar en la lista.
    """
    board_espacio[posicion] = letra

def es_ganador(board_espacio:list, simbolo:str):
    """Validar si se gano en el juego

    Args:
        board (list): lista a validar.
        simbolo (str): caracter a validar si se encuentra en la lista.

    Returns:
        bool
    """
    return (
                (board_espacio[0] == simbolo and board_espacio[1] == simbolo and board_espacio[2] == simbolo)
                or (board_espacio[3] == simbolo and board_espacio[4] == simbolo and board_espacio[5] == simbolo)
                or (board_espacio[6] == simbolo and board_espacio[7] == simbolo and board_espacio[8] == simbolo)
                or (board_espacio[0] == simbolo and board_espacio[3] == simbolo and board_espacio[6] == simbolo)
                or (board_espacio[1] == simbolo and board_espacio[4] == simbolo and board_espacio[7] == simbolo)
                or (board_espacio[2] == simbolo and board_espacio[5] == simbolo and board_espacio[8] == simbolo)
                or (board_espacio[0] == simbolo and board_espacio[4] == simbolo and board_espacio[8] == simbolo)
                or (board_espacio[2] == simbolo and board_espacio[4] == simbolo and board_espacio[6] == simbolo)
            )

def movimiento_computador():
    """Generar movimiento del computador."""
    movimientos_posibles = [i for i, letra in enumerate(board_espacio) if letra == ' ']

    # validar si el movimiento es el ganador
    for jugador in ['O', 'X']:
        for movimiento in movimientos_posibles:
            board_copia = board_espacio[:]
            board_copia[movimiento] = jugador
            if es_ganador(board_copia, jugador):
                return movimiento

    # validar si la posición del centro esta libre
    if 4 in movimientos_posibles:
        return 4

    # jugar en las esquina
    esquinas_abiertas = []
    for i in [0, 2, 6, 8]:
        if i in movimientos_posibles:
            esquinas_abiertas.append(i)

    if len(esquinas_abiertas) > 0:
        return movimiento_aleatorio(esquinas_abiertas)

    # jugar en los bordes
    bordes_abiertos = []
    for i in [1, 3, 5, 7]:
        if i in movimientos_posibles:
            bordes_abiertos.append(i)

    if len(bordes_abiertos) > 0:
        return movimiento_aleatorio(bordes_abiertos)

    # retornar movimiento aleatorio
    return movimiento_aleatorio(movimientos_posibles)

def movimiento_aleatorio(movimientos_posibles:list):
    """Generar movimiento aleatorio de la maquina.
    
    Args:
        movimientos_posibles (list): movimientos disponibles de la maquina

    Returns:
        int: posición a jugar de la maquina.
    """
    tamano = len(movimientos_posibles)
    aleatorio = random.randrange(0, tamano)
    return movimientos_posibles[aleatorio]

def board_llena():
    """Validar si el board esta lleno"""
    if board_espacio.count(' ') > 1:
        return False
    else:
        return True

if __name__ == "__main__":
    main()