import pygame
from lib_archivos import *
from funciones import *
import random
from start_game import *
import sys
from class_objeto import Objeto
from configuraciones import *
from funciones_secundarias import *

# Inicializar Pygame
pygame.init()

pygame.font.init()

niveles = [
    
    (nivel_dos_dos, palabras_dos_nivel, botones),
    (nivel_uno_uno, palabras_uno_nivel, botones),
    (nivel_tres_tres, palabras_tres_nivel, botones)
    
]


for configuracion_nivel in niveles:
    nivel_completado,puntaje_obtenido = nivel(PANTALLA, FONDO, *configuracion_nivel)

   
    if not nivel_completado:
        
        break
    else:
        guardar_datos_csv(nivel_completado, puntaje_obtenido)
