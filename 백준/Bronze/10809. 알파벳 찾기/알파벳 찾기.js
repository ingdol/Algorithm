const input = require("fs").readFileSync("/dev/stdin").toString().split("");

const alphabet = "abcdefghijklmnopqrstuvwxyz";
const counts = new Array(26).fill(-1);
let arr = [...input].reverse();
arr.forEach(
  (s, index) => (counts[alphabet.indexOf(s)] = arr.length - index - 1)
);

console.log(counts.join(" "));
