# Author: Sam Thomas

import sys
import sdl2
import sdl2.ext


RESOURCES = sdl2.ext.Resources(__file__, 'assets')


rectWidth = 70
rectHeight = 70

x1 = 100
y1 = 100







def run():
	# Window setup
	sdl2.ext.init()
	window = sdl2.ext.Window('prebalefire prototype', size=(1200,900))
	window.show()
	# Create sprite factory (hardware accelerated)
	renderer = sdl2.ext.Renderer(window)
	factory = sdl2.ext.SpriteFactory(sdl2.ext.TEXTURE,renderer=renderer)
	# Create rendering system
	spriterenderer = factory.create_sprite_render_system(window)


	# Load 2d texture assets
	ss_floor = factory.from_image(RESOURCES.get_path('ss_floor.png'))

	
	
	renderer.clear(color=sdl2.ext.Color(200,200,200))
	spriterenderer.render(ss_floor)

	# Spritesheet clip draw
	srcrect = (140,0,rectWidth,rectHeight)
	dstrect = (x1,y1,rectWidth,rectHeight)
	renderer.copy(ss_floor, srcrect, dstrect)
	#renderer.draw_rect(dstrect, color=sdl2.ext.Color(50,100,100))



	renderer.present()





	# Main game loop
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
