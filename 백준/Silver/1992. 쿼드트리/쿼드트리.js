let input = require("fs").readFileSync("/dev/stdin").toString().trim().split(/\n/);

const N = Number(input[0]);
const arr = input.slice(1).map(str => str.trim().split("").map(Number));

function recursion(n, x, y) {
  let sum = 0;
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      sum += arr[i + x][j + y];
    }
  }
  if (sum === 0) return "0";
  else if (n * n === sum) return "1";
  else {
    n /= 2;
    let topLeft = recursion(n, x, y);
    let topRight = recursion(n, x, y + n);
    let bottomLeft = recursion(n, x + n, y);
    let bottomRight = recursion(n, x + n, y + n);
    return `(${topLeft}${topRight}${bottomLeft}${bottomRight})`;
  }
}
console.log(recursion(N, 0, 0));