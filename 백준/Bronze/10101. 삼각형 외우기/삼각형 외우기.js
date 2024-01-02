let N = require("fs").readFileSync("/dev/stdin").toString().trim().split(/\n/).map(Number);

function checkTriangle(n) {
  let sum = n.reduce((a, b) => a + b);
  if (sum === 180) {
    if (n[0] === n[1] && n[1] === n[2]) return "Equilateral";
    else if (n[0] === n[1] || n[1] === n[2] || n[0] === n[2])
      return "Isosceles";
    else return "Scalene";
  } else return "Error";
}
console.log(checkTriangle(N));
