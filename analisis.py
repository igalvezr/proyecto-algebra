import re
import math

from Tipos import Representaciones



def analizar_angulo(s: str) -> float:
    '''
    Convierte un texto que representa un pangulo a su valor en radianes.
    
    :param s: El string que contiene la sintaxis del ángulo
    :type s: str
    :return: El valor del ángulo en radianes
    :rtype: float
    '''
    if not s:
        raise Exception('El string de ángulo está vacío')
    
    angulo = 0.0
    rad = True

    # Se determina si se usan grados sexagesimales, o radianes
    if '°' in s:
        # Se usan grados
        s = s.replace('°', '')
        if not s:
            raise Exception('Grados sexagesimales sin literal numérica')
        rad = False
    elif 'pi' in s or 'π' in s:
        # Se usan radianes
        s = s.replace('pi', '')
        s = s.replace('π', '')
        rad = True
    else:
        # Si no contiene ninguno de ambos símbolos es una literal inválida
        raise Exception(f'Sintaxis de ángulo inválida: "{s}"')
    
    # Se intenta convertir el texto restante a un número
    try:
        # si el string quedó vacío, significaba que el símbolo estaba solo. Por tanto, se tiene un 1 de valor
        angulo = float(s) if s else 1
    except:
        # No era un número flotante válido
        try:
            angulo = float(eval(s)) if s else 1
        except SyntaxError:
            raise Exception(f'Sintaxis inválida "{s}"')
    
    # Según si se tenían radianes o grados, se convierten para que sean el valor correcto
    if rad:
        return angulo * math.pi
    else:
        return angulo * (math.pi / 180)


def desde_binomica(s: str) -> tuple[float, float, Representaciones]:
    '''
    Convierte una literal de texto a un complejo en forma binómica
    
    :param s: La literal de texto que representa el complejo
    :type s: str
    :return: Un tupla con tres elementos: la parte real, la parte imaginaria, y una constante indicando la representación
    :rtype: tuple[float, float, Representaciones]
    '''

    # No se puede analizar un string vacío
    if not s:
        raise Exception('El string de entrada está vacío')
    
    # Este regex separa el string en secciones cuando encuentra un número seguido de un signo, ya sea + o -
    secciones = re.split(r'(?<=\d)(?=[+-])', s)
    real = 0.0
    imag = 0.0

    # Se analiza cada parte encontrada por re.split
    for seccion in secciones:
        # se extrae el símbolo del signo para mayor facilidad de análisis
        signo = -1 if '-' in seccion else 1
        seccion = seccion.replace('+', '')
        seccion = seccion.replace('-', '')

        if 'i' in seccion:
            # si se encuentra la literal i, significa que es la parte imaginaria
            # Se elimina la literal i para quedarse solo con el número
            seccion = seccion.replace('i', '')
            if not seccion:
                # Si la literal queda vacía, se asume un 1
                imag = signo
            else:
                # Se transforma el texto a número, multiplicando por el signo
                imag = float(seccion) * signo
        else:
            # Si no, es la parte real
            try:
                real = float(seccion) * signo if seccion else 0.0
            except:
                raise Exception('No se puede convertr a float')
    # Nota: si se encuentran dos o mas partes, ya sean reales o imaginarias, se queda con la última, ya que se sobreescriben los valores
    
    return (real, imag, Representaciones.BINOMICA)


def desde_polar(s: str) -> tuple[float, float, Representaciones]:
    '''
    Convierte una literal de texto en un complejo en forma polar
    
    :param s: La literal que representa al complejo
    :type s: str
    :return: Una tupla con tres valores: el módulo, el ángulo, y una literal que indica la representación.
    :rtype: tuple[float, float, Representaciones]
    '''

    # Se separa en dos partes justo donde se encuentre la palabra 'cis'
    radio_s, angulo_s = re.split(r'(?=cis)', s)
    # se eliminan los símbolos adicionales
    angulo_s = angulo_s.replace('cis(', '')
    angulo_s = angulo_s.replace(')', '')

    # se envía a la función de apoyo para analizar el texto que contiene solo el ángulo
    angulo = analizar_angulo(angulo_s)
    # Se convierte el valor del módulo a un número flotante. Si está vacío, se asume la presencia de un 1
    radio = float(eval(radio_s)) if radio_s else 1

    return (radio, angulo, Representaciones.POLAR)


def desde_exponencial(s: str) -> tuple[float, float, Representaciones]:
    '''
    Convierte una literal de texto en un complejo en forma exponencial
    
    :param s: La literal que representa al complejo
    :type s: str
    :return: Una tupla con tres valores: el módulo, el ángulo, y una literal que indica la representación.
    :rtype: tuple[float, float, Representaciones]
    '''

    # Se separa en dos partes justo donde se encuentre la literal 'e^'
    radio_s, angulo_s = re.split(r'(?=e\^)', s)

    # Se utiliza eval para evaluar cualquier fracción que pueda aparecer en la literal del módulo
    radio = float(eval(radio_s)) if radio_s else 1

    # Se eliminan los símbolos adicionales
    angulo_s = angulo_s.replace('e^(', '')
    angulo_s = angulo_s.replace(')', '')
    angulo_s = angulo_s.replace('i)', '')
    # Se convierte el valor del módulo a un número flotante.
    angulo = analizar_angulo(angulo_s)

    return (radio, angulo, Representaciones.EXPONENCIAL)

def a_complejo(s: str) -> tuple[float, float, Representaciones]:
    '''
    Transforma una literal de texto a un número complejo
    
    :param s: La literal representando el complejo en cualquiera de sus tres formas.
    :type s: str
    :return: Un complejo de la forma que corresponda a su representación como una tupla de tres valores.
    :rtype: tuple[float, float, Representaciones]
    '''

    # Se convierten todas las letras a minúsculas para evitar problemas
    s = s.lower()
    # Se eliminan todos los espacios
    s = s.replace(' ', '')
    # Se determina el tipo de representación del texto
    if 'cis' in s:
        return desde_polar(s)
    elif 'e^' in s:
        return desde_exponencial(s)
    else:
        # Si el texto no fuera un complejo válido, se permite que desde_binomica se encargue de lanzar la excepción.
        return desde_binomica(s)