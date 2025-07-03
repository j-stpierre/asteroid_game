import pygame
from constants import SHOT_RADIUS
from circleshape import CircleShape


class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        pygame.draw.circle(
            surface=screen,
            radius=self.radius,
            width=2,
            center=self.position,
            color="white",
        )

    def update(self, dt):
        self.position += self.velocity * dt
