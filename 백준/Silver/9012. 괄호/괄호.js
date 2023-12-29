let input = require("fs").readFileSync("/dev/stdin").toString().trim().split(/\n/);

const N = Number(input[0]);
const arr = input.slice(1).map(s => s.trim().split(""));

function checkVps(i) {
  let sum = 0;
  for (let j = 0; j < arr[i].length; j++) {
    arr[i][j] === "(" ? sum++ : sum--;
    if (sum === -1) return "NO";
  }
  if (sum === 0) return "YES";
  else return "NO";
}

for (let i = 0; i < N; i++) {
  console.log(checkVps(i));
}
