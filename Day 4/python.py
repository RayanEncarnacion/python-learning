import random
from game_asciis import asciis

your_choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n'))

print(asciis[your_choice])
print("Compute chose: \n")

computer_choice = random.randint(0, len(asciis) - 1)
print(asciis[computer_choice])

if your_choice == computer_choice:
    print("Draw!")
    exit()
    
outcomes = {
    0: { 1: "You lose", 2: "You win" },
    1: { 2: "You lose", 0: "You win" },
    2: { 0: "You lose", 1: "You win" }
}

print(outcomes[your_choice][computer_choice])
