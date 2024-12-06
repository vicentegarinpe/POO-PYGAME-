import pygame

class Circle:
    def __init__(self, x, y, radius, color):
        self.pos = [x, y]
        self.radius = radius
        self.color = color
        self.default_color = color
        self.speed = [0, 0]
    
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.pos, self.radius)
    
    def move(self, dx, dy):
        self.pos[0] += dx
        self.pos[1] += dy

    def reset_color(self):
        self.color = self.default_color

    # Detección de colisión con otro círculo
    def detect_collision(self, other_circle):
        dx = self.pos[0] - other_circle.pos[0]
        dy = self.pos[1] - other_circle.pos[1]
        distance_squared = dx * dx + dy * dy
        radius_sum = self.radius + other_circle.radius
        return distance_squared < radius_sum * radius_sum
