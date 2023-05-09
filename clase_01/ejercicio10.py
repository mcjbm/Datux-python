#EJERCICIO 10
dnis = ['12345678A', '23456789B', '34567890C']
datos = [
    ['Juan', 25, 'SJL', 'Datux', 'Curso: Python'],
    ['Ana', 17, 'Breña', 'Datux', 'Curso: SQL'],
    ['Pedro', 30, 'La Victoria', 'Datux', 'Curso: Python']
]

dni = input("Ingrese su DNI: ")
# Verificar si el DNI existe en la lista de DNI's
if dni in dnis:
    # Obtener la posición del DNI en la lista de DNI's
    indice = dnis.index(dni)
    
    # Obtener los datos de la persona en la posición correspondiente de la lista de datos
    persona = datos[indice]
    
    # Verificar si cumple con los requisitos para ingresar al curso de Python
    if persona[1] >= 18 and persona[3]=='Datux' and "Python" in persona[4]:
        print("Tiene permitido ingresar al curso de Python.")
    else:
        print("Lo siento, no cumple con los requisitos para ingresar al curso de Python.")
else:
    print("Lo siento, su DNI no está en la lista.")