# Author: Sam Thomas

import os
import sys
import sdl2


class Bunker:

	
	def __init__(self, width=10, numFloors=1, floorHeight=3):
		self.width = width
		self.numFloors = numFloors
		self.floorHeight = floorHeight
		self.floors = genFloors(numFloors,floorHeight,width)

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
	i = 0
	while (i < numFloors):
		floors.append(Floor(i,height,width))
		i += 1
	return floors





def run():
	bunker = Bunker(numFloors=3)
	print(bunker)

if __name__ == '__main__':
	sys.exit(run())








