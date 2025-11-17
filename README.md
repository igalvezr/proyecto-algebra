# Proyecto Álgebra
Éste proyecto implementa una calculadora que trabaja con números complejos, ofrecienco una interfaz que permite introducir dos números complejos en cualquiera de sus representaciones: binómica, polar y exponencial, y ofrece realizar todas las operaciones definidas para éstos. Además, presenta los vectores que representa cada número complejo en el plano de Argand.

## Instalar y ejecutar

### Instalación - dependencias

Las dependencias son:
- python (versión 3.13)
- matplotlib
- pytest (para ejecutar tests)

### Windows
1. Instalar python (en la tienda de microsoft está gratis)
2. Comprobar si python está correctamente instalado: `$ python --version`
3. Una vez instalado, las dependencias se instalan usando: `$ pip install matplotlib`

### Linux
1. Instalar python usando el gestor de paquetes de la distro específica
2. Comprobar si python está instalado: `$ python --version`
3. Una vez instalado, las dependencias se instalan usando: `$ pip install matplotlib`

### Usando ambientes virtuales
Depende del gestor de ambientes específico es que debes obtener las dependencias adecuadas.

### Instalación - proyecto
Usando git:
1. Clonar el repositorio usando `$ git clone <url>`
2. Entrar al directorio raíz. Desde ahí, se puede ejecutar.

### Ejecución
Para ejecutar la calculadora en la terminal, se debe ejecutar el siguiente comando estando en la raíz del proyecto: `$ python calculadora.py`


## Capacidades:
- Ingresar dos números complejos como operandos en cualquiera de sus representaciones (ver las [formas de representación](#formato-de-complejos)).
- Observar en el plano de Argand ambos operandos.
- Elegir entre las operaciones disponibles para los operandos (ver las [operaciones permitidas](#operaciones-disponbibles) y sus características).
- Obtener el resultado de la operación elegida entre los operandos proporcionados.
- Observar en el plano de Argand el resultado.

## Operaciones disponibles
Las operaciones que la calculadora soporta son las siguientes:
Para la forma binómica:
- Suma
- Resta
- Multiplicación
- División

Para la forma exponencial:
- Multiplicación
- División

Para la forma polar:
- Multiplicación
- División
- Potencia
- Raíz enésima

Cada operación, tiene unas características específicas. Pero, en general, si ambos operandos tienen la misma representación, y siempre que la operación solicitada esté definida para la representación, entonces el resultado estará en esa misma representación. Si no, se dará prioridad a la representación _binómica_.

## Formato de complejos
Los números complejos se pueden introducir y visualizar en los formatos siguientes, para cada representación:

### Binómica

La forma estándar es: `a + bi`, donde puede omitirse tanto `a` como `bi`, pero no ambas.

### Polar

La forma polar sigue la siguiente estructura: 
- `r cis(θπ)` ó `r cis(θpi)` para radianes.
- `r cis(θ°)` para grados sexagesimales.

Donde _r_ es el radio (magnitud del vector), y $\theta$ es el ángulo.

Si $r = 1$, entonces puede omitirse _r_, teniendo la forma `cis(θ)` Además, para representar la constante de pi se puede usar tanto la literal `pi` o el símbolo `π`. Además, **el valor de _r_ debe ser positivo**.

$\theta$ puede representarse ya sea con un valor conocido, como sería `0.25` o con un cociente simple como `2/3`. La expresión será evaluada y el valor será utilizado.

### Exponencial

La forma exponencial debe seguir la siguiente estructura: 
- `r e^(θπ)` para radianes,

Donde _r_ es la magnitud del vector, y $\theta$ es el ángulo.

De igual forma, si $r = 1$, entonces _r_ puede omitrse y la estructura queda como `e^(θπ)`.

$\theta$ puede representarse con un valor conocido o una fracción, de la misma manera que en la forma Polar.

## Riesgos
1. La evaluación del ángulo de las formas exponencial y polar usan la función `eval`, que ejecuta código python arbitrario, lo que puede representar un riesgo para el sistema.