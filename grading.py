num_grade = input("Enter your score: ")
num_grade = int(num_grade)
letter_grade = "You got a"
while not valid_input:
	if num_grade >= 90 and num_grade <= 100:
		letter_grade += "n A"
	elif num_grade >= 80 and num_grade <=89:
		letter_grade += " B"
	elif num_grade >= 70 and num_grade <=79:
		letter_grade += " C"
	elif num_grade >= 0 and num_grade <=69:
		letter_grade += " F"
	else:
		letter_grade = "Invalid input"
print(letter_grade)