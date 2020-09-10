import threading
import random
import math as m

class Hilo(threading.Thread):

	def __init__(self, n):
		super().__init__()
		self.inside = 0
		self.n = n

	def run(self):
		self.inside = Inside(self.n)

	def get_inside(self):
		return self.inside

def Inside(n):
	dots = []

	for x in range(n):
		cord = (random.uniform(0,1),random.uniform(0,1))
		dots.append(m.sqrt(cord[0]**2 + cord[1]**2))

	dentro = 0

	for dot in dots:
		if dot < 1:
			dentro += 1

	return dentro