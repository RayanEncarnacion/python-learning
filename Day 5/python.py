import random

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"];  
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"];  
symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")"];  


print('Welcome to the PyPassword Generator!\n')
nr_letters = int(input('How many letters should you like in your password?\n'))
nr_numbers = int(input('How many numbers should you like?\n'))
nr_symbols = int(input('How many symbols should you like?\n'))

password_list = []

for char in range(nr_letters):
    password_list.append(random.choice(letters))
    
for char in range(nr_numbers):
    password_list.append(random.choice(numbers))
    
for char in range(nr_symbols):
    password_list.append(random.choice(symbols))
    
""" 
    # Implemented with list comprehensions
    password_list = (
        [random.choice(letters) for _ in range(nr_letters)] +
        [random.choice(numbers) for _ in range(nr_numbers)] +
        [random.choice(symbols) for _ in range(nr_symbols)]
    )
"""
    
random.shuffle(password_list)
random_password = ''.join(password_list)



print(f'Your generated password is: {random_password}')