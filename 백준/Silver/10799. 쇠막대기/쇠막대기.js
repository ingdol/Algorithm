let input = require('fs').readFileSync('/dev/stdin').toString().trim();

let openCnt = 0;
let res = 0;
for (let i = 0; i < input.length; i++) {
  if (input[i] === '(') openCnt++;
  else {
    openCnt--;
    input[i - 1] !== input[i] ? (res += openCnt) : res++;
  }
}
console.log(res);
