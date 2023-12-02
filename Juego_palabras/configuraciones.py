import pygame
from funciones import *

from class_objeto import Objeto
from niveles import *

pygame.font.init()
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
VIOLETA = (145, 84, 250)

# Definir dimensiones de la pantalla
ANCHO, ALTO = 1200, 600
PANTALLA = pygame.display.set_mode((ANCHO, ALTO))
FONDO = pygame.image.load('fondo/fondo_quiz.png')
FONDO = pygame.transform.scale(FONDO, (ANCHO, ALTO))

puntaje = 0
letras_a_eliminar= []
reloj = pygame.time.Clock()
resultados_lista = []
letras_seleccionadas=[]
palabras_eliminadas=[]
fuente = pygame.font.SysFont(None, 36)



letras_seleccionadas =[]


letras_tomadas =[]
lista_pos_x = []

tiempo_inicial = 90*1000  # 90 segundos en milisegundos
tiempo_restante = tiempo_inicial



palabras_dos = ["marenta", "mar", "renta", "arme", "tren", "rabo"]
palabras_tres = ["esfera", "sera", "fea", "esa", "ser", "resefa", "fase", "era"]



letras_seleccionadas=[]



