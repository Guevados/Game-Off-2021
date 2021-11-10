import pygame
from settings import tile_size, screen_width, screen_height
from components.tiles import Tile
from components.player import Player

class Level:
  def __init__(self,level_data,surface):
    self.display_surface = surface
    self.world_shift_x = self.direction_x = 0
    self.world_shift_y = self.direction_y = 0
    self.setup_level(level_data)

  def setup_level(self,layout):
    self.tiles = pygame.sprite.Group()
    self.player = pygame.sprite.GroupSingle()
    for row_index,row in enumerate(layout):
      for col_index,cell in enumerate(row):
        x = col_index * tile_size
        y = row_index * tile_size
        if cell == 'X':
          tile=Tile((x,y),tile_size)
          self.tiles.add(tile)
        if cell == 'P':
          player_sprite = Player((x,y))
          self.player.add(player_sprite)

  def scroll_x(self):
    player = self.player.sprite
    player_x = player.rect.centerx
    direction_x = player.direction.x
    player_y = player.rect.centery
    direction_y = player.direction.y

    # Hacia izquierda
    if player_x < screen_width/4 and direction_x < 0:
      self.world_shift_x = 8
      player.speed = 0
    elif player_x > screen_width-(screen_width/4) and direction_x > 0:
      self.world_shift_x = -8
      player.speed = 0
    elif player_y < screen_height/4 and direction_y < 0:
      self.world_shift_y = 8
      player.speed = 0
    elif player_y > screen_height-(screen_height/4) and direction_y > 0:
      self.world_shift_y = -8
      player.speed = 0
    else:
      self.world_shift_x = 0
      self.world_shift_y = 0
      player.speed = 8

  def run(self):
    #level tiles
    self.tiles.update(self.world_shift_x,self.world_shift_y)
    self.tiles.draw(self.display_surface)
    #player
    self.player.update()
    self.player.draw(self.display_surface)
    self.scroll_x()
