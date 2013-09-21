#!/usr/bin/env python

import time
import math
import itertools
import sys
import thread

from lib import dac
from lib.common import *
from lib.stream import PointStream
from lib.entity import Entity
from lib.point import *
from lib.frame import *
from lib.wrap import Wrap

from entities.circle import Circle
from entities.square import Square

IPAddrs = {
	'china':	'169.254.156.114',
	'usa':		'169.254.97.16',
}

dacs = {}
dacs['china'] = dac.DAC(IPAddrs['china'])
dacs['usa']	  = dac.DAC(IPAddrs['usa'])

entities = []
entities.append(Circle())
entities.append(Square())

entities[0].x = 10000
entities[0].y = 10000
entities[0].laserKey = 'china'
entities[1].laserKey = 'usa'

frame = LogicalFrame()
frame.add(entities[0])
frame.add(entities[1])

def set_frame(frame):
	frame.freeze()
	for d in dacs.values():
		d.stream.setNextFrame(frame)

def dac_thread(key):
	d = dacs[key]
	d.stream = PointStream()
	while True:
		try:
			d.play_stream(d.stream)

		except KeyboardInterrupt:
			sys.exit()

		except Exception as e:
			import sys, traceback
			print '\n---------------------'
			print 'Exception: %s' % e
			print '- - - - - - - - - - -'
			traceback.print_tb(sys.exc_info()[2])
			print "\n"

def game_thread():
	while True:
		try:
			frame = LogicalFrame()

			# "Game movement", or whatever
			for e in entities:
				e.x += (10 * e.direc)
				if e.x > 5000:
					e.x = 5000
					e.direc = -1
				elif e.x < -5000:
					e.x = -5000
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

