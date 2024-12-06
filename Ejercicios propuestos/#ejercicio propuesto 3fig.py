#ejercicio propuesto de mas de una figura
import pygame

# Inicializar Pygame
pygame.init()

# Configuraciones de la ventana
ancho, alto = 800, 600
ventana = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("ejercicio de fig ")

# Clase para el triángulo
class Triangulo:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocidad = 0.5
        self.color = (219, 148, 255)

    def dibujar(self, ventana):
        puntos = [(self.x, self.y), (self.x - 50, self.y + 100), (self.x + 50, self.y + 100)]
        pygame.draw.polygon(ventana, self.color, puntos)

    def mover(self, teclas):
        if teclas[pygame.K_LEFT]:
            self.x -= self.velocidad
        if teclas[pygame.K_RIGHT]:
            self.x += self.velocidad
        if teclas[pygame.K_UP]:
            self.y -= self.velocidad
        if teclas[pygame.K_DOWN]:
            self.y += self.velocidad

# Clase para el círculo
class Circulo:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocidad = 0.5
        self.color = (255, 0, 0)
        self.radio = 50

    def dibujar(self, ventana):
        pygame.draw.circle(ventana, self.color, (int(self.x), int(self.y)), self.radio)

    def mover(self, teclas):
        if teclas[pygame.K_a]:
            self.x -= self.velocidad
        if teclas[pygame.K_d]:
            self.x += self.velocidad
        if teclas[pygame.K_w]:
            self.y -= self.velocidad
        if teclas[pygame.K_s]:
            self.y += self.velocidad

# Class del cuadrado
class Cuadrado:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocidad = 0.5
        self.color = (0, 255, 0)
        self.tamano = 100

    def dibujar(self, ventana):
        pygame.draw.rect(ventana, self.color, (self.x - self.tamano // 2, self.y - self.tamano // 2, self.tamano, self.tamano))

    def mover(self, teclas):
        if teclas[pygame.K_j]:
            self.x -= self.velocidad
        if teclas[pygame.K_l]:
            self.x += self.velocidad
        if teclas[pygame.K_i]:
            self.y -= self.velocidad
        if teclas[pygame.K_k]:
            self.y += self.velocidad

# Idimensiones de las  figuras
triangulo = Triangulo(400, 300)
circulo = Circulo(200, 300)
cuadrado = Cuadrado(600, 300)

# Bucle principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    teclas = pygame.key.get_pressed()
    
    # Mover figuras
    triangulo.mover(teclas)
    circulo.mover(teclas)
    cuadrado.mover(teclas)

    # Dibujar
    ventana.fill((0, 0, 2))  # Fondo
    triangulo.dibujar(ventana)
    circulo.dibujar(ventana)
    cuadrado.dibujar(ventana)

    pygame.display.flip()
    

pygame.quit()
