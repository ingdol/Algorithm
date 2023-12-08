let input = require("fs").readFileSync("/dev/stdin").toString().trim().split(/\n/); 

const haveCard = input[1].split(" ").map(Number);

let cardDic = new Map();
haveCard.forEach(n => {
  if (cardDic.has(n)) {
    cardDic.set(n, cardDic.get(n) + 1);
  } else cardDic.set(n, 1);
});

const checkCard = input[3].split(" ").map(Number);
let resultArr = checkCard.map(m => (cardDic.has(m) ? cardDic.get(m) : 0));

console.log(resultArr.join(" "));
