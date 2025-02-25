import random

print("Welcome to the Number Guessing Game!")

START_NUMBER = 1
END_NUMBER = 100
HARD_LEVEL_TURNS = 5
EASY_LEVEL_TURNS = 10

def set_difficulty() -> int:
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower().strip()
    
    if level == 'hard': return HARD_LEVEL_TURNS
    else: return EASY_LEVEL_TURNS

def make_guess() -> int:
    return int(input("Make a guess: ")) 

def check_answer(guess: int, answer: int) -> str:
    if guess > answer: return "Too high."
    elif guess < answer: return "Too low."
    else: return 'correct'

answer = random.randint(START_NUMBER, END_NUMBER)
turns = set_difficulty()
print(f"I'm thinking of a number between {END_NUMBER} and {END_NUMBER}.")
print(f'You have {turns} to guess the number.')

while turns > 0:
    result = check_answer(make_guess(), answer)
    
    if result == "correct":
        print(f"You got it! The answer is {answer}.")
        break
    print(result)
    turns -= 1
    
    if turns > 0:
        print(f"Guess again. You have {turns} attempts remaining.")
    else:
        print("You're out of attempts. You lose!")
        print(f"The correct answer was {answer}.")