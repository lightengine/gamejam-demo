#!/usr/bin/env python

import time
import math
import itertools
import sys
import random
import thread

from lib import dac
from lib.common import *
from lib.stream import PointStream
from lib.entity import Entity
from lib.point import *
from lib.frame import *
from lib.wrap import Wrap
from lib.distortion import Distortion

from entities.circle import Circle
from entities.square import Square

IPAddrs = {
	'china':	'169.254.156.112',
	'usa':		'169.254.97.11',
}

dacs = {}
dacs['china'] = dac.DAC(IPAddrs['china'])
dacs['usa']	  = dac.DAC(IPAddrs['usa'])

distortions = {}
distortions['china'] = Distortion(5000, -6600, 0.75, 0.75)
distortions['usa'] = Distortion(-5000, 6600)

frame = LogicalFrame()

entities = []
entities.append(Circle())
entities.append(Circle())
entities.append(Circle())
entities.append(Circle())

for i in range(len(entities)):
	entity = entities[i]
	entity.laserKey = 'china' if i%2 == 0 else 'usa'
	#entity.x = random.randint(-5000, 5000)
	#entity.y = random.randint(-5000, 5000)
	entity.x = 0
	entity.y = 0
	frame.add(entity)

def set_frame(frame):
	frame.setDistortions(distortions)
	frame.freeze()
	for d in dacs.values():
		d.stream.setNextFrame2(frame)

	"""
	for laserKey, d in dacs.iteritems():
		physFrame = frame.getPhysical(laserKey)
		d.stream.setNextPhysicalFrame(physFrame)
	"""

def dac_thread(key):
	while True:
		try:
			print 'Connecting to dac @ %s' % IPAddrs[key]
			dacs[key] = dac.DAC(IPAddrs[key])
			d = dacs[key]
			d.stream = PointStream()
			d.stream.laserKey = key
			d.stream.distortion = distortions[key]
			d.play_stream(d.stream)

		except KeyboardInterrupt:
			sys.exit()

		except Exception as e:
			"""
			import sys, traceback
			print '\n---------------------'
			print 'Exception: %s' % e
			print '- - - - - - - - - - -'
			traceback.print_tb(sys.exc_info()[2])
			print "\n"
			"""
			continue

def game_thread():
	while True:
		try:
			frame = LogicalFrame()

			# "Game movement", or whatever
			for e in entities:
				e.x += (10 * e.direc)
				if e.x > 500:
					e.x = 500
					e.direc = -1
				elif e.x < -500:
					e.x = -500
					e.direc = 1

				frame.add(e)

			set_frame(frame)

		except:
			import sys, traceback
			print '\n---------------------'
			print 'Exception: %s' % e
			print '- - - - - - - - - - -'
			traceback.print_tb(sys.exc_info()[2])
			print "\n"

thread.start_new_thread(dac_thread, ('china',))
thread.start_new_thread(dac_thread, ('usa',))
thread.start_new_thread(game_thread, ())

while True:
	time.sleep(100000)

