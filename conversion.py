from Conversiones.bin_a_pol import binomica_a_polar
from Conversiones.bin_a_pol import binomica_a_polar
from Conversiones.bin_a_expo import binomica_a_exponencial
from Conversiones.pol_a_bin import polar_a_binomica
from Conversiones.pol_a_expo import polar_a_exponencial
from Conversiones.expo_a_bin import exponencial_a_binomica
from Conversiones.expo_a_pol import exponencial_a_polar
from Tipos import Representaciones


mapa_conversiones = {
    (Representaciones.BINOMICA, Representaciones.POLAR): binomica_a_polar,
    (Representaciones.BINOMICA, Representaciones.EXPONENCIAL): binomica_a_exponencial,
    (Representaciones.POLAR, Representaciones.BINOMICA): polar_a_binomica,
    (Representaciones.POLAR, Representaciones.EXPONENCIAL): polar_a_exponencial,
    (Representaciones.EXPONENCIAL, Representaciones.BINOMICA): exponencial_a_binomica,
    (Representaciones.EXPONENCIAL, Representaciones.POLAR): exponencial_a_polar,
}

def convertir_a(z: tuple[float, float, Representaciones], a: Representaciones):
    if z[2] == a:
        return z
    return mapa_conversiones[(z[2], a)](z[0], z[1])