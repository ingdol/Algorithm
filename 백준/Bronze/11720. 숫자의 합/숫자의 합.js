let input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
let cnt = input[0];
let sum = 0;
for (let i = 0; i < cnt; i++) {
  sum += Number(input[1][i]);
}
console.log(sum);
