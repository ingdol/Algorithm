let input = require("fs").readFileSync("/dev/stdin").toString().trim().split(/\n/).map(Number);

function check(arr) {
  if (arr.reduce((a, b) => a + b) !== 180) return "Error";
  if (arr.every(n => n === 60)) return "Equilateral";
  if (arr[0] === arr[1] || arr[1] === arr[2] || arr[0] === arr[2])
    return "Isosceles";
  return "Scalene";
}
console.log(check(input));
