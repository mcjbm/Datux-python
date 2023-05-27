import logging
from datetime import datetime

def configurar_logger():
    logger = logging.getLogger('my_logger')
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s-%(name)s-%(message)s')
    file_handler = logging.FileHandler('info.log')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger

def registrar_evento(logger, nombarchivo, nombevento):
    fecha = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    mensaje = f'{fecha}-{nombarchivo}-{nombevento}'
    logger.info(mensaje)

logger = configurar_logger()

nom_archivo = 'file.txt'
nom_evento = 'event_1'
registrar_evento(logger, nom_archivo, nom_evento)