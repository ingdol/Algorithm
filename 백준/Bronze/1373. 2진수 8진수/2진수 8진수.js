let N = require('fs').readFileSync("./dev/stdin").toString().trim();
let answer = '';


while(N.length>3){
  let S = N.slice(N.length-3,N.length)
  answer = parseInt(S,2).toString(8)+answer
  N = N.slice(0,N.length-3)
}
console.log(parseInt(N,2).toString(8)+answer)