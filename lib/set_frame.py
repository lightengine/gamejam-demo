"""
I hate this function.
I am sorry that it exists.
"""

def set_frame(frame, distortions, queues):
	frame.setDistortions(distortions)
	frame.freeze()

	for key in ['china', 'usa']:
		physFrame = frame.getPhysical(key, distortions[key])
		queues.put(key, physFrame)

