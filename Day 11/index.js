const getCard = () => Math.floor(Math.random() * 10) + 1;

const shouldContinue = (promptMessage) =>
    prompt(promptMessage).toLowerCase().trim() === "y";

const calculateTotal = (cards) => cards.reduce((sum, card) => sum + card, 0);

function displayHands(yourCards, computerCards, revealAll = false) {
    console.log(`Your cards: ${yourCards}, current total: ${calculateTotal(yourCards)}`);

    if (revealAll) {
        console.log(`Computer's cards: ${computerCards}, total: ${calculateTotal(computerCards)}`);
    } else {
        console.log(`Computer's first card: ${computerCards[0]}`);
    }
}

function determineWinner(yourTotal, computerTotal) {
    if (yourTotal > 21) return "Computer wins! You busted.";
    if (computerTotal > 21) return "You win! Computer busted.";
    if (yourTotal === computerTotal) return "It's a draw!";
    return yourTotal > computerTotal ? "You win!" : "Computer wins!";
}

function playGame() {
    const yourCards = [getCard(), getCard()];
    const computerCards = [getCard(), getCard()];

    while (true) {
        displayHands(yourCards, computerCards);

        if (calculateTotal(yourCards) > 21) {
            console.log("You busted! Computer wins.");
            break;
        }

        if (!shouldContinue("Type 'y' to get another card, type 'n' to pass: ")) {
            displayHands(yourCards, computerCards, true);
            console.log(
                determineWinner(
                    calculateTotal(yourCards),
                    calculateTotal(computerCards)
                )
            );
            break;
        }

        yourCards.push(getCard());
    }
}

while (shouldContinue("Do you want to play a game of Blackjack? Type 'y' or 'n': "))
    playGame();

console.log("Thanks for playing!");
