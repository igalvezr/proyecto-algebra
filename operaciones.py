from Tipos import Operacion, Representaciones
import math

from conversion import convertir_a

# ============================================================================
# OPERACIONES BINÓMICAS
# ============================================================================

def binomica_suma(z1: tuple[float, float, Representaciones], z2: tuple[float, float, Representaciones]) -> list[tuple[float, float, Representaciones]]:
    return [(z1[0] + z2[0], z1[1] + z2[1], Representaciones.BINOMICA)]
    

def binomica_resta(z1: tuple[float, float, Representaciones], z2: tuple[float, float, Representaciones]) -> list[tuple[float, float, Representaciones]]:
    return [(z1[0] - z2[0], z1[1] - z2[1], Representaciones.BINOMICA)]

def binomica_multiplicacion(z1: tuple[float, float, Representaciones], z2: tuple[float, float, Representaciones]) -> list[tuple[float, float, Representaciones]]:
    return [(z1[0]*z2[0] - z1[1]*z2[1], z1[0]*z2[1] + z1[1]*z2[0], Representaciones.BINOMICA)]

def binomica_division(z1: tuple[float, float, Representaciones], z2: tuple[float, float, Representaciones]) -> list[tuple[float, float, Representaciones]]:
    divisor = z2[0]**2 + z2[1]**2
    if divisor == 0:
        raise Exception('El divisor es cero')
    
    return [((z1[0]*z2[0] + z1[1]*z2[1]) / divisor, (z1[1]*z2[0] - z1[0]*z2[1]) / divisor, Representaciones.BINOMICA)]

def binomica_conjugado(z1: tuple[float, float, Representaciones], z2 = None) -> list[tuple[float, float, Representaciones]]:
    return [(z1[0], -z1[1], Representaciones.BINOMICA)]

# ============================================================================
# OPERACIONES POLARES
# ============================================================================

def polar_multiplicacion(z1: tuple[float, float, Representaciones], z2: tuple[float, float, Representaciones]) -> list[tuple[float, float, Representaciones]]:
    return [(z1[0] * z2[0], z1[1] + z2[1], Representaciones.POLAR)]
    

def polar_division(z1: tuple[float, float, Representaciones], z2: tuple[float, float, Representaciones]) -> list[tuple[float, float, Representaciones]]:
    if z2[0] == 0:
        raise Exception('el radio de z2 es cero')
    return [(z1[0] / z2[0], z1[1] - z2[1], Representaciones.POLAR)]


def polar_potencia(z1: tuple[float, float, Representaciones], z2: tuple[float, float, Representaciones]) -> list[tuple[float, float, Representaciones]]:
    z2_b = convertir_a(z2, Representaciones.BINOMICA)
    n = int(z2_b[0])
    
    return [(z1[0] ** n, z1[1] * n, Representaciones.POLAR)]


def polar_raiz(z1: tuple[float, float, Representaciones], z2: tuple[float, float, Representaciones]) -> list[tuple[float, float, Representaciones]]:
    z2_b = convertir_a(z2, Representaciones.BINOMICA)
    n = int(z2_b[0])
    
    k = list(range(0, n))

    w = list()
    for elem in k:
        w.append((z1[0] ** (1/n), (z1[1] + 2 * math.pi * elem) / n))
    return w


# ============================================================================
# OPERACIONES EXPONENCIALES
# ============================================================================

def exponencial_multiplicacion(z1: tuple[float, float, Representaciones], z2: tuple[float, float, Representaciones]) -> list[tuple[float, float, Representaciones]]:
    return [(z1[0]*z2[0], z1[1]+z2[1], Representaciones.EXPONENCIAL)]

def exponencial_division(z1: tuple[float, float, Representaciones], z2: tuple[float, float, Representaciones]) -> list[tuple[float, float, Representaciones]]:
    if z2[0] == 0:
        raise Exception('el radio de z2 es cero')
    return [(z1[0]/z2[0], z1[1] - z2[1], Representaciones.EXPONENCIAL)]

def exponencial_potencia(z1: tuple[float, float, Representaciones], z2: tuple[float, float, Representaciones]) -> list[tuple[float, float, Representaciones]]:
    z2_b = convertir_a(z2, Representaciones.BINOMICA)
    n = int(z2_b[0])
    return [(z1[0] ** n, z1[1] * n, Representaciones.EXPONENCIAL)]

def exponencial_raiz(z1: tuple[float, float, Representaciones], z2: tuple[float, float, Representaciones]) -> list[tuple[float, float, Representaciones]]:
    z2_b = convertir_a(z2, Representaciones.BINOMICA)
    n = int(z2_b[0])
    
    k = list(range(0, n))

    w = list()
    for elem in k:
        w.append((z1[0] ** (1/n), (z1[1] + 2 * math.pi * elem) / n, Representaciones.EXPONENCIAL))
    return w


# ============================================================================
# DISPATCH TABLE - Tabla de operaciones
# ============================================================================


mapa_operaciones = {
    (Representaciones.BINOMICA, Operacion.SUMA): binomica_suma,
    (Representaciones.BINOMICA, Operacion.RESTA): binomica_resta,
    (Representaciones.BINOMICA, Operacion.MULTIPLICACION): binomica_multiplicacion,
    (Representaciones.BINOMICA, Operacion.DIVISION): binomica_division,
    (Representaciones.BINOMICA, Operacion.CONJUGADO): binomica_conjugado,
    (Representaciones.EXPONENCIAL, Operacion.MULTIPLICACION): exponencial_multiplicacion,
    (Representaciones.EXPONENCIAL, Operacion.DIVISION): exponencial_division,
    (Representaciones.EXPONENCIAL, Operacion.POTENCIA): exponencial_potencia,
    (Representaciones.EXPONENCIAL, Operacion.RAIZ): exponencial_raiz,
}

def operar(z1: tuple[float, float, Representaciones], z2: tuple[float, float, Representaciones], operacion: Operacion):
    # definir el tipo deseado
    tipo_deseado = Representaciones.BINOMICA
    if z1[2] == z2[2]:
        tipo_deseado = z1[2]
    # definir el tipo a realizar
    tipo_operacion = Representaciones.POLAR
    funcion = mapa_operaciones.get((tipo_operacion, operacion), None)

    if not funcion:
        tipo_operacion = Representaciones.EXPONENCIAL
        funcion = mapa_operaciones.get((tipo_operacion, operacion), None)
    if not funcion:
        tipo_operacion = Representaciones.BINOMICA
        funcion = mapa_operaciones.get((tipo_operacion, operacion), None)
    if not funcion:
        raise Exception("La operacion no está definida")
    
    # operar
    z1_c = convertir_a(z1, tipo_operacion)
    z2_c = convertir_a(z2, tipo_operacion)
    resultados = funcion(z1_c, z2_c)

    # convertir los resultados
    resultados_c = [convertir_a(w, tipo_deseado) for w in resultados]

    # normalizar los resultados antes de entregarlos
    if resultados_c[0][2] != Representaciones.BINOMICA:
        resultados_c = [(res[0], res[1] % (2*math.pi), res[2]) for res in resultados_c]

    # regresar los resultados
    return resultados_c