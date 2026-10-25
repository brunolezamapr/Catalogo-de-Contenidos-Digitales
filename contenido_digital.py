 
class ContenidoDigital:

    def __init__(self,titulo:str,duracion_segundos:int):
        self.titulo = titulo
        self.duracion_segundos = duracion_segundos

    @property
    def duracion_minutos(self):
        return self.duracion_segundos / 60

    @staticmethod 
    def formatear_tiempo(segundos:int) -> str:

        minutos,segundos_restantes = divmod(segundos,60)
        
        formato_string = f"{minutos:02d}:{segundos_restantes:02d}"
        return formato_string

    

    

    