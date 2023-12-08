from nivel_uno import *
import json

import csv
from datetime import datetime


def guardar_puntaje_en_csv(puntaje, nombre_archivo="puntaje.csv"):
    """guarda el puntaje, la hora y la fecha 

    Args:
        puntaje (int): 
        nombre_archivo (str)"puntaje.csv".
    """
    ahora = datetime.now()
    fecha_hora = ahora.strftime("%Y-%m-%d %H:%M:%S")

    # Datos a escribir en el archivo CSV
    datos = [fecha_hora, puntaje]

    
    with open(nombre_archivo, mode='a', newline='') as file:
        writer = csv.writer(file)

        # Escribir los datos en el archivo
        writer.writerow(datos)

    print(f"Puntaje guardado en {nombre_archivo}")
  

def guardar_datos_csv( puntaje, nombre_archivo="datos_juego.csv"):
    """_summary_

    Args:
        nivel (_type_): _description_
        puntaje (_type_): _description_
        nombre_archivo (str, optional): _description_. Defaults to "datos_juego.csv".
    """
    
    fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    datos = [f"'Fecha': { fecha_hora}, puntaje: {puntaje}"]

    # Escribir los datos en el archivo
    with open(nombre_archivo, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(datos)

def guardar_datos_json(puntaje):
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data = {"fecha_hora": fecha,
            "puntaje":puntaje}

    try:
        with open('datos.json', 'w') as file:
            json.dump(data, file, indent=4)
    except TypeError:
        print("error al guardar el archivo")


