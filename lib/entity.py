import numpy
from math import cos, sin

class Entity(object):

	# Static object counter. 
	_ENTITY_ID_COUNTER = 0

	def __init__(self):

		# Points in the system (x, y, isBlank)
		self.points = []

		# Positioning stuff
		self.x = 0
		self.y = 0
		self.xVel = 0.0
		self.yVel = 0.0
		self.scale = 1.0
		self.rotation = 0.0

		self.rotateZ = 0.0
		self.rotateX = 0.0
		self.rotateY = 0.0

		self._matStack = []
		self.fMatStack = []
		self._matTransformX = None
		self._matTransformY = None

		# Id handling
		self.eid = Entity._ENTITY_ID_COUNTER
		Entity._ENTITY_ID_COUNTER += 1

		# Which Laser/DAC are we assigned to?
		# If not set, the algo will decide how to distribute.
		self.laserKey = None

	def initMatStack(self):
		self._matStack = []

	def pushRotateX(self, theta):
		mat = numpy.matrix([[1, 0, 0],
							[0, cos(theta), -1*sin(theta)],
							[0, sin(theta), cos(theta)]])
		self._matStack.append(mat)


	def pushRotateY(self, theta):
		mat = numpy.matrix([[cos(theta), 0, sin(theta)],
							[0, 1, 0],
							[-1*sin(theta), 0, cos(theta)]])
		self._matStack.append(mat)

	def pushRotateZ(self, theta):
		mat = numpy.matrix([[cos(theta), -1*sin(theta), 0],
							[sin(theta), cos(theta), 0],
							[0, 0, 1]])
		self._matStack.append(mat)

	def doneMatStack(self):
		self.fMatStack = self._matStack[:]
		rotX = None
		rotY = None
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

		self._matTransformX = rotX
		self._matTransformY = rotY

		self._matStack = []

	def produce(self):
		for i in range(len(self.points)):
			yield self.points[i]

