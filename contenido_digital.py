"""
Módulo de Contenido Digital.
Representa un ítem individual de audio o video en una plataforma multimedia,
haciendo uso de propiedades calculadas y utilidades estáticas de formateo de tiempo.
"""


class ContenidoDigital:

    def __init__(self, titulo: str, duracion_segundos: int):
        """
        Inicializa un nuevo objeto de contenido digital.
        :param titulo: Nombre del contenido multimedia.
        :param duracion_segundos: Cantidad total de segundos que dura el contenido.
        """
        if duracion_segundos <= 0:
            raise ValueError(
                "La duración del contenido debe ser un entero estrictamente mayor a 0 segundos."
            )

        self.titulo = titulo
        self.duracion_segundos = int(duracion_segundos)

    @property
    def duracion_minutos(self) -> float:
        """
        Propiedad calculada (@property) de solo lectura.
        Convierte automáticamente la duración en segundos a minutos flotantes.
        """
        return self.duracion_segundos / 60.0

    @staticmethod
    def formatear_tiempo(segundos: int) -> str:
        """
        Método Estático (@staticmethod):
        Toma una cantidad de segundos enteros y retorna una representación con formato visual "MM:SS".
        Ejemplo: 300 segundos -> "05:00"
        """
        if segundos < 0:
            return "00:00"
        minutos = segundos // 60
        seg_restantes = segundos % 60
        return f"{minutos:02d}:{seg_restantes:02d}"

    def __repr__(self) -> str:
        tiempo_str = ContenidoDigital.formatear_tiempo(self.duracion_segundos)
        return f"ContenidoDigital(titulo='{self.titulo}', duracion='{tiempo_str}')"