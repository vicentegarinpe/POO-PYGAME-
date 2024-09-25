#rectangulopequeno

import pygame

class Rectangulopequeno:
    def __init__(self,x,y,ancho,alto):
        self.x=x
        self.y=y
        self.ancho=ancho
        self.alto=alto
        self.velocidad=0.5
        self.color=(63,232,234)
        self.react= pygame.react(self.x,self.y,self.ancho,self.alto)

    def dibujar(self,ventana):
        pygame.draw.react(ventana,self.color,self.react)

    def mover(self,teclas):
        mov_x=0
        mov_y=0

        if teclas[pygame.K_LEFT]:
            mov_x=-1
        if teclas[pygame.K_RIGHT]:
            mov_x=1
        if teclas[pygame.K_UP]:
            mov_y=-1
        if teclas[pygame.K_DOWN]:
            mov_y=1
        
        self.react.x += mov_x * self.velocidad
        self.react.y += mov_y * self.velocidad 
    def restablecer_posicion(self,x,y):
        self.react.x=x
        self.react.y=y
    def obtener_posicion(self):
        return(self.react.x,self.react.y)
    def cambiar_color(self,color):
        self.color=color
        