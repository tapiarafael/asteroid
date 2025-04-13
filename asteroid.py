import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
  def __init__(self, x, y, radius):
    super().__init__(x, y, radius)

  def draw(self, screen):
    pygame.draw.circle(screen, "white", self.position, self.radius, width=2)
  
  def update(self, dt):
    self.position += self.velocity * dt

  def split(self):
    VELOCITY_INCREASE = 1.2
    self.kill()

    if self.radius <= ASTEROID_MIN_RADIUS:
      return

    angle = random.uniform(20, 50)
    vector1 = self.velocity.rotate(angle)
    vector2 = self.velocity.rotate(-angle)
    radius = self.radius - ASTEROID_MIN_RADIUS

    asteroid1 = Asteroid(self.position.x, self.position.y, radius)
    asteroid2 = Asteroid(self.position.x, self.position.y, radius)
    asteroid1.velocity = vector1 * VELOCITY_INCREASE
    asteroid2.velocity = vector2 * VELOCITY_INCREASE

