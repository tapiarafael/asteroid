import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
  print_start_info()
  pygame.init()
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  clock = pygame.time.Clock()
  dt = 0

  updatable, drawable, asteroids, shoots = pygame.sprite.Group(), pygame.sprite.Group(), pygame.sprite.Group(), pygame.sprite.Group()
  Player.containers = (updatable, drawable)
  Asteroid.containers = (updatable, drawable, asteroids)
  Shot.containers = (shoots, drawable, updatable)
  AsteroidField.containers = (updatable,)
  
  field = AsteroidField()
  player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

  while True:
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
      print("Player closed the game")
      sys.exit(0)

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return
      
    screen.fill(color="black")
    for sprite in drawable:
      sprite.draw(screen)

    updatable.update(dt)
    check_asteroid_colisions(asteroids, player)
    check_bullets_colision(shoots, asteroids)

    pygame.display.flip()
    dt = clock.tick(60) / 1000

def check_asteroid_colisions(asteroids, player):
    for asteroid in asteroids:
      if asteroid.colide(player):
        print("Game Over!")
        sys.exit(0)

def check_bullets_colision(shoots, asteriods):
  for asteroid in asteriods:
    for shoot in shoots:
      if shoot.colide(asteroid):
        asteroid.kill()
        shoot.kill()

def print_start_info():
  print("Starting Asteroids!")
  print(f"Screen width: {SCREEN_WIDTH}")
  print(f"Screen height: {SCREEN_HEIGHT}")
  

if __name__ == "__main__":
  main()