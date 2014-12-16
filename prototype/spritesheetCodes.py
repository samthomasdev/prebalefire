# Author: Sam Thomas

# Desc: This file holds the classes which contain
# all of the clipping rectangles for their respective
# spritesheets. Each rectangle is hardcoded and is
# to as a 'Code'.


# !HARDCODED
# spritesheet: ss_floor.png
class FLOORCODES:
	TILESIZE = 70
	h = TILESIZE # height
	w = TILESIZE # width

	TOP = 		(280,0,h,w)
	BOTTOM = 	(70,0,h,w)
	WALL = 		(210,0,h,w)
	



# A template class to make the hardcoding easier.
# spritesheet: TODO
class CODETEMPLATE:
	h = 0 # height
	w = 0 # width

	CODE1 = (0,0,h,w)
	CODE2 = (0,0,h,w)
	CODE3 = (0,0,h,w)














