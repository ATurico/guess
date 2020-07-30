import pygame
from ship import *
from asteroid import *

pygame.init()
screen_info = pygame.display.Info()
print(screen_info)
size = (width, height) = (screen_info.current_w, screen_info.current_h)
screen = pygame.display.set_mode(size)
clock =  pygame.time.Clock()
color = (0, 10, 30)

Numlevels = 4
Level = 1
AsteroidCount = 3
player = Ship()
danger = Asteroid()

def main():
   while Level <= Numlevels:
      clock.tick(60)
      for event in pygame.event.get():
        for event.type == pygame.KEYDOWN:
          if event.key == pygame.K_RIGHT:
            Player.speed[0] = 10
      player.update()
      screen.fill(color)
      screen.blit(danger.image, danger.rect)
      screen.blit(player.image, player.rect)
      pygame.display.flip()

if __name__=='__main__':
  main()