from lib_archivos import *
from nivel_uno import *
import random


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
def sumar_puntaje(resultado,lista_palabras,puntaje):
    """suma puntaje

    Args:
        resultado (str):cadena resultado
        lista_palabras (lista): lista de palabras del juego
        puntaje (int): puntaje juego

    Returns:
        int: el puntaje sumado
    """
    if resultado in lista_palabras:
                        # Despues esto se cambia por un blit de texto
        puntaje += len(resultado)
        return puntaje

def chequear_boton(evento,boton,lista_botones):
    """toma el evento del juego y chequea en la lista de botones 

    Args:
        evento (event): evento de pyga
        boton (str): es un str de la etiqueta de lalista de diccionarios
        lista_botones (list): lista de botones

    Returns:
        str: retorna el str de la etiqueta del boton
    """
    for boton in lista_botones:
            boton_seleccionado = seleccionar(evento,boton)
            return boton_seleccionado    
def validar_valor_indice(lista_palabras,resultado):
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


def agregar_bandera(diccionario,clave):
    for letra in diccionario:
        diccionario[clave]=False

def cambiar_posicion(diccionario):
    """cambia la posicion de un elemento de un diccionario

    Args:
        diccionario (): es un elemento de una list de diccionarios
    """
    diccionario["pos_y"] +=150
def seleccionar(event,letra):
        
    """chequea los eventos del mouse y cheque que colisione con unrectangulo de una letra

    Returns:
        retorna le etiqueta del elemento del diccionarios
    """
    if event.type == pygame.MOUSEBUTTONDOWN:
        x, y = pygame.mouse.get_pos()
        
        if letra["rectangulo"].collidepoint(x, y):

            letra["seleccionada"] = True
            print(letra["etiqueta"])
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
        palabra_nivel.append(palabra["palabra"])
    
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

def quitar_elmento_especifico(lista,elemento):
    """quita un elemento especidfico de una lista

    Args:
        lista (list): 
        elemento: 
    """
    lista.remove(elemento)

        


