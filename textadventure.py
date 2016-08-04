start = '''
Congratulations! You're dead. You see a bright light in front of you. 
'''
print(start)
print("You go towards the light. You come to an elevater and you can go up or down.")
valid_input = False
while not valid_input:
	print("Type 'up' to go up and 'down' to go down")
	user_input = input()
	if user_input != 'up' and user_input != 'down':
		print("Invalid input")
	else:
		valid_input = True
if user_input == 'up':
	print("You go up.")
	print("Welcome to Hell! You can go left or right.")
	valid_input = False
	while not valid_input:
		print("Type 'left' or 'right'")
		user_input = input()
		if user_input != 'left' and user_input != 'right':
			print("Invalid input")
		else:
			valid_input = True
			
	if user_input == 'left':
		print("You go left.")
		print("You are doomed to burn forever in a pit of flames.")
	else:
		print("You go right.")
		print("You have to listen to bad eighties music for eternity.")
else:
	print("You go down.")
	print("Welcome to Heaven! Would you like to float or walk?")
	valid_input = False
	while not valid_input:
		print("Type 'float' or 'walk'")
		user_input = input()
		if user_input != 'float' and user_input != 'walk':
			print("Invalid input")
		else:
			valid_input = True
	
	if user_input == 'float':
		print("You try to float.")
		print("You don't know how to float. You're a human. You fall down and plummet back to Earth.")
	else:
		print("You walk and eventually come to a garden.")
		print("You meet God and share a meal in the Garden of Eden.")
		print("Good job! You won!")
print("Game Over")
input("Hit 'enter' to leave")	
	
	
