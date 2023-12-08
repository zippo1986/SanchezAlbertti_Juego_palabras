
import pygame
from funciones_secundarias import *
from funciones import *
from configuraciones import *
import sys

def nivel (pantalla,fondo,lista_letras,lista_palabras,lista_botones,posicion_res_parcial):
    """Maneja todas las interacciones entre las listas y las funciones del nivel

    Args:
        pantalla (list): Pantalla del juego
        fondo (list): fondo del juego
        lista_letras (list): lista de diccionarios de las letras
        lista_palabras (list): lista de diccionarios de las palabras
        lista_botones (list): lista de diccionarios de los botones
        posicion_res_parcial (list): lista de diccionarios de posiciones para indicar las elecciones parciales 

    Returns:
        bool: retorna una False o True segun si el nivel fue finalizado o no
    """
    letras_nivel = cargar_diccionario(lista_letras)
    lista_botones = cargar_diccionario(lista_botones)
    lista_palabras = cargar_lista(lista_palabras)
    palabras_nivel=[]
    posicion_parcial_x = []
    cargar_lista_clave(posicion_res_parcial,posicion_parcial_x,"pos_x")
    cargar_lista_clave(lista_palabras,palabras_nivel,"palabra")
    tiempo_inicial = 90000  # 90 segundos en milisegundos
    tiempo_restante = tiempo_inicial
    lista_pos_x = []
    palabras_visibles =[]
    cargar_lista_clave(letras_nivel,lista_pos_x,"pos_x")
    letras_tomadas =[]
    posicion_x_seleccionadas = 821
    posicion_y_seleccionadas = 400
    letras_seleccionadas=[]
    letras_blit=[]
    puntaje = 0
    puntaje_requerido = 10
    bandera_finalizado = False

    while not bandera_finalizado:
        
        pantalla.blit(fondo,(0,0))
        blitear_letras(letras_nivel,PANTALLA) 
        blitear_letras(lista_botones,PANTALLA) 
        eventos= pygame.event.get()
        for evento in eventos:
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
          
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                print(f"{x}, {y}")
                
                letra_seleccionada = seleccionar_letra(lista_letras,x,y,letras_tomadas,letras_seleccionadas)
                mostrar_texto(fuente,pantalla,letra_seleccionada,821,400)
                
                for boton in lista_botones:
                    boton_seleccionado = seleccionar(boton,x,y)
                    match boton_seleccionado:
                        case "submit":
                            resultado = crear_resultado(letras_seleccionadas)
                            
                            if chequear_resultado(resultado,palabras_nivel,palabras_visibles):
                                mostrar_texto(fuente,PANTALLA,"CORRECTO", ANCHO//2,ALTO//2)
                                
                                puntaje = sumar_puntaje(resultado,puntaje,palabras_nivel)
                                validar_valor_indice(lista_palabras,resultado)  
                                falsear_banderas_lista(letras_tomadas)
                                cambiar_visibilidad(lista_palabras,resultado,palabras_visibles)
                                quitar_elmento_especifico(palabras_nivel,resultado)

                            print(palabras_visibles)
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
        
                   
        mostrar_elemento_pantalla(fuente,PANTALLA,"puntaje", puntaje,(10,10))
        
        
        
        
        try:   
            for i in range(6):
                if letras_seleccionadas[i] is not None:
                    mostrar_texto(fuente, PANTALLA,letras_seleccionadas[0],posicion_parcial_x[0], 256)
                    mostrar_texto(fuente, PANTALLA,letras_seleccionadas[1],posicion_parcial_x[1], 256)
                    mostrar_texto(fuente, PANTALLA,letras_seleccionadas[2],posicion_parcial_x[2], 256)
                    mostrar_texto(fuente, PANTALLA,letras_seleccionadas[3],posicion_parcial_x[3], 256)
                    mostrar_texto(fuente, PANTALLA,letras_seleccionadas[4],posicion_parcial_x[4], 256)
                    mostrar_texto(fuente, PANTALLA,letras_seleccionadas[5],posicion_parcial_x[5], 256)
        except IndexError:
            pass



        
        mostrar_aciertos(palabras_visibles,fuente, PANTALLA)
        tiempo_restante = max(tiempo_inicial - pygame.time.get_ticks(), 0)
        mostrar_elemento_pantalla(fuente, PANTALLA,"tiempo", tiempo_restante // 1000,(10,50))
        mostrar_texto(fuente,PANTALLA,"Forma las palabras",200,100)
    
        tiempo_restante = max(tiempo_inicial - pygame.time.get_ticks(), 0)
        if tiempo_restante <= 0:
            if puntaje >= puntaje_requerido or not palabras_nivel  :
                bandera_finalizado = True
            else:
                break
        elif tiempo_restante> 0 and not palabras_nivel:
            bandera_finalizado = True
        
    
        
            

        
        pygame.display.update()
        reloj.tick(60)
    
    return bandera_finalizado,puntaje