import os
import pygame

pygame.init()
#pygame.mixer.init()
#freq = 48000
freq = 44100
#freq = 22050
#freq = 11025
#pygame.mixer.init()
#pygame.mixer.init(freq, 8, 2, 2048)
size = -16
size = 8
buff=2048
#buff=4096
pygame.mixer.init(frequency=freq, size=size, channels=2, buffer=buff)

class Sound(object):

	def __init__(self, filename):
		direc = os.path.abspath(os.path.join(os.path.dirname(__file__), '../sounds'))
		filename = os.path.join(direc, filename)

		print filename

		self.filename = filename
		self.sound = pygame.mixer.Sound(filename)

	def play(self):
		pygame.event.pump()
		channel = self.sound.play()
		#while channel.get_busy():
		#	pygame.time.delay(100)

	def playLoop(self):
		pygame.event.pump()
		channel = self.sound.play(loops=-1)

	def stop(self):
		pygame.event.pump()
		self.sound.stop()

class SOUND:
	#TROLOLO = Sound('trololo1.wav')
	#BEEP = Sound('beep.mp3')
	#ZIPPO = Sound('zippo-open-1.wav')
	ZELDA = Sound('zelda_oot_item.wav')
	MOTHER = Sound('mother_talk.wav')
	TECHNO = Sound('techno1.wav')
	MARIO_DIE = Sound('smb_mariodie.wav')
	LASERS = [
		Sound('laser1.wav'),
		Sound('laser2.wav'),
		Sound('laser3.wav'),
	]
	PIANOS = [
		Sound('piano/pianotone_a.wav'),
		Sound('piano/pianotone_aflat.wav'),
		Sound('piano/pianotone_b.wav'),
		Sound('piano/pianotone_bflat.wav'),
		Sound('piano/pianotone_c.wav'),
		Sound('piano/pianotone_cmiddle.wav'),
		#Sound('piano/pianotone_d.wav'),
		#Sound('piano/pianotone_eflat.wav'),
		Sound('piano/pianotone_f.wav'),
		Sound('piano/pianotone_g.wav'),
		#Sound('piano/pianotone_gflat.wav'),
	]

