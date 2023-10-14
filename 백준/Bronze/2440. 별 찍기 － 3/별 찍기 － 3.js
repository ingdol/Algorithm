const input = require("fs").readFileSync("/dev/stdin").toString();

let n = Number(input);
let answer = "";
for (let i = n; i >= 1; i--) {
  answer += "*".repeat(i) + "\n";
}
console.log(answer);
