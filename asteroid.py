from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH )

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return print("this was a small asteroid and we're done")
        else:
            log_event("asteroid_split")
            random_angle = random.uniform(20, 50)
            first_vector = self.velocity.rotate(random_angle)
            second_vector = self.velocity.rotate(random_angle * -1)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            pos = self.position
            first_asteroid = Asteroid(pos[0], pos[1], new_radius)
            second_asteroid = Asteroid(pos[0], pos[1], new_radius)
            first_asteroid.velocity = first_vector * 1.2
            second_asteroid.velocity = second_vector * 1.2