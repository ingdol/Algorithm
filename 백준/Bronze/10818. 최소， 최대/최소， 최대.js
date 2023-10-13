const input = require("fs").readFileSync("/dev/stdin").toString().split("\n");

let arr = input[1].split(" ");
console.log(Math.min(...arr), Math.max(...arr));
