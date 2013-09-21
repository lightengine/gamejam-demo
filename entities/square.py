from lib.entity import Entity
from lib.point import *

import math

class Square(Entity):
	def __init__(self, edgeLen=1000, edgeSample=20, vertSample=20):
		super(Square, self).__init__()

		self.direc = 1 # XXX TEMPORARY 

		def make_line(pt1, pt2, steps=edgeSample):
			xdiff = pt1.x - pt2.x
			ydiff = pt1.y - pt2.y
			line = []
			for i in xrange(0, steps, 1):
				j = float(i)/steps
				x = pt1.x - (xdiff * j)
				y = pt1.y - (ydiff * j)
				line.append(Point(x, y))
			return line

		ed = edgeLen/2

		edges = []
		edges.append(Point(ed, ed))
		edges.append(Point(-ed, ed))
		edges.append(Point(-ed, -ed))
		edges.append(Point(ed, -ed))

		p = None # Save in scope

		self.points.extend(make_line(edges[0], edges[1]))
		for i in range(vertSample):
			self.points.append(edges[1].copy())

		self.points.extend(make_line(edges[1], edges[2]))
		for i in range(vertSample):
			self.points.append(edges[2].copy())

		self.points.extend(make_line(edges[2], edges[3]))
		for i in range(vertSample):
			self.points.append(edges[3].copy())

		self.points.extend(make_line(edges[3], edges[0]))
		for i in range(vertSample):
			self.points.append(edges[0].copy())

