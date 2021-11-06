import pygame
import physics as pf
import pygame.gfxdraw
import numpy as np
from text import write
from bloodAndSolution import *

pygame.init()

DIM = np.asarray([800, 400])
screen = pygame.display.set_mode(DIM)
pygame.display.set_caption('E-kidney')

running = True

def display(env):
	move = 0 if env.side =="left" else 400
	for p in env.particles:
		pygame.gfxdraw.filled_circle(screen, int(p.X[0][0])+move, int(p.X[0][1]), p.radius, p.colour)


# keeps running until quitting
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	# screen.fill((205,205,205))
	screen.fill((255,204,204), (0, 0, screen.get_width()// 2, screen.get_height()))#-200
	screen.fill((204,204,204), (401, 0, screen.get_width()// 2, screen.get_height()))

	blood.update()
	display(blood)
	solution.update()
	display(solution)
	pygame.display.flip()

