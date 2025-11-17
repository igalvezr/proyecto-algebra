from enum import Enum

# operaciones
class Operacion(Enum):
    SUMA = 1
    RESTA = 2
    MULTIPLICACION = 3
    DIVISION = 4
    POTENCIA = 5
    RAIZ = 6
    CONJUGADO = 7

# representaciones
class Representaciones(Enum):
    BINOMICA = 1
    POLAR = 2
    EXPONENCIAL = 3