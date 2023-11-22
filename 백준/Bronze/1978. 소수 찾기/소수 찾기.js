let input = require("fs").readFileSync("/dev/stdin").toString().trim().split("\n").map(n => n.split(" ").map(Number));

let answer = 0;
function isPrime(n) {
  if (n === 1) return;
  for (let i = 2; Math.sqrt(n) >= i; i++) {
    if (n % i === 0) return;
  }
  return n;
}

input[1].forEach(n => isPrime(n) && answer++);
console.log(answer);


