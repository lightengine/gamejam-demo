from position import Position

class Region(object):

	def __init__(self, centerX=0, centerY=0, width=100, height=100,
						centerPosition=None):

		self._center = None
		self._width = width
		self._height = height

		if centerPosition:
			self._center = centerPosition
		else:
			self._center = Position(centerX, centerY)

		self._top = self._center.x + height/2
		self._bottom = self._center.x - height/2
		self._left = self._center.y - width/2
		self._right = self._center.y + width/2

	def contains(self, position):
		if position.x > self._left and position.x < self._right and \
			position.y > self._bottom and position.y < self._top:
				return True
		return False

