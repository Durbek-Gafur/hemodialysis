import pygame
import physics as pf

pygame.init()
DIM = [800,400]

screen = pygame.display.set_mode(DIM)
pygame.display.set_caption('E-kidney')

running = True
ions = ["A","B","C","D","E"]

blood = pf.Environment(DIM,[0,0],0.01)


def display(env):
    for p in env.particles:
        pygame.gfxdraw.filled_circle(screen, int(p.X[0][0]), int(p.X[0][1]), p.radius, p.colour)


# keeps running until quitting
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	# screen.fill((205,205,205))
	screen.fill((205,205,205), (0, 0, screen.get_width()// 2, screen.get_height()))

	# Draw a solid blue circle in the center
	pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

	# Flip the display
	pygame.display.flip()

