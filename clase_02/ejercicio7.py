texto = "Lorem Ipsum es simplemente el texto de relleno de las imprentas y archivos de texto. Lorem Ipsum ha sido el texto de relleno estandar de las industrias desde el año 1500, cuando un impresor (N. del T. persona que se dedica a la imprenta) desconocido usó una galeria de textos y los mezcló de tal manera que logró hacer n libro de textos especimen. No solo sobrevio 500 años, sino que tambien ingreso como texto de relleno en documentos electronicos, quedando esencialmente igual al original. Fue popularizado en los 60s con la creación de las hojas 'Letraset', las cuales contenian pasajes de Lorem Ipsum, y mas recientemente con software de autoedicion, como por ejemplo Aldus PageMarker, el cual incluye versiones de Lorem Ipsum"

longitud_texto = len(texto)
print("La longitud del texto es:", longitud_texto)
texto_mayusculas = texto.upper()
print("----------------------------------------------------\n")
print("Texto en mayúsculas:", texto_mayusculas)
print("----------------------------------------------------\n")
palabra_a_buscar = "Lorem"
cantidad = texto.count(palabra_a_buscar)
print("La palabra '{}' aparece {} veces en el texto".format(palabra_a_buscar, cantidad))
print("----------------------------------------------------\n")
palabra_a_reemplazar = "Lorem"
nueva_palabra = "DOLOR"
texto_modificado = texto.replace(palabra_a_reemplazar, nueva_palabra)
print(texto_modificado)



