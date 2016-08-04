from hashlib import *

#login dictionary
#Database for usernames and their corresponding hashed passwords
loginDict = {}

#makes a hash of the password passed to it
def make_hash (password):
	salt = "HJ89;"
	return md5((salt + password).encode("utf-8")).hexdigest() 

#gets username and password and checks them against the loginDict
def login ():
	username = input("Enter your username: ")
	password = input("Enter your password: ")
	
	#hashes password
	password = make_hash(password)
	
	if username in loginDict:
		if loginDict[username] == password:
			print("You're in!")
		else:
			print ("Your password is incorrect")
			login()
	else:
		print("You are not signed up.")
		choice = input ("Would you like to sign up? (Y or N)")
		if choice == "Y":
			sign_up(loginDict)
		else:
			choice = input ("Would you like to try to login again? (Y or N)")
			if choice == "Y":
				login()

#lets the user create a unique username and password and stores them in the loginDict
def sign_up(loginDict):
	username = input("Create a username: ")
	password = input("Create a password: ")
	
	#hashes password
	password = make_hash(password)
	
	if username in loginDict:
		print("Username is taken.")
		sign_up(loginDict)
		
	#Store in dict
	loginDict[username] = password
	
	#confirma that they have been successfully signed up
	print("Congrats! You have been successfully signed up")
	prompt()	#asks if they now want to login or sign up again
	
#ask user to login / sign up 
def prompt():
	command = input("Would you like to login or sign up? (L or S): ")
	if command == "L":
		login()
	elif command == "S":
		sign_up(loginDict)
	else:
		print("Invalid input")
		prompt()
		
		
prompt()