'''
Mapeo de funciones para conversión.

Se encarga de tomar las funciones de conversión definidas individualmente,
colocarlas en un dispath table para una indexación más sencilla,
y se define una interfaz genérica para acceder a la conversión desde 
la representación de un complejo dado a cualquier otra, sin
necesidad de utilizar cada conversión de forma individual.
'''
from Conversiones.bin_a_pol import binomica_a_polar
from Conversiones.bin_a_pol import binomica_a_polar
from Conversiones.bin_a_expo import binomica_a_exponencial
from Conversiones.pol_a_bin import polar_a_binomica
from Conversiones.pol_a_expo import polar_a_exponencial
from Conversiones.expo_a_bin import exponencial_a_binomica
from Conversiones.expo_a_pol import exponencial_a_polar
from Tipos import Representaciones


# El dispatch table
#
# Permite obtener la función que transforma la primera representación a la
# segunda
mapa_conversiones = {
    (Representaciones.BINOMICA, Representaciones.POLAR): binomica_a_polar,
    (Representaciones.BINOMICA, Representaciones.EXPONENCIAL): binomica_a_exponencial,
    (Representaciones.POLAR, Representaciones.BINOMICA): polar_a_binomica,
    (Representaciones.POLAR, Representaciones.EXPONENCIAL): polar_a_exponencial,
    (Representaciones.EXPONENCIAL, Representaciones.BINOMICA): exponencial_a_binomica,
    (Representaciones.EXPONENCIAL, Representaciones.POLAR): exponencial_a_polar,
}

def convertir_a(z: tuple[float, float, Representaciones], a: Representaciones):
    '''
    Convierte un complejo dado a otra representación.
    
    :param z: El complejo a convertir
    :type z: tuple[float, float, Representaciones]
    :param a: La literal que indica la representación objetivo
    :type a: Representaciones
    '''

    # Si el complejo dado ya tiene la representación objetivo, se devuelve tal cual
    if z[2] == a:
        return z
    
    # Se indexa la dispatch table para obtener la función de conversión adecuada, y se ejecuta
    # dicha función para devolver el complejo convertido.
    return mapa_conversiones[(z[2], a)](z[0], z[1])