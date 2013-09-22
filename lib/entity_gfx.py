
class GfxEntity(object):

	def __init__(self, entity):
		self.points = []
		self.x = entity.x
		self.y = entity.y
		self.scale = entity.scale
		self.rotation = entity.rotation

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

		for i in range(len(self.points)):
			#self.points[i].x *= self.scale
			#self.points[i].y *= self.scale
			self.points[i].x += self.x
			self.points[i].y += self.y

		self.x = 0
		self.y = 0
		self.scale = 1
		self.rotation = 0

