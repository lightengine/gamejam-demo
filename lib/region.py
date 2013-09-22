
class Region(object):

	def __init__(self, centerX=0, centerY=0, width=100, height=100,
						centerPosition=None):

		self.center = None
		self.width = None
		self.height = None

		if centerPosition:
			self.center = centerPosition
		else:
			self.center = Position(centerX, centerY)

		self.topX = self.center.x

	def isWithin(position):

