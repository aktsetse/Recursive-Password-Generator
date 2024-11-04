
import random
# Password Generator

    # Uppercase Letters
UppercaseLetters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    
    # Lowercase Letters
LowercaseLetters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    # Numbers
Numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    
    # Symbols
Symbols = ['.', ',', '?', '!', ':', ';', "'", '"', '/', '\\', '(', ')', '[', ']', '{', '}', '<', '>', '-', '_', '+', '=', '@', '&', '*', '#', '$', '%', '^', '~', '|', '`', '<', '>']

print("Welcome to Amenuveve's PyPassword Generator!")
nr_letters = int(input("How many lowercase letters would you like in your password?\n"))
nr_LETTERS = int(input("How many Uppercase letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like in your password?\n"))

password_list = []
for char in range(1, nr_letters + 1):
    password_list += random.choice(LowercaseLetters)
for char in range(1, nr_LETTERS + 1):
     password_list += random.choice(UppercaseLetters)
for char in range(1, nr_symbols + 1):
    password_list += random.choice(Symbols)
for char in range(1, nr_numbers+ 1):
    password_list += random.choice(Numbers)

print(password_list)
random.shuffle(password_list)
print(password_list)
password = " "
for char in password_list: 
    password += char
print(f"Your password is: {password}")
