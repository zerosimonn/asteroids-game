import pygame
from constants import *
from circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self, x, y, velocity):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = velocity

    def circle(self):
        center = self.position
        rad = SHOT_RADIUS
        return (center, rad)

    def draw(self, screen):
        center, rad = self.circle()
        pygame.draw.circle(screen, "white", center, rad, 2)

    def update(self, dt):
        self.position += self.velocity * dt
