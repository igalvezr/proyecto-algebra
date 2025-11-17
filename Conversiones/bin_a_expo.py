import math
from fractions import Fraction

from Tipos import Representaciones

def binomica_a_exponencial(real, imag):
    modulo = math.sqrt(real**2 + imag**2)
    argumento = math.atan2(imag, real)

    return (modulo, argumento % (2*math.pi), Representaciones.EXPONENCIAL)