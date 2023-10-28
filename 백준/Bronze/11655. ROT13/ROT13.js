const input = require("fs").readFileSync("/dev/stdin").toString().split("");

let answer = "";
for (let i = 0; i < input.length; i++) {
  let char = input[i].charCodeAt(0);
  if (char >= 65 && char <= 90) {
    let upper = char + 13;
    if (upper > 90) upper -= 26;
    answer += String.fromCharCode(upper);
  } else if (char >= 97 && char <= 122) {
    let lower = char + 13;
    if (lower > 122) lower -= 26;
    answer += String.fromCharCode(lower);
  } else if (char === 32) {
    answer += " ";
  } else {
    answer += input[i];
  }
}
console.log(answer);
