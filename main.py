# Password in sequential order
import random

print("Welcome to the PyPassword Generator")
pass_length = int(input("How long would you like your password? : "))
no_of_symbols = int(input("How many symbols would you like in your password? : "))
no_of_numbers = int(input("How many numbers would you like in your password? : "))
no_of_letters = pass_length - (no_of_symbols + no_of_numbers)
lowercase = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
uppercase = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
letters = lowercase + uppercase
number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
characters = ["!", "#", "$", "%", "&", "(", ")", "+", "_", "-"]
my_pass = []
for symbol in range(no_of_symbols):
    random_symbol = random.choice(characters)
    my_pass.append(random_symbol)
for num in range(no_of_numbers):
    random_number = random.choice(number)
    my_pass.append(random_number)
for let in range(no_of_letters):
    random_letter = random.choice(letters)
    my_pass.append(random_letter)

print_count = 0
for this in range(pass_length):
    print(my_pass[this], end='')

