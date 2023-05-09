def cuadros():
    lado = int(input('Ingresa el lado: '))
    print('*'*lado)
    alto = lado-(lado-2)
    while alto < lado:
        print('*'+' '*(lado-2)+'*')
        alto = alto + 1
    print('*'*lado)

def multiplos(*args):
    for arg in args:
        if int(arg)%2==0:
            print(arg)

def clasificar(lista_p):
    for persona in lista_p:
        nombre = persona[0]
        edad = int(persona[1])
        if edad >= 18:
            print(f"{nombre} es mayor de edad, tiene {edad} años.")

print("""
    --------MENU----------
    1. Dibuja un cuadrado
    2. Identifica multiplos de 2
    3. Mayores de edad
""")
opcion = int(input("Elige una opcion: "))

if opcion == 1:
    cuadros()
elif opcion == 2:
    entrada = input('Ingresa tu lista de números separando cada elemento con una <,>: ')
    lista = entrada.split(",")
    multiplos(*lista)
elif opcion == 3:
    entrada = input("Ingrese los nombres y edades separados por comas: ")
    lista_personas = [item.split(",") for item in entrada.split(";")]
    clasificar(lista_personas)
else:
    print("Ingresaste opcion no válida")