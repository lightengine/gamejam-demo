
class World(object):

	def __init__(self, width = 10000, height = 10000):
		self.width = width
		self.height = height
		self.camera = None
		self.entities = []

	def addEntity(self, entity):
		for i in range(len(self.entities)):
			e = self.entities[i]
			if entity.eid == e.eid:
				return False
		self.entities.append(entity)
		return True

	def removeEntity(self, entity):
		for i in range(len(self.entities)):
			e = self.entities[i]
			if entity.eid == e.eid:
				self.entities.pop(i)
				return True
		return False

	def setCamera(self, camera):
		self.camera = camera
		self.camera.world = self

