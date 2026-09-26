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