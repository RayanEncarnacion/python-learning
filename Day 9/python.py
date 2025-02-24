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

bidders = []

def store_bidder():
    bidders.append({
        'name': input('What is your name? '),
        'bid': int(input('What is your bid? $'))
    })

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
max_bidder = max(bidders, key=lambda x: x['bid'])
print(f"The highest bidder is {max_bidder['name']} with a bid of ${max_bidder['bid']}.")
    
