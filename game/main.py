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
from entities.letterx import LetterX

entities = []
"""
for i in xrange(-2,3):
	tmpLine = Line()
	tmpLine.y = 3000 * i
	tmpLine.x = 21000
	tmpLine.laserKey = 'usa'
	entities.append(tmpLine)
"""
player = LetterX()

player.laserKey = 'usa'
player.scale = 10
player.rotation = .5
entities.append(player)

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
		joystick.get_button(4),
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



# FOR THE LOVE OF GOD LOOK AWAY THIS CODE IS HIDIOUS!



def update_thread():
	last_time = datetime.now()
	timeSinceMove = 0
	timeSinceShot = 0
	enemySpawnCounter = 0
	enemies, bullets = ([],[])
	while True:
		delta_t = datetime.now() - last_time

		pygame.event.pump()

		timeSinceMove-=delta_t.microseconds
		if timeSinceMove < 0:
			#move the player up and down the music lines
			if joystick.get_axis(1) < -0.5 and player.y<6000:
				player.y += 3000
				timeSinceMove = 150000
			if joystick.get_axis(1) > 0.5 and player.y>-6000:
				player.y -= 3000
				timeSinceMove = 150000

		#move player back and froth
		if player.x>-20000 and player.x<20000:
			player.x -= (delta_t.microseconds/50) * joystick.get_axis(0)
			if player.x<-20000:
				player.x = -19999
			if player.x>20000:
				player.x = 19999


		#create enemies
		enemySpawnCounter -= delta_t.microseconds
		if enemySpawnCounter < 0:
			enemy = Square()
			enemy.laserKey = 'china'
			enemy.x = -22000
			enemy.y = random.randint(-2,2) * 3000
			enemies.append(enemy)
			entities.append(enemy)
			enemySpawnCounter = random.randint(1000000,5000000)
		
		#move/collide enemies/player
		enemyDeleteList = []
		for enemy in enemies:
			enemy.x += delta_t.microseconds * 0.01
			if enemy.x > 20000:
				enemyDeleteList.append(enemy)		

		#create bullets
		timeSinceShot -= delta_t.microseconds
		if joystick.get_button(11) and timeSinceShot<0:
			bullet = Line()
			bullet.laserKey = 'usa'
			bullet.x = player.x - 1000
			bullet.y = player.y
			bullets.append(bullet)
			entities.append(bullet)
			timeSinceShot = 400000


		#move/collide bullets
		bulletDeleteList = []
		for bullet in bullets:
			bullet.x -= delta_t.microseconds * 0.03
			#check for off screen
			if bullet.x < -20000:
				bulletDeleteList.append(bullet)
			else:
				#check for collision with enemy
				for enemy in enemies:
					# all enemies are 2000 points wide
					if abs(bullet.x - enemy.x)<1000 and bullet.y == enemy.y:
						#remove enemy
						enemyDeleteList.append(enemy)
						enemy.doDelete = True
						#remove bullet
						bulletDeleteList.append(bullet)


		for enemy in enemyDeleteList:
			enemy.doDelete = True
			enemies.remove(enemy)
			thread.start_new_thread(destroy_thread, (enemy,))

		for bullet in bulletDeleteList:
			bullets.remove(bullet)
			thread.start_new_thread(destroy_thread, (bullet,))

		last_time = datetime.now()
		time.sleep(1/100.0)

def destroy_thread(entity):
	animationCounter = 500000
	last_time = datetime.now()

	while animationCounter>0:
		delta_t = datetime.now() - last_time
		entity.scale += 0.1
		entity.rotateZ += random.randint(0,5) * 0.1
		entity.initMatStack()
		entity.pushRotateX(2*math.pi * entity.scale*-0.01)
		entity.pushRotateY(2*math.pi * entity.scale*0.02)
		entity.doneMatStack()
		animationCounter -= delta_t.microseconds
		last_time = datetime.now()
		time.sleep(1/30.0)
	entities.remove(entity)

def create_game_threads(dacs, distortions, queues):
	thread.start_new_thread(draw_thread, (dacs, distortions, queues))
	thread.start_new_thread(update_thread,())
