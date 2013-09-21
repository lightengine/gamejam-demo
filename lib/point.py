
class Point(object):
	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y
		self.isBlank = False

	def __repr__(self):
		return '(%d,%d)' % (self.x, self.y)

class ColorPoint(Point):
	def __init__(self, x=0, y=0, r=0, g=0, b=0):
		self.x = x
		self.y = y
		self.r = r
		self.g = g
		self.b = b
		self.isBlank = False

class BlankPoint(Point):
	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y
		self.isBlank = True

