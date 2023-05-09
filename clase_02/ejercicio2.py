biblioteca = {
    "novelas": [
        {"nombre": "don quijote", "autor": "cervantes", "prestado": False},
        {"nombre": "platero", "autor": "pepe luna", "prestado": True},
        {"nombre": "naranja", "autor": "acuña", "prestado": False}
    ],
    "Ciencia": [
        {"nombre": "biologia", "autor": "canito", "prestado": False},
        {"nombre": "quimica", "autor": "bertha", "prestado": False}
    ]
}

def categorias(biblioteca):
    return list(biblioteca.keys())

#print(categorias(biblioteca))

def autor_libro(biblioteca):
    libros=[]
    for categoria in biblioteca:
        for libro in biblioteca[categoria]:
            libros.append((libro['nombre'],libro['autor']))
    print(libros)

autor_libro(biblioteca)
