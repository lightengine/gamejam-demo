import time
import math
import itertools
import sys
import thread
import random

from lib.frame import LogicalFrame

from entities.circle import Circle
from entities.square import Square

from set_frame import set_frame

entities = []
for i in range(10):
	entities.append(Circle())

for i in range(len(entities)):
	entity = entities[i]
	entity.laserKey = 'china' if i%2 == 0 else 'usa'
	#entity.x = random.randint(-5000, 5000)
	#entity.y = random.randint(-5000, 5000)
	entity.x = 2000*i
	entity.y = 2000*i
	entity.xVel = 100 if random.randint(0, 1) else -100
	entity.yVel = 100 if random.randint(0, 1) else -100

# define our game loops

def update_thread(dacs, distortions, queues):
	while True:
		try:
			frame = LogicalFrame()

			# "Game movement", or whatever
			for e in entities:
				e.x += e.xVel
				e.y += e.yVel
				if e.x > 10000:
					e.x = 10000
					e.xVel = random.randint(50, 1000) * -1
				elif e.x < -10000:
					e.x = -10000
					e.xVel = random.randint(50, 1000)
				if e.y > 10000:
					e.y = 10000
					e.yVel = random.randint(50, 1000) * -1
				elif e.y < -10000:
					e.y = -10000
					e.yVel = random.randint(50, 1000)

				frame.add(e)

			print 'update thread ended... set_frame() now'
			set_frame(frame, dacs, distortions, queues)
			time.sleep(0.05)

		except Exception as e:
			import sys, traceback
			print '\n---------------------'
			print 'Exception: %s' % e
			print '- - - - - - - - - - -'
			traceback.print_tb(sys.exc_info()[2])
			print "\n"

def game_thread(dacs, distortions):
	pass

def create_game_threads(dacs, distortions, queues):
	print 'creating game threads...'
	thread.start_new_thread(update_thread, (dacs, distortions, queues))

