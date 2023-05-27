import pandas as pd

# Ruta del archivo Excel
ruta_archivo = r"C:\Users\santi\OneDrive\Escritorio\WordSpace\tarea_final\ejercicio_04\ed.csv"

# Cargar el archivo Excel en un DataFrame
datos = pd.read_csv(ruta_archivo)
# Crear una serie booleana basada en el filtro deseado
filtro = datos["Edad"] >= 30
# Aplicar el filtro utilizando indexación booleana
datos_filtrados = datos[filtro]
# Mostrar las primeras filas del archivo
print(datos_filtrados.head())