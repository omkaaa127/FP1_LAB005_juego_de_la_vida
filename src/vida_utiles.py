import random

def crear_tablero(filas: int, columnas: int) -> list[list[bool]]:
    """
    Crea un nuevo tablero vacío, con todas las células muertas.
    Parametros:
        filas (int): Número de filas del tablero.
        columnas (int): Número de columnas del tablero.
    Devuelve:
        Una lista de listas con todos los elementos False.
    """
    tablero = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append(False)
        tablero.append(fila)
    return tablero

    

def crear_tablero_aleatorio(filas: int, columnas: int, probabilidad_vida: float) -> list[list[bool]]:
    """
    Crea un tablero con células vivas distribuidas aleatoriamente.

    Parámetros:
        filas (int): Número de filas del tablero.
        columnas (int): Número de columnas del tablero.
        probabilidad_vida (float): Un valor entre 0.0 y 1.0 que representa la
                                   probabilidad de que una célula esté viva.

    Devuelve:
        Una lista de listas que representa el tablero con células vivas (True) y muertas (False).
    """
    tablero = crear_tablero(filas, columnas)
    for fila in tablero:
        for j in range(len(fila)):  # ← aquí estaba el error
            if random.random() < probabilidad_vida:
                fila[j] = True
    return tablero


def insertar_patron(tablero: list[list[bool]], patron: list[list[bool]], pos_fila: int, pos_col: int):
    """
    Inserta un patrón (una pequeña matriz) en el tablero en una posición dada.
    Parámetros:
        tablero (list[list[bool]]): El tablero donde se insertará el patrón.
        patron (list[list[bool]]): El patrón a insertar.
        pos_fila (int): La fila en la que se insertará la esquina superior izquierda del patrón.
        pos_col (int): La columna en la que se insertará la esquina superior izquierda del patrón.
    """

    for i in range(len(patron)):
        if i + pos_fila < len(tablero):
            for j in range(len(patron[i])):
                if j + pos_col < len(tablero[0]):
                    tablero[i + pos_fila][j + pos_col] = patron[i][j]
    return tablero


def contar_vecinos(tablero: list[list[bool]], fila: int, col: int) -> int:
    """
    Cuenta el número de vecinos vivos de una célula en la posición (fila, col).
    El tablero es toroidal, lo que significa que los bordes se conectan.
    Parámetros:
        tablero (list[list[bool]]): El tablero actual.
        fila (int): La fila de la célula.
        col (int): La columna de la célula.
    Devuelve:
        El número de vecinos vivos (int).
    """
    vecinos = 0
    filas = len(tablero)
    columnas = len(tablero[0])

    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            if tablero[(fila + i) % filas][(col + j) % columnas]:
                vecinos += 1
    return vecinos
def calcular_siguiente_generacion(tablero):
    """
    Calcula el estado del tablero en el siguiente paso de tiempo basándose en las reglas
    del Juego de la Vida.
    Parámetros:
        tablero (list[list[bool]]): El tablero actual.
    Devuelve:
        Una nueva lista de listas que representa el tablero en la siguiente generación.
    """
    filas = len(tablero)
    columnas = len(tablero[0])
    res = crear_tablero(filas, columnas)

    for i in range(filas):
        for j in range(columnas):
            vecinos = contar_vecinos(tablero, i, j)
            if tablero[i][j]:
                res[i][j] = vecinos in (2, 3)
            else:
                res[i][j] = vecinos == 3
    return res

