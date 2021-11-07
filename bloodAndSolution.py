import physics as pf
import pygame.gfxdraw
import numpy as np

NORMS = {
		# NAME   NORM  COLOR   RADIUS
		"Hydrogen":[4,(51,205,51),7],
		"Sodium":[3,(151,205,151),9],
		"Potasium":[3,(51,100,51),11],
		"Chloride":[3,(151,105,51),13],
		"Urea":[3,(51,51,51),15],
		"Drug":[0,(0,0,0),17]
		}

class Fluid(pf.Environment):

	def addNeighbor(self, env):
		self.neighbor = env

	def moveParticle(self, p,x):
		c1 = len([x for x in self.particles if x.name==p.name])
		c2 = len([x for x in self.neighbor.particles if x.name==p.name])
		self.particles.remove(p)
		if self.side=="left" and 2*NORMS[p.name][0]<(c1+c2):
			return
		if self.side=="left": 
			p.X[0][0] = p.radius
			p.X[0][1] += p.radius
		else:
			p.X[0][0] = 400-p.radius
			p.X[0][1] -= p.radius

		self.neighbor.particles.append(p)
		# p.addAcceleration(self.GRAVITY)


	def getProbability(self,name):
		c1 = sum(1 for x in self.particles if x.name==name)
		c2 = sum(1 for x in self.neighbor.particles if x.name==name)
		sm = c1/(c1+c2)
		return np.random.choice([False,True],1,p=[1-sm,sm])

	def display(self,screen):
		move = 0 if self.side =="left" else 400
		for p in self.particles:
			pygame.gfxdraw.filled_circle(screen, int(p.X[0][0])+move, int(p.X[0][1]), p.radius, p.colour)

	def addElectrolytes(self, electrolytes):
		for electrolyte in electrolytes:
			radius = NORMS[electrolyte[0]][2] 
			density = np.random.randint(50, 75)
			mass = (4/3)*density*3.14*radius**3
			color = NORMS[electrolyte[0]][1]
			for _ in range(electrolyte[1]):
				# particle.addPosition(pos)
				X = np.random.rand(1, 2)*(self.DIM-radius)+radius
				V = np.random.rand(1, 2)*75
				A = np.asarray([0, 0])		
				particle = pf.Particle(blood, X, V, A, radius, mass, density,electrolyte[0],color)
				self.addParticle(particle)


# need to change enviroment once particle moves to another enviroment
blood = Fluid("left")
solution = Fluid("right")
blood.addNeighbor(solution)
solution.addNeighbor(blood)

# electrolytes = [("Hydrogen",5,(51,205,51))] #
electrolytesDeficit = [
						["Hydrogen",1],
						["Sodium",1],
						["Potasium",1],
						["Chloride",1],
						["Urea",1],
						["Drug",7],
					   ] # [("Hydrogen",5)] #

electrolytesExcess = [
						["Hydrogen",7],
						["Sodium",4],
						["Potasium",7],
						["Chloride",7],
						["Urea",7],
						["Drug",7],
					   ] # [("Hydrogen",5)] #


electrolytes = electrolytesDeficit #electrolytesExcess
blood.addElectrolytes(electrolytes)
# creating solution for this blood type
for electrolyte in electrolytes: electrolyte[1] = max(2*(NORMS[electrolyte[0]][0]) - electrolyte[1],0) 
solution.addElectrolytes(electrolytes)








