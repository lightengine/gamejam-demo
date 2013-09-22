import time
import math
import itertools
import sys
import thread
import random
from datetime import datetime
from lib.frame import LogicalFrame
from lib.set_frame import set_frame
from lib.position import Position

from entities.circle import Circle
from entities.square import Square
from entities.note1 import Note1
from entities.arrow import Arrow
from entities.letterx import LetterX
from entities.triangle import Triangle

entities = []

# TRIFORCE
triforce = {
	'power': Triangle(),
	'courage': Triangle(),
	'wisdom': Triangle(),
}

initialLoc= {
	'power': Position(0, 15000),
	'courage': Position(-15000, 0),
	'wisdom': Position(15000, 0),
}

finalLoc = {
	'power': Position(0, 3800),
	'courage': Position(-2200, 0),
	'wisdom': Position(2200, 0),
}

for key in triforce:
	triforce[key].laserKey = 'china'
	triforce[key].x = initialLoc[key].x
	triforce[key].y = initialLoc[key].y
	triforce[key].percent = 0.0
	triforce[key].percentInc = 0.04
	triforce[key].percentIncStep = -0.0005
	triforce[key].tempRotX = 0
	triforce[key].tempRotY = 0
	triforce[key].tempRotZ = 0
	entities.append(triforce[key])

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
	inc = max(triforce['power'].percentInc + triforce['power'].percentIncStep,
				0.002)
	triforce['power'].percentInc = inc
	percent = min(triforce['power'].percent + inc, 1.0)
	triforce['power'].percent = percent

	for key in ['power', 'courage', 'wisdom']:
		dLoc = finalLoc[key] - initialLoc['power']
		pLoc = initialLoc[key].percentTo(finalLoc[key],
											triforce['power'].percent)

		triforce[key].x = pLoc.x
		triforce[key].y = pLoc.y
		triforce[key].rotateZ = PERIOD * percent

		triforce[key].initMatStack()
		if key in ['power']:
			triforce[key].pushRotateX(2*PERIOD * percent)
			#triforce[key].pushRotateY(-2*PERIOD * percent)
		if key in ['courage']:
			triforce[key].pushRotateX(2*PERIOD * percent)
			#triforce[key].pushRotateY(-2*PERIOD * percent)
		if key in ['wisdom']:
			triforce[key].pushRotateX(2*PERIOD * percent)
			#triforce[key].pushRotateY(2*PERIOD * percent)
		triforce[key].doneMatStack()

