const input = require("fs").readFileSync("/dev/stdin").toString();

let i = 0;
while (i < input.length) {
  console.log(input.slice(i, i + 10));
  i += 10;
}
console.log(input.slice(i));
