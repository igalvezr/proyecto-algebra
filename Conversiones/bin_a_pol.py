import math
from fractions import Fraction

from Tipos import Representaciones

def binomica_a_polar(real, imag):
    modulo = math.sqrt(real**2 + imag**2)
    angulo = math.atan2(imag, real)

    return (modulo, angulo % (2*math.pi), Representaciones.POLAR)