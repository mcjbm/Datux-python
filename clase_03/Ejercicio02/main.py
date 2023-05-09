from catalogo import Catalogo, Producto

if __name__ == "__main__":
    catalogo = Catalogo()
    catalogo.agregar_producto(Producto("Llanta", "LLA001", 1500))
    catalogo.agregar_producto(Producto("Bujía", "BUJ001", 200))
    catalogo.agregar_producto(Producto("Filtro de aceite", "FIL001", 300))
    catalogo.mostrar_productos()

