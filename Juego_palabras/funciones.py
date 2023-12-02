
import pygame
import random
from configuraciones import *
from lib_archivos import *
#lista_nivel_uno = cargar_archivo('nivel_uno.json')
def cargar_palabras_nivel(nivel,clave):
    palabras_nivel= []
    for palabra in nivel[clave] :
        palabras_nivel.append(palabra)
    
    return palabras_nivel
        

def cargar_lista_clave(lista_entrada,lista_salida):
    for elemento in lista_entrada:
        lista_salida.append(elemento["pos_x"])


# Función para obtener letras aleatorias
def shuffle_letras(lista_letras):
    """
    Esta función toma una lista de letras y las reordena aleatoriamente.

    :param lista_letras: Lista de letras a reorganizar.
    :return: Lista de letras reorganizada.
    """
    random.shuffle(lista_letras)
    return lista_letras

contador = 0
def crear_resultado (letras_seleccionadas):
        resultado = "".join(letras_seleccionadas)
        print(resultado)
        return resultado
def verificar_palabra(resultado, lista):
    if resultado in lista:
        return True
def mostrar_puntaje(fuente, pantalla, puntaje):
    texto = fuente.render(f"Puntaje: {puntaje}", True, (255, 255, 255))
    pantalla.blit(texto, (10, 10))
def mostrar_tiempo(fuente, pantalla, tiempo_restante):
    texto = fuente.render(f"Tiempo: {tiempo_restante}", True, (255, 255, 255))
    pantalla.blit(texto, (10, 40))
def mostrar_texto(fuente,pantalla,texto,pos_x,pos_y):    
    texto_letra = fuente.render(f"{texto}", True, (255, 255, 255))
    pantalla.blit(texto_letra, (pos_x, pos_y))


def actualizar_letras_pantalla(letras_en_pantalla, letra_seleccionada):
    letras_a_eliminar = []
    for rect, letra in letras_en_pantalla:
        if letra_seleccionada == letra:
            letras_a_eliminar.append((rect, letra))
    
    for item in letras_a_eliminar:
        letras_en_pantalla.remove(item)

def falsear_banderas_lista(lista):
    for elemento in lista:
        elemento["seleccionada"] = False

def shaffle(lista_pos_x,lista_dicc):
    lista_aleatoria = random.shuffle(lista_pos_x)
    print(lista_aleatoria)
    for letra in lista_dicc:
        for x in lista_aleatoria:
            letra["pos_x"] = x
            letra["rectangulo"].x = x 




letras_en_pantalla= []


lista_etiqueta_letras= []
#cargar_lista_clave(lista_etiqueta_letras,letras_en_pantalla)
#print(lista_etiqueta_letras)
#palabras_nivel = cargar_palabras_nivel(palabras_uno)


bandera_entrada= True

posicion_x =200