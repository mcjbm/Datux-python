import sqlite3
import pandas as pd

ruta_archivo = r"C:\Users\santi\OneDrive\Escritorio\WordSpace\tarea_final\ejercicio_04\ed.csv"

# Cargar el archivo Excel en un DataFrame
datos = pd.read_csv(ruta_archivo)

# Conectar a la base de datos SQLite
conn = sqlite3.connect('base05.db')
co = conn.cursor()

crear_bd = """
    CREATE TABLE IF NOT EXISTS user(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre VARCHAR(60),
    edad INT,
    ciudad VARCHAR(30)
    )
"""
co.execute(crear_bd)

# Insertar los datos en la tabla "user"
# Insertar los datos en la tabla "user"
for _, fila in datos.iterrows():
    nombre = fila['Nombre']
    edad = fila['Edad']
    ciudad = fila['Ciudad']
    
    co.execute('''
        INSERT INTO user (nombre, edad, ciudad) VALUES (?, ?, ?)
    ''', (nombre, edad, ciudad))


conn.commit()
conn.close()



