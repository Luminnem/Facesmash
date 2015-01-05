from pygame import Rect

class Element(object):
	def __init__(self, state, x = 0, y = 0, autoUpdate = True, autoRender = True, width = 0, height = 0):
		state.elements.append(self)
		self.state = state
		
		self.tp = "nan"
		self.autoRender = autoRender
		self.autoUpdate = autoUpdate
		self.bounds = Rect(x, y, width, height)
	
	def doUpdate(self):
		#MUST BE OVERRIDE
		pass
	
	def doRender(self, screen):
		#MUST BE OVERRIDE
		pass
	
	def update(self):
		#MUSN'T BE MODIFIED
		if self.autoUpdate:
			self.doUpdate()
			
	def render(self, screen):
		#MUSN'T BE MODIFIED
		if self.autoRender:
			self.doRender(screen)
			
		
