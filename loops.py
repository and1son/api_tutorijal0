my_variable = "hello"

for a in my_variable:
	print(a)

my_list = [1,2,3,4,5,6]

for number in my_list:
	print(number**2)

	user_wants_number = True

	while user_wants_number == True:
		print(10)

		user_input = input("Should we print again? (y/m) ")
		if user_input == 'n':
			user_wants_number = False
		if user_input == 'y':
			user_wants_number = True

