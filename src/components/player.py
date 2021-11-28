import os
import pygame
from libs.sprite_sheets import SpriteSheet
class Player(pygame.sprite.Sprite):
  def __init__(self, pos):
    super().__init__()

    filename = os.path.join('src','assets','player-sheet.png')
    sprites = SpriteSheet(filename)
    ALPHA = (255, 255, 255)
    img_front_1 = sprites.image_at((10, 5, 27, 44), ALPHA)
    img_front_2 = sprites.image_at((57, 5, 29, 44), ALPHA)
    img_front_3 = sprites.image_at((107, 5, 28, 44), ALPHA)

    img_right_1 = sprites.image_at((10, 53, 27, 44), ALPHA)
    img_right_2 = sprites.image_at((57, 53, 29, 44), ALPHA)
    img_right_3 = sprites.image_at((107, 53, 28, 44), ALPHA)

    img_left_1 = sprites.image_at((10, 102, 27, 44), ALPHA)
    img_left_2 = sprites.image_at((57, 102, 29, 44), ALPHA)
    img_left_3 = sprites.image_at((107, 102, 28, 44), ALPHA)

    img_back_1 = sprites.image_at((10, 149, 27, 44), ALPHA)
    img_back_2 = sprites.image_at((57, 149, 29, 44), ALPHA)
    img_back_3 = sprites.image_at((107, 149, 28, 44), ALPHA)

    pygame.sprite.Sprite.__init__(self)
    self.images = {
      'front': [img_front_1, img_front_2, img_front_3],
      'right': [img_right_1, img_right_2, img_right_3],
      'left': [img_left_1, img_left_2, img_left_3],
      'back': [img_back_1, img_back_2, img_back_3],
    }

    self.index = 0
    self.image = self.images['front'][self.index]
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

  def animate(self):
    self.index += 1
    if(self.index >= len(self.images['front'])):
      self.index = 0

    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
      self.image = self.images['left'][self.index]
    elif keys[pygame.K_a]:
      self.image = self.images['right'][self.index]
    elif keys[pygame.K_w]:
      self.image = self.images['back'][self.index]
    elif keys[pygame.K_s]:
      self.image = self.images['front'][self.index]
    else:
      pass

  def update(self):
    self.get_input()
    self.animate()
