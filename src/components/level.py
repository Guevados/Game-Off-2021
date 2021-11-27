import pygame
from settings import tile_size, screen_width, screen_height
from components.tiles import Tile, StaticTile
from components.player import Player
from components.support_level import import_csv_layout, import_cut_graphics

class Level:
  def __init__(self, level_data, surface):
    self.display_surface = surface
    self.world_shift_x = 0
    self.world_shift_y = 0

    #player
    player_layout = import_csv_layout(level_data['player'])
    self.player = pygame.sprite.GroupSingle()
    self.setup_player(player_layout)

    #terrain
    terrain_layout = import_csv_layout(level_data['terrain'])
    self.terrain_sprites = self.create_tile_group(terrain_layout, 'terrain')

    #limit terrain
    limit_terrain_layout = import_csv_layout(level_data['limit_terrain'])
    self.limit_terrain_sprites = self.create_tile_group(limit_terrain_layout, 'limit_terrain')

    #river
    river_layout = import_csv_layout(level_data['river'])
    self.river_sprites = self.create_tile_group(river_layout, 'river')

    #road
    road_layout = import_csv_layout(level_data['road'])
    self.road_sprites = self.create_tile_group(road_layout, 'road')

    #bridge
    bridge_layout = import_csv_layout(level_data['bridge'])
    self.bridge_sprites = self.create_tile_group(bridge_layout, 'bridge')

    #details bridge
    details_bridge_layout = import_csv_layout(level_data['details_bridge'])
    self.details_bridge_sprites = self.create_tile_group(details_bridge_layout, 'details_bridge')

    #buildings
    buildings_layout = import_csv_layout(level_data['buildings'])
    self.buildings_sprites = self.create_tile_group(buildings_layout, 'buildings')

    #vegatation1
    vegetation1_layout = import_csv_layout(level_data['vegetation1'])
    self.vegetation1_sprites = self.create_tile_group(vegetation1_layout, 'vegetation1')

    #vegatation2
    vegetation2_layout = import_csv_layout(level_data['vegetation2'])
    self.vegetation2_sprites = self.create_tile_group(vegetation2_layout, 'vegetation2')

    #vegatation3
    vegetation3_layout = import_csv_layout(level_data['vegetation3'])
    self.vegetation3_sprites = self.create_tile_group(vegetation3_layout, 'vegetation3')

    #vegatation4
    vegetation4_layout = import_csv_layout(level_data['vegetation4'])
    self.vegetation4_sprites = self.create_tile_group(vegetation4_layout, 'vegetation4')



  def create_tile_group(self, layout, type):
    sprite_group = pygame.sprite.Group()

    for row_index,row in enumerate(layout):
      for col_index, val in enumerate(row):
        if val != '-1':
          x = col_index * tile_size
          y = row_index * tile_size

          if type == 'terrain':
            terrain_tile_list = import_cut_graphics('src/assets/tiles/terrain/world_terrain.png')
            tile_surface = terrain_tile_list[int(val)]
            sprite = StaticTile(tile_size,x,y,tile_surface)

          if type == 'limit_terrain':
            limit_terrain_tile_list = import_cut_graphics('src/assets/tiles/terrain/world_terrain.png')
            tile_surface = limit_terrain_tile_list[int(val)]
            sprite = StaticTile(tile_size,x,y,tile_surface)

          if type == 'river':
            river_tile_list = import_cut_graphics('src/assets/tiles/terrain/world_terrain.png')
            tile_surface = river_tile_list[int(val)]
            sprite = StaticTile(tile_size,x,y,tile_surface)

          if type == 'road':
            road_tile_list = import_cut_graphics('src/assets/tiles/terrain/world_terrain.png')
            tile_surface = road_tile_list[int(val)]
            sprite = StaticTile(tile_size,x,y,tile_surface)

          if type == 'vegetation1':
            if val == '4': sprite = StaticTile(tile_size,x,y,pygame.image.load('src/assets/tiles/tree/tree1.png'))

          if type == 'vegetation2':
            if val == '5': sprite = StaticTile(tile_size,x,y,pygame.image.load('src/assets/tiles/tree/tree2.png'))

          if type == 'vegetation3':
            if val == '6': sprite = StaticTile(tile_size,x,y,pygame.image.load('src/assets/tiles/tree/tree3.png'))

          if type == 'vegetation4':
            if val == '7': sprite = StaticTile(tile_size,x,y,pygame.image.load('src/assets/tiles/tree/tree4.png'))

          if type == 'buildings':
            if val == '4046': sprite = StaticTile(tile_size,x,y,pygame.image.load('src/assets/tiles/buildings/buildings1.png'))
            if val == '4047': sprite = StaticTile(tile_size,x,y,pygame.image.load('src/assets/tiles/buildings/buildings2.png'))

          if type == 'bridge':
            if val == '2': sprite = StaticTile(tile_size,x,y,pygame.image.load('src/assets/tiles/bridge/bridge.png'))

          if type == 'details_bridge':
            if val == '3': sprite = StaticTile(tile_size,x,y,pygame.image.load('src/assets/tiles/bridge/details_bridge.png'))

          sprite_group.add(sprite)

    return sprite_group

  def setup_player(self,layout):
    for row_index,row in enumerate(layout):
      for col_index,val in enumerate(row):
        x = col_index * tile_size
        y = row_index * tile_size
        if val == '0':
          sprite = Player((x,y),self.display_surface)
          self.player.add(sprite)

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
    #terrain
    self.terrain_sprites.draw(self.display_surface)
    self.terrain_sprites.update(self.world_shift_x,self.world_shift_y)

    #limit_terrain
    self.limit_terrain_sprites.draw(self.display_surface)
    self.limit_terrain_sprites.update(self.world_shift_x,self.world_shift_y)

    #river
    self.river_sprites.draw(self.display_surface)
    self.river_sprites.update(self.world_shift_x,self.world_shift_y)

    #road
    self.road_sprites.draw(self.display_surface)
    self.road_sprites.update(self.world_shift_x,self.world_shift_y)

    #vegetation1
    self.vegetation1_sprites.draw(self.display_surface)
    self.vegetation1_sprites.update(self.world_shift_x,self.world_shift_y)

    #vegetation2
    self.vegetation2_sprites.draw(self.display_surface)
    self.vegetation2_sprites.update(self.world_shift_x,self.world_shift_y)

    #vegetation3
    self.vegetation3_sprites.draw(self.display_surface)
    self.vegetation3_sprites.update(self.world_shift_x,self.world_shift_y)

    #vegetation4
    self.vegetation4_sprites.draw(self.display_surface)
    self.vegetation4_sprites.update(self.world_shift_x,self.world_shift_y)

    #buildings
    self.buildings_sprites.draw(self.display_surface)
    self.buildings_sprites.update(self.world_shift_x,self.world_shift_y)

    #bridge
    self.bridge_sprites.draw(self.display_surface)
    self.bridge_sprites.update(self.world_shift_x,self.world_shift_y)

    #detail_bridge
    self.details_bridge_sprites.draw(self.display_surface)
    self.details_bridge_sprites.update(self.world_shift_x,self.world_shift_y)

    #player
    self.player.update()
    self.player.draw(self.display_surface)

    self.scroll_world()

    self.horizontal_movement_collision()
    self.vertical_movement_collision()