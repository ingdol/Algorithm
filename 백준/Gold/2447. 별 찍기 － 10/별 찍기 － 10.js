let input = require("fs").readFileSync("/dev/stdin").toString().trim();
const N = Number(input);
let lines = [];
function star(i, j, num) {
  if (i % 3 === 1 && j % 3 === 1) {
    lines.push(" ");
  } else {
    if (num === 1) lines.push("*");
    else star(parseInt(i / 3), parseInt(j / 3), parseInt(num / 3));
  }
}

function printStars(num) {
  for (let i = 0; i < num; i++) {
    for (let j = 0; j < num; j++) {
      star(i, j, num);
    }
    lines.push("\n");
  }
}

printStars(N);
console.log(lines.join(""));
