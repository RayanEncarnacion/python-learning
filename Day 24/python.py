from pathlib import Path

parent_folder = Path(__file__).parent
input_folder = parent_folder / "Input"
starting_letter_content = ""

with open(input_folder /  "Letters" / "starting_letter.txt") as starting_letter:
    starting_letter_content += starting_letter.read();
    
with open(input_folder /  "Names" / "invited_names.txt") as names:
    for name in names.read().splitlines():
        letter = starting_letter_content.replace("[name]", name)
        letter_path = parent_folder / "Output" / "ReadyToSend" / f"letter_for_{name.replace(" ", "_")}" 
        
        with open(letter_path, mode="w") as new_letter:
            new_letter.write(letter)

