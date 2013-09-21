"""
Provides a wrapper to the old Streamer interface
"""

from shape import Shape
from color import CMAX

class Wrap(Shape):
	def __init__(self, entity):
		super(Wrap, self).__init__()
		self.entity = entity

	def produce(self):
		for i in xrange(len(self.entity.points)):
			point = self.entity.points[i]
			yield (point.x, point.y, CMAX, CMAX, CMAX)

