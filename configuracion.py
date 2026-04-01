import json
import os

""" GESTIÓN DE LA CONFIGURACIÓN DEL JUEGO """

ARCHIVO_CONFIG = "config.json"

CONFIG_PREDETERMINADA = {
    "numero_maximo": 1000,
    "pistas_activadas": True
}

def cargar_configuracion():
    """Carga la configuración desde el archivo, o crea una nueva si no existe"""
    if os.path.exists(ARCHIVO_CONFIG): #Verifico si ya existe el archivo.
        with open(ARCHIVO_CONFIG, 'r') as archivo:
            return json.load(archivo)
    else:
        guardar_configuracion(CONFIG_PREDETERMINADA) #Si no existe, lo creo
        return CONFIG_PREDETERMINADA.copy()

def guardar_configuracion(config):
    """Guarda la configuración en el archivo"""
    with open(ARCHIVO_CONFIG, 'w') as archivo:
        json.dump(config, archivo) #Hago dump del diccionario config en el json contenido en la variable ARCHIVO_CONFIG.

def resetear_configuracion():
    """Resetea la configuración a valores predeterminados"""
    guardar_configuracion(CONFIG_PREDETERMINADA)
    return CONFIG_PREDETERMINADA.copy()