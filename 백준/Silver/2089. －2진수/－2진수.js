let n = require("fs").readFileSync("/dev/stdin").toString().trim();

let result = "";
if (n === 0) result += 0;
while (n != 0) {
  result += Math.abs(n % -2);
  n = Math.ceil(n / -2);
}
if (result) console.log(result.split("").reverse().join(""));
else console.log(0);
