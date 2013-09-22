import time
import math
import itertools
import sys
import thread
import random
from datetime import datetime
from lib.frame import LogicalFrame
from lib.set_frame import set_frame

from entities.circle import Circle
from entities.square import Square
from entities.note1 import Note1
from entities.arrow import Arrow
from entities.line import Line
from entities.letterx import LetterX

entities = []

for i in xrange(-2,3):
	tmpLine = Line()
	tmpLine.y = 3000 * i
	tmpLine.x = 10000
	tmpLine.laserKey = 'usa'
	entities.append(tmpLine)

player = LetterX()
player.tempRotX = 0.0
player.tempRotY = 0.0
player.tempRotZ = 0.0


player.laserKey = 'china'
player.scale = 2
player.rotation = .5
entities.append(player)

# define our game loops

def draw_thread(dacs, distortions, queues):
	while True:
		try:
			frame = LogicalFrame()
			for e in entities:
				frame.add(e)

			set_frame(frame, distortions, queues)
			time.sleep(0.05)

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
			update(delta_t.microseconds)
			last_time = datetime.now()

			time.sleep(0.05);

def create_game_threads(dacs, distortions, queues):
	thread.start_new_thread(draw_thread, (dacs, distortions, queues))
	thread.start_new_thread(update_thread,())

# FOR THE LOVE OF GOD LOOK AWAY THIS CODE IS HIDIOUS!

PERIOD = 2*math.pi

def update(delta_t):
	player.tempRotX += 0.1
	if player.tempRotX > PERIOD:
		player.tempRotX = 0

	player.tempRotY += 0.07
	if player.tempRotY > PERIOD:
		player.tempRotY = 0

	player.tempRotZ += 0.09
	if player.tempRotZ > PERIOD:
		player.tempRotZ = 0

	#move the player
	player.rotateZ += 0.1
	player.rotateX += 0.00001

	player.initMatStack()
	#player.pushRotateZ(player.tempRotZ)
	#player.pushRotateX(math.pi/140)
	player.pushRotateY(player.tempRotY)
	#player.pushRotateX(player.tempRotX)
	player.doneMatStack()

