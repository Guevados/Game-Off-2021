import os
import pygame

from libs.sprite_sheets import SpriteSheet

class Building(pygame.sprite.Sprite):
  def __init__(self, pos, type):
    super().__init__()

    filename = os.path.join('src', 'assets','buildings.png')
    sprites = SpriteSheet(filename)
    ALPHA = (0, 255, 0)

    buildings = {
      1: (10, 5, 170, 120),
      2: (180, 5, 170, 140),
      3: (10, 133, 170, 140),
    }

    img = sprites.image_at(buildings[type], ALPHA)

    pygame.sprite.Sprite.__init__(self)
    self.images = [img]

    self.index = 0
    self.image = self.images[self.index]
    self.rect = self.image.get_rect(topleft=pos)
    self.direction = pygame.math.Vector2(0,0)
    self.speed = 8

  def update(self, x_shift, y_shift):
    self.rect.x += x_shift
    self.rect.y += y_shift
