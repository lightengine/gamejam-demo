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
from game.enemy import Enemy

entities = []
player = Player()
player.entity = Cross()
player.type = 3

player.entity.laserKey = 'usa'
entities.append(player.entity)

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
						time.sleep(1 / 60.0)

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



# FOR THE LOVE OF GOD LOOK AWAY THIS CODE IS HIDIOUS!



def update_thread():
		last_time = datetime.now()
		timeSinceMove = 0
		timeSinceShot = 0
		enemySpawnCounter = 0
		enemies, bullets = ([], [])
		difficulty = 1
		while True:
				delta_t = datetime.now() - last_time
				pygame.event.pump()
				difficulty += delta_t.microseconds / 6000000.0
				print(difficulty)
				if joystick.get_button(12):
						if player.type != 0:
								tmp = Triangle()
								tmp.x = player.entity.x
								tmp.y = player.entity.y
								tmp.laserKey = 'usa'
								entities.remove(player.entity)
								player.entity = tmp
								entities.append(player.entity)
								player.type = 0
				if joystick.get_button(13):
						if player.type != 1:
								tmp = Circle()
								tmp.x = player.entity.x
								tmp.y = player.entity.y
								tmp.laserKey = 'usa'
								entities.remove(player.entity)
								player.entity = tmp
								entities.append(player.entity)
								player.type = 1
				if joystick.get_button(14):
						if player.type != 2:
								tmp = Cross()
								tmp.x = player.entity.x
								tmp.y = player.entity.y
								tmp.laserKey = 'usa'
								entities.remove(player.entity)
								player.entity = tmp
								entities.append(player.entity)
								player.type = 2
				if joystick.get_button(15):
						if player.type != 3:
								tmp = Square()
								tmp.x = player.entity.x
								tmp.y = player.entity.y
								tmp.laserKey = 'usa'
								entities.remove(player.entity)
								player.entity = tmp
								entities.append(player.entity)
								player.type = 3

				timeSinceMove -= delta_t.microseconds
				if timeSinceMove < 0:
						#move the player up and down the music lines
						if joystick.get_axis(1) < -0.5 and player.entity.y < 6000:
								player.entity.y += 3000
								timeSinceMove = 150000
						if joystick.get_axis(1) > 0.5 and player.entity.y > -6000:
								player.entity.y -= 3000
								timeSinceMove = 150000

				#move player back and froth
				if player.entity.x > -20000 and player.entity.x < 20000:
						player.entity.x -= (delta_t.microseconds / 50) * joystick.get_axis(0)
						if player.entity.x < -20000:
								player.entity.x = -19999
						if player.entity.x > 20000:
								player.entity.x = 19999


				#create enemies
				enemySpawnCounter -= delta_t.microseconds
				if enemySpawnCounter < 0:
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
						enemies.append(enemy)
						entities.append(enemy.entity)
						enemySpawnCounter = random.randint(2000000, 4000000) - (difficulty * 100000)

				#move/collide enemies/player
				enemyDeleteList = []
				for enemy in enemies:
						enemy.entity.x += delta_t.microseconds * 0.01
						if enemy.entity.x > 20000:
							enemy.entity.no_animation = True
							enemyDeleteList.append(enemy)

				#create bullets
				timeSinceShot -= delta_t.microseconds
				if joystick.get_button(11) and timeSinceShot < 0:
						bullet = Line()
						bullet.laserKey = 'usa'
						bullet.type = player.type
						bullet.x = player.entity.x - 1000
						bullet.y = player.entity.y
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
										if abs(bullet.x - enemy.entity.x) < 1000 and bullet.y == enemy.entity.y and bullet.type == enemy.type:
												#remove enemy
												enemyDeleteList.append(enemy)
												#remove bullet
												bulletDeleteList.append(bullet)

				for enemy in enemyDeleteList:
						if enemy in enemies:
							enemies.remove(enemy)
						thread.start_new_thread(destroy_thread, (enemy.entity,))

				for bullet in bulletDeleteList:
					if bullet in bullets:
						bullets.remove(bullet)
					if bullet in entities:
						entities.remove(bullet)

				last_time = datetime.now()
				time.sleep(1 / 100.0)


def destroy_thread(entity):
		if not hasattr(entity, 'no_animation'):
			animationCounter = 500000
			last_time = datetime.now()

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

