"""
LOGICAL FRAME
	* No blanking -- that's a physical artifact
	* No laser projectors -- just one logical frame
"""

import random

from color import CMAX
from entity_gfx import GfxEntity
from frame_physical import PhysicalFrame

class LogicalFrame(object):
	def __init__(self):
		self.entities = []
		self.gfxEntities = []
		self.frozen = False

		# An array of copied Points
		self.points = []

		# Physically computed frames
		# Indexed by `laserKey`:
		#	physicalFrame[laserKey] => PhysicalFrame()
		self.physicalFrames = {}

		# Distortion map
		self.distortions = {}

	def add(self, entity):
		if hasattr(entity, 'isDestroyed'):
			return
		self.entities.append(entity)

	def setDistortions(self, distortions):
		self.distortions = distortions

	def freeze(self):
		self.frozen = True

		# FIXME: Better way of specifying hardware
		for key in self.distortions.keys():
			self.physicalFrames[key] = PhysicalFrame()
			self.physicalFrames[key].setDistortion(self.distortions[key])

		for entity in self.entities:
			if hasattr(entity, 'isDestroyed'):
				continue

			key = entity.laserKey

			gfxEntity = GfxEntity(entity)
			gfxEntity.normalize()
			self.gfxEntities.append(gfxEntity)

			self.physicalFrames[key].addEntity(gfxEntity)

		for physFrame in self.physicalFrames.values():
			physFrame.calculate()

	def getPhysical(self, key, distortion=None):
		if key not in self.physicalFrames:
			return False

		physFrame = self.physicalFrames[key]
		physFrame.setDistortion(distortion)
		return physFrame

