ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def shift_letter(letter: str, shift: int, mode: str) -> str:
    if letter.isspace() or letter.upper() not in ALPHABET:
        return letter
    
    letter_idx = ALPHABET.index(letter.upper())
    shifted_idx = (letter_idx + shift) % len(ALPHABET) if mode == "encode" else (letter_idx - shift) % len(ALPHABET)
        
    return ALPHABET[shifted_idx]

def process_text(text: str, shift: int, mode: str) -> str:
    return "".join([shift_letter(char, shift, mode) for char in text])

playing = True

while playing:
    direction = input("Type 'encode' to encrypt or 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").upper()
    shift = int(input("Type the shift number:\n"))

    processed_text = process_text(text, shift, direction).lower()
    print(f"Here's the result: {processed_text}")

    playing = input("Type 'yes' if you want to go again. Otherwise type 'no':\n").lower() == 'yes'