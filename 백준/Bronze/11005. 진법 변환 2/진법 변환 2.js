const input = require("fs").readFileSync("/dev/stdin").toString().trim().split(" ").map(n => Number(n));

[a, b] = input;
let arr = [];
while (a > 0) {
  arr.push(a % b);
  a = Math.floor(a / b);
}
arr = arr.map(n => {
  if (n >= 10) {
    return String.fromCharCode(n + 55);
  } else return n;
});
console.log(arr.reverse().join(""));

