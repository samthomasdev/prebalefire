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
		self.bunker = Bunker()
		
		
		self.floorsrc = []
		self.floordst = []




	def draw(self,renderer):
		x=2



