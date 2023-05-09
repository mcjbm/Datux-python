#EJERCICIO 3
num1 = int(input("Ingresa el primer valor: "))
num2 = int(input("Ingresa el segundo valor: "))
num3 = int(input("Ingresa el tercer valor: "))
suma = num1 + num2 + num3
resta = num1 - num2 - num3
multi = num1 * num2 * num3
division = num1 / num2 / num3
entera = (num1%num2)%num3
print(f"""
suma: {suma}
resta: {resta}
multiplicacion {multi}
division: {division}
div. entera:{entera}
""")
