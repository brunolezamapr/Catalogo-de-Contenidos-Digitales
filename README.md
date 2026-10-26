# 🎧 Catálogo de Contenidos Digitales

Proyecto en **Python** que simula, de forma sencilla, el funcionamiento de un catálogo de contenidos multimedia (podcasts, tutoriales, audios o videos) y de **listas de reproducción (playlists)**. Está construido con **Programación Orientada a Objetos (POO)**, modularización y buenas convenciones de código para que sea fácil de leer, mantener y ampliar.

---

## 📑 Tabla de contenidos

1. [Descripción general](#-descripción-general)
2. [Objetivos del proyecto](#-objetivos-del-proyecto)
3. [Estructura del repositorio](#-estructura-del-repositorio)
4. [Requisitos](#-requisitos)
5. [Cómo ejecutar el proyecto](#-cómo-ejecutar-el-proyecto)
6. [Explicación de cada módulo](#-explicación-de-cada-módulo)
7. [Conceptos de POO aplicados](#-conceptos-de-poo-aplicados)
8. [Ejemplo de uso](#-ejemplo-de-uso)
9. [Salida esperada](#-salida-esperada)
10. [Posibles mejoras](#-posibles-mejoras)
11. [Autor](#-autor)

---

## 📖 Descripción general

El sistema modela dos conceptos principales:

| Clase | Qué representa |
|---|---|
| `ContenidoDigital` | Un ítem individual de audio o video (por ejemplo, un podcast o un tutorial) con un **título** y una **duración en segundos**. |
| `PlaylistDigital` | Una **lista de reproducción** que agrupa varios `ContenidoDigital`. Permite agregar contenidos, contarlos, recorrerlos y **fusionar dos playlists** en una nueva. |

Cada clase vive en su propio archivo (módulo), y el archivo `main.py` sirve como punto de entrada para probar que todo funciona correctamente.

---

## 🎯 Objetivos del proyecto

- Aplicar los principios de la **Programación Orientada a Objetos** en Python.
- Practicar la **modularización**: separar el código en archivos con responsabilidades claras.
- Usar **propiedades (`@property`)**, **métodos estáticos (`@staticmethod`)** y **métodos mágicos (dunder)**.
- Aplicar la **sobrecarga de operadores** (en este caso, el operador `+`).
- Escribir código **legible**, con **docstrings** y **anotaciones de tipo** (type hints).

---

## 🗂️ Estructura del repositorio

```text
Catalogo-de-Contenidos-Digitales/
│
├── .gitignore              # Archivos y carpetas que Git debe ignorar
├── __init__.py             # Marca la carpeta como paquete de Python
├── contenido_digital.py    # Clase ContenidoDigital (un ítem individual)
├── playlist_digital.py     # Clase PlaylistDigital (colección de contenidos)
├── main.py                 # Punto de entrada: script de prueba
└── README.md               # Este documento
```

---

## ⚙️ Requisitos

- **Python 3.7 o superior** (se usan type hints y f-strings).
- No requiere instalar librerías externas: usa únicamente la biblioteca estándar de Python.

Para verificar tu versión de Python:

```bash
python --version
```

---

## ▶️ Cómo ejecutar el proyecto

1. **Clona el repositorio:**

   ```bash
   git clone https://github.com/brunolezamapr/Catalogo-de-Contenidos-Digitales.git
   ```

2. **Entra a la carpeta del proyecto:**

   ```bash
   cd Catalogo-de-Contenidos-Digitales
   ```

3. **Ejecuta el script principal:**

   ```bash
   python main.py
   ```

   > En algunos sistemas (Linux/macOS) puede ser necesario usar `python3 main.py`.

---

## 🧩 Explicación de cada módulo

### 1. `contenido_digital.py` → clase `ContenidoDigital`

Representa **un solo contenido** multimedia.

**Atributos**

| Atributo | Tipo | Descripción |
|---|---|---|
| `titulo` | `str` | Nombre del contenido. |
| `duracion_segundos` | `int` | Duración total en segundos. |

**Validación:** si la duración es **menor o igual a 0**, el constructor lanza un `ValueError`, evitando crear contenidos con duraciones inválidas.

**Métodos y propiedades**

| Elemento | Tipo | Qué hace |
|---|---|---|
| `duracion_minutos` | `@property` (solo lectura) | Convierte automáticamente los segundos a minutos (valor decimal). Ej.: `300` s → `5.0` min. |
| `formatear_tiempo(segundos)` | `@staticmethod` | Recibe segundos y devuelve un texto con formato `MM:SS`. Ej.: `90` → `"01:30"`. Si recibe un valor negativo, devuelve `"00:00"`. |
| `__repr__()` | método mágico | Define cómo se muestra el objeto al imprimirlo. Ej.: `ContenidoDigital(titulo='Podcast Python POO', duracion='05:00')`. |

---

### 2. `playlist_digital.py` → clase `PlaylistDigital`

Es una **colección** que guarda objetos `ContenidoDigital` (relación de **agregación**).

**Atributos**

| Atributo | Descripción |
|---|---|
| `nombre` | Nombre de la playlist. |
| `_contenidos` | Lista **interna (privada por convención)** con los contenidos agregados. |

**Métodos**

| Método | Qué hace |
|---|---|
| `agregar(contenido)` | Añade un `ContenidoDigital` a la playlist. Si el objeto no es de ese tipo, lanza un `TypeError`. |
| `__len__()` | Permite usar `len(playlist)` para saber cuántos contenidos hay. |
| `__getitem__(index)` | Permite acceder con índice (`playlist[0]`), usar *slicing* (`playlist[0:2]`) y recorrer la playlist con un bucle `for`. |
| `__add__(otra)` | **Sobrecarga del operador `+`**: combina dos playlists y devuelve una **nueva**, sin modificar las originales. El nombre resultante es `Combinada (A & B)`. |
| `__repr__()` | Muestra el nombre de la playlist y el total de ítems. |

---

### 3. `main.py` → punto de entrada

Ejecuta una prueba secuencial que demuestra todo lo anterior:

1. Crea dos contenidos digitales.
2. Muestra la duración en minutos (propiedad).
3. Usa el método estático para formatear tiempo.
4. Crea dos playlists y les agrega un contenido a cada una.
5. Las fusiona con el operador `+`.
6. Muestra la cantidad de elementos con `len()`.
7. Recorre la playlist combinada con un bucle `for`.

---

## 🧠 Conceptos de POO aplicados

| Concepto | Dónde se aplica |
|---|---|
| **Clases y objetos** | `ContenidoDigital` y `PlaylistDigital`. |
| **Encapsulamiento** | `_contenidos` es un atributo interno de la playlist; se accede mediante métodos. |
| **Propiedades (`@property`)** | `duracion_minutos`: valor calculado y de solo lectura. |
| **Métodos estáticos (`@staticmethod`)** | `formatear_tiempo()`: no depende de ninguna instancia. |
| **Agregación** | Una `PlaylistDigital` *contiene* objetos `ContenidoDigital`. |
| **Métodos mágicos (dunder)** | `__init__`, `__repr__`, `__len__`, `__getitem__`, `__add__`. |
| **Sobrecarga de operadores** | `playlist1 + playlist2`. |
| **Validación de datos** | `ValueError` y `TypeError` para entradas incorrectas. |
| **Modularización** | Cada clase está en su propio archivo; `main.py` las importa y las usa. |
| **Type hints y docstrings** | Documentación y tipado en todo el código. |

---

## 💡 Ejemplo de uso

```python
from contenido_digital import ContenidoDigital
from playlist_digital import PlaylistDigital

# Crear contenidos
c1 = ContenidoDigital("Podcast Python POO", 300)       # 5 minutos
c2 = ContenidoDigital("Tutorial Descriptores", 650)    # 10 min 50 s

# Propiedad calculada
print(c1.duracion_minutos)                 # 5.0

# Método estático
print(ContenidoDigital.formatear_tiempo(90))   # 01:30

# Crear playlists
pl1 = PlaylistDigital("Desarrollo Tech")
pl1.agregar(c1)

pl2 = PlaylistDigital("Curso Avanzado")
pl2.agregar(c2)

# Fusionar con el operador +
combinada = pl1 + pl2

print(len(combinada))        # 2
print(combinada[0])          # Primer contenido
print(combinada[0:2])        # Slicing

# Recorrer con for
for contenido in combinada:
    print(contenido.titulo)
```

### Manejo de errores

```python
ContenidoDigital("Audio inválido", 0)
# ValueError: La duración del contenido debe ser un entero estrictamente mayor a 0 segundos.

pl1.agregar("esto no es un contenido")
# TypeError: Solo se pueden agregar objetos de tipo ContenidoDigital.
```

---

## 🖥️ Salida esperada

Al ejecutar `python main.py` se obtiene:

```text
============================================================
PRUEBA EJERCICIO 2: PLAYLIST Y CONTENIDO DIGITAL
============================================================
Contenido 1: ContenidoDigital(titulo='Podcast Python POO', duracion='05:00')
Duración en minutos (Property): 5.00 min
Formato estático (90 segundos): 01:30

Nueva Playlist Creada: PlaylistDigital(nombre='Combinada (Desarrollo Tech & Curso Avanzado)', total_items=2)
Cantidad total de elementos (__len__): 2 contenidos.

Recorriendo la playlist con bucle `for`:
 - Podcast Python POO | ContenidoDigital(titulo='Podcast Python POO', duracion='05:00')
 - Tutorial Descriptores | ContenidoDigital(titulo='Tutorial Descriptores', duracion='10:50')
```

---

## 🚀 Posibles mejoras

- Agregar un método `duracion_total()` a la playlist que sume todas las duraciones.
- Implementar `__str__` para una presentación más amigable al usuario.
- Añadir métodos para **eliminar** o **buscar** contenidos por título.
- Crear subclases (`Podcast`, `Video`, `Audiolibro`) usando **herencia**.
- Incorporar **pruebas unitarias** con `unittest` o `pytest`.
- Guardar y cargar playlists desde archivos **JSON**.

---

## 👤 Autor

**brunolezamapr**  
Repositorio: [Catalogo-de-Contenidos-Digitales](https://github.com/brunolezamapr/Catalogo-de-Contenidos-Digitales)

---

> 📌 *Proyecto con fines educativos, enfocado en el aprendizaje de Programación Orientada a Objetos en Python.*
