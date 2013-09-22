
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

		# Id handling
		self.eid = Entity._ENTITY_ID_COUNTER
		Entity._ENTITY_ID_COUNTER += 1

		# Which Laser/DAC are we assigned to?
		# If not set, the algo will decide how to distribute.
		self.laserKey = None

	def produce(self):
		for i in range(len(self.points)):
			yield self.points[i]

