import pygame

class Player(pygame.sprite.Sprite):
  def __init__(self,pos):
    super().__init__()
    self.image = pygame.Surface((32,64))
    self.image.fill('red')
    self.rect = self.image.get_rect(topleft=pos)
    #Player move
    self.direction = pygame.math.Vector2(0,0)
    self.speed = 8

  def get_input(self):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
      self.direction.x = 1
      self.facing_rigth = True
    elif keys[pygame.K_a]:
      self.direction.x = -1
      self.facing_rigth = False
    elif keys[pygame.K_w]:
      self.direction.y = -1
      self.facinf_up = True
    elif keys[pygame.K_s]:
      self.direction.y = 1
      self.facinf_up = False
    else:
      self.direction.x = 0
      self.direction.y = 0

  def update(self):
    self.get_input()
    self.rect.move_ip(self.direction)