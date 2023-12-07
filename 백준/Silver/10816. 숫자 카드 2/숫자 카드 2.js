let input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

let arr = input[1].split(' ');
let arr2 = input[3].split(' ');
let dic = {};
arr.map((n) => {
  if (dic[Number(n)] > 0) {
    ++dic[Number(n)];
  } else dic[Number(n)] = 1;
});
let answer = [];
arr2.map((n) => answer.push(dic[Number(n)] || 0));
console.log(answer.join(' '));
