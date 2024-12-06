import pygame

class Rectangulo:
    def __init__(self, x, y, ancho, alto):
        self.x = x
        self.y = y
        self.ancho = ancho
        self.alto = alto
        self.velocidad = 0.05  # Velocidad de movimiento en píxeles
        self.color = (219, 148, 255)  # Color del rectángulo

    def dibujar(self, ventana):
        # Dibujar el rectángulo
        pygame.draw.rect(ventana, self.color, (self.x, self.y, self.ancho, self.alto))

    # Movimiento del rectángulo según las teclas presionadas
    def mover(self, teclas):
        if teclas[pygame.K_LEFT]:
            self.x -= self.velocidad
        if teclas[pygame.K_RIGHT]:
            self.x += self.velocidad
        if teclas[pygame.K_UP]:
            self.y -= self.velocidad
        if teclas[pygame.K_DOWN]:
            self.y += self.velocidad

# Inicializar Pygame
pygame.init()
ventana = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Movimiento de Rectángulo")

# Crear un objeto Rectángulo
rectangulo = Rectangulo(400, 300, 100, 50)  # x, y, ancho, alto

# Bucle principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            break  # Salir del bucle si se cierra la ventana

    # Limpiar la pantalla
    ventana.fill((0, 0, 0))  # Color de fondo negro

    # Obtener el estado de las teclas
    teclas = pygame.key.get_pressed()
    
    # Mover el rectángulo
    rectangulo.mover(teclas)

    # Dibujar el rectángulo
    rectangulo.dibujar(ventana)

    # Actualizar la pantalla
    pygame.display.flip()
