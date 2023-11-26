let input = require("fs").readFileSync("/dev/stdin").toString();

function factorial(n) {
  return n ? BigInt(BigInt(n) * BigInt(factorial(n - 1))) : 1;
}

const solution = n => {
  const arr = [...factorial(n).toString()];
  let res = 0;
  while (true) {
    const cur = arr.pop();
    if (cur === "0") {
      res++;
    } else break;
  }
  return res;
};
console.log(solution(Number(input)));
