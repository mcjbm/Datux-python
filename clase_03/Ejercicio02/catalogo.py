class Producto:
    def __init__(self, nombre, codigo, precio):
        self.nombre = nombre
        self.codigo = codigo
        self.precio = precio

class Catalogo:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_productos(self):
        for producto in self.productos:
            print(f"{producto.nombre} ({producto.codigo}): ${producto.precio}")
