import pygame
import math

# Inicializar Pygame
pygame.init()

# Configurar la pantalla
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Detección de Colisiones Circulares")

# Definir colores
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Configurar círculos
circle1_pos = [150, 200]
circle2_pos = [450, 200]
circle_radius = 40
circle1_color = BLUE
circle2_color = RED
speed = 5

# Función para detectar colisión entre círculos
def detect_collision(pos1, pos2, radius):
    distance = math.sqrt((pos2[0] - pos1[0])**2 + (pos2[1] - pos1[1])**2)
    return distance < 2 * radius

# Función para evitar superposición
def resolve_collision(pos1, pos2, radius):
    distance = math.sqrt((pos2[0] - pos1[0])**2 + (pos2[1] - pos1[1])**2)
    if distance == 0:  # Evitar división por cero
        return
    overlap = 2 * radius - distance
    # Calcular la dirección de separación
    dx = (pos2[0] - pos1[0]) / distance
    dy = (pos2[1] - pos1[1]) / distance
    # Mover los círculos para que no se superpongan
    pos1[0] -= dx * overlap / 2
    pos1[1] -= dy * overlap / 2
    pos2[0] += dx * overlap / 2
    pos2[1] += dy * overlap / 2

# Ciclo principal del juego
running = True
while running:
    screen.fill(WHITE)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Controles de movimiento para el círculo 1
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:  # Mover a la izquierda
        circle1_pos[0] -= speed
    if keys[pygame.K_d]:  # Mover a la derecha
        circle1_pos[0] += speed
    if keys[pygame.K_w]:  # Mover hacia arriba
        circle1_pos[1] -= speed
    if keys[pygame.K_s]:  # Mover hacia abajo
        circle1_pos[1] += speed

    # Controles de movimiento para el círculo 2
    if keys[pygame.K_LEFT]:  # Mover a la izquierda
        circle2_pos[0] -= speed
    if keys[pygame.K_RIGHT]:  # Mover a la derecha
        circle2_pos[0] += speed
    if keys[pygame.K_UP]:  # Mover hacia arriba
        circle2_pos[1] -= speed
    if keys[pygame.K_DOWN]:  # Mover hacia abajo
        circle2_pos[1] += speed

    # Detectar colisión y evitar superposición
    if detect_collision(circle1_pos, circle2_pos, circle_radius):
        circle1_color = GREEN
        circle2_color = GREEN
        resolve_collision(circle1_pos, circle2_pos, circle_radius)
    else:
        circle1_color = BLUE
        circle2_color = RED

    # Dibujar círculos
    pygame.draw.circle(screen, circle1_color, circle1_pos, circle_radius)
    pygame.draw.circle(screen, circle2_color, circle2_pos, circle_radius)

    pygame.display.flip()
    pygame.time.Clock().tick(60)

# Cerrar Pygame
pygame.quit()