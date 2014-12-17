# Author: Sam Thomas

import sys
from collections import namedtuple
import sdl2
import sdl2.ext
from bunker import Bunker
from drawLayer import TiledMapLayer
from spritesheetCodes import FLOORCODES as FLOOR


# !HARDCODE
RESOURCES = sdl2.ext.Resources(__file__, 'assets')
spritesheets = dict(floor='ss_floor.png', character='hello.bmp')



class Camera:
	def __init__(self, zoomLevel=0, zoomIncrement=2, panOffset=[0,0], panIncrement=2):
		self.zoomLevel = zoomLevel
		self.zoomIncrement = zoomIncrement
		self.panOffset = panOffset
		self.panIncrement = panIncrement
	def __str__(self):
		s = '\nCamera State:\n'
		s += 'Pan Offset = ' + str(self.panOffset) + '\n'
		s += 'Zoom Level = ' + str(self.zoomLevel) + '\n'
		return s

	def panX(self, direction):
		self.panOffset[0] += self.panIncrement*direction
	def panY(self, direction):
		self.panOffset[1] += self.panIncrement*direction
	def zoom(self, direction):
		delta = self.zoomIncrement*direction
		self.zoomLevel += delta
		#self.zoomLevel += direction
		#self.panOffset[0] -= self.zoomLevel
		#self.panOffset[1] -= self.zoomLevel 

class Viewport:
	def __init__(self, x, y, width, height):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.center = lambda: (self.x+(self.width/2), self.y+(self.height/2))





# The visual representation for the Bunker. (assumes that floor sizes are uniform)
class BunkerView(Viewport):
	
	def __init__(self, resolution, bunker, camera=Camera()):
		Viewport.__init__(self, 0, 0, resolution[0], resolution[1])
		#super().__init__(0, 0, resolution[0], resolution[1]) #python3 only :(

		self.bunker = bunker
		self.camera = camera
		self.drawlayers = []
		self.tiles = self.gen_BunkerTileMap(self.bunker)

	def __str__(self):
		s = ''
		#width = self.bunker.width
		#height = self.bunker.floorHeight
		width = len(self.tiles)
		height = len(self.tiles[0])

		# formats the matrix of source rectangles and adds it to string s (x&y coord only)
		s += '\n' + '-floor source rectangles-' + '\n'
		for y in xrange(0,height):
			for x in xrange(0,width):
				r = self.tiles[x][y].source
				valuePair = r[:2]
				s += '{0:<10}'.format(str(valuePair))
				s +=  ' '
			s += '\n'

		# formats the matrix of destination rectangles and adds it to string s (x&y coord only)
		s += '-floor destination rectangles-' + '\n'
		for y in xrange(0,height):
			for x in xrange(0,width):
				r = self.tiles[x][y].destination
				valuePair = r[:2]
				s += '{0:<10}'.format(str(valuePair))
				s +=  ' '
			s += '\n'
		return s


	# Loads the sprite sheets.
	def loadSpritesheets(self, factory):
		ss_floor = factory.from_image(RESOURCES.get_path(spritesheets['floor']))
		tiledMapLayer = TiledMapLayer(ss_floor,self.tiles)		
		self.drawlayers.append(tiledMapLayer)

	# Draws the all of the drawLayers in order.
	def draw(self, renderer):
		for layer in self.drawlayers:
			x = self.camera.panOffset[0]# - self.camera.zoomLevel*FLOOR.w# * len(self.tiles)
			y = self.camera.panOffset[1]# - self.camera.zoomLevel*FLOOR.h# * len(self.tiles[0])
			centeredOffset = [x,y]
			layer.draw(renderer, offset=centeredOffset, zoom=self.camera.zoomLevel)


	def zoom(self, direction):
		self.camera.zoom(direction)
	def panX(self, direction):
		self.camera.panX(direction)
	def panY(self, direction):
		self.camera.panY(direction)

	# Generates a tile map for a single floor.
	def gen_FloorTileMap(self,floor):

		floorStartPosition = floor.floorNumber*FLOOR.h*floor.height

		# Gets the rectangle that represents the location on the
		# sprite sheet that should be clipped.
		def getSource(y, maxIndex):
			src = None
			if(y == maxIndex-1):
				src = FLOOR.BOTTOM
			elif(y == 0):
				src = FLOOR.TOP
			else:
				src = FLOOR.WALL
			return src
		
		# Gets the rectangle that represents the location where
		# the clipped sprite should be drawn.
		def getDestination(x,y):
			w = FLOOR.w
			h = FLOOR.h
			dst = (x*w, floorStartPosition+y*h, w, h)
			return dst

		gridsize = (floor.width, floor.height)
		Tile = namedtuple('Tile', 'source destination')

		row = []
		for x in xrange(0, gridsize[0]):
			col = []
			for y in xrange(0, gridsize[1]):
				source = getSource(y,gridsize[1])
				destination = getDestination(x,y)
				tile = Tile(source, destination)
				col.append(tile)
			row.append(col)
		return row


	# Generates & Compiles all the floor tile maps into a 
	# single bunker tile map.
	def gen_BunkerTileMap(self, bunker):

		# generate floor tile maps
		floorTileMaps = []
		for f in bunker.floors:
			tilemap = self.gen_FloorTileMap(f)
			floorTileMaps.append(tilemap)
		
		# compile floor tile maps into a single tile map
		bunkerTileMap = []
		for x in xrange(0, bunker.width):
			column = []
			for f in floorTileMaps:
				column += f[x]
			bunkerTileMap.append(column)

		return bunkerTileMap



	
	'''
	# Draws the floor tiles.
	def draw(self, renderer):
		h = FLOOR.TOP[3] # tile height (in pixels)
		floorOffsetY = h * self.bunker.floorHeight # the y-offset for each floor (in pixels)
		for f in self.bunker.floors:
			offset = f.floorNumber * floorOffsetY # the y-offset for this floor
			for x in xrange(0,self.bunker.width):
				for y in xrange(0,self.bunker.floorHeight):
					src = self.floorsrc[x][y]
					dst = self.floordst[x][y]
					offsetRect = (dst[0], dst[1]+offset, dst[2], dst[3]) # the offset destination rectangle
					renderer.copy(self.ss_floor, src, offsetRect)
	'''
		




class BunkerScene:
	

	def __init__(self):
		self.bunker = Bunker(width=50,numFloors=4)
		self.resolution = (1200,900)
		cam = Camera(panIncrement=10)
		self.bunkerView = BunkerView(self.resolution, self.bunker,camera=cam)
	
	def __str__(self):
		return str(self.bunkerView)
		
	def loadSpritesheets(self, factory):
		self.bunkerView.loadSpritesheets(factory)

	def draw(self, renderer):
		self.bunkerView.draw(renderer)


	def zoom(self, direction):
		self.bunkerView.zoom(direction)
		print(self.bunkerView.camera)
	def panX(self, direction):
		self.bunkerView.panX(direction)
		print(self.bunkerView.camera)
	def panY(self, direction):
		self.bunkerView.panY(direction)
		print(self.bunkerView.camera)


def test():
	scene = BunkerScene()
	print(scene)

if __name__ == '__main__':
	sys.exit(test())



