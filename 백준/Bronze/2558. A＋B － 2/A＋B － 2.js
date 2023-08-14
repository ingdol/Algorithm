let input = require('fs').readFileSync('/dev/stdin').toString().split('\n')
input = [...input].map((x) => x.replace('\r', ''))
console.log(Number(input[0]) + Number(input[1]))