let input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
for (let i = 1; i <= input[0]; i++) {
  let arr = input[i].split(',');
  console.log(Number(arr[0]) + Number(arr[1]));
}
