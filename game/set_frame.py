"""
I hate this function.
I am sorry that it exists.
"""

from multiprocessing import Process, Queue


def set_frame(frame, dacs, distortions, queues):
	print 'set_frame(%s, %s, %s, queuuesss)' % \
			(str(frame), str(dacs), str(distortions))
	frame.setDistortions(distortions)
	frame.freeze()

	for key in ['china', 'usa']:
		physFrame = frame.getPhysical(key, distortions[key])
		queues.put(key, physFrame)

	"""
	for d in dacs.values():
		if not d:
			print 'no dac in set_frame'
			continue
		d.stream.setNextFrame(frame)
	"""

