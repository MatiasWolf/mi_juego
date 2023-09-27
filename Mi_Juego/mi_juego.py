import pygame
from Constantes import *
from datos import *

boton_pregunta = "PREGUNTA"
boton_reiniciar = "REINICIAR"
puntuacion = "PUNTUACIÓN:"
pregunta = ""
opcion_a = ""
opcion_b = ""
opcion_c = ""
mensaje_final_1 = ""
mensaje_final_2 = ""
puntuacion_final = ""


opcion_correcta = lista_opcion_correcta
indice = 0
acumulador_puntuacion = 0
chances = 0
bandera_click_a = False
bandera_click_b = False
bandera_click_c = False
reiniciado = False
contador_preguntas = 0
indice_opcion_correcta = indice - 1

pygame.init()
pygame.mixer.init()
pygame.mixer.music.set_volume(0.7)
sonido_opcion_correcta = pygame.mixer.Sound("audio_mario_correcta.mp3")
sonido_opcion_correcta.set_volume(0.2)
sonido_error = pygame.mixer.Sound("error-fallo-1.mp3")
sonido_error.set_volume(0.2)
sonido_final = pygame.mixer.Sound("audio_final.mp3")
sonido_final.set_volume(0.2)
#Definimos una imagen
imagen = pygame.image.load("preguntados_pygame.png")
imagen = pygame.transform.scale(imagen,(200,200))

#Definimos la pantalla
pantalla = pygame.display.set_mode([1000, 800])#tamaño de la pantalla
pygame.display.set_caption("PyGame")#titulo

#Definimos texto
fuente = pygame.font.SysFont("Arial", 35)
fuente_puntuacion = pygame.font.SysFont("Times New Roman", 60)
texto_boton_pregunta = fuente.render(str(boton_pregunta), True, COLOR_NEGRO)
texto_boton_reiniciar = fuente.render(str(boton_reiniciar), True, COLOR_NEGRO)
texto_puntuacion = fuente.render(str(puntuacion), True, COLOR_NEGRO)
texto_cantidad_puntuacion = fuente.render(str(acumulador_puntuacion), True, COLOR_NEGRO)
texto_pregunta = fuente.render(str(pregunta), True, COLOR_NEGRO)
texto_opcion_a = fuente.render(str(opcion_a), True, COLOR_BLANCO)
texto_opcion_b = fuente.render(str(opcion_b), True, COLOR_BLANCO)
texto_opcion_c = fuente.render(str(opcion_c), True, COLOR_BLANCO)
texto_mensaje_final_1 = fuente_puntuacion.render(str(mensaje_final_1), True, COLOR_ROJO)
texto_mensaje_final_2 = fuente_puntuacion.render(str(mensaje_final_2), True, COLOR_ROJO)
texto_puntuacion_final = fuente_puntuacion.render(str(puntuacion_final), True, COLOR_ROJO)

running = True
while running:
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False #Si se toca la cruz de la pantalla, se cierra el juego
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            #print(list(event.pos))  #me printea la posicion en pixeles del click en la pantalla
            posicion_click = list(event.pos)
            
            #boton pregunta 
            if posicion_click[0]>105 and posicion_click[0]<295 and posicion_click[1]>95 and posicion_click[1]<145:
                contador_preguntas += 1
                if reiniciado == True:
                    sonido_final.stop()
                    indice += 1
                    if indice > len(lista_preguntas) - 1:
                        indice = 0
                    
                    pregunta = lista_preguntas[indice] 
                    opcion_a = lista_opcion_a[indice]
                    opcion_b = lista_opcion_b[indice]
                    opcion_c = lista_opcion_c[indice]
                    mensaje_final_1 = ""
                    mensaje_final_2 = ""
                    puntuacion_final = ""
                    puntuacion = "PUNTUACIÓN:"
                    
                    texto_pregunta = fuente.render(str(pregunta), True, COLOR_NEGRO)
                    texto_opcion_a = fuente.render(str(opcion_a), True, COLOR_BLANCO)
                    texto_opcion_b = fuente.render(str(opcion_b), True, COLOR_BLANCO)
                    texto_opcion_c = fuente.render(str(opcion_c), True, COLOR_BLANCO)
                    texto_mensaje_final_1 = fuente.render(str(mensaje_final_1), True, COLOR_ROJO)
                    texto_mensaje_final_2 = fuente.render(str(mensaje_final_2), True, COLOR_ROJO)
                    texto_puntuacion_final = fuente.render(str(puntuacion_final), True, COLOR_ROJO)
                    texto_puntuacion = fuente.render(str(puntuacion), True, COLOR_NEGRO)
                    texto_cantidad_puntuacion = fuente.render(str(acumulador_puntuacion), True, COLOR_NEGRO)
                    
                    
                    
                    bandera_click_a = False
                    bandera_click_b = False
                    bandera_click_c = False
                        
                    chances = 0
                        
                    if contador_preguntas == 17:
                        pregunta = ""
                        opcion_a = ""
                        opcion_b = ""
                        opcion_c = ""
                        texto_pregunta = fuente.render(str(pregunta), True, COLOR_NEGRO)
                        texto_opcion_a = fuente.render(str(opcion_a), True, COLOR_BLANCO)
                        texto_opcion_b = fuente.render(str(opcion_b), True, COLOR_BLANCO)                        
                        texto_opcion_c = fuente.render(str(opcion_c), True, COLOR_BLANCO)
                        mensaje_final_1 = "Gracias por jugar"
                        mensaje_final_2 = "PREGUNTADOS"
                        puntuacion_final = f"Puntuación final: {acumulador_puntuacion}"
                        texto_mensaje_final_1 = fuente_puntuacion.render(str(mensaje_final_1), True, COLOR_ROJO)
                        texto_mensaje_final_2 = fuente_puntuacion.render(str(mensaje_final_2), True, COLOR_ROJO)
                        texto_puntuacion_final = fuente_puntuacion.render(str(puntuacion_final), True, COLOR_ROJO)
                        puntuacion = ""
                        acumulador_puntuacion = ""
                        texto_puntuacion = fuente.render(str(puntuacion), True, COLOR_NEGRO)
                        texto_cantidad_puntuacion = fuente.render(str(acumulador_puntuacion), True, COLOR_NEGRO)
                        contador_preguntas = 0
                        acumulador_puntuacion = 0
                        reiniciado = False
                        sonido_final.play()
                    elif contador_preguntas == 18:
                        indice = 0
                    indice_opcion_correcta = indice + 1
                else:
                    sonido_final.stop()
                    if contador_preguntas <= 17:
                        pregunta = lista_preguntas[indice] 
                        opcion_a = lista_opcion_a[indice]
                        opcion_b = lista_opcion_b[indice]
                        opcion_c = lista_opcion_c[indice]
                        mensaje_final_1 = ""
                        mensaje_final_2 = ""
                        puntuacion_final = ""
                        puntuacion = "PUNTUACIÓN:"
                        texto_pregunta = fuente.render(str(pregunta), True, COLOR_NEGRO)
                        texto_opcion_a = fuente.render(str(opcion_a), True, COLOR_BLANCO)
                        texto_opcion_b = fuente.render(str(opcion_b), True, COLOR_BLANCO)
                        texto_opcion_c = fuente.render(str(opcion_c), True, COLOR_BLANCO)
                        texto_mensaje_final_1 = fuente.render(str(mensaje_final_1), True, COLOR_ROJO)
                        texto_mensaje_final_2 = fuente.render(str(mensaje_final_2), True, COLOR_ROJO)
                        texto_puntuacion = fuente.render(str(puntuacion), True, COLOR_NEGRO)
                        texto_cantidad_puntuacion = fuente.render(str(acumulador_puntuacion), True, COLOR_NEGRO)
                        texto_puntuacion_final = fuente.render(str(puntuacion_final), True, COLOR_ROJO)
                            
                        
                        if indice < len(lista_preguntas) - 1:
                            indice += 1
                        else:
                            indice = 0
                        
                        bandera_click_a = False
                        bandera_click_b = False                        
                        bandera_click_c = False

                        chances = 0
                    
                    elif contador_preguntas == 18:
                        pregunta = ""
                        opcion_a = ""
                        opcion_b = ""
                        opcion_c = ""
                        texto_pregunta = fuente.render(str(pregunta), True, COLOR_NEGRO)
                        texto_opcion_a = fuente.render(str(opcion_a), True, COLOR_BLANCO)
                        texto_opcion_b = fuente.render(str(opcion_b), True, COLOR_BLANCO)                        
                        texto_opcion_c = fuente.render(str(opcion_c), True, COLOR_BLANCO)
                        mensaje_final_1 = "Gracias por jugar"
                        mensaje_final_2 = "PREGUNTADOS"
                        puntuacion_final = f"Puntuación final: {acumulador_puntuacion}"
                        texto_mensaje_final_1 = fuente_puntuacion.render(str(mensaje_final_1), True, COLOR_ROJO)
                        texto_mensaje_final_2 = fuente_puntuacion.render(str(mensaje_final_2), True, COLOR_ROJO)
                        texto_puntuacion_final = fuente_puntuacion.render(str(puntuacion_final), True, COLOR_ROJO)
                        puntuacion = ""
                        acumulador_puntuacion = ""
                        texto_puntuacion = fuente.render(str(puntuacion), True, COLOR_NEGRO)
                        texto_cantidad_puntuacion = fuente.render(str(acumulador_puntuacion), True, COLOR_NEGRO)
                        acumulador_puntuacion = 0
                        contador_preguntas = 0
                        sonido_final.play()
                    
                    indice_opcion_correcta = indice - 1
                    
                
                
            #boton reiniciar
            if posicion_click[0]>705 and posicion_click[0]<895 and posicion_click[1]>95 and posicion_click[1]<145:
                
                indice = 0
                acumulador_puntuacion = 0
                contador_preguntas = 0
                bandera_click_a = False
                bandera_click_b = False
                bandera_click_c = False
                
                pregunta = lista_preguntas[indice]
                opcion_a = lista_opcion_a[indice]
                opcion_b = lista_opcion_b[indice]
                opcion_c = lista_opcion_c[indice]
                mensaje_final_1 = ""
                mensaje_final_2 = ""
                puntuacion_final = ""
                
                texto_pregunta = fuente.render(str(pregunta), True, COLOR_NEGRO)
                texto_opcion_a = fuente.render(str(opcion_a), True, COLOR_BLANCO)
                texto_opcion_b = fuente.render(str(opcion_b), True, COLOR_BLANCO)
                texto_opcion_c = fuente.render(str(opcion_c), True, COLOR_BLANCO)
                texto_puntuacion = fuente.render(str(puntuacion), True, COLOR_NEGRO)
                texto_cantidad_puntuacion = fuente.render(str(acumulador_puntuacion), True, COLOR_NEGRO)
                texto_mensaje_final_1 = fuente_puntuacion.render(str(mensaje_final_1), True, COLOR_ROJO)
                texto_mensaje_final_2 = fuente_puntuacion.render(str(mensaje_final_2), True, COLOR_ROJO)
                texto_puntuacion_final = fuente_puntuacion.render(str(puntuacion_final), True, COLOR_ROJO)
                reiniciado = True
            
            if reiniciado == True:
                indice_opcion_correcta = indice
            
            #tocar opciones
            if opcion_correcta[indice_opcion_correcta] == "a":
                if posicion_click[0]>170 and posicion_click[0]<365 and posicion_click[1]>400 and posicion_click[1]<440 and bandera_click_a == False:
                    acumulador_puntuacion = acumulador_puntuacion + 10
                    bandera_click_a = True
                    texto_cantidad_puntuacion = fuente.render(str(acumulador_puntuacion), True, COLOR_NEGRO)
                    pregunta = ""
                    opcion_a = ""
                    opcion_b = ""
                    opcion_c = ""
                    texto_pregunta = fuente.render(str(pregunta), True, COLOR_NEGRO)
                    texto_opcion_a = fuente.render(str(opcion_a), True, COLOR_BLANCO)
                    texto_opcion_b = fuente.render(str(opcion_b), True, COLOR_BLANCO)                        
                    texto_opcion_c = fuente.render(str(opcion_c), True, COLOR_BLANCO)
                    sonido_error.stop()
                    sonido_opcion_correcta.play()
                elif posicion_click[0]>410 and posicion_click[0]<585 and posicion_click[1]>400 and posicion_click[1]<440 and bandera_click_b == False:
                    sonido_error.stop()
                    sonido_error.play()
                    bandera_click_b = True
                    chances += 1
                    opcion_b = ""
                    texto_opcion_b = fuente.render(str(opcion_b), True, COLOR_BLANCO)
                elif posicion_click[0]>650 and posicion_click[0]<895 and posicion_click[1]>400 and posicion_click[1]<440 and bandera_click_c == False:
                    sonido_error.stop()
                    sonido_error.play()
                    bandera_click_c = True
                    chances += 1
                    opcion_c = ""
                    texto_opcion_c = fuente.render(str(opcion_c), True, COLOR_BLANCO)
                if chances == 2:
                    pregunta = ""
                    opcion_a = ""
                    opcion_b = ""
                    opcion_c = ""
                    texto_pregunta = fuente.render(str(pregunta), True, COLOR_NEGRO)
                    texto_opcion_a = fuente.render(str(opcion_a), True, COLOR_BLANCO)
                    texto_opcion_b = fuente.render(str(opcion_b), True, COLOR_BLANCO)
                    texto_opcion_c = fuente.render(str(opcion_c), True, COLOR_BLANCO)
                    chances = 0
                    bandera_click_a = True
                    bandera_click_b = True
                    bandera_click_c = True
            elif opcion_correcta[indice_opcion_correcta] == "b":
                if posicion_click[0]>410 and posicion_click[0]<585 and posicion_click[1]>400 and posicion_click[1]<440 and bandera_click_b == False:
                    acumulador_puntuacion += 10
                    bandera_click_b = True
                    texto_cantidad_puntuacion = fuente.render(str(acumulador_puntuacion), True, COLOR_NEGRO)
                    pregunta = ""
                    opcion_a = ""
                    opcion_b = ""
                    opcion_c = ""
                    texto_pregunta = fuente.render(str(pregunta), True, COLOR_NEGRO)
                    texto_opcion_a = fuente.render(str(opcion_a), True, COLOR_BLANCO)
                    texto_opcion_b = fuente.render(str(opcion_b), True, COLOR_BLANCO)
                    texto_opcion_c = fuente.render(str(opcion_c), True, COLOR_BLANCO)
                    sonido_error.stop()
                    sonido_opcion_correcta.play() 
                elif posicion_click[0]>170 and posicion_click[0]<365 and posicion_click[1]>400 and posicion_click[1]<440 and bandera_click_a == False:
                    sonido_error.stop()
                    sonido_error.play()
                    bandera_click_a = True
                    chances += 1
                    opcion_a = ""
                    texto_opcion_a = fuente.render(str(opcion_a), True, COLOR_BLANCO)
                elif posicion_click[0]>650 and posicion_click[0]<895 and posicion_click[1]>400 and posicion_click[1]<440 and bandera_click_c == False:
                    sonido_error.stop()
                    sonido_error.play()
                    bandera_click_c = True
                    chances += 1
                    opcion_c = ""
                    texto_opcion_c = fuente.render(str(opcion_c), True, COLOR_BLANCO)
                if chances == 2:
                    pregunta = ""
                    opcion_a = ""
                    opcion_b = ""
                    opcion_c = ""
                    texto_pregunta = fuente.render(str(pregunta), True, COLOR_NEGRO)
                    texto_opcion_a = fuente.render(str(opcion_a), True, COLOR_BLANCO)
                    texto_opcion_b = fuente.render(str(opcion_b), True, COLOR_BLANCO)
                    texto_opcion_c = fuente.render(str(opcion_c), True, COLOR_BLANCO)
                    chances = 0
                    bandera_click_a = True
                    bandera_click_b = True
                    bandera_click_c = True
                    
            elif opcion_correcta[indice_opcion_correcta]  == "c":
                if posicion_click[0]>650 and posicion_click[0]<895 and posicion_click[1]>400 and posicion_click[1]<440 and bandera_click_c == False:
                    acumulador_puntuacion += 10
                    bandera_click_c = True
                    texto_cantidad_puntuacion = fuente.render(str(acumulador_puntuacion), True, COLOR_NEGRO)
                    pregunta = ""
                    opcion_a = ""
                    opcion_b = ""
                    opcion_c = ""
                    texto_pregunta = fuente.render(str(pregunta), True, COLOR_NEGRO)
                    texto_opcion_a = fuente.render(str(opcion_a), True, COLOR_BLANCO)
                    texto_opcion_b = fuente.render(str(opcion_b), True, COLOR_BLANCO)
                    texto_opcion_c = fuente.render(str(opcion_c), True, COLOR_BLANCO)
                    sonido_error.stop()
                    sonido_opcion_correcta.play()
                elif posicion_click[0]>170 and posicion_click[0]<365 and posicion_click[1]>400 and posicion_click[1]<440 and bandera_click_a == False:
                    sonido_error.stop()
                    sonido_error.play()
                    bandera_click_a = True
                    chances += 1
                    opcion_a = ""
                    texto_opcion_a = fuente.render(str(opcion_a), True, COLOR_BLANCO)
                elif posicion_click[0]>410 and posicion_click[0]<585 and posicion_click[1]>400 and posicion_click[1]<440 and bandera_click_b == False:
                    sonido_error.stop()
                    sonido_error.play()
                    bandera_click_b = True
                    chances += 1
                    opcion_b = ""
                    texto_opcion_b = fuente.render(str(opcion_b), True, COLOR_BLANCO)
                if chances == 2:
                    pregunta = ""
                    opcion_a = ""
                    opcion_b = ""
                    opcion_c = ""
                    texto_pregunta = fuente.render(str(pregunta), True, COLOR_NEGRO)
                    texto_opcion_a = fuente.render(str(opcion_a), True, COLOR_BLANCO)
                    texto_opcion_b = fuente.render(str(opcion_b), True, COLOR_BLANCO)
                    texto_opcion_c = fuente.render(str(opcion_c), True, COLOR_BLANCO)
                    chances = 0
                    bandera_click_a = True
                    bandera_click_b = True
                    bandera_click_c = True
    
    pantalla.fill(COLOR_VERDE_OSCURO)#Le da un color al fondo
    pantalla.blit(imagen,(400,20))#Funde la imagen en la superficie de la pantalla
    
    #recuadro y texto del boton pregunta
    pygame.draw.rect(pantalla, COLOR_NEGRO, (100,90,200,60))
    pygame.draw.rect(pantalla, COLOR_VERDE, (105,95,190,50))
    pantalla.blit(texto_boton_pregunta, (120,100))
    
    #recuadro y texto del boton reiniciar
    pygame.draw.rect(pantalla, COLOR_NEGRO, (700,90,200,60))
    pygame.draw.rect(pantalla, COLOR_VERDE, (705,95,190,50))
    pantalla.blit(texto_boton_reiniciar, (727,100))
    
    #texto pregunta
    pantalla.blit(texto_pregunta, (100,250))
    
    #texto opciones
    pantalla.blit(texto_opcion_a, (180,400))
    pantalla.blit(texto_opcion_b, (420,400))
    pantalla.blit(texto_opcion_c, (660,400))
    
    #texto puntuacion
    pantalla.blit(texto_puntuacion, (10,750))
    pantalla.blit(texto_cantidad_puntuacion, (215,750))
    
    #texto final del juego
    pantalla.blit(texto_mensaje_final_1,(290,250))
    pantalla.blit(texto_mensaje_final_2,(290,310))
    pantalla.blit(texto_puntuacion_final,(260,400))
    
    pygame.display.flip()#actualiza la pantalla, siempre va al final



pygame.quit()
