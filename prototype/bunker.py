# Author: Sam Thomas

import os
import sys
import sdl2


class Bunker:

	
	def __init__(self, width=10, numFloors=1, floorHeight=4):
		self.width = width
		self.numFloors = numFloors
		self.floorHeight = floorHeight
		self.floors = genFloors(numFloors,floorHeight,width)

		#self.GridSize = lambda: (self.width, self.numFloors*self.floorHeight)

	def __str__(self):
		s = ''
		for f in self.floors:
			s+=str(f)+'\n'
		return s




class Floor:
	
	def __init__(self, floorNumber, height, width):
		self.height = height
		self.width = width
		self.floorNumber = floorNumber

	def __str__(self):
		return 'Floor {0}: height = {1}, width = {2}'.format(self.floorNumber, self.height, self.width)


def genFloors(numFloors,height, width):
	floors = []
	for i in xrange(0,numFloors):
		floors.append(Floor(i,height,width))
	return floors





def run():
	bunker = Bunker(numFloors=3)
	print(bunker)

if __name__ == '__main__':
	sys.exit(run())








