const input = require("fs").readFileSync("/dev/stdin").toString();

let n = Number(input);
let answer = "";
let i = 1;
let distance = n;
while (i <= 2 * n - 1 && distance) {
  distance -= 1;
  answer += "*".repeat(i) + " ".repeat(distance * 2) + "*".repeat(i) + "\n";
  i++;
}
distance = 1;
i = n - 1;
while (i > 0 && distance !== n) {
  answer += "*".repeat(i) + " ".repeat(distance * 2) + "*".repeat(i) + "\n";
  distance += 1;
  i--;
}
console.log(answer);
