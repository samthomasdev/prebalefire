# Author: Sam Thomas

import os
import sys
import sdl2




class Floor:
	
	def __init__(self, height, position):
		self.height = height
		self.position = position

	def __str__(self):
		return 'Floor {0}: height = {1}'.format(self.position, self.height)



def genFloors(numFloors):
	floors = []
	height = 1.0/numFloors 

	i = 0
	while (i < numFloors):
		floors.append(Floor(height,i+1))
		i += 1

	return floors




def run():
	numFloors = 2
	floors = genFloors(numFloors)
	for f in floors:
		print(f)



if __name__ == '__main__':
	sys.exit(run())








