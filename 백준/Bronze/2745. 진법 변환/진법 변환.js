let [num, divider] = require("fs").readFileSync("/dev/stdin").toString().trim().split(" ");

let ans = parseInt(num, Number(divider));

console.log(ans);