"""
Módulo de Playlist Digital.
Clase contenedora que aplica agregación sobre objetos `ContenidoDigital`.
Soporta sobrecarga del operador `+` para fusionar listas de reproducción,
así como acceso por índice y recorrido mediante métodos Dunder (`__len__` y `__getitem__`).
"""

from typing import List
from contenido_digital import ContenidoDigital


class PlaylistDigital:

    def __init__(self, nombre: str):
        """Inicializa una lista de reproducción vacía."""
        self.nombre = nombre
        self._contenidos: List[ContenidoDigital] = []

    def agregar(self, contenido: ContenidoDigital):
        """Agrega un nuevo contenido digital a la colección interna."""
        if not isinstance(contenido, ContenidoDigital):
            raise TypeError(
                "Solo se pueden agregar objetos de tipo ContenidoDigital."
            )
        self._contenidos.append(contenido)

    # --- SOBRECARGA DE MÉTODOS DUNDER DE COLECCIÓN Y OPERADORES ---

    def __len__(self) -> int:
        """
        Método Mágico `__len__`:
        Permite invocar `len(playlist)` para obtener el número total de elementos guardados.
        """
        return len(self._contenidos)

    def __getitem__(self, index):
        """
        Método Mágico `__getitem__`:
        - Permite la indexación directa mediante corchetes (ej: `playlist[0]`).
        - Permite la iteración nativa en bucles `for` (ej: `for canción in playlist:`).
        - Soporta slicing / rebanado (ej: `playlist[0:2]`).
        """
        return self._contenidos[index]

    def __add__(self, otra_playlist: "PlaylistDigital") -> "PlaylistDigital":
        """
        Sobrecarga del Operador de Suma (`+`):
        Combina los contenidos de dos instancias de `PlaylistDigital` y retorna
        una NUEVA lista de reproducción manteniendo inmutables las originales.
        """
        if not isinstance(otra_playlist, PlaylistDigital):
            return NotImplemented

        # Creamos una nueva instancia combinada
        nueva_playlist = PlaylistDigital(
            nombre=f"Combinada ({self.nombre} & {otra_playlist.nombre})"
        )

        # Agregamos los ítems de ambas colecciones
        for item in self._contenidos:
            nueva_playlist.agregar(item)

        for item in otra_playlist._contenidos:
            nueva_playlist.agregar(item)

        return nueva_playlist

    def __repr__(self) -> str:
        return f"PlaylistDigital(nombre='{self.nombre}', total_items={len(self)})"