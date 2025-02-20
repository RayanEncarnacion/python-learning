print("\nWelcome the Treasure Island!")

direction = input("Where do you want to go? \n \t 'left' or 'right': ")

if direction.lower().strip() == 'right':
    print("You fell into a hole. Game over")
    exit()

decision = input("You've come to a lake. There is an island in the middle of the lake. \n \t Type 'wait' to wait for a boat. Type 'swim' to swim across: ")

if decision.lower().strip() == 'swim':
    print("You were eaten by shars. Game over")
    exit()
    
chosen_door = input("You arrive at the island unharmed. There is a house with 3 doors \n \t One red, one yellow and one blue. Which colour do you choose? ")

if chosen_door.lower().strip() != 'green':
        print("You were captured by the pirates. Game over")
        exit()
        
print("You've found the treasure!")
