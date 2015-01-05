class StatesManager(object):
	def __init__(self):
		self.current = 0
		self.states = []
		
	def update(self):
		if len(self.states) > 0:
			self.states[self.current].update()
		
	def render(self, screen):
		if len(self.states) > 0:
			self.states[self.current].render(screen)
