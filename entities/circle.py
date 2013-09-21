from lib.entity import Entity
from lib.point import *

import math

class Circle(Entity):
	def __init__(self, samplePts=100, radius=1000):
		super(Circle, self).__init__()

		self.direc = 1 # XXX TEMPORARY 

		for i in range(0, samplePts):
			i = float(i) / samplePts * 2 * math.pi
			x = int(math.cos(i) * radius)
			y = int(math.sin(i) * radius)
			self.points.append(Point(x, y))

