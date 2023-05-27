import requests
import sqlite3

def guardar_db(valores):
    # Conexión a la base de datos
    conn = sqlite3.connect('base01.db')
    co = conn.cursor()

    # Guardar los valores en la base de datos
    data = "INSERT INTO sunat (moneda, origen, venta, compra) VALUES (?, ?, ?, ?)"
    co.execute(data, (valores['moneda'], valores['origen'], valores['venta'], valores['compra']))

    # Guardar los cambios y cerrar la conexión
    conn.commit()
    conn.close()

def sunat():
    url = 'https://api.apis.net.pe/v1/tipo-cambio-sunat'
    # REQUERIMIENTO AL SERVIDOR
    respuesta = requests.get(url)
    return respuesta.json()

valores = sunat()
# Guardar los valores en la base de datos
guardar_db(valores)