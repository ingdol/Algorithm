let input = require("fs").readFileSync("/dev/stdin").toString().trim().split(/\n/);

const haveCard = input[1].split(" ").map(Number);

let cardArr = new Map();
haveCard.forEach(n =>
  cardArr.has(n) ? cardArr.set(n, cardArr.get(n) + 1) : cardArr.set(n, 1)
);
const compareCard = input[3].split(" ").map(Number);
const res = compareCard.map(m => cardArr.get(m) || 0);
console.log(res.join(" "));
