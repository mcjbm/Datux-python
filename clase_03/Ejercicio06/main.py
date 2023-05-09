from catalogo import Catalogo
from pelicula import Pelicula

if __name__ == "__main__":
    peli1=Pelicula("ant man",120,2020)
    peli2=Pelicula("mario b",80,2023)
    c1=Catalogo()
    c1.agregar(peli1)
    c1.agregar(peli2)
    c1.mostrar()
