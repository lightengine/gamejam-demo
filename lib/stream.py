"""
PointStream
	Formerly the main galvo multiple object drawing
	algorithm. This code is responsible for
	drawing multiple objects. It will need to
	be improved for efficiency.
"""

import math
import random
import itertools
import sys
import threading
import time

from multiprocessing import Process, Queue

class PointStream(object):
	def __init__(self):
		self.called = False
		self.stream = self.produce()

		# Frame system
		self.frame = None
		self.nextFrame = None

		# Multilaser hack
		self.laserKey = None
		self.distortion = None

		self.queue = None

	def setQueue(self, queue):
		self.queue = queue

	def getNextFrame(self):
		try:
			physFrame = self.queue.get(block=False)
			if physFrame:
				self.nextFrame = physFrame
		except:
			pass

	def read(self, n):
		"""
		Return the next 'n' points that the laser projector wants.
		This is how DAC.py interfaces with us.
		"""
		#print 'stream.read( %s )' % self.laserKey
		return [self.stream.next() for i in xrange(n)]

	def produce(self):
		"""
		This infinite loop functions as an infinite point
		generator. It generates points for objects as
		well as the "tracking" and "blanking" points
		that must occur between object draws.
		"""
		#print 'producex'
		while True:
			try:
				#print 'produce...trygetnextframe'
				self.getNextFrame()
				#print 'produce...gotnextframe'
				if self.nextFrame:
					self.frame = self.nextFrame

				frame = self.frame

				if not frame:
					#print 'noframe'
					yield (0, 0, 0, 0, 0)
					continue

				frame.calculate()

				for pt in frame.ptBuf:
					yield pt

			except Exception as e:
				print "PointStream.produce() exception."
				print e
				pass

