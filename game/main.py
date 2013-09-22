import time
import math
import itertools
import sys
import thread

from datetime import datetime


from lib.frame import LogicalFrame

from entities.circle import Circle
from entities.square import Square

from set_frame import set_frame

entities = []

player = Circle()

entities.append(player)

# define our game loops
def draw_thread(dacs, distortions):
	while True:
		try:
			frame = LogicalFrame()
			for e in entities:
				frame.add(e)

			set_frame(frame, dacs, distortions)

		except Exception as e:
			import sys, traceback
			print '\n---------------------'
			print 'Exception: %s' % e
			print '- - - - - - - - - - -'
			traceback.print_tb(sys.exc_info()[2])
			print "\n"


def update_thread():
		last_time = datetime.now()
		while True:
			delta_t = datetime.now() - last_time
			update(delta_t)
			last_time = datetime.now()


def create_game_threads(dacs, distortions):
	thread.start_new_thread(draw_thread, (dacs, distortions))
	thread.start_new_thread(update_thread,())

# FOR THE LOVE OF GOD LOOK AWAY THIS CODE IS HIDIOUS!

def update(delta_t):
	#move the player
	pass
	