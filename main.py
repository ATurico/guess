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

player = Ship()
danger = Asteroid()

def main():
   while 1>0:
      clock.tick(60)
      player.update()
      screen.fill(color)
      screen.blit(danger.image, danger.rect)
      screen.blit(player.image, player.rect)
      pygame.display.flip()

if __name__=='__main__':
  main()