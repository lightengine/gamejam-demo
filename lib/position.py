
class Position(object):

	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y

	def __sub__(self, pos):
		x = self.x - pos.x
		y = self.y - pos.y
		return Position(x, y)

	def __repr__(self):
		return '<Pos %d,%d>' % (self.x, self.y)

	def isWithin(self, region):
		return region.contains(self)

	def percentTo(self, pos, percent=0.5):
		diff = self - pos
		return Position(self.x - (diff.x*percent),
						self.y - (diff.y*percent))

