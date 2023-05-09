class Producto:
    def __init__(self, nombre, codigo):
        self.nombre = nombre
        self.codigo = codigo

    def __str__(self):
        pais, lote, anio = self.codigo.split("-")
        return f"Nombre: {self.nombre}\nCódigo: {self.codigo}\nPaís de origen: {pais}\nNúmero de lote: {lote}"
