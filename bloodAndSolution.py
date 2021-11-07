import physics as pf
import pygame.gfxdraw
import numpy as np



DIM_BLOOD = np.asarray([400, 400])
DIM_SOLUTION = np.asarray([400, 400])
GRAVITY = np.asarray([0, 0])
dt = 0.01
# electrolytes = [("Hydrogen",5,(51,205,51))] #
electrolytesDeficit = [
["Hydrogen",1,(51,205,51),7],
["Sodium",1,(151,205,151),9],
["Potasium",1,(51,100,51),11],
["Chloride",1,(151,105,51),13],
["Urea",1,(51,51,51),15],
["Drug",7,(0,0,0),17],
] # [("Hydrogen",5)] #

electrolytesExcess = [
["Hydrogen",7,(51,205,51),7],
["Sodium",4,(151,205,151),9],
["Potasium",7,(51,100,51),11],
["Chloride",7,(151,105,51),13],
["Urea",7,(51,51,51),15],
["Drug",7,(0,0,0),17],
] # [("Hydrogen",5)] #



# need to change enviroment once particle moves to another enviroment
blood = pf.Environment(DIM_BLOOD,[0,0],0.01,"left")
solution = pf.Environment(DIM_SOLUTION,[0,0],0.01,"right")
blood.addNeighbor(solution)
solution.addNeighbor(blood)

def createAndAdd(electrolyte,medium):
	radius = electrolyte[3]
	density = np.random.randint(50, 75)
	mass = (4/3)*density*3.14*radius**3
	color = electrolyte[2]
	for _ in range(electrolyte[1]):
		# particle.addPosition(pos)
		X = np.random.rand(1, 2)*(DIM_BLOOD-radius)+radius
		V = np.random.rand(1, 2)*75
		A = np.asarray([0, 0])		
		particle = pf.Particle(blood, X, V, A, radius, mass, density,electrolyte[0],color)
		medium.addParticle(particle)



electrolytes = electrolytesDeficit #electrolytesExcess



# incoming blood
for electrolyte in electrolytes:
	createAndAdd(electrolyte,blood)

# creating solution for this blood type
for electrolyte in electrolytes:
	electrolyte[1] = max(2*(blood.norms[electrolyte[0]]) - electrolyte[1],0) 

	createAndAdd(electrolyte,solution)






