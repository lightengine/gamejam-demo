
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

		# Physically computed frames
		# Indexed by `laserKey`:
		#	physicalFrame[laserKey] => PhysicalFrame()
		self.physicalFrames = {}

	def add(self, entity):
		if self.frozen:
			return
		self.entities.append(entity)

	def freeze(self):
		self.frozen = True
		for entity in self.entities:
			key = entity.laserKey
			if key not in self.physicalFrames:
				self.physicalFrames[key] = PhysicalFrame()
			self.physicalFrames[key].addEntity(entity)

		#for physFrame in self.physicalFrames.values():
		#	physFrame.calculate()

	def getPhysical(self, key, distortion=None):
		if key not in self.physicalFrames:
			return False

		physFrame = self.physicalFrames[key]
		physFrame.setDistortion(distortion)
		return physFrame

"""
PHYSICAL FRAME
	* Blanking exists
	* Objects moved to a laser projector.
"""

class PhysicalFrame(object):
	def __init__(self):
		self.entities = []
		self.distortion = None

		# An array of converted and cached pos/color 5-tuples 
		# These are converted from Points
		self.ptBuf = []
		self.isCalculated = False

	def addEntity(self, entity):
		self.entities.append(entity)

	def setDistortion(self, distortion):
		self.distortion = distortion

	def calculate(self):
		for entity in self.entities:
			for point in entity.points:
				x = point.x + entity.x
				y = point.y + entity.y

				if self.distortion:
					x *= self.distortion.scaleX
					y *= self.distortion.scaleY
					x += self.distortion.x
					y += self.distortion.y

				pt = (x, y, CMAX, CMAX, CMAX)
				self.ptBuf.append(pt)

		self.isCalculated = True

	def produce(self):
		if not self.isCalculated:
			self.calculate()

		for i in xrange(len(self.ptBuf)):
			yield self.ptBuf[i]


