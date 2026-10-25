from contenido_digital import ContenidoDigital

class PlaylistDigital:

    def __init__(self,nombre):

        self.nombre = nombre
        self._contenidos = []

    def agregar(self,contenido:ContenidoDigital):

        self._contenidos.append(contenido)

    def __len__(self):
        return len(self._contenidos)

    def __getitem__(self, key):
        return self._contenidos[key]

    def __add__(self, other):
        if not isinstance(other,PlaylistDigital):
            return NotImplemented
        
        nuevo_nombre = f"Fusionado ({self.nombre} & {other.nombre})"
        nueva_playlist = PlaylistDigital(nombre=nuevo_nombre)

        for play in self._contenidos:
            nueva_playlist.agregar(play)

        for play in other._contenidos:
            nueva_playlist.agregar(play)

        return nueva_playlist