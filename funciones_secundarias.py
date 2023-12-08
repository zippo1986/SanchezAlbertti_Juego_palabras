from lib_archivos import *
from nivel_uno import *
import random
import pygame

def chequear_resultado(resultado,palabras_nivel,palabras_visibles):
    """Verifica si la palabra se encuentra en la lista de palabras

    Args:
        resultado (str): el resultado que deriva de la funcion crear_resultado
        lista (list): lista de palabras (str) del nivel

    Returns:
        bool: retorna True si coincide y False si no coincide
    """
    check =False
    if resultado in palabras_nivel:
        check=True
    
    return check

def sumar_puntaje (resultado,puntaje,palabras_nivel):
    """Suma el puntaje segun la longitud de la palabra (cada letra vale 1 punto)

    Args:
        resultado (str): es el resultado de la seleccion de letras
        puntaje (int): el puntaje actual
        palabras_nivel (list): es una lista con las palabras del nivel extraidas de la lista de diccionarios

    Returns:
        int: retorna el nuevo puntaje 
    """
    
    if resultado in palabras_nivel:
        puntaje += len(resultado)

    return puntaje

def cambiar_visibilidad(lista_palabras,resultado,palabras_visibles):
    """Cambia la visibilidad de las palabras si ya fueron elegidas

    Args:
        lista_palabras (list): lista de palabras
        resultado (str): el resultado a comparar
        palabras_visibles (list): lista de palabras
    """
    for palabra in lista_palabras:
        if palabra["palabra"] == resultado:
            palabra["es_visible"] =True
            palabras_visibles.append(palabra)
def mostrar_texto(fuente,pantalla,texto,pos_x,pos_y):    
    """Muestra un tetxo en pantalla

    Args:
        fuente (font): fuente de tipografia pygame
        pantalla (surf): la pantalla del juego 
        texto (str): texto a mostrar
        pos_x (int): posicion en x
        pos_y (int): posicion en y
    """
    texto_letra = fuente.render(f"{texto}", True, (255, 255, 255))
    pantalla.blit(texto_letra, (pos_x, pos_y))
def mostrar_aciertos(palabras_visibles,fuente,pantalla):
    """muestra las palabras descubiertas en la pantalla

    Args:
        palabras_visibles (list): lista de palabras con la bandera["es_visible"] = True
        fuente (font): fuente de pygame
        pantalla (surf): la pantalla del juego
    """
    for palabra in palabras_visibles:
            mostrar_texto(fuente,pantalla, palabra["palabra"], palabra["pos_x"],palabra["pos_y"])
    
        
def chequear_boton(evento,boton,lista_botones):
    """toma el evento del juego y chequea en la lista de botones 

    Args:
        evento (event): evento de pyga
        boton (str): es un str de la etiqueta de lalista de diccionarios
        lista_botones (list): lista de botones

    Returns:
        str: retorna el str de la etiqueta del boton
    """
    
    boton_seleccionado = seleccionar(evento,boton)
    return boton_seleccionado    
def validar_valor_indice(lista_palabras,resultado):
    """Valida las excepciones

    Args:
        lista_palabras (list): lista de palabras
        resultado (str): 
    """
    try:
        quitar_elmento_especifico(lista_palabras,resultado)
        
    except ValueError:
        pass
    except IndexError:
        pass    
    
def mostrar_game_over(pantalla):
    """muestra la pantalla de game over

    Args:
        pantalla (surf): la pantalla 
    """
    fuente = pygame.font.SysFont(None, 55)
    texto_game_over = fuente.render("Game Over", True, (255, 0, 0))  # Rojo

    
    posicion_texto = texto_game_over.get_rect(center=(pantalla.get_width() / 2, pantalla.get_height() / 2))

    pantalla.blit(texto_game_over, posicion_texto)
    pygame.display.flip()



def cargar_diccionario(lista):

    """carga el diccionario

    Returns:
        lista: retorna la lista cargada
    """
    lista_cargada = []
    for letra in lista:
        ruta_imagen = letra["imagen"]
        imagen_cargada = pygame.image.load(ruta_imagen)

        
        imagen_reescalada = pygame.transform.scale(imagen_cargada, (50, 50))
        letra["imagen"] = imagen_reescalada

        
        rectangulo = imagen_reescalada.get_rect()

      
        rectangulo.x = letra["pos_x"]
        rectangulo.y = letra["pos_y"]

        letra["rectangulo"] = rectangulo

        lista_cargada.append(letra)

    return lista_cargada
def blitear_letras(diccionario,pantalla):
    for letra in diccionario:
        pantalla.blit(letra["imagen"],(letra["pos_x"],letra["pos_y"]))




def cambiar_posicion(diccionario):
    """cambia la posicion de un elemento de un diccionario

    Args:
        diccionario (): es un elemento de una list de diccionarios
    """
    diccionario["pos_y"] +=150
def seleccionar(letra,x,y):
        
    """chequea los eventos del mouse y cheque que colisione con unrectangulo de una letra

    Returns:
        retorna le etiqueta del elemento del diccionarios
    """
    
        
    if letra["rectangulo"].collidepoint(x, y):

        letra["seleccionada"] = True
        
        return letra["etiqueta"]
def cargar_lista(diccionario):
    """carga una lista

    Args:
        diccionario (_type_): _description_

    Returns:
        _type_: _description_
    """
    palabra_nivel=[]
    for palabra in diccionario:
        palabra_nivel.append(palabra)
    
    return palabra_nivel

            
def regenerar_letras_(lista):
    """cambiia la posicion dem un rect de un elemento de la lista

    Args:
        lista de diccionarios
    """
    for letra in lista:
        letra["pos_y"] -= 150

def quitar_elemento_lista(lista):
    """recorre una lista y elimina  elementos de una lista"""
    for elemento in lista:
        lista.remove(elemento)

def quitar_elmento_especifico(lista,resultado):
    """quita un elemento especidfico de una lista

    Args:
        lista (list): 
        elemento: 
    """
    for elemento in lista:
        if elemento == resultado:
            lista.remove(resultado)



        


