# Author: Sam Thomas

import sys
import sdl2
import sdl2.ext
from bunkerScene import BunkerScene

RESOURCES = sdl2.ext.Resources(__file__, 'assets')
CONFIG = sdl2.ext.Resources(__file__, 'config')

def run():

	## Window setup ##
	sdl2.ext.init()
	window = sdl2.ext.Window('prebalefire prototype', size=(1200,900))
	window.show()


	## Renderer Initialization ##
	renderer = sdl2.ext.Renderer(window)
	factory = sdl2.ext.SpriteFactory(sdl2.ext.TEXTURE,renderer=renderer)

	spriterenderer = factory.create_sprite_render_system(window)


	## Load Assets ##
	ss_floor = factory.from_image(RESOURCES.get_path('ss_floor.png'))

	
	## Render ##
	renderer.clear(color=sdl2.ext.Color(130,150,150))

	scene_bunker = BunkerScene()	
	scene_bunker.loadSpritesheets(factory)
	scene_bunker.draw(renderer)

	renderer.present()




	## Main game loop ##
	running = True
	while running:
		events = sdl2.ext.get_events()
		for event in events:
			if event.type == sdl2.SDL_QUIT:
				running = False
				break
			if event.type == sdl2.SDL_KEYDOWN:
				if event.key.keysym.sym == sdl2.SDLK_ESCAPE:
					running = False
				break
		window.refresh()
	sdl2.ext.quit()
	return 0				







if __name__ == '__main__':
	sys.exit(run())
