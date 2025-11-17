import math

from Tipos import Representaciones

def polar_a_binomica(modulo, argumento):
    #Calcular el numero real
    real = modulo * math.cos(argumento)
    
    #Calcular el numero imaginario
    imag = modulo * math.sin(argumento)
    
    return (real, imag, Representaciones.BINOMICA)