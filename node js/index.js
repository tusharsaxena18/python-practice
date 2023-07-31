const prompt = require("prompt-sync")();

let sum = 0 
let n = prompt("Enter a number: ");
n = parseFloat(n);

for (let i = 1; i <= n ; i++) {
    sum += i;         
}

console.log(sum);
