secret_num = input("Player 1, enter a number (1-10): ")
guess_num = input("Player 2, try to guess player 1's number (1-10): ")
if secret_num == guess_num:
	print("You guessed it!")
else:
	print("You got it wrong. Player 1's number was " + secret_num)