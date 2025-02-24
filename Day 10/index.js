const ALLOWED_OPERATORS = {
    "+": (a, b) => a + b,
    "-": (a, b) => a - b,
    "*": (a, b) => a * b,
    "/": (a, b) => a / b,
};

const continueCalculations = (result) =>
    prompt(
        `Type 'y' to continue calculating with ${result}, or type 'n' to start a new calculation: `
    )
        .toLowerCase()
        .trim() === "y";

const calculate = (firstNumber, operator, secondNumber) =>
    ALLOWED_OPERATORS[operator](firstNumber, secondNumber);

function completeCalculation(firstNumber) {
    for (const op of Object.keys(ALLOWED_OPERATORS)) console.log(op);

    const operator = prompt("Pick an operator from the above: ").trim();
    const nextNumber = parseFloat(prompt("What's the next number?: "));
    const result = calculate(firstNumber, operator, nextNumber);
    console.log(`${firstNumber} ${operator} ${nextNumber} = ${result}`);

    return result;
}

let firstNumber = parseFloat(prompt("What's the first number?: "));
let result = completeCalculation(firstNumber);

while (continueCalculations(result)) result = completeCalculation(result);
