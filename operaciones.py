# Este módulo implementa operaciones con números complejos en tres representaciones:
# - BINÓMICA: (a, b) → a + bi
# - POLAR: (r, θ) → r cis(θ)
# - EXPONENCIAL: (r, e^{iθ}) → r·e^{iθ}
#
# Todas las funciones devuelven una lista de resultados incluso si la operación
# solo genera un valor (por coherencia con las raíces, que generan varios).
#
# Cada tupla de resultado sigue el formato:
#     (valor_1, valor_2, Representaciones.<tipo>)
#
# donde valor_1 y valor_2 tienen significados diferentes según la representación:
#   - BINÓMICA: (a, b)
#   - POLAR / EXPONENCIAL: (radio, ángulo)
from Tipos import Operacion, Representaciones
import math

from conversion import convertir_a

# ============================================================================
# OPERACIONES BINÓMICAS
# ============================================================================

# Estas funciones operan directamente sobre la representación a + bi sin
# convertir al sistema polar ni exponencial. Son las más directas y precisas
# para suma/resta y suficientemente estables para multiplicación/división.
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
# Las operaciones definidas aquí utilizan propiedades naturales de la forma
# polar: multiplicaciones y divisiones se traducen en operar radios y sumar/
# restar ángulos. Las potencias y raíces se implementan mediante el teorema
# de De Moivre.

def polar_multiplicacion(z1: tuple[float, float, Representaciones], z2: tuple[float, float, Representaciones]) -> list[tuple[float, float, Representaciones]]:
    return [(z1[0] * z2[0], z1[1] + z2[1], Representaciones.POLAR)]
    

def polar_division(z1: tuple[float, float, Representaciones], z2: tuple[float, float, Representaciones]) -> list[tuple[float, float, Representaciones]]:
    if z2[0] == 0:
        raise Exception('el radio de z2 es cero')
    return [(z1[0] / z2[0], z1[1] - z2[1], Representaciones.POLAR)]


def polar_potencia(z1: tuple[float, float, Representaciones], z2: tuple[float, float, Representaciones]) -> list[tuple[float, float, Representaciones]]:
    # Interpreta el primer valor de z2 como el exponente (n).
    # Convierte z2 a binómica porque la parte real de esa forma es la más
    # adecuada para extraer un exponente numérico.
    # NO valida que n sea entero: se asume por diseño que el usuario lo provee.
    z2_b = convertir_a(z2, Representaciones.BINOMICA)
    n = int(z2_b[0])
    
    return [(z1[0] ** n, z1[1] * n, Representaciones.POLAR)]


def polar_raiz(z1: tuple[float, float, Representaciones], z2: tuple[float, float, Representaciones]) -> list[tuple[float, float, Representaciones]]:
    # Calcula la raíz n-ésima de un complejo en forma polar.
    # Devuelve n resultados, correspondientes a los ángulos:
    #   (θ + 2πk) / n   para k = 0, 1, ..., n-1
    #
    # Cada resultado lleva un radio r^(1/n).
    # El ángulo NO se normaliza aquí porque se normaliza globalmente en `operar()`.
    z2_b = convertir_a(z2, Representaciones.BINOMICA)
    n = int(z2_b[0])
    
    k = list(range(0, n))

    w = list()
    for elem in k:
        w.append((z1[0] ** (1/n), (z1[1] + 2 * math.pi * elem) / n, Representaciones.POLAR))
    return w


# ============================================================================
# OPERACIONES EXPONENCIALES
# ============================================================================
# Estas funciones son análogas a las polares, pero operan bajo la convención
# r·e^{iθ}. Matemáticamente son equivalentes a polar, pero se mantienen
# separadas por claridad semántica en la interfaz del programa.

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
# Tabla que asocia:
#   (tipo_de_representación, operación) → función correspondiente
#
# Esto permite que `operar()` seleccione automáticamente la función adecuada
# sin depender de estructuras condicionales extensas.

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
    # FUNCIÓN PRINCIPAL DE OPERACIÓN
    #
    # `operar(z1, z2, operacion)` determina qué representación es más conveniente
    # para realizar la operación, la ejecuta y luego devuelve el resultado en una
    # representación "deseada".
    #
    # Flujo general:
    # 1. Determinar el tipo de salida:
    #    - Si z1 y z2 comparten representación, se usa esa.
    #    - Si no, por defecto se regresa en BINÓMICA.
    #
    # 2. Seleccionar la representación con la que se realizará la operación:
    #    Intenta POLAR → luego EXPONENCIAL → luego BINÓMICA.
    #    (El orden refleja que ciertas operaciones son más naturales/eficientes en
    #     forma polar o exponencial, por ejemplo multiplicaciones o potencias.)
    #
    # 3. Convertir z1 y z2 a la representación seleccionada.
    #
    # 4. Ejecutar la función correspondiente de `mapa_operaciones`.
    #
    # 5. Convertir cada resultado a la representación deseada.
    #
    # 6. Normalizar los ángulos (si la representación no es binómica), forzándolos
    #    al rango [0, 2π).
    # Nota: La operación "conjugado" ignora z2, pero mantiene la firma general
    # (z1, z2) para poder convivir sin problemas dentro del sistema de despacho.

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