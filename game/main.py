import time
import math
import itertools
import sys
import thread

from lib.frame import LogicalFrame

from entities.circle import Circle
from entities.square import Square

from set_frame import set_frame

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

# define our game loops

def update_thread(dacs, distortions):
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

			set_frame(frame, dacs, distortions)

		except Exception as e:
			import sys, traceback
			print '\n---------------------'
			print 'Exception: %s' % e
			print '- - - - - - - - - - -'
			traceback.print_tb(sys.exc_info()[2])
			print "\n"

def game_thread(dacs, distortions):
	pass

def create_game_threads(dacs, distortions):
	thread.start_new_thread(update_thread, (dacs, distortions))

