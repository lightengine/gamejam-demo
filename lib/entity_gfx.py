import math
import numpy

class GfxEntity(object):

	def __init__(self, entity):
		self.points = []
		self.x = entity.x
		self.y = entity.y
		self.scale = entity.scale
		self.rotateZ = entity.rotateZ
		self.rotateX = entity.rotateX
		self.rotateY = entity.rotateY

		self.fMatStack = entity.fMatStack[:]
		self._matTransformX = entity._matTransformX
		self._matTransformY = entity._matTransformY

		# Copy the entity's points
		for point in entity.points:
			self.points.append(point.copy())

		# Normalized yet?
		self.isNormalized = False

		# Which Laser/DAC are we assigned to?
		# If not set, the algo will decide how to distribute.
		self.laserKey = entity.laserKey

	def normalize(self):
		if self.isNormalized:
			return

		self.isNormalized = True

		"""
		rotX = 1.0
		rotY = 1.0
		if len(self.fMatStack) > 0:
			m = None
			for mat in self.fMatStack:
				if m is None:
					m = mat
					continue
				m *= mat

			vec = numpy.matrix([[1], [1], [1]])
			ret = m * vec
			rotX = ret[0,0]
			rotY = ret[1,0]
		"""


		# Scale, Rotate, Translate
		for i in range(len(self.points)):
			x = self.points[i].x
			y = self.points[i].y

			#x *= self.scale
			#y *= self.scale

			if self.rotateZ != 0.0:
				(x2, y2) = (x, y)
				x2 = x
				y2 = y
				x = x2*math.cos(self.rotateZ) - y2*math.sin(self.rotateZ)
				y = y2*math.cos(self.rotateZ) + x2*math.sin(self.rotateZ)

			"""
			if self.rotateX != 0.0:
				x *= math.sin(self.rotateX)

			if self.rotateY != 0.0:
				y *= math.sin(self.rotateY)
			"""

			if self._matTransformX and self._matTransformY:
				x *= self._matTransformX
				y *= self._matTransformY

			x += self.x
			y += self.y

			self.points[i].x = x
			self.points[i].y = y

		self.x = 0
		self.y = 0
		self.scale = 1
		self.rotation = 0

