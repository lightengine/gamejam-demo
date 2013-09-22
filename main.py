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

from game.main import *

IPAddrs = {
	'china':	'169.254.156.112',
	'usa':		'169.254.97.13',
}

dacs = {}
dacs['china'] = None
dacs['usa']	  = None

distortions = {}
distortions['china'] = Distortion(5000, -6600, 0.75, 0.75)
distortions['usa'] = Distortion(-5000, 6600)

frame = LogicalFrame()

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

thread.start_new_thread(dac_thread, ('china',))
thread.start_new_thread(dac_thread, ('usa',))

create_game_threads(dacs, distortions)

while True:
	time.sleep(100000)

