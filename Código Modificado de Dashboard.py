import os
import subprocess

def mostrar_codigo(ruta_script):
    # Asegúrate de que la ruta al script es absoluta
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r') as archivo:
            codigo = archivo.read()
            print(f"\n--- Código de {ruta_script} ---\n")
            print(codigo)
            return codigo
    except FileNotFoundError:
        print("El archivo no se encontró.")
        return None
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")
        return None

def ejecutar_codigo(ruta_script):
    try:
        if os.name == 'nt':  # Windows
            subprocess.Popen(['cmd', '/k', 'python', ruta_script])
        else:  # Unix-based systems
            subprocess.Popen(['xterm', '-hold', '-e', 'python3', ruta_script])
    except Exception as e:
        print(f"Ocurrió un error al ejecutar el código: {e}")

def mostrar_menu():
    # Define la ruta base donde se encuentra el dashboard.py
    ruta_base = os.path.dirname(__file__)

    categorias = {
        'Desarrollo Web': ['Unidad 1', 'Unidad 2'],
        'Análisis de Datos': ['Unidad 3'],
        'Algoritmos': ['Unidad 4']
    }

    while True:
        print("\nMenu Principal - Dashboard")
        # Imprime las categorías del menú principal
        for i, categoria in enumerate(categorias.keys(), start=1):
            print(f"{i} - {categoria}")
        print("0 - Salir")

        eleccion_categoria = input("Elige una categoría o '0' para salir: ")
        if eleccion_categoria == '0':
            print("Saliendo del programa.")
            break
        elif eleccion_categoria.isdigit() and 0 < int(eleccion_categoria) <= len(categorias):
            categoria_seleccionada = list(categorias.keys())[int(eleccion_categoria) - 1]
            mostrar_sub_menu(categoria_seleccionada, categorias[categoria_seleccionada], ruta_base)
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

def mostrar_sub_menu(categoria, unidades, ruta_base):
    while True:
        print(f"\nSubmenú - {categoria}")
        # Imprime las unidades de la categoría
        for i, unidad in enumerate(unidades, start=1):
            print(f"{i} - {unidad}")
        print("0 - Regresar al menú principal")
        print("B - Buscar script")

        eleccion_unidad = input("Elige una unidad, '0' para regresar o 'B' para buscar un script: ")
        if eleccion_unidad == '0':
            break
        elif eleccion_unidad.upper() == 'B':
            buscar_script(ruta_base)
        elif eleccion_unidad.isdigit() and 0 < int(eleccion_unidad) <= len(unidades):
            unidad_seleccionada = unidades[int(eleccion_unidad) - 1]
            mostrar_scripts(os.path.join(ruta_base, categoria, unidad_seleccionada))
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

def buscar_script(ruta_base):
    busqueda = input("Introduce el nombre del script a buscar (o parte de él): ").lower()
    resultados = []

    # Buscar en todas las unidades y subcarpetas
    for categoria in os.listdir(ruta_base):
        categoria_path = os.path.join(ruta_base, categoria)
        if os.path.isdir(categoria_path):
            for unidad in os.listdir(categoria_path):
                unidad_path = os.path.join(categoria_path, unidad)
                if os.path.isdir(unidad_path):
                    for script in os.listdir(unidad_path):
                        if script.endswith('.py') and busqueda in script.lower():
                            resultados.append(os.path.join(unidad_path, script))

    if resultados:
        print("\nScripts encontrados:")
        for i, script in enumerate(resultados, start=1):
            print(f"{i} - {script}")
    else:
        print("No se encontraron scripts que coincidan con la búsqueda.")

def mostrar_scripts(ruta_sub_carpeta):
    scripts = [f.name for f in os.scandir(ruta_sub_carpeta) if f.is_file() and f.name.endswith('.py')]

    while True:
        print("\nScripts - Selecciona un script para ver y ejecutar")
        # Imprime los scripts
        for i, script in enumerate(scripts, start=1):
            print(f"{i} - {script}")
        print("0 - Regresar al submenú anterior")
        print("9 - Regresar al menú principal")

        eleccion_script = input("Elige un script, '0' para regresar o '9' para ir al menú principal: ")
        if eleccion_script == '0':
            break
        elif eleccion_script == '9':
            return  # Regresar al menú principal
        else:
            try:
                eleccion_script = int(eleccion_script) - 1
                if 0 <= eleccion_script < len(scripts):
                    ruta_script = os.path.join(ruta_sub_carpeta, scripts[eleccion_script])
                    codigo = mostrar_codigo(ruta_script)
                    if codigo:
                        ejecutar = input("¿Desea ejecutar el script? (1: Sí, 0: No): ")
                        if ejecutar == '1':
                            ejecutar_codigo(ruta_script)
                        elif ejecutar == '0':
                            print("No se ejecutó el script.")
                        else:
                            print("Opción no válida. Regresando al menú de scripts.")
                        input("\nPresiona Enter para volver al menú de scripts.")
                else:
                    print("Opción no válida. Por favor, intenta de nuevo.")
            except ValueError:
                print("Opción no válida. Por favor, intenta de nuevo.")

# Ejecutar el dashboard
if __name__ == "__main__":
    mostrar_menu()
