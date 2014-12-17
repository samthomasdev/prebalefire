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


	## Render Initialization ## 
	renderer = sdl2.ext.Renderer(window)
	factory = sdl2.ext.SpriteFactory(sdl2.ext.TEXTURE,renderer=renderer)
	spriterenderer = factory.create_sprite_render_system(window)


	## Load Resources ##
	ss_floor = factory.from_image(RESOURCES.get_path('ss_floor.png'))

	
	## Draw ##	
	renderer.clear(color=sdl2.ext.Color(240,220,200))

	scene_bunker = BunkerScene()
	scene_bunker.loadSpritesheets(factory)
	scene_bunker.draw(renderer)

	renderer.present()




	## Main Game Loop ##
	running = True
	while running:
		events = sdl2.ext.get_events()
		for event in events:
			if event.type == sdl2.SDL_MOUSEWHEEL:
				if event.wheel.y != 0:
					scene_bunker.zoom(event.wheel.y)
			elif event.type == sdl2.SDL_KEYDOWN:
				if event.key.keysym.sym == sdl2.SDLK_UP:
					scene_bunker.panY(1);
				elif event.key.keysym.sym == sdl2.SDLK_DOWN:
					scene_bunker.panY(-1);
				elif event.key.keysym.sym == sdl2.SDLK_LEFT:
					scene_bunker.panX(1);
				elif event.key.keysym.sym == sdl2.SDLK_RIGHT:
					scene_bunker.panX(-1);
				elif event.key.keysym.sym == sdl2.SDLK_ESCAPE:
					running = False
					break
			elif event.type == sdl2.SDL_QUIT:
				running = False
				break
		renderer.clear(color=sdl2.ext.Color(240,220,200))
		scene_bunker.draw(renderer)
		renderer.present()
		window.refresh()
	sdl2.ext.quit()
	return 0				







if __name__ == '__main__':
	sys.exit(run())
