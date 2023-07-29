const prompt = require("prompt-sync")();

const ROWS = 3;
const COLS = 3;

const SYMBOLS_COUNT = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

const SYMBOLS_VALUES = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

function deposit() {
    while (true) {
        const depositAmount = prompt("Enter deposit amount: ");
        const NumberdepositAmount = parseFloat(depositAmount);

        if (isNaN(NumberdepositAmount) || NumberdepositAmount <= 0) {
            console.log("Invalid deposit amount, must be a number");
        } else {
            return NumberdepositAmount;
        }
    }
}

function getNumberoflines() {
    while (true) {
        const line = prompt("Enter the number of lines to bet on (1-3): ");
        const numberOfLines = parseFloat(line);

        if (isNaN(numberOfLines) || numberOfLines < 1 || numberOfLines > 3) {
            console.log("Invalid number of lines");
        } else {
            return numberOfLines;
        }
    }
}

function getBet(balance, lines) {
    while (true) {
        const bet = prompt("Enter the betting amount per line: ");
        const numberBet = parseFloat(bet);

        if (isNaN(numberBet) || numberBet <= 0 || numberBet > (balance / lines)) {
            console.log("Invalid bet");
        } else {
            return numberBet;
        }
    }
}

function spin() {
    return 1
}

let balance = deposit();
const numberOfLines = getNumberoflines();
const bet = getBet(balance, numberOfLines);

console.log(balance);
console.log(numberOfLines);
console.log(bet);
