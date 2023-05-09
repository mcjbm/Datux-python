#EJERCICIO 7
n1 = int(input("Ingresa el primer valor: "))
n2 = int(input("Ingresa el segundo valor: "))
if(n1!=n2):
   print("Los numeros ingresados son diferentes")
   if(n1>n2):
    print("El primer numero ingresado es mayor que el segundo")
   else:
    print("El primer numero ingresado es menor que el segundo")
else:
    print("Los numeros ingresados son iguales")