const arr = require("fs").readFileSync("/dev/stdin").toString().split("\n");

for (var i in arr) {
  if (arr[i] === "") continue;

  const strArr = [0, 0, 0, 0];
  for (let s of arr[i]) {
    if (/[a-z]/.test(s)) strArr[0]++;
    else if (/[A-Z]/.test(s)) strArr[1]++;
    else if (/[0-9]/.test(s)) strArr[2]++;
    else strArr[3]++;
  }
  console.log(strArr.join(" "));
}
