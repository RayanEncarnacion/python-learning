import operator

allowed_operators = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv
}

def continue_calculations() -> bool:
    return input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower() == 'y'

def calculate(first_number: int | None, operator, second_number):
    return allowed_operators[operator](first_number, second_number)

def complete_calculation(first_number) -> int | float:
    for item in allowed_operators.keys():
        print(item + '\n')
        
    operator = input("Pick an operator from the above: ")
    next_number = int(input("What's the next number?: "))
    result = calculate(first_number, operator, next_number)
    print(f'{first_number} {operator} {next_number} = {result}')
    return result

first_number = int(input("What's the first number?: "))
result = complete_calculation(first_number)

while continue_calculations():
    complete_calculation(result)
