

def set_frame(frame, dacs, distortions):
	frame.setDistortions(distortions)
	frame.freeze()
	for d in dacs.values():
		if not d:
			continue
		d.stream.setNextFrame2(frame)

	"""
	for laserKey, d in dacs.iteritems():
		physFrame = frame.getPhysical(laserKey)
		d.stream.setNextPhysicalFrame(physFrame)
	"""

