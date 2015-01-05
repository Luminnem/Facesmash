class State(object):
	def __init__(self, statesManager):
		statesManager.states.append(self)
		self.statesManager = statesManager
		self.elements = []
		
	def update(self):
		for element in self.elements:
			element.update()
			
	def render(self, screen):
		for element in self.elements:
			element.render(screen)
