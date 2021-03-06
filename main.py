import pygame
import physics as pf
import pygame.gfxdraw
import numpy as np
from text import write
from bloodAndSolution import *

pygame.init()
DIM = np.asarray([800, 600])
screen = pygame.display.set_mode(DIM)
pygame.display.set_caption('E-kidney')
running = True
startTime = datetime.datetime.now()
bloodClean = False

# keeps running until quitting
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	if bloodClean: continue
	if blood.equalibrium(startTime): bloodClean = True
	else:
		screen.fill((255,255,255), (0, 0, 800,600))
		screen.fill((255,204,204), (0, 0, screen.get_width()// 2, 400))#-200
		screen.fill((204,204,204), (401, 0, screen.get_width()// 2, 400))
		write(screen,"BLOOD",(screen.get_width()//4, 200))
		write(screen,"DIALYSIS SOLUTION",(screen.get_width()//4+screen.get_width()//2, 200))
		ms = str(datetime.datetime.now()-startTime)[:10]
		# write(screen,ms,(screen.get_width()//2, 25)) write(screen,ms,(screen.get_width()//2, 25))
		blood.update()
		blood.display(screen)
		solution.update()
		solution.display(screen)
		write(screen,ms,(screen.get_width()//2, 25))
		
		write(screen,"Deficit    Norm   Excess",(screen.get_width()//2, 420),(0,0,0))
		level = 450
		start = 400
		for e in NORMS:
			numberOfEnow = blood.countParticle(e)
			pygame.draw.line(screen, NORMS[e][1], (start, level), (start+(50*(numberOfEnow - NORMS[e][0])), level),20)
			write(screen,e+" ("+str(numberOfEnow-electrolytes[e])+")",(start-300, level),NORMS[e][1])
			if e in blood.normalizedArray:
				write(screen,blood.normalizedArray[e],(start+300, level),NORMS[e][1])
			level+=25

	pygame.display.flip()

