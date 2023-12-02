
import pygame
from funciones_secundarias import *
from funciones import *
from configuraciones import *
import sys
def nivel (pantalla,fondo,lista_letras,lista_palabras,lista_botones):
    letras_nivel = cargar_diccionario(lista_letras)
    lista_botones = cargar_diccionario(lista_botones)
    lista_palabras = cargar_lista(lista_palabras)
    tiempo_inicial = 90*1000  # 90 segundos en milisegundos
    tiempo_restante = tiempo_inicial
    lista_pos_x = []
    cargar_lista_clave(letras_nivel,lista_pos_x)
    letras_tomadas =[]
    letras_seleccionadas=[]
    puntaje = 0
    puntaje_requerido = 10
    bandera_finalizado = False

    while not bandera_finalizado:
    
        eventos= pygame.event.get()
        for evento in eventos:
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pantalla.blit(fondo,(0,0))
        blitear_letras(letras_nivel,PANTALLA) 
        blitear_letras(lista_botones,PANTALLA)   
        for letra in lista_letras:
            letra_seleccionada = seleccionar(evento,letra)#Guatda la etiqueta de letra "t"
                
            if letra_seleccionada and letra_seleccionada not in letras_seleccionadas:
               letras_tomadas.append(letra)

               cambiar_posicion(letra)
               letras_seleccionadas.append(letra_seleccionada)

        for boton in lista_botones:
            boton_seleccionado = seleccionar(evento,boton)
            match boton_seleccionado:
                case "submit":
                    resultado = crear_resultado(letras_seleccionadas)
                    if resultado in lista_palabras:
                        
                        puntaje += len(resultado)
                        validar_valor_indice(lista_palabras,resultado)
                             
                        falsear_banderas_lista(letras_tomadas)
                        for palabra in lista_palabras:
                            if palabra ==resultado:
                                palabra["es_visible"]= True
                    for palabra in lista_palabras:
                        print(palabra)
                    regenerar_letras_(letras_tomadas)
                    
                    letras_seleccionadas =[]
                    letras_tomadas =[]
                    
                    resultado =""
                case "clear":
                    regenerar_letras_(letras_tomadas)
                    letras_seleccionadas =[]
                    letras_tomadas =[]
                    resultado =""
                    
                case "shuffle":
                
                    shaffle_(lista_pos_x,letras_nivel)
                    
        mostrar_puntaje(fuente,PANTALLA, puntaje)


        tiempo_restante = max(tiempo_inicial - pygame.time.get_ticks(), 0)
        mostrar_tiempo(fuente, PANTALLA, tiempo_restante // 1000)
        mostrar_texto(fuente,PANTALLA,"Forma las palabras",200,100)
    
        tiempo_restante = max(tiempo_inicial - pygame.time.get_ticks(), 0)
        if tiempo_restante <= 0:
            if puntaje >= puntaje_requerido or not lista_palabras:
                bandera_finalizado = True
            else:
                mostrar_game_over(pantalla)

    
        pygame.display.flip()
        reloj.tick(60)
    return bandera_finalizado,puntaje
        
        