import re
import math

from Tipos import Representaciones



def analizar_angulo(s: str) -> float:
    if not s:
        raise Exception('El string de ángulo está vacío')
    
    angulo = 0.0
    rad = True

    if '°' in s:
        s = s.replace('°', '')
        if not s:
            raise Exception('Grados sexagesimales sin literal numérica')
        rad = False
    elif 'pi' in s or 'π' in s:
        s = s.replace('pi', '')
        s = s.replace('π', '')
        rad = True
    else:
        raise Exception(f'Sintaxis de ángulo inválida: "{s}"')
    
    try:
        angulo = float(s) if s else 1
    except:
        try:
            angulo = float(eval(s)) if s else 1
        except SyntaxError:
            raise Exception(f'Sintaxis inválida "{s}"')
    
    if rad:
        return angulo * math.pi
    else:
        return angulo * (math.pi / 180)


def desde_binomica(s: str) -> tuple[float, float, Representaciones]:
    if not s:
        raise Exception('El string de entrada está vacío')
    
    secciones = re.split(r'(?<=\d)(?=[+-])', s)
    real = 0.0
    imag = 0.0

    for seccion in secciones:
        signo = -1 if '-' in seccion else 1
        seccion = seccion.replace('+', '')
        seccion = seccion.replace('-', '')

        if 'i' in seccion:
            seccion = seccion.replace('i', '')
            if not seccion:
                imag = signo
            else:
                imag = float(seccion) * signo
        else:
            try:
                real = float(seccion) * signo if seccion else 0.0
            except:
                raise Exception('No se puede convertr a float')
    
    return (real, imag, Representaciones.BINOMICA)


def desde_polar(s: str) -> tuple[float, float, Representaciones]:
    radio_s, angulo_s = re.split(r'(?=cis)', s)
    angulo_s = angulo_s.replace('cis(', '')
    angulo_s = angulo_s.replace(')', '')

    angulo = analizar_angulo(angulo_s)
    radio = float(eval(radio_s)) if radio_s else 1

    return (radio, angulo, Representaciones.POLAR)


def desde_exponencial(s: str) -> tuple[float, float, Representaciones]:
    radio_s, angulo_s = re.split(r'(?=e\^)', s)

    radio = float(eval(radio_s)) if radio_s else 1

    angulo_s = angulo_s.replace('e^(', '')
    angulo_s = angulo_s.replace(')', '')
    angulo_s = angulo_s.replace('i)', '')
    angulo = analizar_angulo(angulo_s)

    return (radio, angulo, Representaciones.EXPONENCIAL)

def a_complejo(s: str) -> tuple[float, float, Representaciones]:
    s = s.lower()
    s = s.replace(' ', '')
    if 'cis' in s:
        return desde_polar(s)
    elif 'e^' in s:
        return desde_exponencial(s)
    else:
        return desde_binomica(s)