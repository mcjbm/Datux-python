class Pelicula:
    def __init__(self,titulo,duracion,release) -> None:
        self.titulo=titulo
        self.duracion=duracion
        self.release=release
    def __str__(self) -> str:
        return f"{self.titulo} se estreno el {self.release} y dura {self.duracion} minutos"