#EJERCICIO 1
nombres = input("Ingresa nombres completos: ")
dni = input("Ingresa tu DNI:")
edad = input("Ingresa tu edad")

print(f"""Mi nombre es: {nombres}
Mi DNI es:{dni}
y tengo: {edad} años
""")

#EJERCICIO 1 V2
nombres = input("Ingresa nombres completos: ")
dni = input("Ingresa tu DNI:")
edad = input("Ingresa tu edad")

print("""Mi nombre es: {}
Mi DNI es:{}
y tengo: {} años
""".format(nombres,dni,edad))