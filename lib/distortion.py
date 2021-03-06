
class Distortion(object):
	def __init__(self, x=0, y=0, scale=1.0, scaleY=False, scaleX=False,
					blankingSamplePts=15, trackingSamplePts=15,
					blankingDisplay=False, trackingDisplay=False):
		# Easy parameterization API
		scaleX = scale
		if scaleX is not False:
			scaleX = scaleX
			scaleY = scaleY

		if scaleY is False:
			scaleY = scale

		self.x = x
		self.y = y
		self.scaleX = scaleX
		self.scaleY = scaleY

		self.blankingDisplay = blankingDisplay
		self.blankingSamplePts = blankingSamplePts

		self.trackingDisplay = trackingDisplay
		self.trackingSamplePts = trackingSamplePts

	def __repr__(self):
		params = (self.x, self.y, self.scaleX, self.scaleY)
		return '<Distortion %d,%d : %dx%d>' % params
