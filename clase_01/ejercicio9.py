#EJERCICIO 9
python = []
sql = []
powerbi = []
print("""
----------------------------
1. Agrega lista de python
2. Agrega lista de SQL
3. Agregar a lista Power BI
----------------------------
""")
continuar = input("Deseas Ingresar un valor? S/N: ")
while continuar.lower() == "s":
    varx = int(input("Elige opción: "))
    if varx == 1:
        nombre = input("Ingresa nombre")
        python.append(nombre)
    elif varx == 2:
        nombre = input("Ingresa nombre")
        sql.append(nombre)
    elif varx == 3:
        nombre = input("Ingresa nombre")
        powerbi.append(nombre)
    else:
        print("Esa opción no existe")
    continuar = input("Deseas Ingresar un valor? S/N: ")
print(f"""
-----------------------------------
Lista de python
{python}

Lista de sql
{sql}

Lista de power bi
{powerbi}
------------------------------------
""")  