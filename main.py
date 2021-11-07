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




# keeps running until quitting
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	screen.fill((255,204,204), (0, 0, screen.get_width()// 2, screen.get_height()))#-200
	screen.fill((204,204,204), (DIM[1]+1, 0, screen.get_width()// 2, screen.get_height()))

	blood.update()
	blood.display(screen)
	solution.update()
	solution.display(screen)
	pygame.display.flip()

