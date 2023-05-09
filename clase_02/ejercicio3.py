var1 = int(input("Ingresa el valor 1: "))
var2 = int(input("Ingresa el valor 2: "))

def mayor(a,b):
    if a > b:
        return a
    elif b > a:
        return b
    else:
        return 0
resultado = mayor(var1,var2)

if resultado != 0:
    print(f"el valor valor es {resultado}")
else:
    print("ambos valores son iguales")