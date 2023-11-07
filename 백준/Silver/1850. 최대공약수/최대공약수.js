const input = require("fs").readFileSync("/dev/stdin").toString().trim().split(" ");
const a = BigInt(input[0]);
const b = BigInt(input[1]);
const [num1, num2] = [a > b ? a : b, a < b ? a : b];

const gcd = (i, j) => {
  if (j === 0n) {
    return i;
  }
  return gcd(j, i % j);
};

const gcdResult = gcd(num1, num2);
console.log("1".repeat(Number(gcdResult)));
