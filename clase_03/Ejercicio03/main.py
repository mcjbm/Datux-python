from utils.operaciones import dividir

if __name__ == "__main__":
    opcion = ""
    while opcion != "q":
        print("Opciones:")
        print("1. Dividir dos números")
        print("q. Salir")

        opcion = input("Ingrese una opción: ")
        if opcion == "1":
            numero1 = float(input("Ingrese el primer número: "))
            numero2 = float(input("Ingrese el segundo número: "))
            resultado = dividir(numero1, numero2)
            if resultado is not None:
                print(f"El resultado de la división es: {resultado}")
        elif opcion != "q":
            print("Opción no válida.")