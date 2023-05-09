#EJERCICIO 2
lado = int(input("Ingresa el lado: "))
radio = int(input("Ingresa el radio: "))
base = int(input("Ingresa la base: "))
altura = int(input("Ingresa la altura: "))
cuadrado = lado**2
triangulo = (base*altura)/2
circulo = 3.14*(radio**2)
print("""
- El area del circulo es: {}
- El area del triangulo es: {}
- El area del cuadrado es: {}
""".format(circulo,triangulo,cuadrado))