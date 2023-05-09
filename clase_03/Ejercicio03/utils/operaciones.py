def dividir(numero1, numero2):
    try:
        resultado = numero1 / numero2
        return resultado
    except ZeroDivisionError:
        print("Error: No se puede dividir entre cero.")