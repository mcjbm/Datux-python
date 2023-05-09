import os

class Producto:
    def __init__(self, nombre, codigo):
        self.nombre = nombre
        self.codigo = codigo

    def __str__(self):
        pais, lote, anio = self.codigo.split("-")
        return f"Producto: {self.nombre}\nPaís de origen: {pais}\nNúmero de lote: {lote}\nAño: {anio}"

try:
    from funciones import dividir
    from catalogo import Catalogo, Producto
    print("Funciones y clases importadas correctamente.")
except ImportError:
    print("Error al importar funciones o clases.")
else:
    print(f"Directorio de trabajo: {os.getcwd()}")
finally:
    print("Proceso terminado.")