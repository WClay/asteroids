# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from player import *
from asteroid import *
from constants import *
from shot import *
from asteroidField import AsteroidField

def main():
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock()
	updatable = pygame.sprite.Group() 
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()
	Player.containers = (updatable, drawable)
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = (updatable)
	Shot.containers = (shots, updatable, drawable)
	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
	asteroid = AsteroidField()
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
		
		for asteroid in asteroids:
			if asteroid.check_collision(player):
				print("GAME OVER!")
				return
			for shot in shots:
				if shot.check_collision(asteroid):
					asteroid.split()
					shot.kill()

		pygame.display.flip()

		# limit the framerate to 60 FPS
		dt = clock.tick(60) / 1000

		keep_playing = player.keep_playing


if __name__ == "__main__":
	main()
