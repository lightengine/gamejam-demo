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

class SOUND:
	#TROLOLO = Sound('trololo1.wav')
	#BEEP = Sound('beep.mp3')
	#ZIPPO = Sound('zippo-open-1.wav')
	MOTHER = Sound('mother_talk.wav')

