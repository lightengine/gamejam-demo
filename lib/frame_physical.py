"""
PHYSICAL FRAME
	* Blanking exists
	* Objects moved to a laser projector.
"""

from color import CMAX
from entity_gfx import GfxEntity

class PhysicalFrame(object):
	def __init__(self):
		self.entities = []
		self.distortion = None

		# An array of converted and cached pos/color 5-tuples 
		# These are converted from Points
		self.ptBuf = []
		self.isCalculated = False

		self.blankingSamplePts = 15
		self.blankingDisplay = False
		self.trackingSamplePts= 15
		self.trackingDisplay = False

	def addEntity(self, entity):
		self.entities.append(entity)

	def setDistortion(self, distortion):
		self.distortion = distortion
		self.blankingSamplePts = distortion.blankingSamplePts
		self.blankingDisplay = distortion.blankingDisplay
		self.trackingSamplePts = distortion.trackingSamplePts
		self.trackingDisplay = distortion.trackingDisplay

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

				r, g, b = (CMAX, CMAX, CMAX)
				if entity.color:
					r = entity.color.r
					g = entity.color.g
					b = entity.color.b

				pt = (x, y, r, g, b)
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
			for i in xrange(self.blankingSamplePts):
				if self.blankingDisplay:
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
			for i in xrange(self.blankingSamplePts):
				if self.blankingDisplay:
					pt = (lastX, lastY, CMAX, CMAX, 0)
					self.ptBuf.append(pt)
				else:
					pt = (lastX, lastY, 0, 0, 0)
					self.ptBuf.append(pt)

			# Track to the next object  
			# Essentially drawing "black"
			xDiff = currentLastPt[0] - nextFirstPt[0]
			yDiff = currentLastPt[1] - nextFirstPt[1]

			mv = self.trackingSamplePts

			for i in xrange(mv):
				percent = i/float(mv)
				xb = int(lastX - xDiff*percent)
				yb = int(lastY - yDiff*percent)

				# If we want to debug the tracking path
				if self.trackingDisplay:
					pt = (xb, yb, CMAX, CMAX, 0)
					self.ptBuf.append(pt)
				else:
					pt = (xb, yb, 0, 0, 0)
					self.ptBuf.append(pt)

		self.isCalculated = True

	def produce(self):
		for i in xrange(len(self.ptBuf)):
			yield self.ptBuf[i]


