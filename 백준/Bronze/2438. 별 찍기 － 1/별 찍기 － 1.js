const input = require("fs").readFileSync("/dev/stdin").toString();

let n = Number(input);
let answer = "";
for (let i = 1; i <= n; i++) {
  answer += "*".repeat(i) + "\n";
}
console.log(answer);
