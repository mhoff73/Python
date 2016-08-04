import random
import pygame
import math
class Ball(object):
	
	
	def __init__ (self, x, y, color, x_speed, y_speed, size):
		self.x = x
		self.y = y
		self.color = color
		self.x_speed = x_speed
		self.y_speed = y_speed
		self.size = size
	
	def move (self, screen, bouncing_balls):		
		
			
		#if ball is touching another ball
		# for ball in bouncing_balls:
			# if ball == self:
				# continue
			# else:
				# dist = math.sqrt((self.x - ball.x)**2 + (self.y - ball.y)**2)
				# if dist <= (self.size+ball.size):
					# if ball.x == self.x:	#next to each other
						# self.change_x_speed()
						# ball.change_x_speed()
					# elif ball.y == self.y:	#above/below
						# self.change_y_speed()
						# ball.change_y_speed()
					# else:	#on a diagonal
						# if ball.x_speed < 0 and self.x_speed < 0:
							# self.change_x_speed()
							# ball.change_x_speed()
							# self.change_y_speed()
							# ball.change_y_speed()
						
		#if ball is touching a wall
		if self.x >= (700-self.size) or self.x <= (0+self.size):
			self.x_speed *= -1
		if self.y >= (500-self.size) or self.y <= (0+self.size):
			self.y_speed *= -1
			
		self.x+= self.x_speed
		self.y+= self.y_speed
		
		pygame.draw.circle(screen, self.color, (self.x,self.y), self.size)
		
	def change_x_speed (self):
		self.x_speed *= -1
		
	def change_y_speed (self):
		self.y_speed *= -1
		
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (127, 127, 127)
PURPLE = (210, 25, 240)
YELLOW = (255, 255, 0)
LIGHT_BLUE = (0, 255, 255)

color_list = [BLACK, WHITE, RED, BLUE, GREY, PURPLE, YELLOW, GREEN]



pygame.init()

# Set the width and height of the screen [width, height]
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Bouncing Ball Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

bouncing_balls = []

		
# -------- Main Program Loop -----------
while not done:
	# --- Main event loop
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		if event.type == pygame.MOUSEBUTTONDOWN:
			x = pygame.mouse.get_pos()[0]
			y = pygame.mouse.get_pos()[1]
			color = color_list[random.randint(0,len(color_list)-1)]
			x_speed = random.randint(-10,10)
			y_speed = random.randint(-10,10)
			size = random.randint(20,80)
			bouncing_balls.append(Ball(x, y, color, x_speed, y_speed, size))
			
	screen.fill(LIGHT_BLUE)
	
	for ball in bouncing_balls:
		ball.move(screen, bouncing_balls)
		
	pygame.display.flip()
		
	clock.tick(60)
	