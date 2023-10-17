const input = require("fs").readFileSync("/dev/stdin").toString();

let n = Number(input);
let answer = "";
let start = 2 * n - 1;
for (let i = start; i > 0; i -= 2) {
  let distance = start - i;
  answer +=
    " ".repeat(distance / 2) + "*".repeat(i) + " ".repeat(distance && 1) + "\n";
}
for (let i = 3; i <= start; i += 2) {
  let distance = start - i;
  answer +=
    " ".repeat(distance / 2) + "*".repeat(i) + " ".repeat(distance && 1) + "\n";
}
console.log(answer);
