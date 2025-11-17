import math

from Tipos import Representaciones

def exponencial_a_binomica(modulo: float, angulo: float):
   
    #Calcular el numero real
    real = modulo * math.cos(angulo)
    
    #Calcular el numero imaginario
    imag = modulo * math.sin(angulo)
    
    return (real, imag, Representaciones.BINOMICA)
