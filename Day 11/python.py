import random

def get_card() -> int:
    return random.randint(1, 10)

def should_continue(prompt: str) -> bool:
    return input(prompt).lower().strip() == 'y'

def calculate_total(cards: list[int]) -> int:
    return sum(cards)

def display_hands(your_cards: list[int], computer_cards: list[int], reveal_all = False) -> None:
    print(f'Your cards: {your_cards}, current total: {calculate_total(your_cards)}')
    if reveal_all:
        print(f"Computer's cards: {computer_cards}, total: {calculate_total(computer_cards)}")
    else:
        print(f"Computer's first card: {computer_cards[0]}")

def determine_winner(your_total: int, computer_total: int) -> str:
    if your_total > 21:
        return "Computer wins! You busted."
    if computer_total > 21:
        return "You win! Computer busted."
    if your_total == computer_total:
        return "It's a draw!"
    return "You win!" if your_total > computer_total else "Computer wins!"

def play_game() -> None:
    your_cards = [get_card(), get_card()]
    computer_cards = [get_card(), get_card()]
    
    while True:
        display_hands(your_cards, computer_cards)
        
        if calculate_total(your_cards) > 21:
            print("You busted! Computer wins.")
            break
        
        if not should_continue("Type 'y' to get another card, type 'n' to pass: "):
            display_hands(your_cards, computer_cards, reveal_all=True)
            print(determine_winner(calculate_total(your_cards), calculate_total(computer_cards)))
            break
        
        your_cards.append(get_card())

while should_continue("Do you want to play a game of Blackjack? Type 'y' or 'n': "):
    play_game()
    
print("Thanks for playing!")

