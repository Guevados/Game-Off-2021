import pygame
from settings import tile_size, screen_width, screen_height
from components.tiles import Tile
from components.player import Player
from components.building import Building

class Level:
  def __init__(self,level_data,surface):
    self.display_surface = surface
    self.world_shift_x = self.direction_x = 0
    self.world_shift_y = self.direction_y = 0
    self.setup_level(level_data)

  def setup_level(self,layout):
    self.tiles = pygame.sprite.Group()
    self.player = pygame.sprite.GroupSingle()
    self.buildings = pygame.sprite.Group()

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
        if self.is_number(cell):
          building_sprite = Building((x,y), float(cell))
          self.buildings.add(building_sprite)

  def is_number(self,s):
    try:
      float(s)
      return True
    except ValueError:
      return False

  def scroll_world(self):
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

  def horizontal_movement_collision(self):
    player = self.player.sprite
    player.rect.x += player.direction.x * player.speed

    for sprite in self.tiles.sprites():
      if player.rect.colliderect(sprite.rect):
        if player.direction.x > 0:
          player.rect.right = sprite.rect.left
        elif player.direction.x < 0:
          player.rect.left = sprite.rect.right

  def vertical_movement_collision(self):
    player = self.player.sprite
    player.rect.y += player.direction.y * player.speed

    for sprite in self.tiles.sprites():
      if player.rect.colliderect(sprite.rect):
        if player.direction.y > 0:
          player.rect.bottom = sprite.rect.top
        elif player.direction.y < 0:
          player.rect.top = sprite.rect.bottom


  def run(self):
    #level tiles
    self.tiles.update(self.world_shift_x,self.world_shift_y)
    self.tiles.draw(self.display_surface)
    self.scroll_world()
    #buildings
    self.buildings.update(self.world_shift_x,self.world_shift_y)
    self.buildings.draw(self.display_surface)
    #player
    self.player.update()
    self.player.draw(self.display_surface)
    self.horizontal_movement_collision()
    self.vertical_movement_collision()
