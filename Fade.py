from pygame import Rect, Surface
class Fade(object):
	def __init__(self, seconds, colors):
		self.rect = Rect(0, 0, WIDTH, HEIGHT)
		
		self.surface = Surface((WIDTH, HEIGHT), py.SRCALPHA, 32).convert_alpha()
		self.background = Surface((WIDTH, HEIGHT), py.SRCALPHA, 32).convert_alpha()
		
		
		
		self.speed = 5 	 # TOUCHING ONLY IF YOU KNOW WHAT YOU'RE DOING
		self.limit = 255 # TOUCHING ONLY IF YOU KNOW WHAT YOU'RE DOING
		
		
		self.seconds = seconds
		
		
		#---------------------------WARNING-----------------------------#
		self.milliseconds = self.seconds * 1000							#
		self.ticks = self.milliseconds / (self.limit / self.speed)		#
		self.timer = Timer(self.ticks) # Clock							#
		#---------------------------------------------------------------#
		
		
		self.alpha = 0
		
		#self.color = colors
		
		self.color = [
		(243, 233, 229),
		(245, 68, 0),
		(238, 165, 130),
		(255, 250, 244),
		(255, 255, 255),
		(255, 255, 251),
		(250, 214, 165),
		(38, 83, 141),
		(0, 85, 165),
		(25, 25, 112),
		(0, 0, 0)]
		
		self.cur = 0
				
	def update(self):
		if self.timer.update():
			if self.alpha < 255:
				self.alpha += self.speed
			else:
				self.alpha = 0
				self.cur += 1
				if self.cur >= len(self.color):
					self.cur = 0
		
		if self.cur + 1 < len(self.color):
			cur = self.cur + 1
		else:
			cur = 0			
			
		self.background.fill(self.color[cur] + (self.alpha,))
		self.surface.fill(self.color[self.cur] + (255 - self.alpha,))
			
	def render(self, screen):
		screen.blit(self.background, (0, 0))
		screen.blit(self.surface, (0, 0))
				
