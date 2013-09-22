
from multiprocessing import Queue

class NonblockQueue(object):
	def __init__(self):
		self.queues = {}

	def createQueue(self, key):
		self.queues[key] = Queue(maxsize=1)

	def getQueue(self, key):
		return self.queues[key]

	def put(self, key, value):
		try:
			self.queues[key].put(value, block=False)
		except:
			pass

	def get(self, key):
		try:
			return self.queues[key].get(block=False)
		except:
			pass

