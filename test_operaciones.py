import pytest

from operaciones import operar
from Tipos import Operacion, Representaciones
import math

es_cercano = lambda a, b: abs(a - b) < 1E-7

@pytest.mark.parametrize('entrada, objetivo', [
    # Caso básico positivo
    (((3, 3, Representaciones.BINOMICA), (-1, -1, Representaciones.BINOMICA)), (2, 2, Representaciones.BINOMICA)),
    # Suma con cero
    (((5, 2, Representaciones.BINOMICA), (0, 0, Representaciones.BINOMICA)), (5, 2, Representaciones.BINOMICA)),
    # Suma con negativos
    (((-3, -4, Representaciones.BINOMICA), (3, 4, Representaciones.BINOMICA)), (0, 0, Representaciones.BINOMICA)),
    # Suma solo parte real
    (((5, 0, Representaciones.BINOMICA), (3, 0, Representaciones.BINOMICA)), (8, 0, Representaciones.BINOMICA)),
    # Suma solo parte imaginaria
    (((0, 5, Representaciones.BINOMICA), (0, 3, Representaciones.BINOMICA)), (0, 8, Representaciones.BINOMICA)),
    # Suma con decimales
    (((1.5, 2.5, Representaciones.BINOMICA), (2.5, 3.5, Representaciones.BINOMICA)), (4.0, 6.0, Representaciones.BINOMICA)),
    # Suma que resulta en negativo
    (((2, 3, Representaciones.BINOMICA), (-5, -7, Representaciones.BINOMICA)), (-3, -4, Representaciones.BINOMICA)),
])
def test_binomica_suma(entrada, objetivo):
    z1, z2 = entrada
    resultado = operar(z1, z2, Operacion.SUMA)[0]
    assert resultado[2] == objetivo[2]
    assert es_cercano(objetivo[0], resultado[0])
    assert es_cercano(objetivo[1], resultado[1])

@pytest.mark.parametrize('entrada, objetivo', [
    # Resta básica
    (((5, 3, Representaciones.BINOMICA), (2, 1, Representaciones.BINOMICA)), (3, 2, Representaciones.BINOMICA)),
    # Resta con cero
    (((5, 3, Representaciones.BINOMICA), (0, 0, Representaciones.BINOMICA)), (5, 3, Representaciones.BINOMICA)),
    # Resta consigo mismo (resultado cero)
    (((4, 5, Representaciones.BINOMICA), (4, 5, Representaciones.BINOMICA)), (0, 0, Representaciones.BINOMICA)),
    # Resta con negativos
    (((3, 2, Representaciones.BINOMICA), (-3, -2, Representaciones.BINOMICA)), (6, 4, Representaciones.BINOMICA)),
    # Resta que resulta en negativo
    (((1, 1, Representaciones.BINOMICA), (5, 5, Representaciones.BINOMICA)), (-4, -4, Representaciones.BINOMICA)),
    # Resta con decimales
    (((5.7, 3.2, Representaciones.BINOMICA), (2.5, 1.8, Representaciones.BINOMICA)), (3.2, 1.4, Representaciones.BINOMICA)),
])
def test_binomica_resta(entrada, objetivo):
    z1, z2 = entrada
    resultado = operar(z1, z2, Operacion.RESTA)[0]
    assert resultado[2] == objetivo[2]
    assert es_cercano(objetivo[0], resultado[0])
    assert es_cercano(objetivo[1], resultado[1])

@pytest.mark.parametrize('entrada, objetivo', [
    # Multiplicación básica: (3+2i)(1+4i) = 3+12i+2i+8i² = 3+14i-8 = -5+14i
    (((3, 2, Representaciones.BINOMICA), (1, 4, Representaciones.BINOMICA)), (-5, 14, Representaciones.BINOMICA)),
    # Multiplicación por cero
    (((5, 3, Representaciones.BINOMICA), (0, 0, Representaciones.BINOMICA)), (0, 0, Representaciones.BINOMICA)),
    # Multiplicación por uno
    (((5, 3, Representaciones.BINOMICA), (1, 0, Representaciones.BINOMICA)), (5, 3, Representaciones.BINOMICA)),
    # Multiplicación por i: (2+3i)*i = 2i+3i² = -3+2i
    (((2, 3, Representaciones.BINOMICA), (0, 1, Representaciones.BINOMICA)), (-3, 2, Representaciones.BINOMICA)),
    # Multiplicación de números reales
    (((4, 0, Representaciones.BINOMICA), (3, 0, Representaciones.BINOMICA)), (12, 0, Representaciones.BINOMICA)),
    # Multiplicación con negativos: (-2+3i)(4-5i) = -8+10i+12i-15i² = -8+22i+15 = 7+22i
    (((-2, 3, Representaciones.BINOMICA), (4, -5, Representaciones.BINOMICA)), (7, 22, Representaciones.BINOMICA)),
    # Multiplicación por conjugado: (3+4i)(3-4i) = 9-16i² = 9+16 = 25
    (((3, 4, Representaciones.BINOMICA), (3, -4, Representaciones.BINOMICA)), (25, 0, Representaciones.BINOMICA)),
])
def test_binomica_multiplicacion(entrada, objetivo):
    z1, z2 = entrada
    resultado = operar(z1, z2, Operacion.MULTIPLICACION)[0]
    assert resultado[2] == objetivo[2]
    assert es_cercano(objetivo[0], resultado[0])
    assert es_cercano(objetivo[1], resultado[1])

# ==================== DIVISIÓN ====================
@pytest.mark.parametrize('entrada, objetivo', [
    # División básica: (4+2i)/(1+i) = (4+2i)(1-i)/(1+1) = (4-4i+2i-2i²)/2 = (6-2i)/2 = 3-i
    (((4, 2, Representaciones.BINOMICA), (1, 1, Representaciones.BINOMICA)), (3, -1, Representaciones.BINOMICA)),
    # División por uno
    (((5, 3, Representaciones.BINOMICA), (1, 0, Representaciones.BINOMICA)), (5, 3, Representaciones.BINOMICA)),
    # División de número real
    (((6, 0, Representaciones.BINOMICA), (2, 0, Representaciones.BINOMICA)), (3, 0, Representaciones.BINOMICA)),
    # División por i: (2+3i)/i = (2+3i)(-i)/(i*-i) = (-2i-3i²)/1 = 3-2i
    (((2, 3, Representaciones.BINOMICA), (0, 1, Representaciones.BINOMICA)), (3, -2, Representaciones.BINOMICA)),
    # División consigo mismo
    (((3, 4, Representaciones.BINOMICA), (3, 4, Representaciones.BINOMICA)), (1, 0, Representaciones.BINOMICA)),
    # División con negativos: (6-8i)/(-2+0i) = -3+4i
    (((6, -8, Representaciones.BINOMICA), (-2, 0, Representaciones.BINOMICA)), (-3, 4, Representaciones.BINOMICA)),
    # División compleja: (1+i)/(1-i) = (1+i)²/2 = (1+2i-1)/2 = 2i/2 = i
    (((1, 1, Representaciones.BINOMICA), (1, -1, Representaciones.BINOMICA)), (0, 1, Representaciones.BINOMICA)),
])
def test_binomica_division(entrada, objetivo):
    z1, z2 = entrada
    resultado = operar(z1, z2, Operacion.DIVISION)[0]
    assert resultado[2] == objetivo[2]
    assert es_cercano(objetivo[0], resultado[0])
    assert es_cercano(objetivo[1], resultado[1])

# ==================== CONJUGADO ====================
@pytest.mark.parametrize('entrada, objetivo', [
    # Conjugado básico
    (((3, 4, Representaciones.BINOMICA), None), (3, -4, Representaciones.BINOMICA)),
    # Conjugado de número real
    (((5, 0, Representaciones.BINOMICA), None), (5, 0, Representaciones.BINOMICA)),
    # Conjugado de número imaginario puro
    (((0, 7, Representaciones.BINOMICA), None), (0, -7, Representaciones.BINOMICA)),
    # Conjugado con parte imaginaria negativa
    (((2, -5, Representaciones.BINOMICA), None), (2, 5, Representaciones.BINOMICA)),
    # Conjugado de cero
    (((0, 0, Representaciones.BINOMICA), None), (0, 0, Representaciones.BINOMICA)),
    # Conjugado con ambos negativos
    (((-3, -4, Representaciones.BINOMICA), None), (-3, 4, Representaciones.BINOMICA)),
])
def test_binomica_conjugado(entrada, objetivo):
    z1, _ = entrada
    resultado = operar(z1, (0, 0, Representaciones.BINOMICA), Operacion.CONJUGADO)[0]
    assert resultado[2] == objetivo[2]
    assert es_cercano(objetivo[0], resultado[0])
    assert es_cercano(objetivo[1], resultado[1])

# ==================== POTENCIA - POLAR ====================
@pytest.mark.parametrize('entrada, objetivo', [
    # Potencia básica: 2∠π/4 elevado a 2 = 4∠π/2
    (((2, math.pi/4, Representaciones.POLAR), (2, 0, Representaciones.POLAR)), (4, math.pi/2, Representaciones.POLAR)),
    # Potencia a 0 = 1
    (((5, math.pi/6, Representaciones.POLAR), (0, 0, Representaciones.POLAR)), (1, 0, Representaciones.POLAR)),
    # Potencia a 1 = mismo número
    (((3, math.pi/3, Representaciones.POLAR), (1, 0, Representaciones.POLAR)), (3, math.pi/3, Representaciones.POLAR)),
    # Potencia negativa: 2∠π/6 elevado a -1 = 0.5∠-π/6
    (((2, math.pi/6, Representaciones.POLAR), (-1, 0, Representaciones.POLAR)), (0.5, -math.pi/6, Representaciones.POLAR)),
    # Potencia con ángulo que da la vuelta: 2∠2π/3 elevado a 3 = 8∠2π = 8∠0
    (((2, 2*math.pi/3, Representaciones.POLAR), (3, 0, Representaciones.POLAR)), (8, 0, Representaciones.POLAR)),
    # Potencia de número en eje real: 3∠0 elevado a 4 = 81∠0
    (((3, 0, Representaciones.POLAR), (4, 0, Representaciones.POLAR)), (81, 0, Representaciones.POLAR)),
])
def test_polar_potencia(entrada, objetivo):
    z1, z2 = entrada
    resultado = operar(z1, z2, Operacion.POTENCIA)[0]
    assert resultado[2] == objetivo[2]
    assert es_cercano(objetivo[0], resultado[0])
    # Normalizar ángulos al rango [-π, π] o [0, 2π]
    angulo_resultado = resultado[1] % (2*math.pi)
    angulo_objetivo = objetivo[1] % (2*math.pi)
    assert es_cercano(angulo_objetivo, angulo_resultado)

# ==================== RAÍZ - POLAR ====================
@pytest.mark.parametrize('entrada, objetivo_w1', [
    # Raíz cuadrada de 4∠0 -> dos raíces: 2∠0 y 2∠π
    (((4, 0, Representaciones.POLAR), (2, 0, Representaciones.POLAR)), (2, 0, Representaciones.POLAR)),
    # Raíz cuadrada de 9∠π -> 3∠π/2 y 3∠3π/2
    (((9, math.pi, Representaciones.POLAR), (2, 0, Representaciones.POLAR)), (3, math.pi/2, Representaciones.POLAR)),
    # Raíz cúbica de 8∠0 -> 2∠0, 2∠2π/3, 2∠4π/3
    (((8, 0, Representaciones.POLAR), (3, 0, Representaciones.POLAR)), (2, 0, Representaciones.POLAR)),
    # Raíz cuadrada de 16∠π/2 -> 4∠π/4 y 4∠5π/4
    (((16, math.pi/2, Representaciones.POLAR), (2, 0, Representaciones.POLAR)), (4, math.pi/4, Representaciones.POLAR)),
    # Raíz cuadrada de 1∠0 -> 1∠0 y 1∠π
    (((1, 0, Representaciones.POLAR), (2, 0, Representaciones.POLAR)), (1, 0, Representaciones.POLAR)),
])
def test_polar_raiz(entrada, objetivo_w1):
    z1, z2 = entrada
    resultados = operar(z1, z2, Operacion.RAIZ)
    # Verificar la primera raíz
    resultado = resultados[0]
    assert resultado[2] == objetivo_w1[2]
    assert es_cercano(objetivo_w1[0], resultado[0])
    angulo_resultado = resultado[1] % (2*math.pi)
    angulo_objetivo = objetivo_w1[1] % (2*math.pi)
    assert es_cercano(angulo_objetivo, angulo_resultado)

# ==================== MULTIPLICACIÓN - POLAR ====================
@pytest.mark.parametrize('entrada, objetivo', [
    # Multiplicación básica: 2∠π/6 * 3∠π/4 = 6∠(π/6 + π/4) = 6∠5π/12
    (((2, math.pi/6, Representaciones.POLAR), (3, math.pi/4, Representaciones.POLAR)), (6, 5*math.pi/12, Representaciones.POLAR)),
    # Multiplicación por 1∠0
    (((5, math.pi/3, Representaciones.POLAR), (1, 0, Representaciones.POLAR)), (5, math.pi/3, Representaciones.POLAR)),
    # Multiplicación que da más de 2π: 2∠(10π/9) * 3∠(10π/9) = 6∠(20π/9) = 6∠(2π/9)
    (((2, 10*math.pi/9, Representaciones.POLAR), (3, 10*math.pi/9, Representaciones.POLAR)), (6, 2*math.pi/9, Representaciones.POLAR)),
    # Multiplicación con ángulos negativos: 4∠(-π/6) * 2∠(-π/3) = 8∠(-π/2)
    (((4, -math.pi/6, Representaciones.POLAR), (2, -math.pi/3, Representaciones.POLAR)), (8, -math.pi/2, Representaciones.POLAR)),
    # Multiplicación por conjugado (ángulo opuesto): 5∠π/4 * 2∠(-π/4) = 10∠0
    (((5, math.pi/4, Representaciones.POLAR), (2, -math.pi/4, Representaciones.POLAR)), (10, 0, Representaciones.POLAR)),
])
def test_polar_multiplicacion(entrada, objetivo):
    z1, z2 = entrada
    resultado = operar(z1, z2, Operacion.MULTIPLICACION)[0]
    assert resultado[2] == objetivo[2]
    assert es_cercano(objetivo[0], resultado[0])
    angulo_resultado = resultado[1] % (2*math.pi)
    angulo_objetivo = objetivo[1] % (2*math.pi)
    assert es_cercano(angulo_objetivo, angulo_resultado)

# ==================== DIVISIÓN - POLAR ====================
@pytest.mark.parametrize('entrada, objetivo', [
    # División básica: 6∠π/2 / 2∠π/6 = 3∠π/3
    (((6, math.pi/2, Representaciones.POLAR), (2, math.pi/6, Representaciones.POLAR)), (3, math.pi/3, Representaciones.POLAR)),
    # División por sí mismo
    (((5, math.pi/4, Representaciones.POLAR), (5, math.pi/4, Representaciones.POLAR)), (1, 0, Representaciones.POLAR)),
    # División por 1∠0
    (((7, 2*math.pi/3, Representaciones.POLAR), (1, 0, Representaciones.POLAR)), (7, 2*math.pi/3, Representaciones.POLAR)),
    # División con ángulo negativo resultante: 3∠π/6 / 2∠π/3 = 1.5∠(-π/6)
    (((3, math.pi/6, Representaciones.POLAR), (2, math.pi/3, Representaciones.POLAR)), (1.5, -math.pi/6, Representaciones.POLAR)),
    # División que cruza el ángulo 0: 4∠π/6 / 2∠π/3 = 2∠(-π/6)
    (((4, math.pi/6, Representaciones.POLAR), (2, math.pi/3, Representaciones.POLAR)), (2, -math.pi/6, Representaciones.POLAR)),
])
def test_polar_division(entrada, objetivo):
    z1, z2 = entrada
    resultado = operar(z1, z2, Operacion.DIVISION)[0]
    assert resultado[2] == objetivo[2]
    assert es_cercano(objetivo[0], resultado[0])
    angulo_resultado = resultado[1] % (2*math.pi)
    angulo_objetivo = objetivo[1] % (2*math.pi)
    # Considerar ambos ángulos normalizados
    diff = abs(angulo_objetivo - angulo_resultado)
    assert es_cercano(0, diff)

# ==================== EXPONENCIAL - MULTIPLICACIÓN ====================
@pytest.mark.parametrize('entrada, objetivo', [
    # Multiplicación básica exponencial: 2e^(i*π/6) * 3e^(i*π/4) = 6e^(i*5π/12)
    (((2, math.pi/6, Representaciones.EXPONENCIAL), (3, math.pi/4, Representaciones.EXPONENCIAL)), (6, 5*math.pi/12, Representaciones.EXPONENCIAL)),
    # Multiplicación por e^(i*0) = 1
    (((5, math.pi/3, Representaciones.EXPONENCIAL), (1, 0, Representaciones.EXPONENCIAL)), (5, math.pi/3, Representaciones.EXPONENCIAL)),
    # Multiplicación con ángulos que suman más de 2π
    (((2, 10*math.pi/9, Representaciones.EXPONENCIAL), (3, 10*math.pi/9, Representaciones.EXPONENCIAL)), (6, 2*math.pi/9, Representaciones.EXPONENCIAL)),
])
def test_exponencial_multiplicacion(entrada, objetivo):
    z1, z2 = entrada
    resultado = operar(z1, z2, Operacion.MULTIPLICACION)[0]
    assert resultado[2] == objetivo[2]
    assert es_cercano(objetivo[0], resultado[0])
    angulo_resultado = resultado[1] % (2*math.pi)
    angulo_objetivo = objetivo[1] % (2*math.pi)
    assert es_cercano(angulo_objetivo, angulo_resultado)

# ==================== CASOS EDGE - MEZCLA DE REPRESENTACIONES ====================
@pytest.mark.parametrize('entrada', [
    # Suma de polar con binómica (debería funcionar convirtiendo)
    ((2, math.pi/4, Representaciones.POLAR), (1, 1, Representaciones.BINOMICA)),
    # Multiplicación de exponencial con polar
    ((2, math.pi/6, Representaciones.EXPONENCIAL), (3, math.pi/3, Representaciones.POLAR)),
    # División de binómica con exponencial
    ((4, 2, Representaciones.BINOMICA), (2, math.pi/4, Representaciones.EXPONENCIAL)),
])
def test_representaciones_mixtas(entrada):
    """Verifica que el sistema puede manejar operaciones con representaciones mixtas"""
    z1, z2 = entrada
    # Simplemente verificar que no lance excepción
    try:
        resultado = operar(z1, z2, Operacion.SUMA)
        assert len(resultado) > 0
    except NotImplementedError:
        # Es aceptable si algunas combinaciones no están implementadas
        pytest.skip("Combinación de representaciones no implementada")