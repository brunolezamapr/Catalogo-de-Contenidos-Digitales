"""
Punto de Entrada Principal (Main Script) - Catálogo de Contenidos Digitales.
Ejecución secuencial para verificar el comportamiento de formateo de tiempo,
operación de adición de playlists e iteraciones Dunder.
"""

from contenido_digital import ContenidoDigital
from playlist_digital import PlaylistDigital

if __name__ == "__main__":
    print("=" * 60)
    print("PRUEBA EJERCICIO 2: PLAYLIST Y CONTENIDO DIGITAL")
    print("=" * 60)

    # 1. Instanciación de Contenidos
    c1 = ContenidoDigital("Podcast Python POO", 300)  # 5 minutos
    c2 = ContenidoDigital("Tutorial Descriptores", 650)  # 10m 50s

    print(f"Contenido 1: {c1}")
    print(f"Duración en minutos (Property): {c1.duracion_minutos:.2f} min")

    # 2. Prueba del Método Estático de Formateo
    print(
        f"Formato estático (90 segundos): {ContenidoDigital.formatear_tiempo(90)}"
    )

    # 3. Creación y llenado de Playlists
    pl1 = PlaylistDigital("Desarrollo Tech")
    pl1.agregar(c1)

    pl2 = PlaylistDigital("Curso Avanzado")
    pl2.agregar(c2)

    # 4. Fusión de Playlists usando la sobrecarga del operador '+'
    pl_combinada = pl1 + pl2
    print(f"\nNueva Playlist Creada: {pl_combinada}")
    print(
        f"Cantidad total de elementos (__len__): {len(pl_combinada)} contenidos."
    )

    # 5. Iteración sobre la playlist combinada mediante `__getitem__`
    print("\nRecorriendo la playlist con bucle `for`:")
    for contenido in pl_combinada:
        print(f" - {contenido.titulo} | {contenido}")