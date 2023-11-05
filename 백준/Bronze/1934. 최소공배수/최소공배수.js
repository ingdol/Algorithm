const input = require("fs").readFileSync("/dev/stdin").toString().trim().split("\n").map(v => v.split(" ").map(Number));

[T, ...arr] = input;

const answer = [];

arr.map(nums => solution(nums[0], nums[1]));

function solution(a, b) {
  let x = a;
  let y = b;

  while (x % y !== 0) {
    let rest = x % y;

    if (rest !== 0) {
      x = y;
      y = rest;
    }
  }
  answer.push((a * b) / y);
}
console.log(answer.join("\n"));
