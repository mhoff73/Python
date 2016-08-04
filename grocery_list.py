print("Welcome to ShopRite!")

grocery_list = {}
done = False

def add_item():
	item = input("Enter an item: ")
	quantity = input("How many " + item + "s would you like? ")
	grocery_list[item] = quantity
	
def update_item():
	item = input("What item would you like to update? ")

	if item in grocery_list:
		quantity = input("Enter the new quantity: ") 
		grocery_list[item] = quantity
	else:
		print("Item not found")
		choice = input("Would you like to add " + item + " to your list? (Y or N):")
		if choice == "Y":
			add_item()
	

def delete_item():
	item = input("What item would you like to delete? ")
	
	if item in grocery_list:
		del grocery_list[item]
	else:
		print("Item not found")


def print_list():
	print(grocery_list)
	
def options():
	choice = input("What would you like to do next? (add, update, delete, print, done): ")
	if choice == "add":
		add_item()
		stop = False
	elif choice == "update":
		update_item()
		stop = False
	elif choice == "delete":
		delete_item()
		stop = False
	elif choice == "print":
		print_list()
		stop = False
	else:
		stop = True
	return stop

while not done:
	done = options()
