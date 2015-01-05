class Timer(object):
	def __init__(self, delay):
		self.time = py.time.get_ticks()
		self.delay = delay
		
	def update(self):
		if py.time.get_ticks() - self.time > self.delay:
			self.time = py.time.get_ticks()
			return True
		else:
			return False
