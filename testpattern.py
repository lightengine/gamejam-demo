#!/usr/bin/env python

import time
import math
import itertools
import sys
import random
import thread
from multiprocessing import Process, Queue

from lib import dac
from lib.common import *
from lib.set_frame import set_frame
from lib.stream import PointStream
from lib.entity import Entity
from lib.point import *
from lib.frame import *
from lib.wrap import Wrap
from lib.distortion import Distortion
from lib.queues import NonblockQueue

from entities.circle import Circle
from entities.square import Square

entities = []

IPAddrs = {
	'china':	'169.254.156.113',
	'usa':		'169.254.97.12',
}

queues = NonblockQueue()
queues.createQueue('china')
queues.createQueue('usa')

dacs = {}
dacs['china'] = None
dacs['usa']	  = None

distortions = {}
distortions['china'] = Distortion(5000, -6600, 0.75, 0.75,
		blankingSamplePts=15,
		trackingSamplePts=10
)
distortions['usa'] = Distortion(-5000, 6600,
		blankingSamplePts=30,
		trackingSamplePts=30
)

frame = LogicalFrame()

def dac_thread(key, queues):
	while True:
		try:
			print 'Connecting to dac @ %s' % IPAddrs[key]
			dacs[key] = dac.DAC(IPAddrs[key])
			d = dacs[key]
			d.stream = PointStream()
			d.stream.laserKey = key
			d.stream.setQueue(queues.getQueue(key))
			d.stream.distortion = distortions[key]
			print 'playing stream...!'
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

p1 = Process(target=dac_thread, args=('china', queues))
p2 = Process(target=dac_thread, args=('usa', queues))

p1.start()
p2.start()

for i in range(5) :
	for key in ['usa', 'china']:
		e = Square()
		e.laserKey = key
		e.x = 0 + (2000* i)
		e.y = 0 + (2000* i)
		entities.append(e)

def draw_thread(dacs, distortions, queues):
	while True:
		try:
			frame = LogicalFrame()
			tmpEnt = entities[:]
			for e in entities:
				frame.add(e)

			set_frame(frame, distortions, queues)
			time.sleep(1/60.0)

		except Exception as e:
			import sys, traceback
			print '\n---------------------'
			print 'Exception: %s' % e
			print '- - - - - - - - - - -'
			traceback.print_tb(sys.exc_info()[2])
			print "\n"


thread.start_new_thread(draw_thread, (dacs, distortions, queues))

while True:
	time.sleep(100000)

