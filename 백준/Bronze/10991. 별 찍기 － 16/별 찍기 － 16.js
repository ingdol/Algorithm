const input = require("fs").readFileSync("/dev/stdin").toString();
let n = Number(input);
let answer = "";
let distance = n - 1;
for (let i = 1; i <= n; i++) {
  answer += " ".repeat(distance) + "* ".repeat(i) + "\n";
  distance--;
}
console.log(answer);
