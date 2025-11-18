'''
Archivo principal del programa.

Contiene un prototipo de interfaz desde la terminal (CLI), pero principalmente, contiene
la llamada a la función que ejecuta la interfaz con TkInter.
'''

from operaciones import operar
from Tipos import Representaciones, Operacion
from interfaz import gui

#Funcion para almacenar el numero complejo
def pedir_complejo() -> tuple[float, float, Representaciones]:
    print('¿Que representación vas a usar?')
    opcion = input()

    match opcion.upper():
        case Representaciones.BINOMICA.name:
            print('Introduce la parte real: ')
            real = float(input())

            print('Introduce la parte imaginaria: ')
            imag = float(input())

            print(f'{real} {"+" if imag >= 0 else "-"} {abs(imag)}i')

            return (real, imag, Representaciones.BINOMICA)
        case Representaciones.POLAR.name:
            print('')
            return (0, 0, Representaciones.BINOMICA)
        case Representaciones.EXPONENCIAL.name:
            return (0, 0, Representaciones.BINOMICA)
        case _:
            raise Exception("No se ingresó una representación válida")


def cli():
    print('*** CALCULADORA ***')
    while True:
        print('Ingresa la operación: ')
        for op in Operacion:
            print(f'{op.value} - {op.name.lower()}')
        print('>>> ', end='')
        seleccion = int(input())

        if seleccion not in Operacion:
            break

        match seleccion:
            case Operacion.SUMA.value:
                z1 = pedir_complejo() # esto se cambia
                z2 = pedir_complejo()
                res = operar(z1, z2, Operacion.SUMA)
            case Operacion.RESTA.value:
                pass
            case Operacion.MULTIPLICACION.value:
                pass
            case Operacion.DIVISION.value:
                pass
            case Operacion.POTENCIA.value:
                pass
            case Operacion.RAIZ.value:
                pass
            case Operacion.CONJUGADO.value:
                pass
            case _:
                pass  # Puedes manejar el caso desconocido aquí si lo deseas
    print('¡Gracias por usar!')

# ejecutar
#cli()
gui()