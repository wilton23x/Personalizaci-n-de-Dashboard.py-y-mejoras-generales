# Personalizaci-n-de-Dashboard.py-y-mejoras-generales
# Dashboard.py - Gestión de Proyectos de Programación Orientada a Objetos

## Descripción del Proyecto

El proyecto **Dashboard.py** es una herramienta interactiva en Python que permite gestionar y organizar proyectos relacionados con la Programación Orientada a Objetos (POO). Mediante una interfaz de menú, el usuario puede explorar unidades, subcarpetas y scripts `.py` organizados en diferentes categorías. Además, el sistema permite visualizar y ejecutar los scripts directamente desde la aplicación.

## Cambios Realizados

A continuación, se detallan las modificaciones y mejoras implementadas en el archivo **Dashboard.py**:

### 1. **Categorizar Proyectos**
   - Se agregaron categorías para agrupar las unidades. Las categorías incluyen:
     - **Desarrollo Web**
     - **Análisis de Datos**
     - **Algoritmos**
   - Esto organiza mejor el menú principal y permite acceder a las unidades de forma más estructurada.

### 2. **Sistema de Búsqueda**
   - Se implementó un sistema de búsqueda para encontrar scripts específicos dentro de las subcarpetas.
   - El usuario puede introducir una palabra clave para buscar y acceder rápidamente a los scripts `.py` relacionados.

### 3. **Interfaz de Usuario Mejorada**
   - Se rediseñó la interfaz del menú para hacerlo más intuitivo.
   - Se añadió una opción para buscar scripts (`B`) en lugar de navegar manualmente a través de las carpetas.
   - Se mejoró la interacción con el usuario, mostrando opciones claras y fáciles de entender.

### 4. **Soporte para Ejecución de Scripts**
   - Los scripts seleccionados se pueden ejecutar directamente desde el menú. Dependiendo del sistema operativo, se ejecutan en una nueva ventana del terminal.

## Ejemplos de Uso

### Ejemplo 1: Ejecutar el Script

1. Ejecuta el archivo `Dashboard.py` desde la terminal o el IDE de tu preferencia.
2. Aparecerá un menú principal con las categorías disponibles:
3. Selecciona una categoría, por ejemplo, `1 - Desarrollo Web`.
4. Luego, verás las unidades dentro de esa categoría. Por ejemplo:
5. Elige una unidad o selecciona la opción de búsqueda (`B`).
6. Si decides elegir una unidad, verás los scripts `.py` dentro de ella. Selecciona un script para verlo y ejecutarlo.

### Ejemplo 2: Buscar un Script

1. Desde el menú de subcarpetas, selecciona la opción `B - Buscar script`.
2. Introduce una palabra clave del nombre del script. Por ejemplo, si buscas `script1`, se mostrará el archivo correspondiente.
3. Una vez encontrado el script, puedes verlo y ejecutarlo como en el paso anterior.

## Requisitos

- Python 3.x
- `subprocess` y `os` (vienen preinstalados con Python)

## Cómo Contribuir

Si deseas contribuir al proyecto, por favor realiza un **fork** del repositorio y envía tus **pull requests** con las mejoras que consideres. Asegúrate de que tus cambios no rompan la funcionalidad existente y que estén bien documentados.
