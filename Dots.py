import math as m

class Dot():
	cord = []
	dist = 0

	def __init__(self, cord):
		for n in cord:
			self.cord.append(float(n))
		self.dist = m.sqrt(cord[0]**2 + cord[1]**2)
		# print(self.dist)
