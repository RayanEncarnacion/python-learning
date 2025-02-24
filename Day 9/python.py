from os import system


print('''
     ___________
     \         /
      )_______(
      |"""""""|_.-._,.---------.,_.-._
      |       | | |               | | ''-.
      |       |_| |_             _| |_..-'
      |_______| '-' `'---------'` '-'
      )"""""""(
     /_________\
     `'-------'`
    .-------------.
   /_______________\
''')

print('Welcome to the secret auction program. \n')

bidders = {}

def store_bidder():
    name = input('What is your name? ')
    bid = int(input('What is your bid? $'))
    bidders[name] = bid

def no_more_bidders():
    return input("Are there any other bidders? Type 'yes' or 'no'. \n").lower() != 'yes'

def clear_console():
    system('cls')

while True:
    store_bidder()

    if no_more_bidders():
        break
    clear_console()

clear_console()
max_bidder_name = max(bidders, key=bidders.get)
print(f"The highest bidder is {max_bidder_name} with a bid of ${bidders[max_bidder_name]}.")
    
