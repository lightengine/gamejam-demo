
from position import Position

class Camera(object):

	def __init__(self, width=40000, height=40000):
		self.width = width
		self.height = height
		self.position = Position(0, 0)
		self.world = None

	def positionAt(self, x, y):
		self.position.x = x
		self.position.y = y

	def render(self):
		if not self.world:
			return False

		for entity in self.world.entities:
			pos = entity.position

