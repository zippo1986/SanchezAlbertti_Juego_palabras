import pygame
from lib_archivos import *
from funciones import *
import random
from start_game import *
import sys
from configuraciones import *
from funciones_secundarias import *

# Inicializar Pygame
pygame.init()

pygame.font.init()

niveles = [
    (nivel_uno_unoo, palabras_nivel_unoo, botones,posicion_res_parcial),
    (nivel_dos_dos, palabras_dos_nivel, botones_dos,posicion_res_parcial),
    (nivel_tres_tres, palabras_tres_nivel, botones_tres,posicion_res_parcial)
]

nivel_actual = 0

while True:
    nivel_completado, puntaje_obtenido = nivel(PANTALLA, FONDO, *niveles[nivel_actual])

    if not nivel_completado:
        break
        
    guardar_datos_csv( puntaje_obtenido)
    guardar_datos_json(puntaje_obtenido)
    nivel_actual += 1