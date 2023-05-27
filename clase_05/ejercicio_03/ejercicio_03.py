import re

def validar_entrada(expresion_regular, entrada):
    patron = re.compile(expresion_regular)
    return re.match(patron, entrada) is not None

print("-------------------------------------\n")
entrada = input("Ingrese una entrada: ")
print("\n-------------------------------------")
if validar_entrada(r'^\d+$', entrada):
    print('El valor es numerico')
# Validar para texto
elif validar_entrada(r'^[a-zA-Z\s]+$', entrada):
    print('El valor es texto')
# Validar para dirección de correo electrónico
elif validar_entrada(r'^[\w\.-]+@[\w\.-]+\.\w+$', entrada):
    print('El valor es correo electrónico')
# Validar para número de teléfono
elif validar_entrada(r'^\+?51\d{9}$', entrada):
    print('El valor es numero telefonico')
else:
    print('valor inválido')