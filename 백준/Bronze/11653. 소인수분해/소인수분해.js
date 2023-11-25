let input = require("fs").readFileSync("/dev/stdin").toString();
input = Number(input);
let answer = [];
let i = 2;

while (input !== 1) {
  if (input % i === 0) {
    answer.push(i);
    input /= i;
  } else {
    i++;
  }
}
answer.forEach(n => console.log(n));
