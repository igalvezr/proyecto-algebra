import math
from fractions import Fraction

from Tipos import Representaciones

def polar_a_exponencial(modulo: float, argumento: float):
    return (modulo, argumento, Representaciones.EXPONENCIAL)