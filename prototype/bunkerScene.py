# Author: Sam Thomas

import sys
import sdl2
import sdl2.ext
import bunker
from spritesheetCodes import FLOORCODES as FLOOR


# !HARDCODE
RESOURCES = sdl2.ext.Resources(__file__, 'assets')
spritesheets = dict(floor='ss_floor.png', character='hello.bmp')


class BunkerScene:

	def __init__(self):
		self.bunker = bunker.Bunker(width=30,numFloors=4)		
		self.floorsrc = self.gen_floorsrc()
		self.floordst = self.gen_floordst()

	def __str__(self):
		s = ''
		width = self.bunker.width
		height = self.bunker.floorHeight

		# formats the matrix of source rectangles and adds it to string s (x&y coord only)
		s += '-floor destination rectangles-' + '\n'
		s += '\n' + '-floor source rectangles-' + '\n'
		for y in xrange(0,height):
			for x in xrange(0,width):
				r = self.floorsrc[x][y]
				valuePair = r[:2]
				s += '{0:<10}'.format(str(valuePair))
				s +=  ' '
			s += '\n'

		# formats the matrix of destination rectangles and adds it to string s (x&y coord only)
		s += '-floor destination rectangles-' + '\n'
		for y in xrange(0,height):
			for x in xrange(0,width):
				r = self.floordst[x][y]
				valuePair = r[:2]
				s += '{0:<10}'.format(str(valuePair))
				s +=  ' '
			s += '\n'

		# return the completed string
		return s

	def gen_floorsrc(self):
		
		def make_column(height):
			col = []
			for y in xrange(0,height):
				rect = None
				if(y == height-1):
					rect = FLOOR.BOTTOM
				#elif(y == 0):
				#	rect = FLOOR.TOP
				else:
					rect = FLOOR.WALL
				col.append(rect)
			return col

		row = []
		for x in xrange(0,self.bunker.width):
			row.append(make_column(self.bunker.floorHeight))
		return row		
		


	def gen_floordst(self):
		width = self.bunker.width
		height = self.bunker.floorHeight
		w = FLOOR.TOP[2:][0] # slices the TOP rectangle, and then selects the tile width at position [0]
		h = FLOOR.TOP[2:][1] # slices the TOP rectangle, and then selects the tile height at position [1]

		row = []
		for x in xrange(0,width):
			col = []
			for y in xrange(0,height):
				rect = (w*x, h*y, w, h)
				col.append(rect)
			row.append(col)
		return row		


	def loadSpritesheets(self, factory):
		self.ss_floor = factory.from_image(RESOURCES.get_path(spritesheets['floor']))

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




def test():
	scene = BunkerScene()
	print(scene)

if __name__ == '__main__':
	sys.exit(test())



