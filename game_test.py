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

x_rect = 0
y_rect = 100

x_line = 0
y_line = 50

#-------- Main Loop ---------#
while not done:
	#--- Main Event loop ---#
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		
		if event.type == pygame.MOUSEBUTTONDOWN:
			x_rect += 10	#changes the x for the next rectangle
			
		if event.type == pygame.KEYDOWN:
			x_line += 10	#changes the x for the next line
			
	screen.fill(WHITE)	#clears screen
		
	pygame.draw.rect(screen, RED, (x_rect,y_rect,100,150), 0)	#draws a new rectangle
	pygame.draw.line(screen, BLUE, (x_line,y_line), (x_line+100,y_line), 5)	#draws a new line
		
	pygame.display.flip()	#updates the screen to show the rectangle
		
	clock.tick(60)

		
pygame.quit()
exit()




