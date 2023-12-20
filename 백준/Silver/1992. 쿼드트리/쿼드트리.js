let input = require("fs").readFileSync("/dev/stdin").toString().trim().split(/\n/);

let N = Number(input[0]);
let arr = input.slice(1).map(n => n.trim().split("").map(Number));
let res = [];
function recursion(n, x, y) {
  let total = 0;
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      total += arr[i + x][j + y];
    }
  }
  if (total === 0) res.push(0);
  else if (n * n === total) res.push(1);
  else {
    n /= 2;
    res.push("(");
    recursion(n, x, y);
    recursion(n, x, y + n);
    recursion(n, x + n, y);
    recursion(n, x + n, y + n);
    res.push(")");
  }
}
recursion(N, 0, 0);
console.log(res.join(""));
