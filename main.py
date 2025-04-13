import pygame
from constants import *


def main():
  print_start_info()
  pygame.init()
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  clock = pygame.time.Clock()
  dt = 0

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return
      
    screen.fill(color="black")
    pygame.display.flip()

    dt = clock.tick(60) / 1000
  
def print_start_info():
  print("Starting Asteroids!")
  print(f"Screen width: {SCREEN_WIDTH}")
  print(f"Screen height`: {SCREEN_HEIGHT}")
  

if __name__ == "__main__":
  main()