# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from player import *

from constants import *

def main():
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock()
	updatable = pygame.sprite.Group() 
	drawable = pygame.sprite.Group()
	Player.containers = (updatable, drawable)
	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
	keep_playing = True
	dt = 0
	
	print("Starting Asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")


	while keep_playing:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
			
		screen.fill("black")

		updatable.update(dt)

		for thing in drawable:
			thing.draw(screen)
		
		pygame.display.flip()

		# limit the framerate to 60 FPS
		dt = clock.tick(60) / 1000


if __name__ == "__main__":
	main()
