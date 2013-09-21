
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

		# Id handling
		self.eid = Entity._ENTITY_ID_COUNTER
		Entity._ENTITY_ID_COUNTER += 1

	def produce(self):
		for i in range(len(self.points)):
			yield self.points[i]

