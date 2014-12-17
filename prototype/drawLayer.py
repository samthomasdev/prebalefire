# Author: Sam Thomas





'''

class DrawLayer:
	def __init__(self):
		self.tiles = None

	def draw(renderer):
		
'''

class TiledMapLayer():
	def __init__(self, spritesheet, tiles):
		self.spritesheet = spritesheet
		self.tiles = tiles


	def draw(self, renderer, panOffset=[0,0], zoom=0, zoomOffset=[0,0]):
		listWidth = len(self.tiles)
		listHeight = len(self.tiles[0])
		for x in xrange(0, listWidth):
			for y in xrange(0, listHeight):
				source = self.tiles[x][y].source
				dst = self.tiles[x][y].destination
				
				destination =  (dst[0] + x*zoom + panOffset[0] - zoomOffset[0],
						dst[1] + y*zoom + panOffset[1] - zoomOffset[1],
						dst[2] + zoom,
						dst[3] + zoom)
				renderer.copy(self.spritesheet, source, destination)




'''

class DecoratorLayer():
	def __init__(self):
		x=0

	def draw(renderer):




class EntityLayer():
	def __init__(self):
		x=0

	def draw(renderer):



'''












