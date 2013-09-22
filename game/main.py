import time
import math
import itertools
import sys
import thread
import random
import pygame

from datetime import datetime
from lib.frame import LogicalFrame
from lib.set_frame import set_frame

from entities.circle import Circle
from entities.square import Square
from entities.note1 import Note1
from entities.arrow import Arrow
from entities.line import Line
from game.player import Player
from entities.triangle import Triangle
from entities.cross import Cross
from sound import *
from game.enemy import Enemy
from lib.position import Position
entities = []


pygame.joystick.init()
pygame.display.init()
	# Wait until we have joystick
while not pygame.joystick.get_count():
	print "No joystick detected!"
	time.sleep(5)

joystick = pygame.joystick.Joystick(0)
joystick.init()


# define our game loops

def draw_thread(dacs, distortions, queues):
	while True:
		try:
			frame = LogicalFrame()
			tmpEnt = entities[:]
			for e in tmpEnt:
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



"""
		buttons = [
		joystick.get_button(0),
		joystick.get_button(1),
		joystick.get_button(2),
		joystick.get_button(3),
		joystick.get_button(4),#start button
		joystick.get_button(5),#up arrow
		joystick.get_button(6),#rightarrow
		joystick.get_button(7),#down arrow
		joystick.get_button(8),
		joystick.get_button(9),
		joystick.get_button(10),
		joystick.get_button(11),#r1
		joystick.get_button(12),#triangle
		joystick.get_button(13),#o
		joystick.get_button(14),#x
		joystick.get_button(15),#square
		joystick.get_button(16)
		]
		axis = [
		joystick.get_axis(0),#left x
		joystick.get_axis(1),#left y
		joystick.get_axis(2),#right x
		joystick.get_axis(3)#right y
		]
"""

class GAME:
	difficulty = 1
	timeSinceMove = 0
	timeSinceShot = 0
	enemySpawnCounter = 0
	player = None
	enemies, bullets = ([], [])
	changeGameState = 0
# FOR THE LOVE OF GOD LOOK AWAY THIS CODE IS HIDIOUS!
def update_thread():
	last_time = datetime.now()
	gameState = 0
	while True:
		delta_t = datetime.now() - last_time
		pygame.event.pump()
		if GAME.changeGameState == -1:
			if gameState == 1:
				game_loop(delta_t)
			elif gameState == 0:
				triforce_loop(delta_t.microseconds)

		if GAME.changeGameState == 1:
			game_loop(delta_t, True)
			GAME.changeGameState = -1
			gameState = 1
		if GAME.changeGameState == 0:
			triforce_loop(delta_t.microseconds, True)
			GAME.changeGameState = -1
			gameState = 0

		last_time = datetime.now()
		time.sleep(1 / 60.0)

#game_loop

def game_loop(delta_t, init=False):
	if init:
		GAME.timeSinceMove = 0
		GAME.timeSinceShot = 0
		GAME.enemySpawnCounter = 0
		GAME.enemies, GAME.bullets = ([], [])
		GAME.difficulty = 1

		GAME.player = Player()
		GAME.player.entity = Cross()
		GAME.player.type = 2
		GAME.player.entity.laserKey = 'usa'
		entities.append(GAME.player.entity)

	GAME.difficulty += delta_t.microseconds / 6000000.0
	print(GAME.difficulty)
	if joystick.get_button(12):
			if GAME.player.type != 0:
					tmp = Triangle()
					tmp.x = GAME.player.entity.x
					tmp.y = GAME.player.entity.y
					tmp.laserKey = 'usa'
					entities.remove(GAME.player.entity)
					GAME.player.entity = tmp
					entities.append(GAME.player.entity)
					GAME.player.type = 0
	if joystick.get_button(13):
			if GAME.player.type != 1:
					tmp = Circle()
					tmp.x = GAME.player.entity.x
					tmp.y = GAME.player.entity.y
					tmp.laserKey = 'usa'
					entities.remove(GAME.player.entity)
					GAME.player.entity = tmp
					entities.append(GAME.player.entity)
					GAME.player.type = 1
	if joystick.get_button(14):
			if GAME.player.type != 2:
					tmp = Cross()
					tmp.x = GAME.player.entity.x
					tmp.y = GAME.player.entity.y
					tmp.laserKey = 'usa'
					entities.remove(GAME.player.entity)
					GAME.player.entity = tmp
					entities.append(GAME.player.entity)
					GAME.player.type = 2
	if joystick.get_button(15):
			if GAME.player.type != 3:
					tmp = Square()
					tmp.x = GAME.player.entity.x
					tmp.y = GAME.player.entity.y
					tmp.laserKey = 'usa'
					entities.remove(GAME.player.entity)
					GAME.player.entity = tmp
					entities.append(GAME.player.entity)
					GAME.player.type = 3

	GAME.timeSinceMove -= delta_t.microseconds
	if GAME.timeSinceMove < 0:
			#move the player up and down the music lines
			if joystick.get_axis(1) < -0.5 and GAME.player.entity.y < 6000:
					GAME.player.entity.y += 3000
					GAME.timeSinceMove = 150000
			if joystick.get_axis(1) > 0.5 and GAME.player.entity.y > -6000:
					GAME.player.entity.y -= 3000
					GAME.timeSinceMove = 150000

	#move player back and froth
	if GAME.player.entity.x > -20000 and GAME.player.entity.x < 20000:
			GAME.player.entity.x -= (delta_t.microseconds / 50) * joystick.get_axis(0)
			if GAME.player.entity.x < -20000:
					GAME.player.entity.x = -19999
			if GAME.player.entity.x > 20000:
					GAME.player.entity.x = 19999


	#create enemies
	GAME.enemySpawnCounter -= delta_t.microseconds
	if GAME.enemySpawnCounter < 0:
			enemy = Enemy()
			#0 = tri 3 = square
			enemy.type = random.randint(0, 3)
			if enemy.type == 0:
				enemy.entity = Triangle()
			elif enemy.type == 1:
				enemy.entity = Circle()
			elif enemy.type == 2:
				enemy.entity = Cross()
			elif enemy.type == 3:
				enemy.entity = Square()

			enemy.entity.laserKey = 'china'
			enemy.entity.x = -22000
			enemy.entity.y = random.randint(-2, 2) * 3000
			GAME.enemies.append(enemy)
			entities.append(enemy.entity)
			GAME.enemySpawnCounter = random.randint(2000000, 4000000) - (GAME.difficulty * 100000)

	#move/collide enemies/player
	enemyDeleteList = []

	bulletDeleteList = []
	for enemy in GAME.enemies:
			enemy.entity.x += delta_t.microseconds * 0.01
			if enemy.entity.x > 20000:
				enemy.entity.no_animation = True
				enemyDeleteList.append(enemy)
			elif abs(enemy.entity.x - GAME.player.entity.x) < 1000 and GAME.player.type == enemy.type and GAME.player.entity.y == enemy.entity.y:
				#YOU LOOSE, YOU GET NOTHING! YOU ATE THE FIZZY LIFTING DRINK VOIDING THE CONTRACT THERFOR YOU GET NOTHING!
				GAME.changeGameState = 0
				entities.remove(GAME.player.entity)
				for enemy in GAME.enemies:
					enemy.entity.no_animation = True
					enemyDeleteList.append(enemy)
				for bullet in GAME.bullets:
					bulletDeleteList.append(bullet)

	#create bullets
	GAME.timeSinceShot -= delta_t.microseconds
	if joystick.get_button(11) and GAME.timeSinceShot < 0:
			random.choice(SOUND.LASERS).play()
			bullet = Line()
			bullet.laserKey = 'usa'
			bullet.type = GAME.player.type
			bullet.x = GAME.player.entity.x - 1000
			bullet.y = GAME.player.entity.y
			GAME.bullets.append(bullet)
			entities.append(bullet)
			GAME.timeSinceShot = 400000

	#move/collide bullets
	for bullet in GAME.bullets:
			bullet.x -= delta_t.microseconds * 0.03
			#check for off screen
			if bullet.x < -20000:
					bulletDeleteList.append(bullet)
			else:
					#check for collision with enemy
					for enemy in GAME.enemies:
							# all enemies are 2000 points wide
							if abs(bullet.x - enemy.entity.x) < 1000 and bullet.y == enemy.entity.y and bullet.type == enemy.type:
									#remove enemy
									enemyDeleteList.append(enemy)
									#remove bullet
									bulletDeleteList.append(bullet)

	for enemy in enemyDeleteList:
			if enemy in GAME.enemies:
				GAME.enemies.remove(enemy)
			thread.start_new_thread(destroy_thread, (enemy.entity,))

	for bullet in bulletDeleteList:
		if bullet in GAME.bullets:
			GAME.bullets.remove(bullet)
		if bullet in entities:
			entities.remove(bullet)


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
PERIOD = 2*math.pi
def triforce_loop(delta_t, init=False):
	if init:
		SOUND.ZELDA.play()
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
			triforce[key].scale = 1.0 # denormilize
			entities.append(triforce[key])

	if joystick.get_button(3):
		GAME.changeGameState = 1
		for key in triforce:
			entities.remove(triforce[key])

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

def destroy_thread(entity):
		if not hasattr(entity, 'no_animation'):
			animationCounter = 500000
			last_time = datetime.now()
			sound = random.choice(SOUND.PIANOS)
			sound.play()

			if not hasattr(entity, 'xRotInc'):
					# Must maintain rotation state
					entity.xRotState = 0.0
					entity.yRotState = 0.0

					# Random, unique rotations
					sign = 1 if random.randint(0, 1) else -1
					entity.xRotInc = sign * random.uniform(0.01, 1.2)
					sign = 1 if random.randint(0, 1) else -1
					entity.yRotInc = sign * random.uniform(0.01, 1.2)
					sign = 1 if random.randint(0, 1) else -1
					entity.zRotInc = sign * random.uniform(0.01, 1.2)
					entity.scaleInc = random.uniform(0.2, 0.5)

					time.sleep(1 / 30.0)

			while animationCounter > 0:
					delta_t = datetime.now() - last_time
					entity.scale += entity.scaleInc
					entity.rotateZ += entity.zRotInc

					entity.xRotState += entity.xRotInc
					entity.yRotState += entity.yRotInc

					entity.initMatStack()
					entity.pushRotateX(entity.xRotState)
					entity.pushRotateY(entity.yRotState)
					entity.doneMatStack()
					animationCounter -= delta_t.microseconds
					last_time = datetime.now()
					time.sleep(1 / 30.0)
		if entity in entities:
			entities.remove(entity)
		time.sleep(1 / 30.0)


def create_game_threads(dacs, distortions, queues):
		thread.start_new_thread(draw_thread, (dacs, distortions, queues))
		thread.start_new_thread(update_thread, ())

