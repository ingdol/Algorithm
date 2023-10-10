const input = require("fs").readFileSync("/dev/stdin");

let answer = "";
for (let i = 1; i <= input; i++) {
  answer += i + "\n";
}
console.log(answer);
