import pygame
import physics as pf
import pygame.gfxdraw
import numpy as np

pygame.init()
DIM = np.asarray([800, 400])
DIM_BLOOD = np.asarray([400, 400])
DIM_SOLUTION = np.asarray([400, 400])
GRAVITY = np.asarray([0, 0])
dt = 0.01

screen = pygame.display.set_mode(DIM)
pygame.display.set_caption('E-kidney')

running = True
electrolytes = [("Hydrogen",5,(51,205,51))] #[("Hydrogen",5,(51,205,51)),("Sodium",3,(151,205,151)),("Potasium",2,(51,100,51)),("Chloride",5,(151,105,51)),("Urea",3,(51,51,51))] # [("Hydrogen",5)] #

# need to change enviroment once particle moves to another enviroment
blood = pf.Environment(DIM_BLOOD,[0,0],0.01,"left")
solution = pf.Environment(DIM_SOLUTION,[0,0],0.01,"right")
blood.addNeighbor(solution)
solution.addNeighbor(blood)

for electrolyte in electrolytes:
	radius = np.random.randint(7, 15)
	density = np.random.randint(50, 75)
	mass = (4/3)*density*3.14*radius**3
	color = electrolyte[2]

	# particle = pf.Particle(blood, X, V, A, radius, mass, density,electrolyte[0])
	for _ in range(electrolyte[1]):
		# particle.addPosition(pos)
		X = np.random.rand(1, 2)*(DIM_BLOOD-radius)+radius
		V = np.random.rand(1, 2)*75
		A = np.asarray([0, 0])		
		particle = pf.Particle(blood, X, V, A, radius, mass, density,electrolyte[0],color)
		blood.addParticle(particle)


def display(env):
	move = 0 if env.side =="left" else 400
	for p in env.particles:
		# print(int(p.X[0][0]), int(p.X[0][1]))
		# continue
		pygame.gfxdraw.filled_circle(screen, int(p.X[0][0])+move, int(p.X[0][1]), p.radius, p.colour)


# keeps running until quitting
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	# screen.fill((205,205,205))
	screen.fill((255,204,204), (0, 0, screen.get_width()// 2, screen.get_height()))
	screen.fill((204,204,204), (401, 0, screen.get_width()// 2, screen.get_height()))


	blood.update()
	display(blood)
	solution.update()
	display(solution)
	pygame.display.flip()

