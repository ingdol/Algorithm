let input = require("fs").readFileSync("/dev/stdin").toString();
input = Number(input);
let answer = 1;
while (input > 0) {
  answer *= input;
  input--;
}
console.log(answer);
