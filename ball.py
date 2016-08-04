import pygame

#initialize all modules in pygame
pygame.init()

#defining colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0 , 0)
BLUE = (0, 0, 255)

#set width and height of the screen (x,y)
size = (700, 500)

#creates the screen
screen = pygame.display.set_mode(size)

#include an caption on screen
pygame.display.set_caption("My Game")

#loop until user clicks close button
done = False
	
#clock function for managing how fast the screen updates
clock = pygame.time.Clock()

x = 0
y = 100

#-------- Main Loop ---------#
while not done:
	#--- Main Event loop ---#
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		
		#GAME LOGIC
		
		#screen-clearing code
		
		#Here, we clear the screen to white. Don't put the drawing above this,
		# or they will be earased by this command.
		#If you want a background image, replace this clear with
		#blitting the background image using pygame.blit()
		screen.fill(WHITE)
		
		#---- DRAWING CODE -----#
		# goes on top of the background
		pygame.draw.line(screen, BLUE, (0,0) , (700, 500), 5)
		
		
		#pygame.draw.rect(screen, RED, (x,y,100,150), 0)
		#x += 10
		pygame.display.flip()
		
		#---- UPDATE SCREEN ----#
		#drawing takes place behind the background, fliping the screen will reveal them
			# updates entire screen
		#pygame.display.update(rectangle) -> updates part of the screen
		
		#limit to 60 frames per second
		clock.tick(60)

		
pygame.quit()
exit()




