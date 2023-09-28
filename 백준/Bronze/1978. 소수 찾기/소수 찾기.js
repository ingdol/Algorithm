const input = require("fs").readFileSync("/dev/stdin").toString().trim().split("\n")[1].split(" ");

let answer = 0;
for (let i = 0; i < input.length; i++) {
  let num = Number(input[i]);
  let n = 2;
  let cnt = 0;
  while (n <= num) {
    if (num % n === 0) cnt++;
    n++;
  }
  cnt === 1 && answer++;
}
console.log(answer);