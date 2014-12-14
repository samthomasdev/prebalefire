# Author: Sam Thomas

import sys
import sdl2
import sdl2.ext













def run():
	# Window setup
	sdl2.ext.init()
	window = sdl2.ext.Window('prebalefire prototype', size=(1200,900))
	window.show()
	
	# Get drawing surface
	windowsurface = window.get_surface()

	

	# Main game loop
	running = True
	while running:
		events = sdl2.ext.get_events()
		for event in events:
			if event.type == sdl2.SDL_QUIT:
				running = False
				break
			#if event.type == sdl2.SDL_MOUSEBUTTONDOWN:
		window.refresh()
	sdl2.ext.quit()
	return 0				







if __name__ == '__main__':
	sys.exit(run())
