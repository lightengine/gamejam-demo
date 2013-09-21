"""
LOGICAL FRAME
	* No blanking -- that's a physical artifact
	* No laser projectors -- just one logical frame
"""

from color import CMAX
from entity_gfx import GfxEntity

TRACKING_SAMPLE_PTS = 10
TRACKING_DISPLAY = False

BLANKING_SAMPLE_PTS = 10
BLANKING_DISPLAY = False

class LogicalFrame(object):
	def __init__(self):
		self.entities = []
		self.gfxEntities = []
		self.frozen = False

		# An array of copied Points
		self.points = []

		# Physically computed frames
		# Indexed by `laserKey`:
		#	physicalFrame[laserKey] => PhysicalFrame()
		self.physicalFrames = {}

		# Distortion map
		self.distortions = {}

	def add(self, entity):
		if self.frozen:
			return
		self.entities.append(entity)

	def setDistortions(self, distortions):
		self.distortions = distortions

	def freeze(self):
		self.frozen = True
		for entity in self.entities:
			key = entity.laserKey
			if key not in self.physicalFrames:
				self.physicalFrames[key] = PhysicalFrame()
				self.physicalFrames[key].setDistortion(self.distortions[key])

			gfxEntity = GfxEntity(entity)
			gfxEntity.normalize()
			self.gfxEntities.append(gfxEntity)

			self.physicalFrames[key].addEntity(gfxEntity)

		for physFrame in self.physicalFrames.values():
			physFrame.calculate()

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

		# A list of lists
		entitiesPts = []

		for entity in self.entities:
			entityPts = []

			for point in entity.points:
				x = point.x
				y = point.y

				if self.distortion:
					x *= self.distortion.scaleX
					y *= self.distortion.scaleY
					x += self.distortion.x
					y += self.distortion.y

				pt = (x, y, CMAX, CMAX, CMAX)
				entityPts.append(pt)

			entitiesPts.append(entityPts)

		# Add objects and tracking
		for i in xrange(len(entitiesPts)):
			entityPts = entitiesPts[i]
			pt = None

			firstPt = entityPts[0]
			firstX = firstPt[0]
			firstY = firstPt[1]

			# Blank the laser on its way "in"
			for i in xrange(BLANKING_SAMPLE_PTS):
				if BLANKING_DISPLAY:
					pt = (firstX, firstY, CMAX, CMAX, 0)
					self.ptBuf.append(pt)
				else:
					pt = (firstX, firstY, 0, 0, 0)
					self.ptBuf.append(pt)

			for pt in entityPts:
				self.ptBuf.append(pt)

			currentLastPt = pt
			nextFirstPt = entitiesPts[(i+1)%len(entitiesPts)][0]

			lastX = currentLastPt[0]
			lastY = currentLastPt[1]

			# Blank the laser.
			for i in xrange(BLANKING_SAMPLE_PTS):
				if BLANKING_DISPLAY:
					pt = (lastX, lastY, CMAX, CMAX, 0)
					self.ptBuf.append(pt)
				else:
					pt = (lastX, lastY, 0, 0, 0)
					self.ptBuf.append(pt)

			# Track to the next object  
			# Essentially drawing "black"
			xDiff = currentLastPt[0] - nextFirstPt[0]
			yDiff = currentLastPt[1] - nextFirstPt[1]

			mv = TRACKING_SAMPLE_PTS

			for i in xrange(mv):
				percent = i/float(mv)
				xb = int(lastX - xDiff*percent)
				yb = int(lastY - yDiff*percent)

				# If we want to debug the tracking path
				if TRACKING_DISPLAY:
					pt = (xb, yb, CMAX, CMAX, 0)
					self.ptBuf.append(pt)
				else:
					pt = (xb, yb, 0, 0, 0)
					self.ptBuf.append(pt)

		self.isCalculated = True

	def produce(self):
		for i in xrange(len(self.ptBuf)):
			yield self.ptBuf[i]


