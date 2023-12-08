
import pygame
import random
from configuraciones import *
from lib_archivos import *
from funciones_secundarias import *
#lista_nivel_uno = cargar_archivo('nivel_uno.json')


def cargar_lista_clave(lista_entrada,lista_salida,clave):
    """A partir de una lista de diccionarios(lista entrada) carga una lista de elementos segun la clave indicada

    Args:
        lista_entrada (list): lista de diccionarios
        lista_salida (list): lista de elementos
        clave (str): clave de la lista de diccionarios que cargará a la lista
    """
    for elemento in lista_entrada:
        lista_salida.append(elemento[clave])

def crear_resultado (letras_seleccionadas):
    """Esta función toma la lista de letras seleccionadas las une con un join y retorna el resultado

    Args:
        letras_seleccionadas (lista): lista de str de cada letra seleccionada

    Returns:
        str: str
    """
    resultado = "".join(letras_seleccionadas)
    print(resultado)
    return resultado

def mostrar_elemento_pantalla(fuente, pantalla,texto, elemento,posicion):
    """Funcion que muestra el puntaje en pantalla

    Args:
        fuente (_type_): _description_
        pantalla (_type_): _description_
        puntaje (_type_): _description_
    """
    texto = fuente.render(f"{texto}: {elemento}", True, (255, 255, 255))
    pantalla.blit(texto, (posicion[0], posicion[1]))

def falsear_banderas_lista(lista):
    """Modifica las banderas de la lista de diccionarios

    Args:
        lista (list): lista de diccionarios (letras)
    """
    for elemento in lista:
        elemento["seleccionada"] = False

def  seleccionar_letra(lista_letras,x,y,letras_tomadas,letras_seleccionadas):
    """Verifica la bandera seleccionada en cada letra y si devuelve True las agrega a una lista

    Args:
        lista_letras (list): lista de diccionareios de letras
        x (int): posicion en X
        y (int): posicion en Y
        letras_tomadas (list): lista de letras
        letras_seleccionadas (list): lista de letras seleccionadas

    Returns:
        str: retorna la letra seleccionada 
    """
    for letra in lista_letras:
                    letra_seleccionada = seleccionar(letra,x,y)#Guatda la etiqueta de letra "t"
             
                    if letra_seleccionada and letra_seleccionada not in letras_seleccionadas:
                        letras_tomadas.append(letra)
                        
                        

                        cambiar_posicion(letra)
                        
                        letras_seleccionadas.append(letra_seleccionada)
                        return letra_seleccionada
    


def shaffle_(lista_pos_x,letras_nivel):
    """Toma una lista de posiciones en x y las mezcla luego las asigna a una lista de diccionarios

    Args:
        lista_pos_x (list): lista posicion x
        letras_nivel (list): lista diccionarios
    """
    random.shuffle(lista_pos_x)
                    # Asegurarse de que ambas listas tengan la misma longitud
    if len(lista_pos_x) == len(letras_nivel):
                        # Emparejar cada letra con una posición única de x
        for x, letra in zip(lista_pos_x, letras_nivel):        
            letra["pos_x"] = x
            letra["rectangulo"].x = x
    
