from Tipos import Representaciones
from conversion import convertir_a

import matplotlib.pyplot as plt



def graficar_en_argand(z1_a, z2_a, resultados: list[tuple[float, float, Representaciones]]):
    '''
    Muestra en pantalla un gráfico con los números proporcionados
    
    :param z1_a: Una tupla representando el primer operando
    :param z2_a: Una tupla representando el segundo operando
    :param resultados: Una lista de tuplas que representen los valores de resultados
    :type resultados: list[tuple[float, float, Representaciones]]
    '''
    # Se crean dos Axis dentro del gráfico: uno para los operandos, otro para lso resultados
    _, (ax, axr) = plt.subplots(1, 2, figsize=(10, 5))

    # Se transforman ambos operandos a su forma binómica para poder graficar usando coordenadas cartesianas
    z1 = convertir_a(z1_a, Representaciones.BINOMICA)
    z2 = convertir_a(z2_a, Representaciones.BINOMICA)
    
    # Colocar los puntos en la gráfica
    ax.plot(z1[0], z1[1], 'r^', label='$z_1$')
    ax.plot(z2[0], z2[1], 'b^', label='$z_2$')

    # determinar la magnitud del margen a dejar en la gráfica
    oper_sizes = [abs(s) for s in [z1[0], z1[1], z2[0], z2[1]]]

    # escalar el márgen
    oper_max_size = max(oper_sizes) * 1.3

    # establecer los márgenes para que quepan los vectores
    ax.set_ylim(-oper_max_size, oper_max_size)
    ax.set_xlim(-oper_max_size, oper_max_size)

    # Colocar los vectores (flechas)
    ax.annotate('', (z1[0], z1[1]), (0, 0), arrowprops={'width': 0.2})
    ax.annotate('', (z2[0], z2[1]), (0, 0), arrowprops={'width': 0.2})

    # Colocar los ejes x e y en el origen
    #ax.spines[["left", "bottom"]].set_position(("data", 0))
    ax.axhline(y=0, color='black', linewidth=0.8)
    ax.axvline(x=0, color='black', linewidth=0.8)

    # Etiquetar cada eje como Re o Im según sea el caso
    ax.text(0.9, 0.45, '$Re$', fontsize=14, va='center', transform=ax.transAxes, zorder=10)
    ax.text(0.4, 0.95, '$Im$', fontsize=14, va='center', transform=ax.transAxes, zorder=10)

    # Mostrar el grid de la gráfica 1
    ax.grid(True)

    # Establecer el título
    ax.set_title('Operadores')
    ax.legend()


    # --- RESULTADO ---
    # Convertir todas las representaciones a binomica
    resultados_b = [convertir_a(w, Representaciones.BINOMICA) for w in resultados]

    # Determinar la magnitud del margen
    maximo_real = max([abs(w[0]) for w in resultados_b])
    maximo_imag = max([abs(w[1]) for w in resultados_b])

    # Escalar al margen deseado
    res_max_size = max(maximo_real, maximo_imag) * 1.3

    for index, w1 in enumerate(resultados_b):
        # colocar el punto en la gráfica
        axr.plot(w1[0], w1[1], 'g*', label=f'$w_{index}$')

        # Establecer los límites
        axr.set_ylim(-res_max_size, res_max_size)
        axr.set_xlim(-res_max_size, res_max_size)

        #axr.spines[["left", "bottom"]].set_position(("data", 0))

        # Mostrar el grid
        axr.grid(True)
        # Dibujar la flecha
        axr.annotate('', (w1[0], w1[1]), (0, 0), arrowprops={'width': 0.2})
    
    axr.set_title('Resultados')
    # Colocar los ejes x e y en el orígen
    axr.axhline(y=0, color='black', linewidth=0.8)
    axr.axvline(x=0, color='black', linewidth=0.8)
    # Etiquetar cada eje como Re o Im según sea el caso
    axr.text(2.1, 0.45, '$Re$', fontsize=14, va='center', transform=ax.transAxes, zorder=10)
    axr.text(1.6, 0.95, '$Im$', fontsize=14, va='center', transform=ax.transAxes, zorder=10)
    axr.legend()

    plt.show()



