import sqlite3

def leer_datos_tabla():
    # Conectar a la base de datos SQLite
    conn = sqlite3.connect('base05.db')
    co = conn.cursor()

    # Leer todos los datos de la tabla "user"
    co.execute('SELECT * FROM user')
    datos = co.fetchall()

    # Iterar sobre los resultados
    for fila in datos:
        id = fila[0]
        nombre = fila[1]
        edad = fila[2]
        email = fila[3]
        
        # Realizar las operaciones que desees con los datos
        # Por ejemplo, imprimir los valores
        print(f"ID: {id}, Nombre: {nombre}, Edad: {edad}, Email: {email}")

    # Cerrar la conexión a la base de datos
    conn.commit()
    conn.close()

leer_datos_tabla()