let input = require("fs").readFileSync("/dev/stdin").toString().trim();

const arr = [...input].map(Number);
let comN = input[0];
let cnt = [0, 0];

arr.forEach(n => {
  if (comN !== n) {
    n === 0 ? cnt[0]++ : cnt[1]++;
    comN = n;
  }
});
console.log(Math.min(cnt[0], cnt[1]));
