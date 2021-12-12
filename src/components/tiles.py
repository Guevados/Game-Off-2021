import pygame

class Tile(pygame.sprite.Sprite):
	def __init__(self,size,x,y):
		super().__init__()
		self.image = pygame.Surface((size,size))
		self.rect = self.image.get_rect(topleft = (x,y))

	def update(self,x_shift,y_shift):
		self.rect.x += x_shift
		self.rect.y += y_shift

class  StaticTile(Tile):
	def __init__(self,size,x,y,surface):
		super().__init__(size,x,y)
		self.image = surface

class Load_image(StaticTile):
	def __init__(self,size,x,y,path):
		super().__init__(size,x,y,path)
		offset_y = y + size
		self.rect = self.image.get_rect(bottomleft = (x,offset_y))
