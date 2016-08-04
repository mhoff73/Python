import random

five_syllables = ["Blistering paper", "Summer is coming", "Release is not near", "Need coldness here", "I am not dying"]
seven_syllables = ["Dragons fly through the night sky", "The stream flows through the dark woods", "Light shines off shiny objects", "Rain falls softly on the ground", "Bright red lights illuminate", "Majestic trees stand above", "Sadness seeps through the heart's cracks", "The sun blazes through my skin", "The water rises to me", "Tingling and shuddering"]
five_syllables2 = ["Breathtakingly nice", "Juggle fire and ice", "Don't you ever dare mess", "My toungue is tangled", "Why art thou weary"]

five_length = len(five_syllables)
seven_length = len(seven_syllables)
	
random_index5a = random.randint(0, five_length-1)
random_index7 = random.randint(0, seven_length - 1)
random_index5b = random.randint(0, five_length-1)

indexes5a = []

for i in range(3):
	
		
		
		
	
	print (five_syllables[random_index5a])
	print(seven_syllables[random_index7])
	print(five_syllables2[random_index5b])
	
	print("")
	
	name = input("Name the poem: ")	
	print(name)
	
	print("")