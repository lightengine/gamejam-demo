
"""
LOGICAL FRAME
	* No blanking -- that's a physical artifact
	* No laser projectors -- just one logical frame
"""

from color import CMAX

class LogicalFrame(object):
	def __init__(self):
		self.entities = []
		self.frozen = False

		# An array of converted and cached pos/color 5-tuples 
		# These are converted from Points
		self.ptBuf = []

	def add(self, entity):
		if self.frozen:
			return
		self.entities.append(entity)

	def freeze(self):
		self.frozen = True
		for entity in self.entities:
			for point in entity.points:
				x = point.x + entity.x
				y = point.y + entity.y
				pt = (x, y, CMAX, CMAX, CMAX)
				self.ptBuf.append(pt)

	def produce(self):
		for i in xrange(len(self.ptBuf)):
			yield self.ptBuf[i]

"""
PHYSICAL FRAME
	* Blanking exists
	* Objects moved to a laser projector.
"""

class PhysicalFrame(object):
	def __init__(self):
		pass


