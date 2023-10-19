const input = require("fs").readFileSync("/dev/stdin").toString();

let n = Number(input);
let answer = n > 1 ? " ".repeat(n - 1) + "*\n" : "";
let distance = n - 2;
for (let i = 2; i < n * 2 - 2; i += 2) {
  answer += " ".repeat(distance);
  answer += "*";
  for (let j = 2; j <= i; j++) {
    answer += " ";
  }
  answer += "*\n";
  distance--;
}
answer += "*".repeat(n * 2 - 1);
console.log(answer);
