import physics as pf
import pygame.gfxdraw
import numpy as np
import time 
import datetime

NORMS = {
		# NAME   NORM  COLOR   RADIUS
		"Hydrogen":[4,(255,0,0),7],
		"Sodium":[3,(151,205,151),9],
		"Potasium":[3,(0,255,0),11],
		"Chloride":[3,(0,191,255),13],
		"Urea":[3,(51,51,51),15],
		"Drug":[0,(0,0,0),17]
		}

class Fluid(pf.Environment):
	def __str__(self):
		ans = [[key,self.countParticle(key)] for key in NORMS]
		return str(ans)
	def equalibrium(self,startTime):
		count = len(NORMS)
		for key in NORMS:
			if NORMS[key][0]!=self.countParticle(key):
				continue
			count-=1
			if key not in self.normalizedArray:
				ms = str(datetime.datetime.now()-startTime)[:10]
				self.normalizedArray[key] = ms
				self.text +=key[:3]+"\t\t"+ms+"\n"
				print(key[:3],"\t\t",ms)
		if count==0: 
			ms = str(datetime.datetime.now()-startTime)[:10]
			self.text +="All\t\t"+ms
			print("All","\t\t",ms)
			file1 = open("results.txt","a")
			file1.writelines(self.text)
			file1.close() #to change file access modes
		return count==0
			# print(NORMS[key][0],self.countParticle(key))

	def addNeighbor(self, env):
		self.neighbor = env

	def countParticle(self,name):
		return len([x for x in self.particles if x.name==name])

	def moveParticle(self, p,x):
		c1 = self.countParticle(p.name)
		c2 = self.neighbor.countParticle(p.name) 
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
		c1 = self.countParticle(name)
		c2 = self.neighbor.countParticle(name) 
		sm = c1/(c1+c2)
		return np.random.choice([False,True],1,p=[1-sm,sm])

	def display(self,screen):
		move = 0 if self.side =="left" else 400
		for p in self.particles:
			pygame.gfxdraw.filled_circle(screen, int(p.X[0][0])+move, int(p.X[0][1]), p.radius, p.colour)

	def addElectrolytes(self, electrolytes):
		for electrolyte in electrolytes:

			radius = NORMS[electrolyte][2] 
			density = np.random.randint(50, 75)
			mass = (4/3)*density*3.14*radius**3
			color = NORMS[electrolyte][1]

			for _ in range(electrolytes[electrolyte]):

				# particle.addPosition(pos)
				X = np.random.rand(1, 2)*(self.DIM-radius)+radius
				V = np.random.rand(1, 2)*75
				A = np.asarray([0, 0])		
				particle = pf.Particle(blood, X, V, A, radius, mass, density,electrolyte,color)
				self.addParticle(particle)


# need to change enviroment once particle moves to another enviroment
blood = Fluid("left")
startTime = datetime.datetime.now()
blood.text+="\n"+str(startTime)+"\n"
solution = Fluid("right")
blood.addNeighbor(solution)
solution.addNeighbor(blood)

# electrolytes = [("Hydrogen",5,(51,205,51))] #
electrolytesDeficit = {
						"Hydrogen":1,
						"Sodium":1,
						"Potasium":1,
						"Chloride":1,
						"Urea":1,
						"Drug":1,
					   } # [("Hydrogen",5)] #

electrolytesExcess = {
						"Hydrogen":7,
						"Sodium":4,
						"Potasium":7,
						"Chloride":7,
						"Urea":7,
						"Drug":7,
					   } # [("Hydrogen",5)] #

electrolytesRandom = {
						"Hydrogen":np.random.randint(-4,9),
						"Sodium":np.random.randint(-4,9),
						"Potasium":np.random.randint(-4,9),
						"Chloride":np.random.randint(-4,9),
						"Urea":np.random.randint(-4,9),
						"Drug":np.random.randint(0,9),
					   } # [("Hydrogen",5)] #

electrolytes = electrolytesRandom # electrolytesDeficit #electrolytesExcess
blood.text += "Blood: "+str(electrolytes)+"\n"
blood.addElectrolytes(electrolytes)

# creating solution for this blood type
solutionElectrolytes={}
for electrolyte in electrolytes: solutionElectrolytes[electrolyte] = max(2*(NORMS[electrolyte][0]) - electrolytes[electrolyte],0) 
solution.addElectrolytes(solutionElectrolytes)
blood.text += "Solution: "+str(solution)+"\n"










