import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']



print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Creates a list to store passwords from for loops. Used to shuffle
placeholder_list = []

#Sets value from user input to declare how often to execute the loop
#Used in a,b, and c for loop
for a in range(0, nr_letters):
    placeholder_list.append(random.choice(letters))

for b in range(0, nr_symbols):
    placeholder_list.append(random.choice(symbols))

for c in range(0, nr_numbers):
    placeholder_list.append(random.choice(numbers))

#Can remove this piece of code if selected variables do not want to be displayed.
print(placeholder_list)
random.shuffle(placeholder_list)
print(placeholder_list)

#Creates a variable to store the returned strings from for loops and loops to add the values from the list to the password
    #variable
password = ""
for d in placeholder_list:
    password += d

print(f"Your password is: {password}")