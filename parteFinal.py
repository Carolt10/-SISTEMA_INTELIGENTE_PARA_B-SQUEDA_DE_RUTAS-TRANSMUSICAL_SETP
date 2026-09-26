# 8. MOSTRAR UNA RUTA AL USUARIO
# ================================================================

def mostrar_ruta(rutas, origen, destino):

    print("\n---------------------------------------------")
    print("RUTA ENCONTRADA")
    print("---------------------------------------------")

    print(f"Origen : {origen}")
    print(f"Destino: {destino}")

    print("\nRecorrido:")

    for posicion, ruta in enumerate(rutas):

        print(f"  {posicion + 1}. {ruta}")

    # Calculamos cantidad de transbordos
    transbordos = len(rutas) - 1

    print(f"\nCantidad de vehículos/rutas: {len(rutas)}")
    print(f"Cantidad de transbordos: {transbordos}")

# ================================================================

# 9. FUNCIÓN PRINCIPAL DEL SISTEMA INTELIGENTE
# ================================================================

def sistema_inteligente():

    print("=" * 60)
    print(" SISTEMA INTELIGENTE DE RUTAS - TRANSMUSICAL SETP")
    print("=" * 60)

    print("\nPuntos disponibles:")

    # Creamos conjunto de todos los puntos conocidos
    puntos = set()

    for ruta in rutas_transmusical.values():
        puntos.update(ruta)

    for punto in sorted(puntos):
        print(" -", punto)

    # ------------------------------------------------------------
    # Solicitar información al usuario
    # ------------------------------------------------------------

    origen = input("\nIngrese el punto de origen: ").strip()

    destino = input("Ingrese el punto de destino: ").strip()

    # ------------------------------------------------------------
    # Validar que los puntos existan
    # ------------------------------------------------------------

    if origen not in puntos:

        print("\nEl punto de origen no se encuentra en la")
        print("base de conocimiento.")

        return

    if destino not in puntos:

        print("\nEl punto de destino no se encuentra en la")
        print("base de conocimiento.")

        return

    if origen == destino:

        print("\nEl origen y el destino son iguales.")
        print("No es necesario utilizar una ruta.")

        return

    # ============================================================
    # PRIMERA REGLA:
    # Buscar una ruta directa
    # ============================================================

    rutas_directas = buscar_rutas_directas(
        origen,
        destino
    )

    # ------------------------------------------------------------
    # Si existe una ruta directa
    # ------------------------------------------------------------

    if rutas_directas:

        print("\n✓ Se encontró una ruta directa.")

        for ruta in rutas_directas:

            mostrar_ruta(
                [ruta],
                origen,
                destino
            )

    # ============================================================
    # Si no existe una ruta directa
    # se buscan conexiones.
    # ============================================================

    else:

        print("\nNo existe una ruta directa.")
        print("Analizando posibles conexiones...")

        soluciones = buscar_rutas_con_conexiones(
            origen,
            destino
        )

        soluciones = evaluar_rutas(soluciones)

        # --------------------------------------------------------
        # Mostrar resultados
        # --------------------------------------------------------

        if soluciones:

            print("\n✓ Se encontraron alternativas.")

            # Mostramos máximo las primeras 5 alternativas
            for numero, rutas in enumerate(soluciones[:5], 1):

                print(f"\nALTERNATIVA {numero}")

                mostrar_ruta(
                    rutas,
                    origen,
                    destino
                )

            # ----------------------------------------------------
            # Regla para seleccionar la alternativa con menos transbordos.
            # ----------------------------------------------------

            mejor_ruta = soluciones[0]

            print("\n=============================================")
            print(" ALTERNATIVA CON MENOS TRANSBORDOS")
            print("=============================================")

            mostrar_ruta(
                mejor_ruta,
                origen,
                destino
            )

        else:

            print("\n✗ No se encontró una ruta disponible")
            print("entre los puntos indicados.")

# ================================================================

# 10. EJECUTAR EL SISTEMA
# ================================================================

sistema_inteligente()
