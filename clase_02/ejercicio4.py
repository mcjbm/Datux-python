import sys

def imprimir_documentos(*args):
    for documento in args:
        print(documento)

documentos = sys.argv[1:]
imprimir_documentos(*documentos)