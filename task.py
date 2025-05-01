import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Easy Level

#Create a variable for each letter, symbol, and number to equal to zero.
# This will be used in their respective for loops
my_letters = 0
my_symbols = 0
my_numbers = 0
#Randomizes the letters
#Creates a for loop condition to loop through the letters
#Uses my_letters variable declared earlier and increases by one until it reaches the nr_letters(the input from the user)
    #For each time the my_letters is less than nr_letters it will print out a random item from the letters list
    #Until my_letters is equal to the input declared in nr_letters by the user
for a in letters:
    if my_letters < nr_letters:
        my_letters += 1
        print(random.choice(letters), end="")
#Randomizes the symbols
#See above comment
for b in symbols:
    if my_symbols < nr_symbols:
        my_symbols += 1
        print(random.choice(symbols), end="")
#Randomizes the numbers
#See above comment
for c in numbers:
    if my_numbers < nr_numbers:
        my_numbers += 1
        print(random.choice(numbers), end="")














#Raw thought processing notes
#If the input is less than a certain number keep looping from the list until it's reached the desired input
#Have to use nr_letters somewhere, but where
# I want 5 numbers, if i am less than 5 i want to add 1