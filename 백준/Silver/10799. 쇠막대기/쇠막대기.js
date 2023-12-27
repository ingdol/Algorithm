let input = require("fs").readFileSync("/dev/stdin").toString().trim();
let cnt = 0;
let res = 0;
for (let i = 0; i < input.length; i++) {
  if (input[i] === "(") cnt++;
  else {
    cnt--;
    input[i - 1] === "(" ? (res += cnt) : res++;
  }
}
console.log(res);
