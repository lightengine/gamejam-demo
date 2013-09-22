import time
import math
import itertools
import sys
import thread

from datetime import *

from Game import *

from lib.frame import LogicalFrame

from entities.circle import Circle
from entities.square import Square

from set_frame import set_frame


# define our game loops
def draw_thread(dacs, distortions, game_objects):
	while True:
		try:
			frame = LogicalFrame()
			for gObject in game_objects:
				if hasattr(gObject, 'entity') && gObject.entity != None
					fame.add(gObject.entity)

			set_frame(frame, dacs, distortions)

		except Exception as e:
			import sys, traceback
			print '\n---------------------'
			print 'Exception: %s' % e
			print '- - - - - - - - - - -'
			traceback.print_tb(sys.exc_info()[2])
			print "\n"

def update_thread:(game)
		last_time = datetime.now()
		while True:
			delta_t = datetime.now() - last_time
			game.update(delta_t)
			last_time = datetime.now()

def create_game_threads(dacs, distortions):
	factory = new GameFactory()
	message_bus = new MessageBus()
	game_objects = []
	game = new Game(factory, game_objects, message_bus)


	thread.start_new_thread(draw_thread, (dacs, distortions, game_objects))
	thread.start_new_thread(update_thread,(game))

