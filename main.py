# # Password in sequential order
import random
import time

print("Welcome to the PyPassword Generator")
print("The first part of the program generates a password in with characters, letters or numbers following each other sequentially.")
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
print("\n")

# Password in random order
# import random
# import time
time.sleep(2)
print("Welcome to the second part of the PyPassword Generator where everything is generated in random order.")
pass_length = int(input("How long would you like your password? : "))
no_of_symbols = int(input("How many symbols would you like in your password? : "))
no_of_numbers = int(input("How many numbers would you like in your password? : "))
time.sleep(0.3)
no_of_letters = pass_length - (no_of_symbols + no_of_numbers)
lowercase = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
uppercase = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
letters = lowercase + uppercase
number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
characters = ["!", "#", "$", "%", "&", "(", ")", "+", "_", "-"]
my_pass = ""
password_indices = []
options = [letters, number, characters]
letter_count = 0
number_count = 0
character_count = 0
for i in range(pass_length):
    random_choice = random.choice(options)
    if random_choice == letters:
        letter_count += 1
        if letter_count >= no_of_letters:
            options.remove(letters)
        chosen = random.choice(letters)
        chosen = str(chosen)
        my_pass += chosen
    elif random_choice == number:
        number_count += 1
        if number_count >= no_of_numbers:
            options.remove(number)
        chosen = random.choice(number)
        chosen = str(chosen)
        my_pass += chosen
    elif random_choice == characters:
        character_count += 1
        if character_count >= no_of_symbols:
            options.remove(characters)
        chosen = random.choice(characters)
        chosen = str(chosen)
        my_pass += chosen
print(f"Your password is {my_pass}")
























# for this_is_it in range(pass_length):
#     chosen_choice = random.choice(options)
#     if chosen_choice == letters and letter_count < no_of_letters:
#         letter_count += 1
#         random_letter = random.choice(letters)
#         random_index = random.randrange()
#         my_pass.insert(random_index, random_letter)
#         password_indices.pop(random_index)
#     elif chosen_choice == number and number_count < no_of_numbers:
#         number_count += 1
#         random_number = random.choice(number)
#         random_index = random.randint(0, pass_length - 1)
#         my_pass.insert(random_index, random_number)
#         password_indices.pop(random_index)
#     elif chosen_choice == characters and character_count < no_of_symbols:
#         character_count += 1
#         random_character = random.choice(characters)
#         random_index = random.randint(0, pass_length - 1)
#         my_pass.insert(random_index, random_character)
#         password_indices.pop(random_index)
#     else:
#         print("Missed this one")
# print(my_pass)


