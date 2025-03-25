# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

from constants import *

def main():
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock= pygame.time.Clock()
	dt = 0
	keep_playing = True
	print("Starting Asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
	while keep_playing:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		screen.fill(000)
		pygame.display.flip()
		dt = clock.tick(60) / 1000
		#dt = clock.get_time() / 1000

	


if __name__ == "__main__":
	main()
