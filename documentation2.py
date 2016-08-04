"""
 Pygame base template for opening a window

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/vRB_983kUMc
"""

import pygame
import random

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


# WRITE YOUR CODE HERE
#x and y coordinates of the ball

been_clicked = False

# -------- Main Program Loop -----------
while not done:
	# --- Main event loop
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		if event.type == pygame.MOUSEBUTTONDOWN:
			print("Here!")
			
			ball_size = random.randint(20,80)
			ball_color = color_list[random.randint(0, len(color_list)-1)]
			x_speed = random.randint(-10,10)
			y_speed = random.randint(-10,10)
			
			x = pygame.mouse.get_pos()[0]
			y = pygame.mouse.get_pos()[1]
			
			# if they click in a spot that woul put the ball out of bounds,
			# the x and y positions are adjusted to keep it inside the window
			if x >= (700-ball_size):
				x -= ball_size
			elif x <= (0+ball_size):
				x += ball_size
			if y >= (500-ball_size):
				y -= ball_size
			elif y <= (0+ball_size):
				y += ball_size
			been_clicked = True

    # --- Game logic should go here

    # --- Screen-clearing code goes here.
	screen.fill(LIGHT_BLUE)

    # --- Drawing code should go here
	if been_clicked:
		pygame.draw.circle(screen, ball_color, (x,y), ball_size)
	
		x+= x_speed
		y+= y_speed
		if x >= (700-ball_size) or x <= (0+ball_size):
			x_speed *= -1
		if y >= (500-ball_size) or y <= (0+ball_size):
			y_speed *= -1


    # --- Go ahead and update the screen with what we've drawn.
	pygame.display.flip()

    # --- Limit to 60 frames per second
	clock.tick(60)
	
# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE
