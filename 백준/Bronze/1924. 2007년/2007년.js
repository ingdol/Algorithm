const input = require("fs").readFileSync("/dev/stdin").toString().split(" ");

let m = Number(input[0]);
let d = Number(input[1]);

const week = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"];
const days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
let calendar = [];
let w = 1;
for (let i = 1; i <= 12; i++) {
  let month = [];
  for (let j = w; j < days[i - 1] + w; j++) {
    month.push(week[j % 7]);
  }
  w = (days[i - 1] + w) % 7;
  calendar.push(month);
}
console.log(calendar[m - 1][d - 1]);
