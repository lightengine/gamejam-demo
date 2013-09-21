#!/usr/bin/env python

import time
import math
import itertools
import sys
import thread

from lib import dac
from lib.common import *
from lib.stream import *
from lib.entity import Entity
from lib.point import *
from lib.wrap import Wrap


IPAddrs = {
	'china':	'169.254.156.114',
	'usa':		'169.254.97.16',
}

class Circle(Entity):
	def __init__(self, samplePts=100, radius=1000):
		super(Circle, self).__init__()
		for i in range(0, samplePts):
			i = float(i) / samplePts * 2 * math.pi
			x = int(math.cos(i) * radius)
			y = int(math.sin(i) * radius)
			self.points.append(Point(x, y))

def dac_thread(ip):
	while True:
		try:
			print 'Dac for %s' % ip
			d = dac.DAC(ip)
			ps = PointStream()
			ps.objects.append(Wrap(Circle()))
			d.play_stream(ps)

		except KeyboardInterrupt:
			sys.exit()

		except Exception as e:
			import sys, traceback
			print '\n---------------------'
			print 'Exception: %s' % e
			print '- - - - - - - - - - -'
			traceback.print_tb(sys.exc_info()[2])
			print "\n"

thread.start_new_thread(dac_thread, (IPAddrs['china'],))
thread.start_new_thread(dac_thread, (IPAddrs['usa'],))

while True:
	time.sleep(100000)

