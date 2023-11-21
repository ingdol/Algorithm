let input = require("fs").readFileSync("/dev/stdin").toString().trim().split("\n").map(n => n.split(" ").map(Number));

const [A, B] = input[0];
const [m] = input[1];
const nums = input[2].reverse();
const answer = [];

let ten = 0;
for (let i = 0; i < m; i++) {
  ten += nums[i] * A ** i;
}

if (ten === 0) {
  console.log(0);
} else {
  while (ten > 0) {
    answer.unshift(ten % B);
    ten = Math.floor(ten / B);
  }
}
console.log(answer.join(" "));
