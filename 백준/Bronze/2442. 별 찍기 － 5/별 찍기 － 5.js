const input = require("fs").readFileSync("/dev/stdin").toString();

let n = Number(input);
let answer = "";
let i = 1;
let distance = n;
while (i <= 2 * n - 1) {
  distance -= 1;
  answer += " ".repeat(distance) + "*".repeat(i) + "\n";
  i += 2;
}
console.log(answer);