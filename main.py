import csv

def cargar_desde_csv(nombre_archivo):
    lista_paises = []
    try:
        with open(nombre_archivo, mode='r', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                # Conversión de tipos y limpieza de datos obligatoria para estadísticas
                pais = {
                    'nombre': fila['nombre'].strip(),
                    'poblacion': int(fila['poblacion']),
                    'superficie': int(fila['superficie']),
                    'continente': fila['continente'].strip()
                }
                lista_paises.append(pais)
        print("¡Datos cargados exitosamente!")
    except FileNotFoundError:
        print(f"Error: El archivo {nombre_archivo} no existe. Se iniciará con una lista vacía.")
    except Exception as e:
        print(f"Error al leer el archivo CSV: {e}")
    return lista_paises

def agregar_pais(lista_paises):
    print("\n--- Agregar Nuevo País ---")
    nombre = input("Nombre: ").strip()
    if not nombre:
        print("Error: El nombre no puede estar vacío.")
        return

    try:
        poblacion = int(input("Población (entero): "))
        superficie = int(input("Superficie en km2 (entero): "))
        if poblacion < 0 or superficie < 0:
            print("Error: La población y la superficie deben ser valores positivos.")
            return
    except ValueError:
        print("Error: Debe ingresar un número entero válido.")
        return

    continente = input("Continente: ").strip()
    if not continente:
        print("Error: El continente no puede estar vacío.")
        return

    nuevo_pais = {
        'nombre': nombre,
        'poblacion': poblacion,
        'superficie': superficie,
        'continente': continente
    }
    lista_paises.append(nuevo_pais)
    print(f"¡{nombre} ha sido agregado correctamente!")

def buscar_pais_por_nombre(lista_paises):
    busqueda = input("\nIngrese el nombre del país a buscar: ").strip().lower()
    encontrados = [p for p in lista_paises if busqueda in p['nombre'].lower()]
    
    if encontrados:
        print("\nResultados encontrados:")
        for p in encontrados:
            print(f"- {p['nombre']} | Población: {p['poblacion']} | Superficie: {p['superficie']} km² | Continente: {p['continente']}")
    else:
        print("No se encontraron países con ese nombre.")

def mostrar_estadisticas(lista_paises):
    if not lista_paises:
        print("No hay datos cargados para calcular estadísticas.")
        return

    print("\n--- Estadísticas del Sistema ---")
    
    pais_mayor_pob = max(lista_paises, key=lambda x: x['poblacion'])
    pais_menor_pob = min(lista_paises, key=lambda x: x['poblacion'])
    print(f"País con MAYOR población: {pais_mayor_pob['nombre']} ({pais_mayor_pob['poblacion']} hab.)")
    print(f"País con MENOR población: {pais_menor_pob['nombre']} ({pais_menor_pob['poblacion']} hab.)")

    total_pob = sum(p['poblacion'] for p in lista_paises)
    total_sup = sum(p['superficie'] for p in lista_paises)
    print(f"Promedio de población: {total_pob / len(lista_paises):.2f}")
    print(f"Promedio de superficie: {total_sup / len(lista_paises):.2f} km²")

    conteo_continentes = {}
    for p in lista_paises:
        cont = p['continente']
        conteo_continentes[cont] = conteo_continentes.get(cont, 0) + 1
    
    print("\nCantidad de países por continente:")
    for cont, cant in conteo_continentes.items():
        print(f"- {cont}: {cant}")

def ordenar_paises(lista_paises):
    """Ordena la lista de países según el criterio seleccionado por consola."""
    print("\nCriterios de ordenamiento:")
    print("1. Nombre\n2. Población\n3. Superficie")
    opc_crit = input("Seleccione criterio (1-3): ")
    
    sentido = input("¿Ascendente (A) o Descendente (D)?: ").strip().upper()
    reversa = True if sentido == 'D' else False

    if opc_crit == '1':
        clave = 'nombre'
    elif opc_crit == '2':
        clave = 'poblacion'
    elif opc_crit == '3':
        clave = 'superficie'
    else:
        print("Criterio inválido.")
        return

    lista_ordenada = sorted(lista_paises, key=lambda x: x[clave], reverse=reversa)
    
    print("\n--- Lista Ordenada ---")
    for p in lista_ordenada:
        print(f"{p['nombre']} -> Población: {p['poblacion']} | Superficie: {p['superficie']} | Continente: {p['continente']}")

def menu_principal():
    """Lazo de control del menú interactivo en consola."""
    archivo_csv = "datos_paises.csv"
    paises = cargar_desde_csv(archivo_csv)

    while True:
        print("\n======================================")
        print("  SISTEMA DE GESTIÓN DE PAÍSES (UTN)  ")
        print("======================================")
        print("1. Agregar un país")
        print("2. Buscar un país por nombre")
        print("3. Ordenar países")
        print("4. Mostrar estadísticas generales")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ").strip()

        if opcion == '1':
            agregar_pais(paises)
        elif opcion == '2':
            buscar_pais_por_nombre(paises)
        elif opcion == '3':
            ordenar_paises(paises)
        elif opcion == '4':
            mostrar_estadisticas(paises)
        elif opcion == '5':
            print("Saliendo del sistema... ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    menu_principal()