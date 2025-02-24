import operator

ALLOWED_OPERATORS = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv
}

def continue_calculations(result: float) -> bool:
    return input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower() == 'y'

def calculate(first_number: int | None, operator: str, second_number: int) -> int | float:
    return ALLOWED_OPERATORS[operator](first_number, second_number)

def complete_calculation(first_number: int | float) -> int | float:
    for op in ALLOWED_OPERATORS:
        print(op)
        
    operator = input("Pick an operator from the above: ").strip()
    next_number = int(input("What's the next number?: "))
    result = calculate(first_number, operator, next_number)
    print(f'{first_number} {operator} {next_number} = {result}')
    return result

first_number = int(input("What's the first number?: "))
result = complete_calculation(first_number)

while continue_calculations(result):
    complete_calculation(result)
