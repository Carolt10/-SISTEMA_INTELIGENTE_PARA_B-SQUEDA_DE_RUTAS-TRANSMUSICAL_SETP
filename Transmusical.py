# ================================================================
# SISTEMA INTELIGENTE PARA BÚSQUEDA DE RUTAS - TRANSMUSICAL SETP
# ================================================================
#
# Propósito: Desarrollar un sistema basado en reglas que permita encontrar diferentes rutas para desplazarse desde un punto A hasta un punto B utilizando una base de conocimiento.
#
# El sistema utiliza:
#   1. Base de conocimiento
#   2. Reglas lógicas
#   3. Ciclos de búsqueda
#   4. Condiciones
#   5. Recursividad
#   6. Evaluación de alternativas
#
# IMPORTANTE:
# Las rutas incluidas abajo son una BASE ACADÉMICA de demostración. Para una aplicación real deben reemplazarse por las rutas, paraderos y conexiones vigentes publicadas por TransMusical.
# ================================================================
# ================================================================
# 1. BASE DE CONOCIMIENTO
# ================================================================
#
# En un sistema basado en reglas, la base de conocimiento contiene los hechos que el sistema conoce.
# En este caso los hechos representan:
#
#    ruta = [punto1, punto2, punto3, ...]
#
# Cada ruta representa los puntos por los cuales pasa un servicio.
#
# Ejemplo:
#
# Ruta 21:
# Centro -> Calle 60 -> Carrera 5 -> Terminal
#
# Esto nos permite que el sistema pueda deducir si dos puntos están conectados mediante una determinada ruta.
# ================================================================

rutas_transmusical = {

    "Ruta 21": [
        "Centro",
        "Calle 20",
        "Carrera 5",
        "Calle 40",
        "Calle 60",
        "Terminal"
    ],

    "Ruta 40": [
        "Centro",
        "Calle 15",
        "Carrera 5",
        "Calle 35",
        "Calle 60",
        "Universidad"
    ],

    "Ruta 82": [
        "Terminal",
        "Calle 60",
        "Carrera 5",
        "Calle 80",
        "Zona Norte"
    ],

    "Ruta 24": [
        "Centro",
        "Calle 20",
        "Carrera 5",
        "Calle 50",
        "Calle 60",
        "Zona Norte"
    ],

    "Ruta 43": [
        "Centro",
        "Calle 10",
        "Carrera 5",
        "Calle 40",
        "Universidad"
    ]
}

# ================================================================
# 2. REGLAS DEL SISTEMA
# ================================================================
#
# Las reglas determinan cómo el sistema utiliza la información almacenada en la base de conocimiento.
#
# REGLA 1:
# Si una ruta contiene el punto de origen y el punto destino, entonces existe una ruta directa.
#
# REGLA 2:
# Si una ruta no llega directamente al destino, se puede realizar una conexión con otra ruta cuando ambas comparten un punto.
#
# REGLA 3:
# Una ruta no puede visitar nuevamente un punto que ya fue visitado.
#
# REGLA 4:
# Entre las rutas encontradas, se puede considerar como mejor alternativa aquella que tenga menos conexiones.
# ================================================================
# 3. FUNCIÓN PARA DETERMINAR SI UNA RUTA CONECTA DOS PUNTOS
# ================================================================

def ruta_conecta(ruta, origen, destino):
    """
    Determina si una ruta contiene tanto el origen como el destino.

    Esta función representa una regla lógica:

    SI el origen pertenece a la ruta
    Y el destino pertenece a la ruta
    ENTONCES la ruta puede conectar ambos puntos.
    """

    if origen in ruta and destino in ruta:

        # Obtenemos la posición del origen
        posicion_origen = ruta.index(origen)

        # Obtenemos la posición del destino
        posicion_destino = ruta.index(destino)

        # El destino debe encontrarse después del origen
        if posicion_origen < posicion_destino:
            return True

    return False
# ================================================================
# 4. FUNCIÓN PARA ENCONTRAR RUTAS DIRECTAS
# ================================================================
#
# Se utiliza un ciclo "for" para revisar toda la base de conocimiento.
#
# Esta es una de las partes principales del sistema inteligente:
#
# Para cada ruta:
#     verificar si permite viajar desde A hasta B.
#
# Si se cumple la regla:
#     guardar la ruta como solución.
# ================================================================

def buscar_rutas_directas(origen, destino):

    rutas_encontradas = []

    # Recorremos todas las rutas conocidas
    for nombre_ruta, paraderos in rutas_transmusical.items():

        # Aplicamos la regla de conexión
        if ruta_conecta(paraderos, origen, destino):

            rutas_encontradas.append(nombre_ruta)

    return rutas_encontradas

# ================================================================

# 5. FUNCIÓN PARA CONSTRUIR EL MAPA DE CONEXIONES
# ================================================================
#
# El sistema necesita saber qué rutas pueden conectarse entre sí.
#
# Dos rutas tienen una conexión cuando comparten al menos un punto.
# ================================================================

def construir_conexiones():

    conexiones = {}

    nombres_rutas = list(rutas_transmusical.keys())

    # Recorremos cada ruta
    for ruta1 in nombres_rutas:

        conexiones[ruta1] = []

        # Comparamos con las demás rutas
        for ruta2 in nombres_rutas:

            # Una ruta no se conecta consigo misma
            if ruta1 == ruta2:
                continue

            # Obtenemos los puntos de ambas rutas
            puntos_ruta1 = set(rutas_transmusical[ruta1])
            puntos_ruta2 = set(rutas_transmusical[ruta2])

            # Buscamos puntos compartidos
            puntos_comunes = puntos_ruta1.intersection(puntos_ruta2)

            # Si existe al menos un punto común, las rutas pueden conectarse
            if len(puntos_comunes) > 0:

                conexiones[ruta1].append(
                    (ruta2, list(puntos_comunes))
                )

    return conexiones
# ================================================================


# 6. BÚSQUEDA DE RUTAS CON CONEXIONES
# ================================================================
#
# Esta función utiliza una búsqueda para encontrar alternativas.
#
# Ahora se emplea un ciclo while para explorar las posibilidades.
#
# Cada elemento de la cola contiene:
#
#     ruta actual
#     rutas utilizadas
#     punto de conexión
#
# De esta manera el sistema puede analizar:
#
# Ruta A
#    ↓
# conexión
#    ↓
# Ruta B
#    ↓
# destino
#
# También evita recorrer indefinidamente las mismas rutas.
# ================================================================

def buscar_rutas_con_conexiones(origen, destino):

    conexiones = construir_conexiones()

    soluciones = []

    # Cola de búsqueda
    cola = []

    # Inicialmente analizamos todas las rutas que pasan por el punto de origen.
    for nombre_ruta, paraderos in rutas_transmusical.items():

        if origen in paraderos:

            cola.append({
                "rutas": [nombre_ruta],
                "punto_actual": origen
            })

    # ============================================================
    # CICLO PRINCIPAL DE BÚSQUEDA
    # ============================================================

    while cola:

        # Sacamos el primer elemento de la cola
        estado = cola.pop(0)

        rutas_actuales = estado["rutas"]

        ruta_actual = rutas_actuales[-1]

        # Obtenemos los puntos de la ruta actual
        puntos_actuales = rutas_transmusical[ruta_actual]

        # --------------------------------------------------------
        # REGLA:
        # Si la ruta actual contiene el destino, encontramos una solución.
        # --------------------------------------------------------

        if destino in puntos_actuales:

            soluciones.append(rutas_actuales)

            continue

        # --------------------------------------------------------
        # Buscar posibles rutas conectadas
        # --------------------------------------------------------

        for ruta_siguiente, puntos_comunes in conexiones[ruta_actual]:

            # Evitar ciclos.
            #
            # Si la ruta ya fue utilizada, no se vuelve a utilizar.
            if ruta_siguiente in rutas_actuales:
                continue

            # ----------------------------------------------------
            # REGLA DE CONEXIÓN
            #
            # La nueva ruta debe tener un punto común con la ruta anterior.
            # ----------------------------------------------------

            nuevas_rutas = rutas_actuales + [ruta_siguiente]

            cola.append({
                "rutas": nuevas_rutas,
                "punto_actual": puntos_comunes[0]
            })

    return soluciones

# ================================================================


# 7. EVALUAR LAS RUTAS ENCONTRADAS
# ================================================================
#
# Una vez encontradas las alternativas, el sistema debe determinar cuál requiere menos transbordos.
#
# La regla utilizada será:
#
# MENOR cantidad de rutas utilizadas
#        =
# MENOR cantidad de transbordos
#
# Esto NO significa que sea necesariamente la ruta real más rápida. Para calcular tiempo real se necesitarían datos de tráfico, frecuencia, horarios y tiempos de viaje.
# ================================================================

def evaluar_rutas(soluciones):

    if not soluciones:
        return None

    # Ordenamos las soluciones de menor a mayor número de rutas
    soluciones_ordenadas = sorted(
        soluciones,
        key=lambda ruta: len(ruta)
    )

    return soluciones_ordenadas

# ================================================================

