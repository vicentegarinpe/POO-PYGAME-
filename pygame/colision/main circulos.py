import pygame
from pygame.colision.circle import Circle  # Importar la clase Circle desde el archivo circle.py

# Inicialización de Pygame
pygame.init()

# Dimensiones de la ventana
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Círculos ")

# Colores
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Función principal del juego
def main():
    # Crear los círculos
    circle1 = Circle(100, 200, 30, BLUE)
    circle2 = Circle(300, 200, 30, GREEN)

    speed = 5  # Velocidad de movimiento

    # Bucle principal
    running = True
    while running:
        screen.fill(WHITE)

        # Dibujar los círculos
        circle1.draw(screen)
        circle2.draw(screen)

        # Detección de colisiones
        if circle1.detect_collision(circle2):
            circle1.color = RED
            circle2.color = RED
        else:
            circle1.reset_color()
            circle2.reset_color()

        # Eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Control del movimiento del círculo 1
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            circle1.move(0, -speed)
        if keys[pygame.K_s]:
            circle1.move(0, speed)
        if keys[pygame.K_a]:
            circle1.move(-speed, 0) 
        if keys[pygame.K_d]:
            circle1.move(speed, 0)

        # Control del movimiento del círculo 2
        if keys[pygame.K_UP]:
            circle2.move(0, -speed)
        if keys[pygame.K_DOWN]:
            circle2.move(0, speed)
        if keys[pygame.K_LEFT]:
            circle2.move(-speed, 0)
        if keys[pygame.K_RIGHT]:
            circle2.move(speed, 0)

        pygame.display.flip()
        pygame.time.Clock().tick(60)

    pygame.quit()

# Llamada a la función principal
if __name__ == "__main__":
    main()
