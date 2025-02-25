const START_NUMBER = 1;
const END_NUMBER = 100;
const HARD_LEVEL_TURNS = 5;
const EASY_LEVEL_TURNS = 10;

const makeGuess = () => arseInt(prompt("Make a guess: "), 10)
const generateAnswer = (START_NUMBER, END_NUMBER) =>
    Math.floor(Math.random() * (END_NUMBER - START_NUMBER + 1)) + START_NUMBER;

function setDifficulty() {
    const level = prompt("Choose a difficulty. Type 'easy' or 'hard': ")
        .toLowerCase()
        .trim();
    return level === "hard" ? HARD_LEVEL_TURNS : EASY_LEVEL_TURNS;
}

function checkAnswer(guess, answer) {
    if (guess > answer) return "Too high.";
    if (guess < answer) return "Too low.";
    return "correct";
}

console.log("Welcome to the Number Guessing Game!");
console.log(`I'm thinking of a number between ${START_NUMBER} and ${END_NUMBER}.`);

const answer = generateAnswer(START_NUMBER, END_NUMBER);
let turns = setDifficulty();
console.log(`You have ${turns} attempts to guess the number.`);

while (turns > 0) {
    const result = checkAnswer(makeGuess(), answer);

    if (result === "correct") {
        console.log(`You got it! The answer is ${answer}.`);
        break;
    }

    console.log(result);
    turns--;
    if (turns > 0) {
        console.log(`Guess again. You have ${turns} attempts remaining.`);
    } else {
        console.log("You're out of attempts. You lose!");
        console.log(`The correct answer was ${answer}.`);
    }
}
