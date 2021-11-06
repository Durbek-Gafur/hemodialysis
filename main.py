import pygame
import physics as pf
import pygame.gfxdraw
import numpy as np

pygame.init()
DIM = np.asarray([800, 400])
DIM_BLOOD = np.asarray([400, 400])
GRAVITY = np.asarray([0, 0])
dt = 0.01

screen = pygame.display.set_mode(DIM)
pygame.display.set_caption('E-kidney')

running = True
ions = ["A","B","C","D","E"]

blood = pf.Environment(DIM_BLOOD,[0,0],0.01)


for n in range(len(ions)):
    radius = 15
    density = 60
    mass = (4/3)*density*3.14*radius**3
    X = np.random.rand(1, 2)*(DIM_BLOOD-radius)+radius
    V = [[15.03452017, 15.76939796]] #np.random.rand(1, 2)*75
    A = np.asarray([0, 0])
    particle = pf.Particle(blood, X, V, A, radius, mass, density,ions[n],ions[n])
    blood.addParticle(particle)


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


	blood.update()
	display(blood)
	pygame.display.flip()

