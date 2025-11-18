'''
Implementación de la interfaz gráfica de usuario usando TkInter.

Define la función gui, que contiene la lógica para construir y ejecutar la
interfaz gráfica. Además, implementa toda la lógica necesaria para interactuar
con la calculadora y realizar todas sus funciones, utilizando las abstracciones
definidas en conversion.py, argand.py, operaciones.py, así como las literales
definidas en Tipos.py para representar tanto las operaciones disponibles
como las representaciones para cada complejo.
'''

from fractions import Fraction
from tkinter import *
from tkinter import ttk, messagebox
import math

from argand import graficar_en_argand
from Tipos import Operacion, Representaciones
from analisis import a_complejo
from conversion import convertir_a
from operaciones import operar



def complejo_a_str(z: tuple[float, float, Representaciones]) -> str:
    '''
    Devuelve la representación en texto de un complejo dado
    
    :param z: El complejo a transformar
    :type z: tuple[float, float, Representaciones]
    :return: Un string con la representación del complejo
    :rtype: str
    '''

    # Dependiendo del tipo de representación, se usa un formato u otro
    if z[2] == Representaciones.BINOMICA:
        return f'{z[0]:.2f} {"-" if z[1] < 0 else "+"} {abs(z[1]):.2f}i'
    if z[2] == Representaciones.EXPONENCIAL:
        return f'{z[0]:.2f}e^({Fraction(z[1] / math.pi).limit_denominator(100)}π·i)'
    if z[2] == Representaciones.POLAR:
        return f'{z[0]:.2f}cis({Fraction(z[1] / math.pi).limit_denominator(100)}π)'
        #return f'{z[0]:.2f}cis({(z[1] / math.pi):.4f}π)'
    return ''


def gui():
    '''
    Función que lanza la interfaz gráfica de usuario con TkInter.
    '''
    # Ventana principal
    origen = Tk()
    origen.config(bg="black")
    origen.title("Calculadora números complejos")
    origen.geometry("420x420")

    # Frame
    cuadro = Frame(origen, bg="gray", width=420, height=420)
    cuadro.pack(side="top")
    cuadro.pack_propagate(False)

    # Explicación
    def mostrar_ayuda():
        ventana_ayuda = Toplevel(origen)
        ventana_ayuda.title("Ayuda - Formato de entrada")
        ventana_ayuda.geometry("700x400")
        ventana_ayuda.config(bg="white")
        
        # Frame con scrollbar
        frame_scroll = Frame(ventana_ayuda, bg="white")
        frame_scroll.pack(fill=BOTH, expand=True, padx=10, pady=10)
        
        scrollbar = Scrollbar(frame_scroll)
        scrollbar.pack(side=RIGHT, fill=Y)
        
        texto_ayuda = Text(frame_scroll, wrap=WORD, yscrollcommand=scrollbar.set, 
                          font=("Arial", 10), bg="white", padx=10, pady=10)
        texto_ayuda.pack(side=LEFT, fill=BOTH, expand=True)
        scrollbar.config(command=texto_ayuda.yview)
        
        # Contenido de ayuda
        contenido = """FORMATO DE ENTRADA
            Para introducir un número, hay que escribirlo con texto dentro de los recuadros.

        FORMA BINÓMICA:
        Debe seguir la forma: a ± bi
        Donde 'a' es la parte real y 'b' es la parte imaginaria.
        Acepta números decimales.
        Ejemplo: 5.2 - 6.7i

        FORMA POLAR:
        La forma es: r cis(θ°)  o  rcis(θpi)
        Donde 'r' es la magnitud y 'θ' es el ángulo.

        El ángulo puede expresarse en:
        • Grados: usar el símbolo °
            Ejemplo: 5.3cis(45°)
        
        • Radianes: usar 'pi'
            Ejemplo: 5.3cis(3/2pi)  o  2cis(1/4π)
            Para radianes, es posible usar fracciones.

        FORMA EXPONENCIAL:
        La forma es: re^(θ)
        Ejemplo: 2.5e^(1/3π)

        NOTAS IMPORTANTES:
        • Usa 'i' para la parte imaginaria (NO 'j')
        • Puedes escribir los números con o sin espacios
        • Para el conjugado, sólo se usa el primer número
        • Para la raíz, el segundo número puede tener la forma que sea, 
            siempre que ésta solo tenga una parte real entera."""
        
        texto_ayuda.insert("1.0", contenido)
        texto_ayuda.config(state=DISABLED)  # Solo lectura
        # Botón cerrar
        Button(ventana_ayuda, text="Cerrar", command=ventana_ayuda.destroy, 
               bg="lightblue", font=("Arial", 10, "bold"), width=10).pack(pady=10)
    
    # Botón de ayuda (símbolo ?)
    btn_ayuda = Button(cuadro, text="?", command=mostrar_ayuda, 
                       bg="lightblue", font=("Arial", 12, "bold"), 
                       width=3, height=1)
    btn_ayuda.place(x=370, y=10)

    # Entradas
    Label(cuadro, text="Primer número complejo", bg="gray", font=("Arial", 11, "bold")).place(x=110, y=60)
    num1 = Entry(cuadro, width=20)
    num1.place(x=130, y=90)

    Label(cuadro, text="Segundo número complejo", bg="gray", font=("Arial", 11, "bold")).place(x=105, y=140)
    num2 = Entry(cuadro, width=20)
    num2.place(x=130, y=170)

    # Lista desplegable
    Label(cuadro, text="Forma:", bg="gray", font=("Arial", 10, "bold")).place(x=60, y=220)
    formas = ["Binómica", "Polar", "Exponencial"]
    combo_forma = ttk.Combobox(cuadro, values=formas, state="readonly", width=17)
    combo_forma.place(x=160, y=220)
    combo_forma.set("Seleccionar")

    # Lista desplegable
    Label(cuadro, text="Operación:", bg="gray", font=("Arial", 10, "bold")).place(x=60, y=260)
    operaciones = ["Suma", "Resta", "Conjugado", "Multiplicación", "División", "Potencia", "Raíz"]
    combo_operacion = ttk.Combobox(cuadro, values=operaciones, state="readonly", width=17)
    combo_operacion.place(x=160, y=260)
    combo_operacion.set("Seleccionar")

    # ===== Verificación =====
    def verificar():
        # Esta función implementa la lógica para tomar la entrada del usuario y con ello realizar
        # las operaciones necesarias.
        forma = combo_forma.get()
        operacion = combo_operacion.get()
        n1 = num1.get().strip()
        n2 = num2.get().strip()

        # determinar la operacion
        oper = Operacion.CONJUGADO
        match operacion:
            case "Suma":
                oper = Operacion.SUMA
            case "Resta":
                oper = Operacion.RESTA
            case "Conjugado":
                oper = Operacion.CONJUGADO
            case "Multiplicación":
                oper = Operacion.MULTIPLICACION
            case "División":
                oper = Operacion.DIVISION
            case "Potencia":
                oper = Operacion.POTENCIA
            case "Raíz":
                oper = Operacion.RAIZ
        
        if not n1:
            messagebox.showwarning("Aviso", "Por favor, ingresa el primer número complejo.")
            return
        if oper != Operacion.CONJUGADO and not n2:
            messagebox.showwarning("Aviso", "Por favor, ingresa el segundo número complejo.")
            return
        if forma == "Seleccionar" or operacion == "Seleccionar":
            messagebox.showwarning("Aviso", "Por favor, selecciona la forma y la operación.")
            return


        try:
            c1 = (0.0, 0.0, Representaciones.BINOMICA)
            c2 = (0.0, 0.0, Representaciones.BINOMICA)
            # Aceptar cis en cualquier forma
            
            try:
                c1 = a_complejo(n1)
            except Exception as e:
                messagebox.showerror('Número inválido', f'Número inválido z1: "{n1}".\nPor favor, verifica el botón de ayuda arriba a la derecha para la forma correcta.')
                return
            
            if oper != Operacion.CONJUGADO:
                try:
                    c2 = a_complejo(n2)
                except Exception:
                    messagebox.showerror('Número inválido', f'Número inválido z2: "{n2}".\nPor favor, verifica el botón de ayuda arriba a la derecha para la forma correcta.')
                    return

            # Convertir según la forma seleccionada
            if forma == "Binómica":
                c1 = convertir_a(c1, Representaciones.BINOMICA)
                c2 = convertir_a(c2, Representaciones.BINOMICA)
            elif forma == "Polar":
                c1 = convertir_a(c1, Representaciones.POLAR)
                c2 = convertir_a(c2, Representaciones.POLAR)
            elif forma == "Exponencial":
                c1 = convertir_a(c1, Representaciones.EXPONENCIAL)
                c2 = convertir_a(c2, Representaciones.EXPONENCIAL)
            else:
                raise ValueError("Forma no reconocida")

            # operar
            result = operar(c1, c2, oper)
            texto_res = ""
            for index, res in enumerate(result):
                texto_res += f"w{index + 1}: {complejo_a_str(res)}\n"
            messagebox.showinfo(
                "Operación correcta",
                f"Forma: {forma}\nOperación: {operacion}\n\n"
                f"z1 = {complejo_a_str(c1)}\nz2 = {complejo_a_str(c2)}" +
                "\n\nResultado:\n" +
                texto_res
            )

            # Graficar
            graficar_en_argand(c1, c2, result)

        except ValueError as e:
            print("109")
            messagebox.showerror("Error", str(e))
            raise e

    # ===== Botón =====
    Button(cuadro, text="Aceptar", command=verificar, bg="lightblue").place(x=170, y=320)

    # ===== Ejecutar =====
    origen.mainloop()
