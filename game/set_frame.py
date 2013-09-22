"""
I hate this function.
I am sorry that it exists.
"""

def set_frame(frame, dacs, distortions):
	frame.setDistortions(distortions)
	frame.freeze()
	for d in dacs.values():
		if not d:
			continue
		d.stream.setNextFrame(frame)

